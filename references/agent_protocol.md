# AGENT_PROTOCOL

## Status
Operational. Applies to any agent, human or automated, that reads CANON, ARCHITECTURE, CURRENT_MODEL, QUESTIONS, or CLAIMS, or writes code against a project governed by this method.

## The failure this file stops
An agent has context available. It does not treat that context as authoritative. It reconstructs reality instead from whatever is easiest to retrieve: a nearby file, a filename, a first search result, a passing test. The convenient source quietly replaces the given one. This file makes that swap harder to do by accident.

## Epistemic status tags
Every claim an agent holds during work carries one tag. Write the tag down, not just the claim.

- **USER-STATED**: the user said it directly.
- **KNOWN**: gate-cleared, cited in ARCHITECTURE.md.
- **OBSERVED**: raw output from a run, a log, a test. Not yet interpreted.
- **ASSUMED**: in CURRENT_MODEL.md, unconfirmed, explicitly provisional.
- **INFERRED**: the agent drew it from evidence, nobody stated it directly.
- **PROPOSED**: a candidate mechanism, awaiting the gate.
- **UNRESOLVED**: in QUESTIONS.md, open.
- **AGENT-GENERATED**: the agent produced this text or code; it did not come from a source.

Rule: a tag never upgrades silently. ASSUMED becomes KNOWN only by clearing the gate in METHOD.md. USER-STATED does not get demoted because a search turned up something that looked different nearby.

## Authority order
When sources disagree, higher wins, for the purpose of deciding what to do next.

1. User-stated fact, this conversation or CANON.
2. OBSERVED: actual execution, actual test output.
3. ARCHITECTURE.md, KNOWN, gate-cleared.
4. Source code as executed, not skimmed.
5. CANON.md hypotheses and explicit constraints.
6. CURRENT_MODEL.md, ASSUMED.
7. QUESTIONS.md, UNRESOLVED. Treating an open question as answered is not permitted at any level.
8. Agent's own fresh search results, filenames, nearby code, README text, package docs, general convention. Lowest authority. Never overrides 1 through 7.

Authority decides which claim controls the next action. It does not decide which claim is true. See `claims.md` for the distinction and for how contradictions get logged instead of silently resolved.

## Rules by failure cluster

**Partial or diluted intake.**
Read a document in full before acting on it. For long documents, work through it section by section against a checklist of what the task needs; never treat a partial read as the whole. If the user already stated something, tag it USER-STATED and stop searching for it elsewhere. Before summarizing any document, pull out its negative constraints, its prohibitions, into an explicit list first. Summaries lose exactly that kind of detail.

**Locality and false authority.**
The nearest matching code is not automatically the governing code. Before editing anything, check whether ARCHITECTURE.md names it. If it isn't there, it is a candidate at best, not a target for direct modification. Filenames are not specifications; check the project's own module or component spec instead of guessing meaning from a name like `manager.py`.

**Premature resolution.**
Ambiguity routes to QUESTIONS.md, not to code. An assumption stays visibly tagged ASSUMED in every sentence downstream that depends on it; it never quietly becomes "the system expects." A negative instruction ("don't add X yet") gets logged as a boundary and checked before every implementation step, not noted once and forgotten. "Not yet resolved, here is what would resolve it" is a complete, acceptable answer. It is not a failure to produce a fix.

**Convention and framework override.**
An unconventional structure in a project is intentional until CANON says otherwise. A new dependency or framework feature has to clear the same gate as anything else: representation, executable path, test, observation. It also has to trace to a specific entry in QUESTIONS.md that it answers. "This is how it's normally done" is not a reason on its own.

**Implementation before understanding.**
Before touching code, write down what state it touches, who owns that state, its lifecycle, and the causal path from input to effect. This goes in CURRENT_MODEL.md or an experiment note before the code, not after. A change counts as successful when system behavior matches what CANON or ARCHITECTURE says should happen, checked explicitly, not when a diff applies cleanly.

**False confidence from tests.**
A passing test establishes only the behavior it tests, tagged OBSERVED for that behavior, not KNOWN for the surrounding architecture. When something breaks, state the causal mechanism before patching. If the mechanism can't be stated, the fix goes to QUESTIONS.md instead of into the code as a quiet patch.

**Fictional architecture.**
This is what the gate in METHOD.md exists to stop. Every ARCHITECTURE.md entry cites a file, a test, an observation, and a CLAIMS.md id. No agent writes an entry describing a component it only intended to build. When an agent generates a new document, it links back to the source context it compressed. The original source stays in place; it is not treated as superseded by the summary.

**Overreach on completion.**
Producing a plan, code, and tests is not the same as answering the question that motivated the work. Every deliverable states which entry in QUESTIONS.md it addresses, and whether it actually closes that entry or just produces more open ones.

## Checklist before writing any code
1. What did the user state directly? Tag it. Do not re-derive it from a search.
2. What does CANON mark in scope, out of scope, or a non-goal?
3. What does ARCHITECTURE currently say exists? Nothing else is real yet.
4. What does CURRENT_MODEL assume here? Is this task resting on one of those assumptions? Flag it.
5. What does QUESTIONS mark open, that this task touches?
6. Is this an experiment testing a hypothesis, or an implementation on a gate-cleared mechanism? If unclear, treat it as an experiment.
7. State state-ownership, lifecycle, and causal path before editing anything.
8. After running it, write down the observation before deciding what it means.

## What this file does not do
It does not replace the gate in METHOD.md. It gives the discipline needed to reach that gate honestly, instead of arriving there through whatever evidence happened to be closest at hand.
