# WRITING_STYLE

## Status
Applies to every document this skill generates, and every explanation Claude gives while this skill is loaded. Not a preference. A rule.

## The rules

**Keep sentences under 30 words.** One idea per sentence. Don't stack three justifications into one sentence. Break it up. Use a bullet list instead if the ideas are parallel.

**Cut qualifiers.** Drop "I think," "I feel," "it's worth considering." "We need to increase the timeout" beats "I think we should maybe consider increasing the timeout." Take the stand.

**Replace adjectives with data.** "Performance improved dramatically" is fluff. "Latency dropped from 800ms to 120ms" is a fact. Whenever an adjective shows up, stop and find the number behind it. If there's no number, that's a sign the claim isn't ready to be stated as settled; check `agent_protocol.md` on tags before writing it down as fact.

**Pass the "so what" test.** If a reader can't tell what to do after reading a sentence, cut it or rewrite it. This applies to background and setup too. Don't recap what the reader already knows. Say who, what changes, and by when.

**Avoid jargon and unexplained acronyms.** Define a term the first time it's used, briefly, in parentheses. After that, use it bare. If a word is already defined in the project's controlled vocabulary (CANON.md), don't redefine it, just use it correctly.

**Use subject-verb-object sentences.** Who did what to what. "The parser rejects malformed input" beats "malformed input is not accepted by the system in cases where parsing constraints are violated." Simple structure produces shorter sentences and fewer adjectives on its own.

**Cut a full draft by a third before calling it done.** Write it, then remove a third of the words. What's left is almost always clearer.

**No unnecessary flourish.** No em-dashes standing in for a real sentence break. No rule-of-three lists used as a rhetorical device rather than genuine enumeration. No "let me explain why I'm explaining this" framing. No landing-sentence summaries that just restate what was already said. Say the thing once, plainly, and stop.

## Why this belongs inside this skill
The documents this skill produces exist to separate what's proven from what's assumed. Vague, adjective-heavy, hedge-loaded prose is exactly the kind of writing that lets an assumption pass as a fact without anyone noticing. Plain, specific, falsifiable sentences are not a style choice here. They are part of how the epistemic discipline gets enforced. A claim written in wishy-washy language is much harder to check than "on-time delivery went from 82% to 91%." Precision in writing and precision in evidence are the same discipline, applied to two different layers of the same problem.

## Quick self-check before finalizing any document
- Does every claim of improvement have a number attached, or is it explicitly tagged ASSUMED/PROPOSED?
- Could a reader tell, from this sentence alone, what to do next?
- Is there a sentence here purely for tone, rhythm, or reassurance? Cut it.
- Did the draft get cut by roughly a third from its first pass?
