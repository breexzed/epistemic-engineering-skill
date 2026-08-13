---
name: epistemic-engineering
description: Enforces a disciplined, evidence-gated process for software projects, so agents stop treating imagined architecture and shallow local evidence as documented fact. Use whenever a user starts a new project, asks for a PRD, spec, or architecture doc, asks Claude to plan or scaffold a codebase, or set up project documentation. Also trigger mid-project when Claude is about to write ARCHITECTURE-style claims, implement from an assumption instead of a checked fact, or document a component with no running tested code behind it, or when the user says "don't let this drift," "keep this grounded," "no hallucinated architecture," or similar. Trigger proactively even if the user only says "a PRD" or "project docs" without naming this process by name.
---

# Epistemic Engineering

A method for converting uncertainty into warranted structure, and a control system that stops an agent from building on claims it never actually earned.

This skill has two halves that always travel together:

1. **The documents.** A small, fixed set of files that separate what's proven from what's assumed from what's still unknown.
2. **The discipline.** Rules that restrict what an agent is allowed to *do* with a claim, based on how well-earned that claim is. This half is not optional reading. It changes what actions are permitted.

Read this file fully before starting. Then read `references/method.md` and `references/agent_protocol.md` and `references/epistemic_control.md` before writing any code or any project document. This is not a suggestion. Treat those three files as load-bearing, the same way you'd treat a compiler error: skipping them does not skip the consequence.

## Writing style, applies to everything this skill produces

Every document this skill generates, and every explanation Claude gives while this skill is loaded, follows `references/writing_style.md`. Short sentences. Subject, verb, object. Numbers instead of adjectives. No throat-clearing, no preamble, no hedged qualifiers, no "it's worth noting." Read that file now, before writing anything. It is not a style preference bolted on at the end. It is how every file below gets written, including the ones you generate for the user during bootstrap.

## Step 0: Detect state

Before anything else, check the project directory for an existing document set: `CANON.md`, `METHOD.md`, `ARCHITECTURE.md`, `CURRENT_MODEL.md`, `QUESTIONS.md`, `CLAIMS.md`, `AGENT_PROTOCOL.md`, `EPISTEMIC_CONTROL.md`.

Run this check with an actual tool call (`view` a directory listing, or `bash_tool` with `find`/`ls`), not by assuming. Then run `scripts/verify_state.py` against the project directory if the documents exist. It reports which files are present, which are missing, and flags any claim in ARCHITECTURE.md that has no matching entry in CLAIMS.md.

Three outcomes:

- **Nothing exists.** Go to Step 1, Bootstrap.
- **Some exist, some don't.** Tell the user exactly which are missing. Do not silently fill gaps with your own invented content for CANON.md; that file is user-defined (see Step 1). You may draft the process files (METHOD.md, AGENT_PROTOCOL.md, EPISTEMIC_CONTROL.md, CLAIMS.md) yourself, since those are universal and not project-specific — copy them from `references/` and do not alter their substance.
- **All exist.** Go to Step 2, Operate. Do not regenerate anything. Read what's there.

## Step 1: Bootstrap (only when CANON.md doesn't exist)

CANON.md is the one document this skill cannot write for the user. It encodes what the project is actually for, and that has to come from the person who owns the project. Your job is to interview them, not to guess.

Ask these questions, in this order, as open conversation, not as multiple-choice cards. These need paragraph answers, not button taps:

1. What problem does this project solve? Who has this problem today, and what do they currently do instead of using your solution?
2. What is this project explicitly *not* trying to do? Name the boundary, not just the target.
3. What are you assuming is true, that you haven't actually verified yet? Push on this one. Most people answer it too fast, with something already proven. Ask "what would have to be false for this whole thing not to work?" if the first answer is too safe.
4. What words will get used constantly in this project, that need one fixed meaning? (This becomes the controlled vocabulary. If the user can't name any yet, skip it and revisit after Step 2 produces some.)
5. What tools, vendors, or frameworks are you leaning toward, and are any of them a real commitment versus a convenient starting guess?

Do not let the interview turn into a requirements document. A requirements document says what the system shall do. CANON says what's worth asking and what would count as an answer. If the user starts dictating features, redirect: "That's useful, but it belongs in a PRD once we've got the hypotheses straight. Right now I want the assumptions underneath it."

Write CANON.md using the template and structure in `references/templates.md`. Show it to the user before treating it as settled. Ask directly: "Does this match what you actually believe, or did I put words in your mouth anywhere?" Revise from their answer, not from your own sense of what sounds right.

Once CANON.md is confirmed, generate the rest of the universal document set from `references/templates.md`: METHOD.md, ARCHITECTURE.md (empty, genesis state), CURRENT_MODEL.md (empty, genesis state), QUESTIONS.md (seeded from whatever the user flagged as unverified in question 3 above), CLAIMS.md (empty ledger), AGENT_PROTOCOL.md and EPISTEMIC_CONTROL.md (copied unmodified from `references/`, these do not get customized per project).

If the user also wants an implementation-facing PRD, write it after CANON is settled, following the pattern in `references/templates.md`'s PRD section: concrete, buildable, but every claim in it traces back to something in CANON, and it opens with the same required-reading line pointing at AGENT_PROTOCOL.md and EPISTEMIC_CONTROL.md.

## Step 2: Operate

Once the document set exists, every action you take is governed by `references/epistemic_control.md`. The short version, repeated here because it matters enough to repeat: **the epistemic status of a claim determines what you're allowed to do with it, not just how you're allowed to describe it.** An assumption can guide an experiment. It cannot become a line of production code that ARCHITECTURE.md then describes as real. If you catch yourself about to do that, stop and say so, out loud, before continuing.

Before any of the following actions, run the checklist in `references/agent_protocol.md` explicitly, not from memory:

- writing or editing ARCHITECTURE.md
- writing or editing CURRENT_MODEL.md
- implementing a feature, rather than an experiment
- adding a dependency
- resolving an entry in QUESTIONS.md

Run `scripts/verify_state.py` again after any of these edits. It is a cheap check: does every claim in ARCHITECTURE.md cite a CLAIMS.md entry with a derivation. Treat a failed check as a stop condition, not a warning to note and move past.

State, out loud, before starting substantive work: which operation this is (investigate, implement, refactor, verify, explain, explore, reproduce, measure — see `references/epistemic_control.md`), and the one-line goal anchor you'll check later steps against.

## Reference files

- `references/method.md` — the loop itself: hypothesis through architecture through questions, the gate, the transition rules, what each document's role is.
- `references/agent_protocol.md` — how belief gets formed: authority order, epistemic tags, the pre-action checklist, failure patterns this stops.
- `references/epistemic_control.md` — what action each epistemic state licenses, operation classification, goal anchor, intervention budget, tool bias, the reconstruction test.
- `references/claims.md` — the ledger format: how a claim gets an id, a derivation chain, and a lifecycle instead of floating free.
- `references/templates.md` — blank, fillable templates for every document in the set, plus the PRD pattern.
- `references/writing_style.md` — the plain-writing rules applied to everything this skill produces.
- `scripts/verify_state.py` — run this after bootstrap and after any architecture-level edit. It checks the document set for presence and checks ARCHITECTURE.md claims against CLAIMS.md entries.

Read the reference file before doing the thing it governs, not after.
