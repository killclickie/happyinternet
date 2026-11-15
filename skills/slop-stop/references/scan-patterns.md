# Scan patterns

The checks to run on every draft (Step 2) and again on the revised draft (Step 4). Each hit is a candidate for the reviewer to judge, not a verdict.

**How to run them.** If you can run code, search the draft for the regular expressions below (case-insensitive, line by line) and the phrase lists (whole words, case-insensitive), then apply the structural checks. If you can't run code, read the draft against this file and `ai-tells.md` by hand. Report each hit with its line, the matched text and the fix, grouped by category.

## Phrase lists (match whole words, case-insensitive)

**Filler adverb.** Fix: Cut unless removing it changes the meaning.
actually, really, simply, just, literally, basically, truly, very, quite, incredibly, genuinely, honestly, definitely, absolutely

**Hedge.** Fix: Make the claim, or state the specific uncertainty once.
i think, i feel like, it seems, arguably, hopefully, perhaps, might potentially, in some ways

**AI vocabulary.** Fix: Use the plain, specific word.
delve, delves, delving, tapestry, landscape, navigate, navigating, realm, unlock, unlocks, unlocking, unleash, elevate, elevates, empower, empowers, empowering, leverage, leveraging, harness, seamless, seamlessly, robust, cutting-edge, game-changer, game-changing, transformative, revolutionize, revolutionizing, synergy, holistic, pivotal, testament to, ever-evolving, fast-paced, embark, journey, foster, fostering, streamline, supercharge, next-level, deep dive, best-in-class, world-class, solution, solutions

**Internet idiom.** Fix: Say what is different and why.
hits different, rent free, it's giving, no notes, chef's kiss, main character, obsessed

**Tired metaphor.** Fix: Say the literal thing.
move the needle, low-hanging fruit, keep the lights on, out of left field, slice of the pie, north star, double-click on, boil the ocean, secret sauce

**Outsourced CTA.** Fix: Write the ask itself, or just ask the question.
reach out, hit reply, drop me a line, shoot me a note, ping me, feel free to

**Email filler.** Fix: Open with the point or the ask.
hope this finds you well, hope this email finds you well, checking in, circling back, circle back, touching base, touch base, per my last email, as previously discussed, i know you're busy

**Announcement inflation.** Fix: Lead with the news itself.
thrilled, humbled, excited to announce, excited to share, honored to, delighted to, beyond grateful, pinch-me, pinch me moment

**Humble brag.** Fix: State the fact; thank specific people for specific things.
don't take that for granted, don't take it for granted, do not take that for granted, lucky enough to, not bad for

**Performed epiphany.** Fix: Say what happened.
finally realized, finally understood, finally clicked, it hit me, finally got it

**Meta-narration.** Fix: Cut the announcement, keep the point.
let me explain, here's what i learned, what i actually want to talk about, the truth is, truth be told, if i'm honest, to be honest, here's the real story, this section is the most important, keep this in mind, it's worth noting, it is worth noting, it's important to note, it is important to note

**Canned opener.** Fix: Open on the point, the news or the specific detail.
picture this, imagine a world, in today's, let's dive, nobody talks about, more often than most, in a world where, almost didn't post this, changed everything

**Neat closer.** Fix: End on the last substantive sentence.
at the end of the day, the bottom line, makes all the difference, let that sink in, read that again

**Tidy diagnosis.** Fix: Name the specific thing that's happening or missing.
the gap, the real problem, that's exactly, they're exactly, is built to, are built to, built for this

**Engagement bait.** Fix: End on the point, or a specific question you want answered.
agree?, thoughts?, follow for more, repost if, tag someone, comment below, like if, smash that, drop a comment

## Regular expressions (case-insensitive, per line)

**Contrast reframe.** Fix: State the second half. The reader never thought the first.
```
\b(it'?s|this is|that'?s|it is)\s+not\s+(just\s+|only\s+|about\s+)?[^.?!]{1,60}?[,;:.]\s*(it'?s|but|this is|it is)\b
```

**Contrast reframe.** Fix: State the second half. The reader never thought the first.
```
\b(isn'?t|wasn'?t|aren'?t)\s+(about|the problem|the point|the issue)\b
```

**Contrast reframe.** Fix: State the second half. The reader never thought the first.
```
\bnot\s+(just|only|merely)\s+[^.?!]{1,60}?,?\s+but\b
```

**Contrast reframe.** Fix: State the point directly.
```
\b[\w\s]{1,30}\bnot\s+[\w\s-]{1,30}\bproblems?\b
```

**Inflated scope.** Fix: Keep only the scope the author wrote; name what is affected. Never add 'everything'.
```
\b(shap|chang|defin|driv|transform|influenc|inform|affect|impact|touch|color|colour|underpin|redefin|reshap)\w*\s+(everything|it all|all of (it|this|that)|every\s+\w+|the (whole|entire)\s+\w+|so much)\b
```

**Vague consequence.** Fix: Name the specific thing affected and how, or cut the sentence.
```
(^|[.!?;,:]\s+|\band\s+|\bbut\s+)(that|this|which|it)\s+(really\s+|fundamentally\s+|deeply\s+|ultimately\s+)?(shapes?|changes?|defines?|drives?|transforms?|influences?|informs?|colou?rs?|underpins?|reshapes?|redefines?)\s+(how|what|the way|the ways|our|my|your|their)\b
```

**Vague tail.** Fix: Cut it, or name the specific outcome the draft already states.
```
\b(the\s+)?((business|underlying|human|real)\s+)?(process(es)?|workflows?|story|stories|people|team|work|logic|intent|reasons?|context|journey|systems?)\s+behind\s+(it|them|this|that|each|every)\b|\b(the bigger picture|what (really |truly )?matters( most)?|the (customer|user|buyer) journey|the full (picture|story)|end-to-end experience)\b
```

**Binary contrast.** Fix: State the second half. The reader never thought the first.
```
\b(isn'?t|aren'?t|wasn'?t|is not|are not)\s+[^.?!]{1,40}[.;]\s+(it'?s|they'?re|it is|they are|it was)\b
```

**Dramatic fragments.** Fix: Write one complete sentence with the actual point.
```
\b(that'?s it|that'?s all|that'?s the (whole|entire) (thing|point|story))[.!]\s+(that'?s|this is)\b
```

**Throat-clearing opener.** Fix: Delete it; the next clause is the sentence.
```
\b(let me be clear|to be clear|let'?s be (honest|real)|make no mistake|the reality is|it'?s worth noting( that)?|it is worth noting( that)?)\b
```

**Faux-insight setup.** Fix: State the insight without the setup.
```
\b(what (nobody|no one|most people|everyone) (tells you|talks about|gets wrong|misses|knows)|the part (everyone|nobody|no one|most people) (misses|gets wrong|ignores|forgets)|(the )?secret (nobody|no one) (talks about|tells you)|what they don'?t (teach|tell) you)\b
```

**Superficial analysis.** Fix: Cut the -ing clause and let the fact stand, or give the evidence.
```
,\s+(highlighting|underscoring|showcasing|reflecting|demonstrating|emphasi[sz]ing|signall?ing|illustrating|reinforcing|cementing|solidifying|symboli[sz]ing)\s+(the|its|their|a|an|his|her|our|how)\b
```

**Importance puffery.** Fix: Say what happened and what changed, with the fact.
```
\b(marks? (a|an) (pivotal|significant|major|key|historic|defining|new) (moment|milestone|turning point|chapter|era|step)|(a|stands as a) testament to|plays? (a|an) (crucial|vital|pivotal|key|critical|significant) role|cements? (its|their|his|her) (place|position|status)|underscores? the importance of|stands as a (symbol|reminder|beacon))\b
```

**Weasel attribution.** Fix: Name the source, or own the claim and add it to To-verify.
```
\b((experts?|studies|research|researchers|scientists|analysts|critics|many people|most people|some people) (agree|show|shows|suggest|suggests|say|says|believe|argue|have (shown|found))|it'?s widely (known|believed|accepted|recognized)|according to (experts|research|studies))\b
```

**Filler 'named'.** Fix: Name them, or cut 'named'.
```
\b(having |with )?named\s+(studies|study|authors?|experts?|researchers?|sources?|partners?|customers?|clients?|accounts?|companies|brands?|people|individuals|owners?|contacts?|investors?|institutions?|organi[sz]ations?|stakeholders?|leaders?|examples?|references?|speakers?|advisors?|backers?|users?)\b
```

**Quietly intensifier.** Fix: Say what's happening and how fast.
```
\b(is|are|was|were|been)\s+quietly\s+\w+
```

**Setup question.** Fix: Delete the question; write the answer as a full sentence.
```
(^|[.!?]\s+)(the|here'?s)?\s*(catch|truth|result|kicker|twist|problem|answer|secret|reality|irony|lesson|thing|best part|worst part|honestly|why does this matter|why it matters|so what)\s*[?:]
```

**Setup phrase.** Fix: Delete it; state the point.
```
\b(here'?s the (thing|kicker|deal|catch)|plot twist)\b
```

**Vague back-reference.** Fix: Restate the concrete noun, or cut the sentence.
```
(^|[.!?]\s+)(that|this)\s+(kind|sort|type|moment|combination|feeling|shift|is why|is what|is exactly|right there)\b
```

**Back-reference filler.** Fix: Delete it and reread. If meaning survives, leave it out; otherwise use the concrete noun.
```
(^|[.!?]\s+)(with (that|this|all this) in mind|that said|having said that|given (all )?(this|that|the above)|building on (this|that)|as (mentioned|noted|discussed|outlined)( above| earlier| before)?|to that end|on that note|with (this|that) in place|all of this means|which brings (us|me) to|this is where)\b
```

**Colon-label setup.** Fix: Write the full sentence, usually with the fact as the subject.
```
(^|[.!?]\s+)(my|our|the|their|his|her|your)\s+(\w+\s+){0,2}(project|goal|result|plan|focus|takeaway|lesson|answer|fix|bet|mission|priority|reason|outcome|secret|move|ask)\s*:\s+\S
```

**Back-reference filler.** Fix: Cut it. If scope matters, state it actively with the concrete noun.
```
\b(across|through|throughout|in|beyond|above|underneath|behind|at the (heart|core|end) of)\s+(it all|all of (it|this|that|these|them)|all this|all that|everything|each of (these|them)|every (step|one of these))\b
```

## Structural checks

- **Em dash.** Any `—`, or ` -- ` / ` – ` between words. Fix: use a colon, comma, period or parentheses.
- **Generic heading.** A Markdown heading that is one word, or one of: about, about me, about us, at a glance, background, benefits, conclusion, context, details, example, examples, features, getting started, highlights, how it works, intro, introduction, key benefits, key features, key takeaways, next steps, overview, results, summary, takeaways, the opportunity, the problem, the request, the solution, usage, use, what happens next, what it catches, what it does, what's inside, why it matters, why this matters. Fix: name the specific content beneath it.
- **Run of fragments.** Three or more consecutive sentences of four words or fewer. Fix: write complete sentences; one fragment at most.
- **Stacked negation.** Two or more consecutive short sentences (seven words or fewer) starting with "No," "Zero" or "Never." Fix: say what the reader gets, once, positively.
- **Reflexive triplets.** Three or more "X, Y and Z" lists, at a rate of two or more per 300 words. Fix: use as many items as the content has.
- **Unicode styled text.** Mathematical bold or italic letters (𝗹𝗶𝗸𝗲 𝘁𝗵𝗶𝘀). Fix: plain text.
- **Emoji bullet.** A line that starts with an emoji. Fix: words or a plain list.
- **Bold in body** (social posts and email). Fix: let sentence structure carry emphasis.
- **Broetry.** Six or more paragraphs, 60% or more of them a single short line (15 words or fewer). Fix: group lines that make one point.
- **Hashtags.** Count them. LinkedIn: 0 to 3, at the end. Any hashtag mid-text: move to the end or cut.
- **Emoji and exclamation marks.** Count them and report.

## Channel limits

Characters, including spaces: LinkedIn 3,000; X 280; Threads 500; Bluesky 300; Instagram 2,200. On LinkedIn, also quote the first 200 characters (the preview before "see more") and check that it carries the point, the news or a specific detail.
