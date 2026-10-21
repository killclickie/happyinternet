# AI tells and formula

Patterns that make writing read as machine-made or templated. Readers spot them in a line and stop trusting the rest. Each is banned by default. Keep one only when it's the plainest way to say the thing, and log why in the change log. `scripts/scan.py` flags most of these; the reviewer still reads for the ones a regex can't catch.

The fix is almost always the same: **delete the setup and state the point.**

## Structures

| Pattern | Looks like | Fix |
|---|---|---|
| Contrast reframe | "It's not X, it's Y." "This isn't about X. It's about Y." "Not just X, but Y." "X isn't the problem. Y is." | State Y. The reader never thought X. |
| Reassure, reframe, tie a bow | "None of this means your process is broken. These are integration gaps, not people problems, and they're exactly what a connection is built to fix." | Say the real point once, without the reassurance, the reframe or the neat resolution. |
| Tidy diagnosis | "the gap," "these are X gaps," "the real problem," "that's exactly what...," "what X is built for" | Name the specific thing that's happening or missing. |
| Setup question or cliffhanger | "The catch?" "Honestly?" "The truth?" "The result?" "Why does this matter?" "Here's the thing:" "Here's the kicker:" "Plot twist:" | Delete the question. Write the answer as a full sentence. |
| Meta-narration | "Let me explain." "Here's what I learned." "What I want to talk about is..." "The truth is..." "If I'm honest..." "This section is the most important." | Cut the announcement, keep the point. |
| Canned opener | "Picture this." "Imagine a world where..." "In today's fast-paced world..." "Let's dive in." "Here's what nobody talks about." "More often than most want to admit." | Open on the point, the news or the specific detail. |
| Neat closer | "At the end of the day..." "The bottom line?" "And that makes all the difference." "Let that sink in." "Read that again." | End on the last substantive sentence. |
| Run of dramatic fragments | "This is execution. One deadline. Zero room for error." | Complete sentences. One fragment can land; three in a row is a formula. |
| Stacked negation | "No delays. No back-and-forth. No surprises." | Say what the reader gets, once, positively. |
| Reflexive triplets | Three adjectives, three parallel clauses, three beats, paragraph after paragraph | Use as many items as the content has. Two is fine. Four is fine. |
| Em-dash asides and pivots | "You choose how it runs (manual or automatic, PCR or biodegradable) from one supplier" written with paired em dashes; "and then everything changed" after an em dash | Colon, comma, period or parentheses. Default to zero em dashes. |
| Performed epiphany | "I finally realized..." "It finally clicked." "That's when it hit me." | Say what happened. |
| Humble brag | "I don't take that for granted." "I'm lucky enough to..." "Not bad for..." "Pinch-me moment." "Humbled to announce." "Beyond grateful." | State the news or the fact. Gratitude, if real, goes to named people for named things. |
| Vague back-reference | A sentence opening "That kind of opportunity...," "This moment...," "That combination..." pointing at an idea, not a noun | Restate the concrete thing, or cut the sentence. |
| Back-reference filler | "Across all of it...," "Through it all...," "In all of this...," "With that in mind...," "That said...," "Given all this...," "Building on this...," "As mentioned...," "To that end...," "This is where X comes in." A pronoun or "the above" pointing back at an earlier idea to connect or frame a sentence without adding meaning | Cut the phrase. If the scope matters, state it actively with the concrete noun: "Every report we ship fits on one page," not "Across all of it, we value brevity." |
| Colon-label setup | "My first project: rebuilding..." "The goal: more referrals." "The result: 40% growth." A short label plus a colon standing in for a sentence | Write the full sentence, usually with the fact as the subject. |
| Vague consequence | "That shapes how we work." "This changes the way teams operate." "...which drives everything we do." "It informs every decision." A pronoun plus an influence verb (shapes, changes, defines, drives, informs, colors, transforms, underpins, influences) that asserts an effect without saying what it is | Name the specific thing affected and how: "The 48-hour SLA sets our staffing rota." If the effect can't be named, cut the sentence. |
| Inflated scope | "That shapes everything." "It changes everything." "...touches every part of the business." "...in every way." "Changed it all." "The whole game." Sweeping words (everything, every, all, entire, whole, always) attached to a claim the author made smaller or didn't make | Keep only the scope the author wrote. If the author said "shaped our pricing," it stays "pricing," never "everything." Sweeping scope the author did write goes to To-verify unless the draft supports it. |
| "Quietly" intensifier | "Costs are quietly climbing." "It's quietly reshaping the category." | Say what's happening and how fast. |
| Unclear to the intended reader | A new subject with no setting ("A phone call carries 15 metres." in a post about office costs); an outcome with no mechanism ("Put the returns policy in the box."); a vague tail ("...and links to the customer journey behind it."); an unintroduced "the pivot" or "Mara's team" | Follow `craft.md`, Clear to the intended reader: anchor the setting, state the mechanism from the sources, cut the tail, or list it under Needs context. Terms the stated reader knows stay. Never invent the missing piece. |
| Parable | A stranger, driver, child or janitor delivers a business lesson | Keep a story only if it's true and its point is specific to the author's work. Otherwise state the point. |

## Words and phrases

**Filler adverbs.** actually, really, simply, just, literally, basically, truly, very, quite, incredibly, genuinely, honestly, definitely, absolutely. Cut unless removing the word changes the meaning.

**Hedges.** I think, I feel like, it seems, arguably, hopefully, perhaps, might potentially, in some ways. Make the claim, or state the specific uncertainty once.

**AI vocabulary.** delve, tapestry, landscape (figurative), navigate (figurative), realm, unlock, unleash, elevate, empower, leverage (as a verb), harness, seamless, robust, cutting-edge, game-changer, transformative, revolutionize, synergy, holistic, pivotal, testament to, ever-evolving, fast-paced, embark, journey (figurative), foster, streamline, supercharge, next-level, deep dive, best-in-class, world-class, solution (as a vague noun). Replace with the plain, specific word.

**Internet idioms.** hits different, lives rent free, it's giving, no notes, chef's kiss, the way I..., main character energy, obsessed (as praise), unhinged (as praise). Say what is different and why.

**Tired metaphors.** move the needle, low-hanging fruit, keep the lights on, out of left field, slice of the pie, north star, double-click on, boil the ocean, secret sauce. Say the literal thing.

**Outsourced calls to action.** reach out, hit reply, drop me a line, shoot me a note, ping me, feel free to. Write the ask itself: "Reply with your top two dates," or just ask the question.

**Email filler.** hope this finds you well, just checking in, circling back, touching base, following up on, per my last email, as previously discussed, I know you're busy. Open with the point or the ask.

**Announcement inflation.** thrilled, excited, humbled, honored, delighted to announce/share. Lead with the news itself.

## Formatting

- Bold scattered through body text for emphasis. Let sentence structure carry emphasis.
- Emoji used as bullets or section markers (✅ 🚀 👉 💡 🔥 📈).
- Headings on a piece short enough to read in one screen.
- Unicode "bold" or "italic" letters (𝗹𝗶𝗸𝗲 𝘁𝗵𝗶𝘀). Screen readers can't read them and search can't index them.
- Every sentence on its own line, separated by blank lines (see LinkedIn in `channels.md`).
- "Thread 🧵," "👇," "A short thread:" announcing structure.
