# Epistemic Engineering

A skill for Claude and other coding agents. It stops an agent from treating a guess as a fact.

## The problem

Agents have context. They don't always treat it as authoritative. Given a choice between what the user already said and whatever a quick search turns up nearby, agents lean toward the search result. Given an ambiguous task, agents guess and implement instead of asking. Given a diagram someone wrote with good intentions, agents treat it as running code, even when nothing behind it has been built or tested.

The result: architecture documents that describe systems that don't exist. Code built around assumptions nobody checked. Claims that started as guesses and ended up load-bearing.

## What this skill does

It gives a project a small, fixed set of documents that separate three things agents normally blur together: what's proven, what's assumed, and what's still unknown. Then it restricts what an agent is allowed to *do* with each kind of claim.

An assumption can guide an experiment. It can't become a line of production code that gets documented as real. A claim only earns architectural status once it has a file, a test, and an observed result behind it. Nothing skips that step because it sounds finished.

The skill also ships a script. It scans a project's documents and checks that every claim in the architecture file actually traces back to real evidence. Not a promise, a check.

And it carries its own writing rule: short sentences, numbers instead of adjectives, no hedging. Vague writing is how a guess passes as a fact without anyone noticing. Plain writing is part of the enforcement, not a separate style note.

## What you get

- `CANON.md` — the project's purpose, boundaries, and open hypotheses. Built through an interview, not invented by the agent.
- `ARCHITECTURE.md` — only what's actually been built and verified. Starts empty. Stays empty until something earns its way in.
- `CURRENT_MODEL.md` — working assumptions, clearly marked as unconfirmed.
- `QUESTIONS.md` — what's still unknown, and what would resolve it.
- `CLAIMS.md` — every claim gets an id and a paper trail back to its evidence.
- `AGENT_PROTOCOL.md` and `EPISTEMIC_CONTROL.md` — the rules governing how an agent is allowed to form and act on belief.
- `verify_state.py` — a script that checks the document set for gaps and unbacked claims.

## How to use it

Load the skill. Start a new project, or ask for a PRD, spec, or set of project docs. The skill runs an interview to build `CANON.md` from what you actually know, not from what sounds plausible. Everything after that follows from it.

If you already have a project, the skill checks what documents exist and picks up from there. It won't overwrite your `CANON.md` or invent one on your behalf.

## If this helps you

Star it. Tell someone building with agents about it. The more projects run on a document set like this, the fewer hours get lost to code built on a guess nobody flagged as a guess.
