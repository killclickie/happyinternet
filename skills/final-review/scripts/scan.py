#!/usr/bin/env python3
"""Slop Stopper scanner.

Flags AI tells, formulaic structures and channel-limit problems in a draft.
Hits are candidates for a human or model editor to judge, not verdicts.

Usage:
    python3 scan.py draft.txt [--channel linkedin|x|threads|bluesky|instagram|email|web|doc]
    cat draft.txt | python3 scan.py - --channel linkedin

Standard library only. Reads the file you give it and prints to stdout.
Makes no network calls and writes no files.
"""

import argparse
import re
import sys
import unicodedata

# ---------------------------------------------------------------------------
# Phrase lists: (category, fix, [phrases]). Matched case-insensitively on
# word boundaries. Keep in sync with references/ai-tells.md.
# ---------------------------------------------------------------------------

PHRASES = [
    ("Filler adverb", "Cut unless removing it changes the meaning.", [
        "actually", "really", "simply", "just", "literally", "basically", "truly",
        "very", "quite", "incredibly", "genuinely", "honestly", "definitely", "absolutely",
    ]),
    ("Hedge", "Make the claim, or state the specific uncertainty once.", [
        "i think", "i feel like", "it seems", "arguably", "hopefully", "perhaps",
        "might potentially", "in some ways",
    ]),
    ("AI vocabulary", "Use the plain, specific word.", [
        "delve", "delves", "delving", "tapestry", "landscape", "navigate", "navigating",
        "realm", "unlock", "unlocks", "unlocking", "unleash", "elevate", "elevates",
        "empower", "empowers", "empowering", "leverage", "leveraging", "harness",
        "seamless", "seamlessly", "robust", "cutting-edge", "game-changer",
        "game-changing", "transformative", "revolutionize", "revolutionizing", "synergy",
        "holistic", "pivotal", "testament to", "ever-evolving", "fast-paced", "embark",
        "journey", "foster", "fostering", "streamline", "supercharge", "next-level",
        "deep dive", "best-in-class", "world-class", "solution", "solutions",
    ]),
    ("Internet idiom", "Say what is different and why.", [
        "hits different", "rent free", "it's giving", "no notes", "chef's kiss",
        "main character", "obsessed",
    ]),
    ("Tired metaphor", "Say the literal thing.", [
        "move the needle", "low-hanging fruit", "keep the lights on", "out of left field",
        "slice of the pie", "north star", "double-click on", "boil the ocean", "secret sauce",
    ]),
    ("Outsourced CTA", "Write the ask itself, or just ask the question.", [
        "reach out", "hit reply", "drop me a line", "shoot me a note", "ping me", "feel free to",
    ]),
    ("Email filler", "Open with the point or the ask.", [
        "hope this finds you well", "hope this email finds you well", "checking in", "circling back", "circle back", "touching base", "touch base",
        "per my last email", "as previously discussed", "i know you're busy",
    ]),
    ("Announcement inflation", "Lead with the news itself.", [
        "thrilled", "humbled", "excited to announce", "excited to share", "honored to", "delighted to", "beyond grateful", "pinch-me", "pinch me moment",
    ]),
    ("Humble brag", "State the fact; thank named people for named things.", [
        "don't take that for granted", "don't take it for granted",
        "do not take that for granted", "lucky enough to", "not bad for",
    ]),
    ("Performed epiphany", "Say what happened.", [
        "finally realized", "finally understood", "finally clicked", "it hit me", "finally got it",
    ]),
    ("Meta-narration", "Cut the announcement, keep the point.", [
        "let me explain", "here's what i learned", "what i actually want to talk about",
        "the truth is", "truth be told", "if i'm honest", "to be honest",
        "here's the real story", "this section is the most important",
        "keep this in mind", "it's worth noting", "it is worth noting",
        "it's important to note", "it is important to note",
    ]),
    ("Canned opener", "Open on the point, the news or the specific detail.", [
        "picture this", "imagine a world", "in today's", "let's dive",
        "nobody talks about", "more often than most",
        "in a world where", "almost didn't post this", "changed everything",
    ]),
    ("Neat closer", "End on the last substantive sentence.", [
        "at the end of the day", "the bottom line", "makes all the difference",
        "let that sink in", "read that again",
    ]),
    ("Tidy diagnosis", "Name the specific thing that's happening or missing.", [
        "the gap", "the real problem", "that's exactly", "they're exactly",
        "is built to", "are built to", "built for this",
    ]),
    ("Engagement bait", "End on the point, or a specific question you want answered.", [
        "agree?", "thoughts?", "follow for more", "repost if", "tag someone",
        "comment below", "like if", "smash that", "drop a comment",
    ]),
]

# ---------------------------------------------------------------------------
# Regex patterns: (category, fix, compiled regex). Run per line.
# ---------------------------------------------------------------------------

PATTERNS = [
    ("Contrast reframe", "State the second half. The reader never thought the first.",
     re.compile(r"\b(it'?s|this is|that'?s|it is)\s+not\s+(just\s+|only\s+|about\s+)?[^.?!]{1,60}?[,;:.]\s*(it'?s|but|this is|it is)\b", re.I)),
    ("Contrast reframe", "State the second half. The reader never thought the first.",
     re.compile(r"\b(isn'?t|wasn'?t|aren'?t)\s+(about|the problem|the point|the issue)\b", re.I)),
    ("Contrast reframe", "State the second half. The reader never thought the first.",
     re.compile(r"\bnot\s+(just|only|merely)\s+[^.?!]{1,60}?,?\s+but\b", re.I)),
    ("Contrast reframe", "State the point directly.",
     re.compile(r"\b[\w\s]{1,30}\bnot\s+[\w\s-]{1,30}\bproblems?\b", re.I)),
    ("Quietly intensifier", "Say what's happening and how fast.",
     re.compile(r"\b(is|are|was|were|been)\s+quietly\s+\w+", re.I)),
    ("Setup question", "Delete the question; write the answer as a full sentence.",
     re.compile(r"(^|[.!?]\s+)(the|here'?s)?\s*(catch|truth|result|kicker|twist|problem|answer|secret|reality|irony|lesson|thing|best part|worst part|honestly|why does this matter|why it matters|so what)\s*[?:]", re.I)),
    ("Setup phrase", "Delete it; state the point.",
     re.compile(r"\b(here'?s the (thing|kicker|deal|catch)|plot twist)\b", re.I)),
    ("Vague back-reference", "Restate the concrete noun, or cut the sentence.",
     re.compile(r"(^|[.!?]\s+)(that|this)\s+(kind|sort|type|moment|combination|feeling|shift|is why|is what|is exactly|right there)\b", re.I)),
    ("Sweeping scope phrase", "Cut it. If scope matters, state it actively with the concrete noun.",
     re.compile(r"\b(across|through|throughout|in|beyond|above|underneath|behind|at the (heart|core|end) of)\s+(it all|all of (it|this|that|these|them)|all this|all that|everything|each of (these|them)|every (step|one of these))\b", re.I)),
]

GENERIC_HEADINGS = {
    "overview", "introduction", "intro", "background", "what it does", "how it works",
    "features", "key features", "benefits", "key benefits", "key takeaways", "takeaways",
    "the opportunity", "the problem", "the solution", "why it matters", "why this matters",
    "next steps", "conclusion", "summary", "about", "about me", "about us", "getting started",
    "what it catches", "what's inside", "example", "examples", "details", "context",
    "the request", "what happens next", "at a glance", "highlights", "results", "use", "usage",
}
HEADING = re.compile(r"^\s{0,3}(#{1,6})\s+(.+?)\s*#*\s*$")

EM_DASH = re.compile(r"—|\s--\s|\s–\s")
UNICODE_STYLED = re.compile(r"[\U0001D400-\U0001D7FF]")
HASHTAG = re.compile(r"(?<![\w#])#[A-Za-z][\w]*")
MD_BOLD = re.compile(r"\*\*[^*\n]+\*\*|__[^_\n]+__")
TRIPLET = re.compile(r"\b[\w'-]+,\s+[\w'-]+,?\s+(and|or)\s+[\w'-]+\b", re.I)
SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")

LIMITS = {
    "linkedin": 3000,
    "x": 280,
    "threads": 500,
    "bluesky": 300,
    "instagram": 2200,
}
SOCIAL = set(LIMITS)


def is_emoji(ch):
    cp = ord(ch)
    return (
        0x1F300 <= cp <= 0x1FAFF
        or 0x2600 <= cp <= 0x27BF
        or 0x1F000 <= cp <= 0x1F2FF
        or cp in (0x2705, 0x274C, 0x2B50, 0x2B06, 0x2B07, 0x27A1)
    )


def phrase_regex(phrase):
    escaped = re.escape(phrase).replace(r"\ ", r"\s+").replace("'", "['’]")
    left = r"\b" if phrase[0].isalnum() else ""
    right = r"\b" if phrase[-1].isalnum() else ""
    return re.compile(left + escaped + right, re.I)


COMPILED_PHRASES = [
    (cat, fix, [(p, phrase_regex(p)) for p in plist]) for cat, fix, plist in PHRASES
]


def sentences(text):
    flat = re.sub(r"\s*\n\s*", " ", text.strip())
    return [s for s in SENTENCE_SPLIT.split(flat) if s.strip()]


def scan(text, channel):
    hits = []  # (line_no, category, match, fix)
    lines = text.splitlines()

    for i, line in enumerate(lines, 1):
        if not line.strip():
            continue
        for cat, fix, plist in COMPILED_PHRASES:
            for phrase, rx in plist:
                for m in rx.finditer(line):
                    hits.append((i, cat, m.group(0), fix))
        for cat, fix, rx in PATTERNS:
            for m in rx.finditer(line):
                hits.append((i, cat, m.group(0).strip(), fix))
        h = HEADING.match(line)
        if h:
            title = re.sub(r"[*_`:]", "", h.group(2)).strip().lower()
            if title in GENERIC_HEADINGS or len(title.split()) <= 1:
                hits.append((i, "Generic heading", h.group(2).strip(),
                             "Name the specific content beneath it. Would it fit a section of another document unchanged? Rewrite."))
        for m in EM_DASH.finditer(line):
            ctx = line[max(0, m.start() - 25): m.end() + 25].strip()
            hits.append((i, "Em dash", ctx, "Use a colon, comma, period or parentheses."))
        if UNICODE_STYLED.search(line):
            hits.append((i, "Unicode styled text", line.strip()[:60],
                         "Use plain text. Screen readers can't read it."))
        stripped = line.lstrip()
        if stripped and is_emoji(stripped[0]):
            hits.append((i, "Emoji bullet", stripped[:40], "Use words or a plain list."))
        bolds = MD_BOLD.findall(line)
        if bolds and channel in SOCIAL | {"email"}:
            hits.append((i, "Bold in body", ", ".join(bolds)[:60],
                         "Let sentence structure carry emphasis."))

    # Multi-sentence patterns
    sents = sentences(text)
    run = []
    for s in sents + [""]:
        words = len(s.split())
        if 0 < words <= 4:
            run.append(s)
        else:
            if len(run) >= 3:
                hits.append((0, "Run of fragments", " ".join(run)[:80],
                             "Write complete sentences; one fragment at most."))
            run = []
    neg = []
    for s in sents + [""]:
        if re.match(r"^(no|zero|never)\s", s, re.I) and len(s.split()) <= 7:
            neg.append(s)
        else:
            if len(neg) >= 2:
                hits.append((0, "Stacked negation", " ".join(neg)[:80],
                             "Say what the reader gets, once, positively."))
            neg = []

    triplets = TRIPLET.findall(text)
    word_count = len(text.split())
    if word_count and len(triplets) >= 3 and len(triplets) / max(word_count, 1) * 300 >= 2:
        hits.append((0, "Reflexive triplets", f"{len(triplets)} three-item lists in {word_count} words",
                     "Use as many items as the content has."))

    return hits


def stats(text, channel):
    out = []
    chars = len(text.strip())
    words = len(text.split())
    out.append(f"Length: {words} words, {chars} characters")
    if channel in LIMITS:
        limit = LIMITS[channel]
        status = "OVER LIMIT" if chars > limit else "ok"
        out.append(f"{channel} limit: {limit} characters ({status})")

    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    if len(paras) >= 6:
        single = sum(1 for p in paras if len(p.split()) <= 15)
        share = single / len(paras)
        if share >= 0.6:
            out.append(f"Broetry: {single} of {len(paras)} paragraphs are one short line. "
                       "Group lines that make one point.")

    tags = HASHTAG.findall(text)
    if tags:
        out.append(f"Hashtags: {len(tags)} ({' '.join(tags[:8])})")
        if channel == "linkedin" and len(tags) > 3:
            out.append("  LinkedIn: use 0 to 3, at the end.")
        last_para = paras[-1] if paras else ""
        mid = [t for t in tags if t not in last_para]
        if mid:
            out.append(f"  Mid-text hashtags: {' '.join(mid[:8])}. Move to the end or cut.")

    emoji = [ch for ch in text if is_emoji(ch)]
    if emoji:
        out.append(f"Emoji: {len(emoji)}")
    excl = text.count("!")
    if excl:
        out.append(f"Exclamation marks: {excl}")

    if channel == "linkedin":
        preview = re.sub(r"\s+", " ", text.strip())[:200]
        out.append(f"Preview before 'see more' (about 200 chars): \"{preview}\"")
        out.append("  Does the preview carry the point, the news or a specific detail?")
    return out


def main():
    ap = argparse.ArgumentParser(description="Flag AI tells and formula in a draft.")
    ap.add_argument("path", help="Draft file, or - for stdin")
    ap.add_argument("--channel", default="doc",
                    choices=["linkedin", "x", "threads", "bluesky", "instagram", "email", "web", "doc"])
    args = ap.parse_args()

    if args.path == "-":
        text = sys.stdin.read()
    else:
        with open(args.path, encoding="utf-8") as f:
            text = f.read()
    text = unicodedata.normalize("NFC", text)

    hits = scan(text, args.channel)
    hits.sort(key=lambda h: (h[1], h[0]))

    print(f"Slop Stopper scan ({args.channel})")
    print("=" * 40)
    for line in stats(text, args.channel):
        print(line)
    print()
    if not hits:
        print("No pattern hits.")
        return
    print(f"{len(hits)} candidate hits (judge each; not every hit is wrong):")
    current = None
    for line_no, cat, match, fix in hits:
        if cat != current:
            print(f"\n[{cat}] {fix}")
            current = cat
        loc = f"line {line_no}" if line_no else "multi-line"
        print(f"  {loc}: {match}")


if __name__ == "__main__":
    main()
