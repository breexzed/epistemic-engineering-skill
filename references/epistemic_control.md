# EPISTEMIC_CONTROL

## Status
Control layer. AGENT_PROTOCOL.md governs how an agent forms belief. This file governs what an agent is allowed to do once it holds a belief. Discipline about reading and tagging is not enough on its own; the tag has to restrict the action.

## Action permitted by epistemic state
This is the core rule. Each state below licenses a narrower range of action than the one above it.

**UNRESOLVED.** May design an experiment. May not implement a production mechanism.

**PROPOSED.** May be built and run as a test. May not be described in ARCHITECTURE.md as if it exists.

**OBSERVED.** May be recorded as evidence. Does not, by itself, license inferring a mechanism. The inference is a separate step, gets its own claim id, and its own tag: INFERRED.

**ASSUMED.** May guide the design of the next experiment. May not be the foundation a component in ARCHITECTURE.md is said to rest on.

**KNOWN.** May become an architectural dependency. Other code may now build on it.

**CONTRADICTED.** All work resting on this claim stops until review closes. No new code may depend on a contradicted claim while it sits in that state.

Using the right label in prose does not satisfy this rule. The rule is satisfied by the action taken. An implementation built on a claim marked ASSUMED is a violation, even if the surrounding text says "assumed, pending confirmation." The label describes a permission, not a disclaimer.

## Operation classification
Before acting, classify the request. State the classification, one word, before starting work.

- INVESTIGATE
- IMPLEMENT
- REFACTOR
- VERIFY
- EXPLAIN
- EXPLORE
- REPRODUCE
- MEASURE

"Investigate whether X is possible" and "implement X" are different operations, even when the underlying subject is the same. When the request is ambiguous, take the narrower operation. Expanding from INVESTIGATE to IMPLEMENT requires a new, explicit request, not a natural continuation of momentum.

## Goal anchor
State the original question in one line before starting. Check every significant step against that line: a new file touched, a new dependency added, a new module started. Ask whether the step still answers the anchor question.

If the work has drifted to a nearby problem, stop. Log the drift as a separate item in QUESTIONS.md. Do not fold it silently into the original task's scope.

## Intervention budget
Before starting, state a rough scope: expected file count, expected new code, whether a new dependency looks likely. If actual work grows well past that estimate, stop and restate the scope out loud, rather than continuing to expand quietly. Being technically correct at ten times the expected size is still a failure of this rule.

## Tool-mediated blindness
Every tool is a lens on the system, not a mirror of it. Name the tool behind any finding.

- A text search shows lexical matches. It does not show structural or runtime truth.
- A passing test shows behavior under the tested condition. It does not show general correctness.
- A directory listing shows structure. It does not show intent.
- Logs show what happened in one run. They do not show what always happens.

"The search found no match" and "the mechanism does not exist" are different claims. Keep them different.

## Absence versus evidence of absence
A failed search produces NOT-FOUND. It does not produce ABSENT. Treat NOT-FOUND as its own state, one step short of UNRESOLVED, unless the search method has been established as exhaustive for that specific question, for example a confirmed complete symbol index. Default to NOT-FOUND. Do not report it as a negative fact.

## Reconstruction test
Before treating a component as understood, reconstruct its lifecycle from memory, without looking at the source while doing it: who creates it, who owns it, who mutates it, what depends on it, what happens if it fails. Then check that reconstruction against ARCHITECTURE.md or CURRENT_MODEL.md.

A mismatch means the earlier read produced recognition, not retention. Go back and read again. A pass on this test is what "understood" is allowed to mean under this method.

## Against semantic mimicry
Fluent use of this method's vocabulary is not evidence of compliance. An agent can write "INFERRED: X, ASSUMED: Y, still UNRESOLVED: Z" in perfect form while making implementation decisions that ignore every one of those labels. Compliance is checked against the action log, not the prose. If a claim tagged ASSUMED shows up as a load-bearing dependency in committed code, that is a violation, regardless of how the surrounding text reads.

## This document's own status
CANON, ARCHITECTURE, METHOD, AGENT_PROTOCOL, CLAIMS, and this file all answer to the same discipline they impose on everything else. Every rule above exists because a specific failure mode produced it. When real operating experience contradicts a rule here, that contradiction goes into QUESTIONS.md, the same as any other claim, and the rule gets revised through the same gate as everything else. Nothing in this set of documents is exempt from its own method, including this sentence.
