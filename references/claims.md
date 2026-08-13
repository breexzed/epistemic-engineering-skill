# CLAIMS

## Status
Ledger. Not a prior, not a posterior. The accounting layer underneath CANON, ARCHITECTURE, CURRENT_MODEL, and QUESTIONS. Every claim living in those files gets an entry here.

## Why this exists
A tag says what kind of claim something is. It does not say where the claim came from, or what happens to it once it's contradicted. Without an address, a claim can drift, get restated in slightly different words, and lose its link back to the evidence that produced it. This file gives every claim an id, a lineage, and a lifecycle.

## Claim entry format
```
[C-<id>]
Statement: <one sentence>
Tag: KNOWN | OBSERVED | ASSUMED | INFERRED | PROPOSED | UNRESOLVED
Derived from: <raw observation id, experiment id, file, or another claim id>
Constrained by: <CANON section, if any>
Lives in: <which document and section holds this claim>
Status: active | contradicted | under review | revised | retracted
Superseded by: <claim id, if any>
```

A decision made downstream cites the claim id it rests on, not a paraphrase of the claim. "This depends on C-17" can be checked. A restatement in new words cannot.

## Observation layering
`OBSERVED` is not one thing. Collapsing raw output and interpretation into the same tag turns `OBSERVED` into a dumping ground. Separate the steps:

```
RAW OBSERVATION
    |
MEASUREMENT
    |
INTERPRETATION
    |
CLAIM
```

Example. A raw observation is a specific log line or data point. A measurement counts how often that pattern repeats across a run. An interpretation names what the pattern looks like. Only the interpretation, tagged INFERRED and cited back to the measurement, becomes a claim. The interpretive sentence is not itself a raw observation, even when it feels like one.

## Lifecycle
```
KNOWN
  |
CONTRADICTED
  |
REVIEW
  |
REVISED / SPLIT / RETRACTED
```

A claim never just disappears. When new evidence contradicts a KNOWN claim, the claim's status changes to `contradicted`, right in this ledger. It does not get quietly deleted or overwritten. Every downstream item that cited it gets flagged for review. The review ends in one of three outcomes: the claim is revised, narrowed or corrected; split into two more precise claims; or retracted outright. Whichever outcome, the record stays, so a future agent can see what was believed and why it changed.

## Authority versus truth
The authority order in `agent_protocol.md` decides which source controls what an agent does next. It does not decide which source is true.

When a user-stated fact, an ARCHITECTURE entry, and an actual observation disagree, the correct move is not to pick the highest-authority one and call it reality. The correct move is:

```
USER-STATED: X
ARCHITECTURE: Y
OBSERVED: Z

CONTRADICTION: logged, status = under review
```

Authority tells the agent which claim to act on in the meantime. It does not resolve the disagreement. The disagreement stays open in this ledger until an experiment or a direct check closes it.

## Rule
No claim above ASSUMED enters ARCHITECTURE.md, CANON.md, or CURRENT_MODEL.md without an entry here first. If a claim can't be given a derivation chain, it isn't ready to leave QUESTIONS.md.
