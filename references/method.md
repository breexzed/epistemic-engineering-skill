# METHOD

## What this file is
The machine that turns uncertainty into warranted structure. Every document in the set sits on this loop. This file describes the loop, not any particular system.

## The loop

```
HYPOTHESIS
    |
    v
  CANON
    |
constrains inquiry
    |
    v
EXPERIMENT
    |
    v
  CODE
    |
    v
OBSERVATION
    |
    v
ARCHITECTURE
    |
exposes what is known
    |
    v
QUESTIONS
    |
    +--> NEXT EXPERIMENT
```

A hypothesis starts in CANON as a named, falsifiable claim. Building begins with an experiment designed to test one hypothesis, not to deliver a feature. The experiment produces code. Running the code produces observations: logs, timings, failures, successes. Only observations update ARCHITECTURE, never intentions. ARCHITECTURE, once updated, exposes gaps. Those gaps become the next round of QUESTIONS. Questions feed the next experiment.

## Transition rules

**Idea to hypothesis.** An idea becomes a hypothesis when it can be stated in a form a specific observation could disprove. "This approach is better" is an idea. "This approach produces fewer errors than the current one, measured over a real batch of cases" is a hypothesis.

**Hypothesis to experiment.** A hypothesis becomes an experiment when someone defines the smallest code able to produce a confirming or disconfirming observation. The experiment tests one hypothesis. It does not ship a product.

**Experiment to observation.** Running the experiment produces a log, a number, a failure trace. This is raw. It is not yet interpreted.

**Observation to mechanism.** A mechanism explains why the observation happened, stated in terms of the code. Mechanisms stay proposed until repeated observation supports them.

**Mechanism to architecture.** A mechanism graduates into ARCHITECTURE.md once it clears the gate below.

**Architecture to invariant.** A component documented in ARCHITECTURE long enough, under enough load, without contradiction, earns the name invariant: a property future code may depend on.

**Invariant to future constraint.** Once named, an invariant restricts what future experiments may assume. Breaking an invariant reopens it as a question. It does not get quietly worked around.

## The gate
A concept enters ARCHITECTURE.md only if all four hold:

1. A concrete representation exists: a file, a schema, a named function.
2. An executable path exists: something actually calls it.
3. A test exists that checks behavior, not just presence.
4. An observable consequence exists: a log, a metric, a state change someone can point to.

Missing any one, the concept stays in CANON as a hypothesis or in QUESTIONS as open. A finished-sounding diagram does not clear the gate.

## What this prevents
Without the gate:

```
imagination -> architecture document -> assumed reality -> implementation built around fiction
```

A confident diagram gets written. People start treating it as running code. Code gets built to match the diagram's assumptions instead of measured behavior. Nobody notices until production.

With the gate:

```
uncertainty -> experiment -> evidence -> claim -> representation
```

Nothing gets documented as real until it has run and been watched.

## Document roles

**CANON.md** is a prior. It states the space of legitimate inquiry: purpose, distinctions, vocabulary, hypotheses, boundaries, non-goals. It does not say how the software works. It says which questions matter and what would count as an answer. It changes rarely, and it is user-defined; it is not the agent's to invent.

**ARCHITECTURE.md** is a posterior. Given the inquiry CANON defines, it states what current evidence supports. It changes often, whenever evidence accumulates or contradicts an entry. It never describes a component as existing when the gate has not been cleared.

**CURRENT_MODEL.md** is the working sketch used to plan the next experiment. Unlike ARCHITECTURE, it may hold provisional beliefs and borrowed assumptions, explicitly marked unconfirmed.

**QUESTIONS.md** is the honest ledger of what remains unknown. An entry here is not a failure. Closing one, by graduation into ARCHITECTURE or by falsification, is the only thing that counts as progress.

**CLAIMS.md** is the accounting layer underneath all four. It gives every claim an id, a derivation chain, and a lifecycle, so nothing floats free of the evidence that produced it.

**AGENT_PROTOCOL.md and EPISTEMIC_CONTROL.md** sit outside the loop. They govern how any agent is allowed to read, believe, and act on everything the loop produces. Every station above assumes those two have already been read.

**Code and tests** are the material the loop runs on. Code without a test cannot produce a trustworthy observation. A test without running code tests nothing.

## Constitution protocol
1. State the question.
2. State why it matters.
3. Define the distinctions needed to reason about it.
4. Define what sits explicitly out of scope.
5. Name candidate concepts without committing to their implementation.
6. Convert the concepts that matter into falsifiable hypotheses.
7. Build the smallest mechanism able to test one hypothesis.
8. Run it. Observe what happens.
9. Separate the raw observation from its interpretation.
10. Promote only gate-cleared mechanisms into ARCHITECTURE.
11. Record everything else as open, in QUESTIONS.
12. Let the resulting architecture generate the next round of questions.
13. Repeat.
