#!/usr/bin/env python3
"""
_bv_ids.py — the ONE way to answer "is this case backed by a BetterVoting election,
and what is its id?"

Four generators need that answer and used to each carry their own version:

    build_bv_registry.py     the canonical BV index (BV_registry.md, bv_cases.csv)
    build_paradox_index.py   the BV column of PARADOX_index.md
    build_divergence_index.py the BV lead line on each divergence case page
    build_catalog.py         (election-grain; resolves from exports, not yamls)

Three copies of a resolution rule is three chances to disagree, and they *did*:
the paradox index only ever read the explicit `bv_election_id` field, so a case
carrying its bvid solely in a frozen export would silently show "—" as though it
had no live election. This module is that rule, once.

THE RULE (inherited from build_bv_registry.py, which is canonical):

  * **test id**     — the `bv_test_id:` field, else `BV<n>` parsed from a
    `bv<n>_…` filename.
  * **election id** — the `bv_election_id:` field, else the `election_id` inside
    the sibling `<stem>_bv_export.json`. **NEVER parsed from the filename.**
  * **results url** — the `bv_results_url:` field, else built from the election id.

That middle rule is the load-bearing one and it is easy to get wrong in the
tempting direction. `bv<testid>_<bvid>_<descriptor>` *looks* like it makes the
second underscore-segment a bvid, but plenty of real cases are named
`bv<testid>_<descriptor>` instead — `bv129_score_tiebreak_bloc`,
`bv131_guido_bloc`, `bv750_tie_breaking_bloc` — and a descriptor that happens to
be six characters would be published as a bvid, minting a confident link to an
election that does not exist. A missing link is a small loss; a link to the wrong
election is a wrong claim on a teaching page. So the election id only ever comes
from a source that actually asserts it.
"""
from __future__ import annotations

import json
import os
import re

# Test ID only — see the module docstring on why the election id is not taken here.
FN_RE = re.compile(r"^bv(\d+(?:-?r\d+|[a-z])?)_", re.IGNORECASE)

BV_RESULTS = "https://bettervoting.com/{}/results"
BV_VOTE = "https://bettervoting.com/{}"


def export_election_id(yaml_path):
    """The authoritative BV election id from the case's frozen `_bv_export.json`."""
    exp = str(yaml_path)[:-5] + "_bv_export.json"
    if not os.path.exists(exp):
        return ""
    try:
        d = json.load(open(exp, encoding="utf-8"))
    except Exception:
        return ""
    E = d.get("Election") or d.get("election") or {}
    return E.get("election_id", "") or ""


def resolve(yaml_path, doc=None):
    """(test_id, election_id, results_url) for a case yaml — empty strings if absent.

    `doc` is the already-parsed YAML mapping when the caller has one (every caller
    does); pass it to avoid re-reading the file. A case is BV-backed for linking
    purposes exactly when `election_id` is non-empty — a test id alone names a QA
    row, not a public election, so there is nothing to link to."""
    doc = doc if isinstance(doc, dict) else {}
    name = os.path.basename(str(yaml_path))
    m = FN_RE.match(name)
    test_id = str(doc.get("bv_test_id") or (f"BV{m.group(1)}" if m else ""))
    election_id = str(doc.get("bv_election_id") or export_election_id(yaml_path))
    results_url = str(doc.get("bv_results_url")
                      or (BV_RESULTS.format(election_id) if election_id else ""))
    return test_id, election_id, results_url


def link(yaml_path, doc=None, dash="—"):
    """A markdown link labelled with the test id (or the bvid), or `dash` if the
    case has no live election. The house form for an index-table BV cell."""
    test_id, election_id, results_url = resolve(yaml_path, doc)
    if not election_id:
        return dash
    return f"[{test_id or election_id}]({results_url})"
