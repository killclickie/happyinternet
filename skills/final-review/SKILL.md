---
name: final-review
description: Final review that strips AI tells and formulaic writing from any draft, tightens it for its real reader, then checks facts, numbers and links before it ships. Works on LinkedIn and other social posts, emails, blog posts, webpages, reports, proposals and essays. An independent reviewer edits against the reader, channel and any style guide or brief. Also use its rules as guidance while drafting new content, then review the result before it ships.
---

# Final Review

Returns an **improved draft** plus a short review summary, not a list of comments.

**Two ways to use it.**
- **Review a draft** that already exists: run Steps 1 to 5 below.
- **Draft new content**: follow `guardrails.md`, `craft.md`, `ai-tells.md` and the channel's section of `channels.md` as writing rules from the first sentence. When the draft is done, run Steps 2 to 5 on it so an independent reviewer checks the result.

## Files

Read all four references on every run. Each rule lives in exactly one file.

- `references/guardrails.md`: integrity. Never overridden.
- `references/craft.md`: how good writing works. Structure, evidence, audience, plain language, asks, length, mechanics.
- `references/ai-tells.md`: phrases and structures that make writing read as machine-made or templated, each with its fix.
- `references/channels.md`: rules for one channel only (LinkedIn, other social, email, web and SEO/AEO, reports, formatted documents).
- `scripts/scan.py`: deterministic scanner for the patterns in `ai-tells.md` plus channel limits. Python 3 standard library, no network.

All paths are relative to this skill's folder.

**Precedence.** `guardrails.md` first, always. Then the user's own style guide, brief or instructions. Then `channels.md`. Then `craft.md` and `ai-tells.md`. The user's rule wins any conflict except a guardrail.

## Step 1: Intake (scale it to the piece)

Four things are needed: the draft, the channel (what it is and where it will be published), the reader, and the goal (what the reader should do or think afterwards). Optional references: a style guide, an audience or positioning document, the original brief, an example the user considers on-voice.

- **Short pieces** (a social post, an email, anything under about 400 words): infer channel, reader and goal from the draft and the conversation. Don't ask. State the inferences in the summary so the user can correct them. Ask only if the channel is unclear, since channel changes the rules.
- **Long or high-stakes pieces** (client-facing, published web content, regulated topics): if the references aren't already in the conversation or project, ask once, in one message. Name the optional references, ask the channel, and ask whether it's web content meant for search or answer engines. Proceed with whatever arrives.
- Never re-ask for material already provided. If a reference the user says exists can't be opened, say so and ask for it. An audit against guessed context is worse than none.

Set two modes from intake:
- **Channel**: picks the section of `channels.md` that applies.
- **SEO/AEO mode**: on only when the user says the piece is web content or is meant for search or answer engines. Off otherwise: never add keywords, FAQs, schema notes or meta descriptions to an email, post, release or print piece.

## Step 2: Scan

Save the draft as plain text and run:

```
python3 scripts/scan.py draft.txt --channel <linkedin|x|threads|bluesky|instagram|email|web|doc>
```

The output lists each hit with its line number, the matched text and the fix. Hits are candidates, not verdicts: the reviewer decides. If Python is unavailable, the reviewer checks the draft against `ai-tells.md` by hand.

## Step 3: Clean-eyes review

Spawn an independent reviewer subagent. Give it only:
- the draft, verbatim
- the channel, reader, goal and mode from Step 1, and any references the user supplied
- the scan output
- the four reference files
- the reviewer brief below

Do **not** give it the drafting conversation, your reasoning, or earlier versions. It judges the artifact, not the intent. If you can't spawn a subagent, run the passes yourself after a hard reset: read the draft top to bottom as a skeptical editor seeing it for the first time.

**Reviewer brief** (pass it verbatim):

> You are the final editor on this piece. You did not write it. Work through the seven passes in order, editing the draft as you go; comments without edits don't count. Follow `guardrails.md` without exception: never invent a fact, number, quote or detail, and never upgrade a claim. Make the lightest edit that fixes each problem. Return four things: (1) the full revised draft, (2) a change log, one line per change, naming the rule it applies, (3) open items you could not fix, split into must-fix and nice-to-have, (4) one consolidated To-verify list.

**The passes** (big problems before polish; don't line-edit a paragraph the first pass will cut):

1. **Purpose and reader.** Does it answer the ask or brief? Is the point clear in the opening to the stated reader, at their level? Ask "what would make this measurably more effective for this reader?" and apply the answer. (`craft.md`: Lead with the point, Know the reader)
2. **Argument and evidence.** Every claim grounded, causal links stated, claim strength matched to the evidence. An ungrounded claim goes to To-verify; the reviewer never supplies the missing number. (`craft.md`: Ground every claim, Thinking)
3. **Structure.** Order, sections, lists, length. Rewrite every title, heading, section label and subject line to name the specific content beneath it. (`craft.md`: Titles, headings and section labels; Structure in formatted pieces; plus the channel section)
4. **Voice and AI tells.** Resolve every scan hit and anything else in `ai-tells.md`. A pattern stays only if it's the plainest way to say the thing; log why.
5. **Channel.** Every rule in the channel's section of `channels.md`, including SEO/AEO rules if that mode is on.
6. **User's style guide and brief.** Voice, required and banned terms, CTA convention, mechanics, compliance.
7. **Line edit.** Plain language, mechanics, final cut for length. Test every word and phrase: delete it and reread; if the meaning survives, it stays deleted. Read it aloud once, end to end.

**Edit discipline.**
- Keep the author's register, point of view and formatting. Don't add bold, headings, emoji or em dashes the original lacked unless the channel calls for them.
- Reordering or cutting a section is allowed when it rescues a buried point. Log it.
- Never change the strategy, angle or message silently. If the piece needs a different direction, make the improvements that don't depend on that call and flag the direction question for the user.

## Step 4: Validation gate (pass/fail)

Run on the revised draft. First rerun `scan.py` on it: edits introduce tells too. Every remaining hit is either fixed or justified in the change log.

| Check | Pass condition |
|---|---|
| Fact and claim integrity | Every stat, quote, spec and claim traces to the draft, its sources, the user's references or the user (`guardrails.md`) |
| Faithful to the author | No detail, emotion or credential added; tense, completion status and claim strength unchanged |
| Numbers, math, dates | Recomputed; comparison periods and dates consistent |
| Links, CTA, placeholders | No dummy URLs, bracketed placeholders or broken merge tokens in the body; CTA present and descriptive where the channel needs one |
| Compliance | Required disclosures present for regulated topics (finance, health, legal, real estate and similar) |
| Channel limits | Within the platform's character or length limits (`scan.py` reports them) |
| Render | If delivered as a file, open or read it back and confirm it looks right; clean source is not proof |

**Never ship** with an invented or unsourced claim, a wrong number, a compliance miss, a broken or placeholder link or CTA, a failed render, or a detail pulled from an unrelated source. Fix it, or list it at the top of To-verify marked **BLOCKING**.

## Step 5: Hand back

1. **The revised draft**, in the original's format (pasted text back as text, an attached file back as the same file type) unless the user asked for another. It holds publishable content only: no inline notes, version markers or commentary.
2. **The review summary**, after the draft:
   - **Verdict**: ready to ship / ready once To-verify is cleared / needs a direction call
   - **Biggest improvement**, in one line
   - **Changes**, one line each, grouped by pass. For a short piece, the five that matter most.
   - **Still open**: must-fix vs nice-to-have
   - **To verify**: the single consolidated list; BLOCKING items first
   - **Assumptions**: channel, reader and goal, if inferred rather than given
   - **New style rules** spotted this run, written as ready-to-paste style-guide lines

Keep the summary shorter than the draft when the draft is short. Say whether the review ran in an independent subagent or as a hard-reset self-review.
