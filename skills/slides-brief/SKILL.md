---
name: slides-brief
description: Plans and writes the content for a slide deck: slide-by-slide copy plus a style guide, ready to build in Claude's Slides artifacts or any slide tool. Use whenever the user wants to create, outline, plan or write the content for slides, a deck, a presentation, pitch deck, keynote, talk, webinar or workshop; turn a document, notes, transcript or outline into slides; decide what goes on each slide; or cut down or fix an existing deck. Use it before building any deck, including one built in Slides artifacts. Works for any deck: talks, team and board updates, investor pitches, sales and proposal decks, training and reports. Defaults to the 10/20/30 rule for presented decks: at most 10 slides, 20 minutes, no text under 30 points.
---

# Slides brief

Produces a downloadable `.md` brief: the style guide plus the copy for every slide. It works for any kind of deck, from a conference talk or team update to an investor pitch or client proposal.

The brief is meant for **Claude's Slides artifacts** (Artifacts → Slides), where Claude turns it into the finished deck. It also works with Claude Design or any other slide tool. If the user asks for the deck itself and a Slides artifact type is available in this session, build the deck from the brief instead of stopping at the file.

## Step 1: Gather the inputs

Needed:
- **The content**: an outline, document, notes or transcript, or an existing deck to cut down or fix (read its slides and keep its order). Keep the user's wording and order. Don't add points, reframe them or justify them.
- **The audience**: who is in the room or will receive the deck, and what they already know.
- **Deck type**: talk, update, pitch, proposal, training, report or other. It shapes the slide order (Step 4).
- **Presented or sent**: will someone present this live, or will the deck be sent and read without a presenter? Ask if it isn't clear; the answer sets how much text goes on each slide (Step 3).
- **Time slot**, if the user gives one.

Ask once, in one message, for whatever is missing. Proceed with what arrives.

## Step 2: Set the style

Use the first source that's available, in this order:

1. **Styling the user specifies** in the request.
2. **An existing brand guide, brand kit or design system** for the organization the deck represents: an attached file, a project document, a design-system artifact, or a connected drive.
3. **The organization's own visual style.** Use the organization the user works for or represents; when the deck is tailored to a client or partner and the user wants it in their brand, use the organization being presented to. If it's unclear which, ask one question. Take the style from its website (with a browser tool, read the computed font family, weight, size and colour of headings, body text and buttons; tally background and text colours; take one screenshot for signature details; decline non-essential cookies; close the tab when done) or from an existing deck or PDF by that organization.
4. **Ask the user** for colours, fonts, or a reference deck or site they like. If no answer is possible, use a plain, high-contrast default (one sans-serif Google Font, a dark text colour, one accent) and say so in the reply.

Record fonts (family, weights), a colour table (role and hex value for each colour) and any signature visual details.

## Step 3: Fit the deck to its format

**Presented live (default): the 10/20/30 rule.**
- **No more than 10 slides.**
- **Built for 20 minutes** of talking, leaving time for discussion in a longer slot.
- **No text smaller than 30 points.**

The deck supports the conversation; it doesn't carry it. One idea per slide. Cut every line the speaker will say aloud. A slide should be readable in the time it takes to glance at it.

When the content can't fit without losing something the user needs (a training session, a board pack, a workshop), say so, follow the length the user wants, and keep the other standards below.

**Sent without a presenter.** Ask for context before writing: who reads it, on what screen, what they need to understand or decide, and whether anyone will walk them through it. If no one will, more text is allowed, but only the minimum the reader needs to understand each slide alone:
- The headline states the takeaway as a full sentence.
- At most one short supporting paragraph or a few bullets per slide.
- No text smaller than 20 points.

## Step 4: Write the copy

- Write every line to `slop-stop`'s rules (this plugin): no AI tells, active voice, concrete details over abstractions, and the point first. If the user has their own style guide or voice skill, it takes precedence.
- **Headlines state the takeaway** ("Onboarding dropped from nine days to four"), not a topic label ("Onboarding").
- **At most about 6 short lines per slide; no line wraps** at the specified sizes.
- Keep the user's wording. When you cut or shorten a line, list the cut in the reply.
- Never invent a figure, quote, logo, client name or claim. Prices, terms and dates appear exactly as the user gave them.
- Leave out anything the user says to handle in person (pricing details, terms, sensitive topics).
- No filler slides ("Agenda" on a short deck, "Thank you," "Questions?") unless the user asks for them.
- No exclamation marks.
- **Charts:** one message per chart, stated in the headline; label data directly; highlight the one value that matters.
- **Order by deck type**, unless the user's outline sets one: a talk or update leads with the main point and then the evidence; a pitch or proposal goes problem, approach, proof, terms; a training deck goes outcome first, then one step per slide. Keep the user's order when they give one.

## Step 5: Write the brief

Sections:
1. **Purpose**: audience, presented or sent, time slot, what the audience should know or decide afterwards.
2. **Style**: fonts, colour table, signature details, and where the style came from.
3. **Type size and layout** (see the standards below).
4. **Slides**: for each slide, the headline, the copy, and a short description of any chart, diagram or image.
5. **Notes for the slide builder** (always include; written so Claude's Slides artifacts, Claude Design or any tool can follow them): apply the style guide to every slide with no outside colours or fonts; keep the copy as written; if text doesn't fit at the specified sizes, flag it rather than shrink the type; no speaker notes, logos or images beyond what's described.

Save it as `<topic>-slides-brief.md` and send it as a file.

In the reply:
- One line describing the file.
- Any cuts made to the user's text, any placeholders to fill, and where the style came from.
- How to turn it into the deck. Say it plainly, for example:
  > **Build your deck from this brief:** in Claude, go to Artifacts → Slides and start a new deck. Attach this file (or paste its contents) and ask Claude to "build this deck exactly as briefed." Edit any slide right there in the Slides editor, or ask Claude for changes. When it's done, download it as PowerPoint or PDF, or share the link.

Nothing else.

## Size, type, contrast and image standards

- **Slide size:** 16:9 at 13.33 × 7.5 inches (1920 × 1080 px canvas, so 1 pt = 2 px).
- **Type (presented):** headlines 44–60 pt (88–120 px); body 30–36 pt (60–72 px); nothing below 30 pt.
- **Type (sent):** headlines 36–48 pt; body 20–28 pt; nothing below 20 pt.
- **Contrast:** at least 4.5:1 for body text and 3:1 for large headlines. Light brand accents used as text get a darker variant. Never carry meaning with colour alone.
- **Fonts:** the brand's fonts; otherwise Google Fonts, so the deck renders in Google Slides, PowerPoint and Keynote.
- **Images:** only what the user supplies or describes. No stock photos or clip art. Describe each chart or image in one line so it can carry alt text.
- **Slide numbers** on every slide except the title.
- **No speaker notes** unless the user asks for them.

## Never add strategy, reorder silently or shrink type

- Add strategy, recommendations or rationale the user didn't give.
- Regroup or reorder the user's sections without saying so.
- Shrink type to fit text. Cut the text or flag it.
