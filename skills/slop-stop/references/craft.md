# Craft

How good writing works. These are defaults: a user's style guide overrides any of them. Pattern-level bans (phrases, formulas, filler words) live in `ai-tells.md`; channel-specific rules live in `channels.md`.

## Lead with the point

- The reader knows where you stand before they know how you got there. The first sentence or paragraph carries the point.
- Asks, recommendations and decisions go up front. Reasoning follows.
- Order by what matters to the reader's decision, not by chronology.
- A long piece earns attention with a short summary at the top. Someone who reads only the first paragraph still gets the point and knows what's being asked of them.
- Match structure to complexity. A simple point is one paragraph with no headings. A multi-part analysis gets consistent sections. Don't impose structure on a straight answer or flatten a complex one into a block.

## Know the reader

- Write up to a smart reader who knows the field. Skip the 101 definitions they don't need; define a term once at most.
- Use the reader's vocabulary and mental model. Don't import jargon from another field (SaaS terms into a trade that doesn't use them, academic terms into a sales email).
- In customer-facing writing, talk to the reader as "you." Third-person distance ("a member needed...," "the customer's deadline") reads cold.
- Don't shame the reader or the brand's own customers. Frame problems constructively and leave people their dignity.
- Know who the asset is for: prospects, customers, colleagues, the public. Internal notes stay out of public copy.
- The test: would a smart, busy person with no context understand it and know what to do next? If not, restructure before wordsmithing.

## Clear to the intended reader

The reader the author is writing for may know the field, the jargon and the people. That excuses unexplained terms; it doesn't excuse unclear sentences. An expert still stalls on a line that skips its subject, hides its mechanism or ends in a vague abstraction.

**Audience knowledge.** Only the author sets what the reader already knows: through the brief, the stated audience, the conversation, or what the draft makes obvious (an industry post can say IBAN, SEPA or 4K without defining them; a newsletter to friends can say "Nash"). Never assume shared context on the author's behalf, and never flag a term or name the stated reader plainly knows.

**The test.** Read each sentence as the intended reader, once, at normal speed. Flag it if that reader couldn't restate it in their own words on first read, or if cutting it would lose nothing.

**What to flag**, from most to least common in AI drafts:

1. **Unanchored frame shift.** A sentence opens on a new subject without naming the setting it belongs to, so the reader has to work out what it's about. Short dramatic lines make this worse.
   - Before: "Open-plan offices cut real-estate costs by 30%. A phone call carries 15 metres."
   - Problem: nothing says the phone call is a colleague's, inside that office.
   - After: "Open-plan offices cut real-estate costs by 30%. In one, a colleague's phone call carries 15 metres."
2. **Compressed mechanism.** A claim or instruction names an outcome and skips how it happens. Often an abstract thing is treated as a physical object that can be moved, put or handed over ("put the data in their hands," "move the conversation to the phone").
   - Before: "Put the returns policy in the box."
   - Problem: printed in the box, a QR code, a card? The reader has to guess.
   - After, using the mechanism the draft or sources give: "Print the returns policy on the packing slip."
   - If no source gives the mechanism, don't supply one: list it under Needs context.
3. **Vague tail.** A trailing clause that sounds like a benefit but ends in a generic abstraction: "the business process behind it," "the bigger picture," "the customer journey," "what matters most," "the people behind the work." Test: could this phrase appear in any company's copy? If yes, it's carrying nothing.
   - Before: "Each refund is tagged with its order number and links to the customer journey behind it."
   - After: cut the tail ("Each refund is tagged with its order number.") or replace it with the specific outcome the draft already states. Never invent one.
4. **Unintroduced specifics** the stated reader wouldn't know: a person, project, event or "the" thing ("the migration," "after the pivot") that never appears earlier on the page.
5. **A leap**: a conclusion that depends on a step the draft never states.
6. **Fragments that don't parse** on first read ("Same story with ops."), and sentences that only restate the one before.

**What to do:**
- The fix uses only what's in the draft, its sources or the user's references: name the setting, state the mechanism, move the sentence after what it depends on, or rewrite the fragment as a sentence.
- A clause that carries nothing gets cut (delete and reread).
- When the fix needs a fact nobody supplied, never invent it. Leave the sentence and list it under **Needs context** with the specific question ("How does the returns policy reach the customer: a printed slip, a QR code, an email?").
- When it's unclear whether the author or an AI wrote a shorthand, flag it rather than cut it.

## Ground every claim

- Every claim gets a number, an example, a comparison, a mechanism or a source. "Strong growth" says nothing; "revenue grew from €40k to €61k between Q1 and Q3" can be checked. The reviewer flags an ungrounded claim; only the author supplies the evidence.
- A number needs a reference point: the prior period, the target, a benchmark, the alternative. A number alone means nothing.
- State causal mechanisms. Don't imply A causes B and leave the reader to build the bridge.
- Argue, don't enumerate. Every list and every section ties back to a claim and says why each item matters.
- Lead with the non-obvious. Open a section on what this reader doesn't already know.
- Match the claim word to the evidence: "indicates," "suggests," "shows" when that's what the evidence supports; "proves" and "guarantees" almost never.
- Give the reason before the offer or ask. A benefit with no stated reason reads as an assertion.

## Thinking (analysis, reports, recommendations, proposals)

- Separate observation from interpretation. State the fact, then what you think it means, and make the boundary visible.
- Name the tradeoff. Every recommendation costs something, risks something or deprioritizes something. A recommendation without a tradeoff reads as a sales pitch.
- Address the strongest objection where the piece argues a position.
- Name problems in plain language, then give each one a next step ("we're testing X," "we'll know by June"). A next step is enough; a full solution is optional.
- Integrate problems with progress rather than quarantining them in a "challenges" section.
- A bad number gets the target, the actual and what changes. Don't apologize for a miss; explain it and say what's next.

## Say it plainly

- Let the fact carry the sentence. When the evidence is the strongest thing in a line, make it the subject and follow with what the author is doing about it: "A third of last year's customers came from the referral program, which I'm working to grow," not "My first project: rebuilding the referral program that brought in a third of last year's customers."
- Declarative sentences: subject, verb, object. "We cut onboarding from nine days to four," not "we were able to successfully reduce the amount of time onboarding takes."
- Strong, specific verbs: led, built, cut, shipped, wrote. Not "helped with," "was involved in," "supported," "partnered on" when the author did the thing.
- One verb over a phrase: "exceeds," not "ends up being far greater than."
- Name the thing. "The invoicing module," not "the solution." If a word could describe any product in any industry, replace it.
- Active voice wherever it shows who did what. Present tense unless the point is about the past.
- Contractions in conversational and marketing writing. Follow the original's register in formal documents.
- Uncertainty is stated once and precisely ("we have six weeks of data, not enough to separate seasonality"), not spread across every sentence as hedging.
- Every sentence stands on its own for a skimmer. If "this," "that," "it" or "they" could point at more than one thing, or at an idea the reader has to reconstruct, name the thing.
- Hold an educated, lively register: between cliché and research-paper flat.
- Be warm and direct. Softening a position to avoid discomfort isn't warmth; credit people by name and by specific contribution.

## Asks and calls to action

- Specific: what, from whom, by when.
- Make acting easy. For a decision, frame the options. For an introduction, say to whom and why.
- Three asks at most in any piece. Marketing pieces get one call to action.
- Link and button text says where it goes ("See the pricing table"), never "click here."

## Length

- Every sentence advances understanding or enables action. Cut the rest.
- Every word and phrase earns its place too. The test: delete it and reread. If the meaning, the precision and the voice survive, it stays deleted. This catches connective padding ("With that in mind," "That said," "As mentioned," "Building on this"), scope framing ("Across all of it," "In every case"), restated setup and empty qualifiers.
- Watch hardest for phrases that point back at an earlier idea ("this," "that," "it," "all of it," "the above") instead of adding a new one. They feel like cohesion and carry no meaning. If a back-reference is needed, replace the pronoun with the concrete noun and make the sentence active.
- Length follows content. Padding thin content and compressing dense content are both failures.
- Say each thing once.

## Titles, headings and section labels

Applies to every title, heading, subheading, section break, table caption, callout label, slide title and email subject line in every piece.

- Each one names the specific content beneath it. A reader scanning only the headings learns what the piece says, not just what kinds of sections it has.
- The test: could this heading sit unchanged on a section of a different document? If yes, it's generic. Rewrite it from the section's own content.
- Generic labels to rewrite: "Overview," "Introduction," "Background," "What it does," "How it works," "Features," "Benefits," "Key takeaways," "The opportunity," "Why it matters," "Next steps," "Conclusion," "Summary," "About," "Getting started."
- Examples:
  - "What it does" → "Five steps from draft to publish-ready"
  - "Key takeaways" → "Churn fell 12% after the onboarding redesign"
  - "Next steps" → "Three decisions needed by 30 June"
  - "About me" → "Former reporter, now building sales software"
- Cut vague evocative lines too ("When the to-do list stops being yours"). Specific beats clever.
- Short functional labels stay when readers look for them by name and the content is standard: "Install," "License," "Contact," "FAQ." Even then, prefer a specific version when it fits ("Install in Claude Code").
- If a section's content is too mixed to name specifically, the section is doing too much. Split it.

## Structure in formatted pieces

- No thin or orphan sections. Merge or cut stubs.
- Each section opens with a full sentence that connects to what came before and ends on a point, not a trail-off.
- Use lists, tables and checklists where they help the reader scan or compare, not as decoration. One plain line before every table says what it shows.
- Resolve optional items into finished copy. Nothing like "[optional: add a line here?]" in the body.
- Keep layout instructions and asset markers (`[LOGO]`, "two columns here") out of the copy.

## Quotes and attribution

- Quotes are real, verbatim and attributed.
- Introduce a speaker before quoting them: full name and title on first mention.
- Don't quote the brand as an authority in its own piece. Quote customers or named outside experts.

## Mechanics

- No apostrophe to pluralize numbers or prices: "the 1990s," "the $400s."
- Subject-verb agreement, including collective nouns ("the team is").
- Timeframes no tighter than the source confirms: "summer 2026," not "early summer 2026," unless the source says early.
- Dashes, capitalization, numerals and serial commas follow the user's style guide. Without one, be consistent within the piece.
