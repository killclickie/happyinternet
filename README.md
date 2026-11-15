# Slop Stopper

Stop sounding like everyone else on the internet. We deserve better.

Slop Stopper is a final review for anything you're about to publish or send: a LinkedIn post, an email, a blog post, a webpage, a report, a proposal. An independent reviewer reads your draft with clean eyes, removes AI tells and formulaic writing, improves structure and headings, tightens it for its real reader, and checks facts, numbers and links before you hit publish. You get back the improved draft and a short summary of what changed.

It also includes **slides-brief**, which turns an outline into a slide-by-slide deck brief that follows a 10/20/30 rule adapted from Guy Kawasaki's: no more than 10 slides, no text smaller than 20 points, and no longer than 30 minutes.

## Why I built a plugin to stop AI slop

I can't bear to read any more poor writing: the formulaic structures, the "it's not X, it's Y" reframes, the over-dramatized humble brags that AI cranks out for people every day.

AI is still useful for the heavy lifting on a post, a proposal or a report. Slop Stopper is the last pass before you publish, so the result sounds like a person who knows their subject. It works on any written piece; social posts are one use among many.

My goal is a happier internet to read and engage with.

## Caroline Cadwell: writer, teacher, software founder

I'm Caroline Cadwell. I have a creative writing degree from a top liberal arts college, wrote for the San Francisco Chronicle and taught at Toulouse Business School. I've worked in software since 2007, first in sales, then marketing, then as a founder. I care about concise, effective writing.

## Five steps from draft to publish-ready

1. **Intake, scaled to the piece.** For a short post or email it infers the channel, reader and goal and tells you what it assumed. For long or high-stakes pieces it asks once for your style guide, audience notes or original brief. All optional.
2. **Scan.** A checklist of search patterns flags known AI tells and formula patterns line by line, plus channel limits (LinkedIn's 3,000 characters and the preview before "see more," X, Threads, Bluesky, Instagram).
3. **Clean-eyes review.** A separate reviewer that never saw how the draft was written works through seven passes, biggest problems first: purpose and reader, argument and evidence, structure, voice and AI tells, channel rules, your style guide, line edit.
4. **Validation gate.** Pass/fail checks on facts and claims, faithfulness to what you said, numbers and dates, links and calls to action, compliance disclosures, length limits and file rendering. It reruns the scan on its own edits.
5. **Hand-back.** The revised draft in its original format, then a verdict, the biggest improvement, the changes, anything still open, and one consolidated "To verify" list.

**What it never does:** invent facts, numbers, quotes or credentials; add emotions or details you didn't state; upgrade "working toward" into "done"; or quietly change your message. Anything it can't confirm goes on the To-verify list.

## AI tells it flags, from "it's not X, it's Y" to engagement bait

- Binary contrasts: "It's not X. It's Y." "This isn't about X."
- Throat-clearing openers and faux-insight setups: "Here's the thing," "Let me be clear," "What nobody tells you," "The part everyone misses"
- Setup questions and cliffhangers: "The catch?" "Honestly?"
- Superficial analysis and importance puffery: "...highlighting the team's commitment to innovation," "marks a pivotal moment," "a testament to"
- Weasel attribution: "Experts agree," "Studies show"
- Synonym cycling: "The agent handles your email. The assistant drafts replies."
- Fake-profound endings: "The future isn't coming. It's already here."
- Filler "named": "named studies," "named authors attached to the study"
- Humble brags and announcement inflation: "Humbled to announce." "I don't take that for granted."
- Performed epiphanies: "That's when it hit me."
- Vague consequences and inflated scope: "That shapes how we work." "It changes everything."
- Lines your intended reader would stall on, even knowing the field: a new subject with no setting, an outcome with no "how", a vague tail like "the business process behind it". It fixes them from your sources or asks you; it never invents the missing piece.
- Filler that points back at earlier ideas without adding meaning: "Across all of it," "With that in mind," "As mentioned above"
- Colon reveals standing in for sentences: "The best part: it learns." "The result: ..."
- Stacked negations and dramatic fragments: "No delays. No excuses. No limits." "That's it. That's the whole thing."
- LinkedIn broetry, engagement bait ("Agree?"), hashtag piles and emoji bullets
- Em dashes, filler adverbs, hedges and the usual AI vocabulary (delve, leverage, seamless, unlock)
- Ungrounded claims, numbers with no reference point, buried asks, recommendations with no tradeoff

It also brings general craft rules: lead with the point, use active voice, untangle hard-to-follow sentences, prefer concrete details over abstractions, write up to a knowledgeable reader, ground every claim, name the tradeoff, keep asks specific, cut every sentence that doesn't earn its place. Channel rules cover LinkedIn posts and profiles, other social platforms, email, web and SEO/AEO content, reports and formatted documents.

## Before and after: a LinkedIn job announcement

Before:

> I'm thrilled and humbled to announce I've joined Acme as Head of Growth 🚀
>
> Honestly? I almost didn't post this.
>
> Growth isn't about hacks. It's about people.
>
> Agree? 👇

After:

> I've joined Acme as Head of Growth. A third of last year's customers came from their referral program, which I'm working to put a bigger flywheel on.

(The detail in the "after" comes from the author. Slop Stopper asks for it rather than making it up.)

## Install in Claude Code or the Claude apps

**Claude Code**

```
/plugin marketplace add killclickie/happyinternet
/plugin install slop-stopper@happyinternet
```

**Claude apps:** install Slop Stopper from the plugin directory once it's listed.

## Run a review on any draft

Say "run a final review on this," "remove the AI tells," "clean up the slop" or "proofread this," and paste, attach or link your draft. Or run `/slop-stopper:slop-stop`. (The skill used to be called `final-review`; that name still works.) You can also point Claude at it while drafting something new ("write this LinkedIn post using Slop Stopper's rules"); it writes to the same rules, then reviews its own draft with clean eyes. Tell it where the piece is going (LinkedIn, an email, a client report) for the sharpest result.

Your own style guide always wins over the defaults here, except for the integrity rules: it never invents.

## Brief a slide deck with the 10/20/30 rule

Use it at either end of deck work. **Starting out:** brainstorming a talk, outlining a pitch, or turning documents, a report or notes into slides. It proposes a one-line-per-slide outline from your material for you to approve, then writes the slides. **Already have a deck that's too wordy:** share it and it cuts each slide to one idea, offers to move the cut text into speaker notes, and shows the words saved per slide. Ask for help with a deck in your own words, or run `/slop-stopper:slides-brief`. It returns a `.md` brief with a style guide and the copy for every slide, to take into Claude's Slides artifacts (Artifacts → Slides) or any slide tool. It works for any deck: talks, team updates, pitches, proposals, training.

- **Presented decks** follow a 10/20/30 rule adapted from Guy Kawasaki's: no more than 10 slides, no text smaller than 20 points (body text defaults to 30–36), no longer than 30 minutes. Slide text is cut so the deck supports the speaker. Longer formats keep the other standards.
- **Decks sent without a presenter** get the minimum extra text a reader needs to follow each slide alone, with nothing below 20 points.
- **Style** comes from what you specify, then your brand guide or kit. If neither is available, it asks whose style to use (yours, your audience's, or a reference you like) and takes it from that organization's website or an existing deck.
- **Copy** is written to Slop Stopper's rules, keeps your wording, and lists anything it cut.

## Files: two skills and five reference files, no scripts

```
skills/slop-stop/
  SKILL.md                  the workflow: intake, scan, review, gate, hand-back
  references/guardrails.md  integrity rules (never invent, never embellish)
  references/craft.md       how good writing works
  references/ai-tells.md    the AI-tell and formula patterns, each with its fix
  references/channels.md    LinkedIn, social, email, web and SEO/AEO, reports, documents
  references/scan-patterns.md  the search patterns and channel limits for the scan
skills/slides-brief/
  SKILL.md                  deck brief workflow: style, 10/20/30 fit, copy, brief
skills/final-review/
  SKILL.md                  the old name, kept so it still opens slop-stop
```

## Your drafts stay in your Claude session

Slop Stopper runs entirely inside your Claude session. It contains only Markdown instructions, JSON settings and an icon: no scripts, no network calls, nothing stored. The plugin connects to no outside services.

## Report a missed tell or a false positive

Spotted a tell it misses, or a false positive? Open an issue with the sentence and what it should have done. Pattern additions go in `references/ai-tells.md` and `references/scan-patterns.md` together.

## License: MIT with the Commons Clause (use and fork freely, don't sell)

MIT with the Commons Clause. Use it, change it and fork it, for personal or work writing. You may not sell it, or sell a product or service whose value comes substantially from it. See [LICENSE](LICENSE).
