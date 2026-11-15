# Channel rules

Apply only the section for the piece's channel. These rules sit on top of `craft.md` and `ai-tells.md` and win where they conflict.

## LinkedIn

LinkedIn is where AI formula is most visible and most tiring to read. A post should sound like a specific person who knows their subject, talking to peers.

**Posts**
- **The opening carries the point.** Only the first two or three lines (roughly 200 characters, depending on device) show before "...see more." Put the news, the claim or the most specific detail there. Cut hooks that withhold it ("I almost didn't post this." "Something happened yesterday that changed everything.").
- **Lead with the news.** "We closed a €2M seed round led by X." Not "I'm thrilled and humbled to announce..." Emotion words stay only if the author wrote them and they add information.
- **One idea per post.** If it needs ten lessons, it's an article or a carousel.
- **Paragraphs, not broetry.** Short paragraphs of one to three sentences read well. A column of single sentences, each on its own line, reads as a formula. Group lines that make one point.
- **Specific and true.** Real numbers, real places, named people (with their permission). No invented dialogue, no composite characters presented as real, no parables of strangers handing out business wisdom.
- **Lessons earn their place.** In a "what I learned" post, keep lessons specific to the author's experience. Cut any lesson anyone could have written without living it.
- **No performed vulnerability.** A failure story says what happened, what it cost and what changed. It isn't a setup for a win.
- **No humble brags** (see `ai-tells.md`).
- **No engagement bait.** "Agree?" "Thoughts?" "Comment YES and I'll send it." "Repost if..." "Follow for more." "Tag someone who..." End on the point, or on a specific question the author wants answered ("Which of these have you tried with enterprise buyers?").
- **Credit specifically.** Tag only people involved and say what each did. No tag-farming.
- **Hashtags**: zero to three, specific, at the end. Never mid-sentence.
- **Emoji**: zero to a few. Never as bullets, never in place of words.
- **No Unicode bold or italic text.**
- **Links**: one sentence on what the reader gets behind the link.
- **Images**: add alt text.
- **Length**: posts have a 3,000-character limit. Most strong posts are well under it. `scan.py` reports the count and the preview.
- **The test**: would the author say this out loud to a respected colleague, in these words? If not, rewrite until they would.

**Profile copy** (headline, About, experience)
- Headline: what you do and for whom. No pipe-separated buzzword stacks ("Visionary | Thought Leader | Passionate about Innovation").
- About: first person. The first two lines say what you do and what you're known for, since that's what shows before "see more."
- Experience: each bullet starts with an active verb and ends with a result. "I" for your own work.

## Other social

- **Limits**: X 280 characters on standard accounts, Threads 500, Bluesky 300, Instagram captions 2,200. `scan.py` checks them.
- The first line carries the point.
- LinkedIn's rules on engagement bait, emoji, Unicode text, humble brags and broetry apply here too.
- Hashtags follow the platform's norms: few and specific; on Instagram they can sit in a separate block at the end.

## Email

- The first sentence is the point or the ask. No greeting followed by a filler sentence.
- Length scales to stakes: a confirmation is one line; a multi-party decision gets structure.
- Two or more questions get numbers, so replies can answer by number.
- The subject line says what's inside and any deadline.
- A follow-up carries one specific question or a time reference. No guilt language.
- A forwarded item gets one line on why it matters to this recipient.
- Cold outreach: where you found them or who connected you; one specific observation about their work; what you offer, stated as fact; a concrete next step with specific times. No list of achievements.
- Newsletters and marketing emails: one promise, one call to action, skimmable.
- Exclamation marks: rare.

## Web and long-form (blog posts, webpages, landing pages, articles)

- Landing pages: one promise, one call to action.
- If the title promises an outcome ("how to choose," "how to prevent"), one consolidated section delivers it.
- Mix in a table, checklist or list where it helps the reader; one or two well-placed, never wall-to-wall.
- In the summary, name the one or two highest-value lines a designer could pull out. Don't bold them in the copy.

**SEO/AEO mode only** (the user said the piece is web content or for search or answer engines):
- Put the primary keyword in the title or title tag, the H1, at least one H2, the first 100 words, the URL slug, the meta description and image alt text. Placement beats repetition; never stuff.
- Use secondary phrases where they read naturally.
- If the piece answers a question, use that question verbatim as a heading or FAQ entry with a self-contained, quotable answer.
- Add key takeaways, an extractable table or checklist, an FAQ pitched at the target reader's level (never beginner questions that attract the wrong buyer), and schema notes. These surfaces go in the summary or a clearly labeled section the user can lift, never mixed into the body without being asked.
- H2s are specific and searchable. No hollow rhetorical-question headings.

## Reports, proposals and memos

- Summary first: the finding, the recommendation and the ask.
- `craft.md` "Thinking" applies in full.
- Number the decisions you need from the reader.

## Formatted documents (when the deliverable is a file)

- Keep the original's template, fonts and styles. If there is none, keep it simple: consistent heading levels, one readable body font.
- Heading levels never skip, and bold body text never stands in for a heading.
- Paragraph spacing renders as real space. When converting HTML into a word-processor file, many importers ignore CSS: use spacer paragraphs and inline styles.
- Design and editor notes stay out of the copy, visually distinct if they must travel with it.
- Open or read the file back after creating it. Clean source markup is not proof it looks right.
