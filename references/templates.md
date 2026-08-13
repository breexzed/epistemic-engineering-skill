# TEMPLATES

Fill these in during bootstrap. Follow `writing_style.md` while filling them. Confirm CANON.md with the user before treating it as settled; everything else in this file can be generated once CANON.md is confirmed.

---

## CANON.md template

```markdown
# CANON

## Status
Prior, not specification. Changes rarely, only by deliberate amendment logged below.

## Purpose
<One paragraph. The problem, who has it, what they do today instead of using this.>

## Distinctions
<The working conceptual cuts this project reasons with. Pull these from the interview; don't invent them. If the user couldn't name any yet, leave this section with a note: "not yet defined, revisit after first experiments produce some.">

## Controlled vocabulary
<Terms that get used constantly, each with one fixed meaning. A word not listed here shouldn't be used in ARCHITECTURE.md as if it names something real.>

- **<Term>**: <definition>

## Hypotheses
<Numbered, each with a falsification condition. Pull these directly from what the user flagged as unverified during the interview.>

**H1.** <claim>. Falsified if <specific observation>.

## Boundaries
In scope: <>
Out of scope for now: <>

## Non-goals
<What this project deliberately does not commit to yet: vendors, frameworks, architecture patterns named as candidates, not commitments.>

## Governing rules
1. No claim enters ARCHITECTURE.md without a concrete representation, an executable path, a passing test, and an observed consequence.
2. Every component named as existing traces to code that runs.
3. Uncertainty gets written down, not smoothed over. QUESTIONS.md holds what is unresolved.
4. CANON changes rarely, by amendment only. ARCHITECTURE changes constantly, as evidence accumulates.
5. METHOD.md governs how this project moves from idea to structure.
6. AGENT_PROTOCOL.md and EPISTEMIC_CONTROL.md govern what an agent may do with any claim in this document. They apply before any of the above are acted on.

## Amendment log
- <date>: initial version, from bootstrap interview.
```

---

## ARCHITECTURE.md template (genesis state)

```markdown
# ARCHITECTURE

## Status
Posterior. States only what has cleared the gate in METHOD.md: representation, executable path, test, observed consequence.

## Current state of the system
As of this writing, no component has cleared the gate. This is not a documentation gap. It is the accurate state of the project.

## How this file grows
Each entry cites: the file and function where the component lives, the test that exercises it, the CLAIMS.md id, and the observation showing it behaving as claimed.

## Template for future entries

### <Component name>
Representation: <file / function>
Executable path: <what calls it, under what condition>
Test: <test name, what it checks>
Claim: <CLAIMS.md id>
Observation: <what was logged or measured, with a date>
Status: confirmed / partially confirmed / contradicted
```

---

## CURRENT_MODEL.md template (genesis state)

```markdown
# CURRENT_MODEL

## Status
Working sketch. Provisional. Used to plan the next experiment, not to describe what exists. Every line here is a belief, not a fact.

## What we believe right now, and why

<Empty at genesis. As beliefs form, add one entry per belief:>

**Belief: <statement>.**
Basis: <where this came from, and how solid it actually is>.

## Revision rule
When an experiment confirms or contradicts a belief here, update this file right away. Confirmed and gate-cleared: move it to ARCHITECTURE.md, remove it here. Contradicted: strike it, record what was learned in QUESTIONS.md as a closed question.
```

---

## QUESTIONS.md template

```markdown
# QUESTIONS

## Status
The honest ledger of what remains unknown. Closing a question, by graduation into ARCHITECTURE or by falsification, is the only unit of real progress.

## Format
Each question names the hypothesis it tests, what would count as an answer, and its current status.

### Q1. <question>
Tests: <hypothesis id, if any>
Answered by: <specific, checkable observation>
Status: open

## Closed questions
<none yet>
```

---

## CLAIMS.md and AGENT_PROTOCOL.md and EPISTEMIC_CONTROL.md

Copy these three unmodified from the `references/` directory of this skill. They are universal, not project-specific. Do not customize them per project; if a real operating experience contradicts a rule in them, that contradiction goes into the project's QUESTIONS.md, not into a rewritten version of these files.

---

## PRD pattern (only if the user wants an implementation-facing spec)

Write this after CANON.md is confirmed. Every requirement in it should trace back to something CANON already established; don't introduce new hypotheses here.

```markdown
# PRD — <project name>

Governed by CANON.md and METHOD.md. AGENT_PROTOCOL.md and EPISTEMIC_CONTROL.md govern how you're permitted to act on this document. Read all four before touching code.

## Problem
<One or two paragraphs, concrete, no adjectives without numbers.>

## What we're building
<One paragraph, plain description of the system.>

## Functional requirements
<Concrete, testable, one requirement per heading. Each should be traceable to a CANON hypothesis or boundary.>

## System components
<A table: component, file, inputs, outputs, what it owns. Mark clearly that these are candidates, not built reality, until ARCHITECTURE.md says otherwise.>

## Data contracts
<Concrete schemas, not descriptions of schemas.>

## Candidate stack
<Name tools. State plainly that none are commitments until code built on them clears the gate.>

## Build sequence
Before any phase starts, read AGENT_PROTOCOL.md and EPISTEMIC_CONTROL.md in full. They govern what you're allowed to do with everything below, not just how to read it.

<Phased plan, concrete milestones, each phase ending with an ARCHITECTURE.md and QUESTIONS.md update.>

## Known risks
<Pull straight from QUESTIONS.md, don't restate them differently here. Reference the question ids.>

## What this document is not
This is not a claim that the system described exists. It is a build target, gated the same way everything else is.
```
