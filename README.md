# Slop Stopper

A final review for anything you're about to publish or send: a LinkedIn post, an email, a blog post, a webpage, a report, a proposal. An independent reviewer reads your draft with clean eyes, strips the AI tells and formulaic structures, tightens it for its real reader, and checks facts, numbers and links before you hit publish. You get back the improved draft and a short summary of what changed.

## Why I made this

I can't bear to read any more poor writing: the formulaic structures, the "it's not X, it's Y" reframes, the over-dramatized humble brags that AI cranks out for people every day.

AI is still useful for the heavy lifting on a post, a proposal or a report. Slop Stopper is the last pass before you publish, so the result sounds like a person who knows their subject. It works on any written piece; social posts are one use among many.

My goal is a happier internet to read and engage with.

Caroline Cadwell

## What it does

1. **Intake, scaled to the piece.** For a short post or email it infers the channel, reader and goal and tells you what it assumed. For long or high-stakes pieces it asks once for your style guide, audience notes or original brief. All optional.
2. **Scan.** A small script flags known AI tells and formula patterns line by line, plus channel limits (LinkedIn's 3,000 characters and the preview before "see more," X, Threads, Bluesky, Instagram).
3. **Clean-eyes review.** A separate reviewer that never saw how the draft was written works through seven passes, biggest problems first: purpose and reader, argument and evidence, structure, voice and AI tells, channel rules, your style guide, line edit.
4. **Validation gate.** Pass/fail checks on facts and claims, faithfulness to what you said, numbers and dates, links and calls to action, compliance disclosures, length limits and file rendering. It reruns the scan on its own edits.
5. **Hand-back.** The revised draft in its original format, then a verdict, the biggest improvement, the changes, anything still open, and one consolidated "To verify" list.

**What it never does:** invent facts, numbers, quotes or credentials; add emotions or details you didn't state; upgrade "working toward" into "done"; or quietly change your message. Anything it can't confirm goes on the To-verify list.

## What it catches

- Contrast reframes: "It's not X, it's Y." "This isn't about X."
- Setup questions and cliffhangers: "The catch?" "Honestly?" "Here's the thing:"
- Humble brags and announcement inflation: "Humbled to announce." "I don't take that for granted."
- Performed epiphanies: "That's when it hit me."
- Stacked negations and runs of dramatic fragments: "No delays. No excuses. No limits."
- LinkedIn broetry, engagement bait ("Agree?"), hashtag piles and emoji bullets
- Em dashes, filler adverbs, hedges and the usual AI vocabulary (delve, leverage, seamless, unlock)
- Ungrounded claims, numbers with no reference point, buried asks, recommendations with no tradeoff

It also brings general craft rules: lead with the point, write up to a knowledgeable reader, ground every claim, name the tradeoff, keep asks specific, cut every sentence that doesn't earn its place. Channel rules cover LinkedIn posts and profiles, other social platforms, email, web and SEO/AEO content, reports and formatted documents.

## Example

Before:

> I'm thrilled and humbled to announce I've joined Acme as Head of Growth 🚀
>
> Honestly? I almost didn't post this.
>
> Growth isn't about hacks. It's about people.
>
> Agree? 👇

After:

> I've joined Acme as Head of Growth. My first project: rebuilding the referral program that brought in a third of last year's customers.

(The detail in the "after" comes from the author. Slop Stopper asks for it rather than making it up.)

## Install

**Claude Code**

```
/plugin marketplace add killclickie/happyinternet
/plugin install slop-stopper@happyinternet
```

**Claude apps:** install Slop Stopper from the plugin directory once it's listed.

## Use

Say "run a final review on this" and paste, attach or link your draft. Or run `/slop-stopper:final-review`. Tell it where the piece is going (LinkedIn, an email, a client report) for the sharpest result.

Your own style guide always wins over the defaults here, except for the integrity rules: it never invents.

## What's inside

```
skills/final-review/
  SKILL.md                  the workflow: intake, scan, review, gate, hand-back
  references/guardrails.md  integrity rules (never invent, never embellish)
  references/craft.md       how good writing works
  references/ai-tells.md    the AI-tell and formula patterns, each with its fix
  references/channels.md    LinkedIn, social, email, web and SEO/AEO, reports, documents
  scripts/scan.py           the pattern scanner (Python 3 standard library)
```

## Data handling

Slop Stopper runs entirely inside your Claude session. The scanner reads the draft file it's given and prints results; it makes no network calls and stores nothing. The plugin connects to no outside services.

## Contributing

Spotted a tell it misses, or a false positive? Open an issue with the sentence and what it should have done. Pattern additions go in `references/ai-tells.md` and `scripts/scan.py` together.

## License

MIT with the Commons Clause. Use it, change it and fork it, for personal or work writing. You may not sell it, or sell a product or service whose value comes substantially from it. See [LICENSE](LICENSE).
