#!/usr/bin/env python3
"""
Verify the epistemic document set in a project directory.

Usage:
    python verify_state.py <project_dir>

Checks:
  1. Which of the required files exist.
  2. Every "Component" entry in ARCHITECTURE.md cites a "Claim:" id.
  3. Every cited claim id actually has a matching [C-<id>] entry in CLAIMS.md.
  4. Every claim in CLAIMS.md marked "status: contradicted" that is still
     referenced by an active ARCHITECTURE.md entry gets flagged.

This is a heuristic text scan, not a parser for a formal grammar. Treat a
clean report as necessary, not sufficient, evidence of a well-formed
document set. It exists to catch the mechanical version of the failure:
an ARCHITECTURE.md claim with no CLAIMS.md backing at all.
"""

import re
import sys
from pathlib import Path

REQUIRED_FILES = [
    "CANON.md",
    "METHOD.md",
    "ARCHITECTURE.md",
    "CURRENT_MODEL.md",
    "QUESTIONS.md",
    "CLAIMS.md",
    "AGENT_PROTOCOL.md",
    "EPISTEMIC_CONTROL.md",
]

COMPONENT_HEADER_RE = re.compile(r"^###\s+(.+)$", re.MULTILINE)
CLAIM_FIELD_RE = re.compile(r"^Claim:\s*(.+)$", re.MULTILINE)
CLAIM_ID_RE = re.compile(r"\[C-([A-Za-z0-9_-]+)\]")
STATUS_RE = re.compile(r"^Status:\s*(\S+)", re.MULTILINE)


def check_presence(project_dir: Path):
    present, missing = [], []
    for name in REQUIRED_FILES:
        if (project_dir / name).exists():
            present.append(name)
        else:
            missing.append(name)
    return present, missing


def extract_architecture_claims(architecture_text: str):
    """Return list of (component_name, claim_id_or_None) tuples."""
    components = []
    sections = re.split(r"(?=^###\s+)", architecture_text, flags=re.MULTILINE)
    for section in sections:
        header_match = COMPONENT_HEADER_RE.match(section.strip())
        if not header_match:
            continue
        name = header_match.group(1).strip()
        claim_match = CLAIM_FIELD_RE.search(section)
        if claim_match:
            id_match = CLAIM_ID_RE.search(claim_match.group(1))
            claim_id = id_match.group(1) if id_match else claim_match.group(1).strip()
        else:
            claim_id = None
        components.append((name, claim_id))
    return components


def extract_claims_ledger(claims_text: str):
    """Return dict of claim_id -> status."""
    ledger = {}
    blocks = re.split(r"(?=\[C-)", claims_text)
    for block in blocks:
        id_match = CLAIM_ID_RE.match(block.strip())
        if not id_match:
            continue
        claim_id = id_match.group(1)
        status_match = STATUS_RE.search(block)
        status = status_match.group(1) if status_match else "unknown"
        ledger[claim_id] = status
    return ledger


def main():
    if len(sys.argv) != 2:
        print("usage: verify_state.py <project_dir>")
        sys.exit(1)

    project_dir = Path(sys.argv[1]).resolve()
    if not project_dir.is_dir():
        print(f"not a directory: {project_dir}")
        sys.exit(1)

    print(f"Checking {project_dir}\n")

    present, missing = check_presence(project_dir)
    print("Present:")
    for name in present:
        print(f"  {name}")
    print("Missing:")
    for name in missing:
        print(f"  {name}")
    print()

    if "ARCHITECTURE.md" not in present:
        print("ARCHITECTURE.md missing. Nothing further to cross-check.")
        return

    architecture_text = (project_dir / "ARCHITECTURE.md").read_text()
    components = extract_architecture_claims(architecture_text)

    if not components:
        print("No component entries found in ARCHITECTURE.md. "
              "Consistent with genesis state, nothing to cross-check.")
        return

    claims_ledger = {}
    if "CLAIMS.md" in present:
        claims_text = (project_dir / "CLAIMS.md").read_text()
        claims_ledger = extract_claims_ledger(claims_text)

    problems = []
    for name, claim_id in components:
        if claim_id is None:
            problems.append(f'"{name}" has no Claim: field. '
                             f'Every ARCHITECTURE.md entry needs one.')
            continue
        if claim_id not in claims_ledger:
            problems.append(f'"{name}" cites claim C-{claim_id}, '
                             f'which has no matching entry in CLAIMS.md.')
            continue
        status = claims_ledger[claim_id]
        if status == "contradicted":
            problems.append(f'"{name}" rests on C-{claim_id}, '
                             f'marked contradicted in CLAIMS.md. '
                             f'Per EPISTEMIC_CONTROL.md, work resting on this '
                             f'claim should stop until review closes.')

    print(f"ARCHITECTURE.md components checked: {len(components)}")
    if problems:
        print("\nProblems found:")
        for p in problems:
            print(f"  - {p}")
        sys.exit(2)
    else:
        print("All ARCHITECTURE.md entries trace to an active CLAIMS.md id.")


if __name__ == "__main__":
    main()
