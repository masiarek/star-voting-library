"""
test_composed_mirror.py
=======================
Repo-wide guard for the '_tabulated' mirror format, covering the method paths
that `test_approval_mirror.py` does not (that file guards STAR + Approval).

House rule: EVERY tabulated YAML gets a full-context mirror — provenance header,
the ORIGINAL election file copied as-is, then TABULATION RESULTS — written by
`write_composed_tabulated()`. Three paths used to bypass it and dump the bare
report instead (`write_tabulated_copy`), losing the whole description and header:

  - single-winner Plurality      (run_plurality_single)
  - multi-winner Plurality        (run_plurality_multi — SNTV / Block / Limited)
  - Ranked Robin, both seat counts (run_ranked_robin — incl. Bloc RR)

The drift was invisible until a mirror was regenerated: the committed copies
predated the dedicated Plurality / Ranked Robin reports, so they still LOOKED
composed while the engine no longer produced that. These tests re-run each path
end-to-end and assert the composed format, so it cannot silently rot again.

The last test locks the other half of the rule: AUXILIARY mirrors (the
method-tagged RCV-IRV / RCV-RR reports written alongside a STAR run) stay BARE
on purpose — the primary mirror sitting beside them already carries the source.
"""
import subprocess
import sys
from pathlib import Path

import pytest

ENGINE_DIR = Path(__file__).resolve().parent.parent
WRAPPER = ENGINE_DIR / "starvote_larry_hastings.py"


def _run(path):
    return subprocess.run([sys.executable, str(WRAPPER), str(path)],
                          capture_output=True, text=True, cwd=str(ENGINE_DIR))


def _mirror_of(src):
    return src.parent / (src.parent.name + "_tabulated") / (src.stem + "_tabulated.txt")


def _aux_mirror_of(src, method_tag):
    return (src.parent / (src.parent.name + "_tabulated")
            / f"{src.stem}_{method_tag}_tabulated.txt")


PLURALITY_SINGLE = (
    "voting_method: Plurality\n"
    "num_winners: 1\n"
    "election_description: |-\n"
    "  A choose-one race the mirror must keep in full.\n"
    "ballots: |-\n"
    "  Ann,Bob,Cal\n"
    "  1,0,0\n"
    "  1,0,0\n"
    "  1,0,0\n"
    "  0,1,0\n"
    "  0,0,1\n"
    "expected_winners:\n"
    "  - Ann\n"
)

PLURALITY_MULTI = (
    "voting_method: Plurality\n"
    "num_winners: 2\n"
    "election_description: |-\n"
    "  SNTV: two seats, one mark per voter.\n"
    "ballots: |-\n"
    "  Ann,Bob,Cal,Dee\n"
    "  1,0,0,0\n"
    "  1,0,0,0\n"
    "  1,0,0,0\n"
    "  0,1,0,0\n"
    "  0,1,0,0\n"
    "  0,0,1,0\n"
    "  0,0,0,1\n"
    "expected_winners:\n"
    "  - Ann\n"
    "  - Bob\n"
)

RANKED_ROBIN_SINGLE = (
    "voting_method: RankedRobin\n"
    "num_winners: 1\n"
    "election_description: |-\n"
    "  Round-robin: Bob is the Condorcet winner.\n"
    "ballots: |-\n"
    "  Ann>Bob>Cal\n"
    "  Ann>Bob>Cal\n"
    "  Bob>Cal>Ann\n"
    "  Cal>Bob>Ann\n"
    "expected_winners:\n"
    "  - Bob\n"
)

RANKED_ROBIN_BLOC = (
    "voting_method: RankedRobin\n"
    "num_winners: 2\n"
    "election_description: |-\n"
    "  Bloc RR: the top two by win-loss record.\n"
    "ballots: |-\n"
    "  Ann>Bob>Cal>Dee\n"
    "  Ann>Bob>Cal>Dee\n"
    "  Bob>Cal>Ann>Dee\n"
    "  Cal>Bob>Ann>Dee\n"
    "expected_winners:\n"
    "  - Bob\n"
    "  - Ann\n"
)

RCV_IRV = (
    "voting_method: RCV_IRV\n"
    "num_winners: 1\n"
    "election_description: |-\n"
    "  Instant runoff: Ann has a first-round majority.\n"
    "ballots: |-\n"
    "  Ann>Bob>Cal\n"
    "  Ann>Bob>Cal\n"
    "  Ann>Bob>Cal\n"
    "  Bob>Cal>Ann\n"
    "  Cal>Bob>Ann\n"
    "expected_winners:\n"
    "  - Ann\n"
)

# (test id, yaml text, substrings the mirror's results section must contain)
COMPOSED_CASES = [
    ("plurality_single", PLURALITY_SINGLE,
     ["--- Choose-One / Plurality Voting Method (single winner) ---",
      "Count the marks:",
      "Winner — Choose-One / Plurality Voting Method (single winner)"]),
    ("plurality_multi_sntv", PLURALITY_MULTI,
     ["--- SNTV (single non-transferable vote) — 2 winners ---",
      "Winners — SNTV (single non-transferable vote), 2 seats:"]),
    ("ranked_robin_single", RANKED_ROBIN_SINGLE,
     ["--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---",
      "Winner — Ranked Robin (RCV-RR): Bob"]),
    ("ranked_robin_bloc", RANKED_ROBIN_BLOC,
     ["--- Ranked Robin (RCV-RR / Copeland) Method (2 winners) ---",
      "Winners — Ranked Robin (RCV-RR), 2 seats (Bloc — the top 2 by record):"]),
    ("rcv_irv", RCV_IRV,
     ["RCV / Instant-Runoff Voting", "Ann"]),
]


@pytest.mark.parametrize("name,yaml_text,needles",
                         COMPOSED_CASES,
                         ids=[c[0] for c in COMPOSED_CASES])
def test_primary_mirror_is_composed(tmp_path, name, yaml_text, needles):
    """Every method path writes the composed mirror: header + source + results."""
    src = tmp_path / f"{name}.yaml"
    src.write_text(yaml_text, encoding="utf-8")
    r = _run(src)
    assert r.returncode == 0, r.stdout + r.stderr

    mirror = _mirror_of(src)
    assert mirror.exists(), f"{name}: run wrote no _tabulated mirror"
    text = mirror.read_text(encoding="utf-8")

    # 1. Provenance header, naming both files.
    assert text.startswith("=" * 70), f"{name}: mirror has no divider header"
    assert f"SOURCE FILE:     {src.name}" in text, f"{name}: no SOURCE FILE line"
    assert f"TABULATED FILE:  {mirror.name}" in text, f"{name}: no TABULATED FILE line"

    # 2. The ORIGINAL file, embedded as-is — this is what the bare report lost.
    assert "TABULATION RESULTS" in text, f"{name}: no results banner"
    original, _, results = text.partition("TABULATION RESULTS")
    assert "election_description: |-" in original, f"{name}: description dropped"
    assert "ballots: |-" in original, f"{name}: source ballots dropped"
    assert yaml_text.rstrip() in original, f"{name}: source file not embedded verbatim"

    # 3. The tabulation itself, AFTER the header (not a bare report standing alone).
    for needle in needles:
        assert needle in results, f"{name}: results missing {needle!r}"


# A STAR election where RCV-IRV disagrees (classic center squeeze), so the run
# also emits the method-tagged AUXILIARY mirror.
STAR_WITH_AUX = (
    "voting_method: STAR\n"
    "num_winners: 1\n"
    "ballots: |-\n"
    "  Ann,Bob,Cal\n"
    + "  5,1,0\n" * 8
    + "  1,5,1\n" * 5
    + "  0,1,5\n" * 7
    + "expected_winners:\n"
    "  - Bob\n"
)


def test_aux_mirror_stays_bare(tmp_path):
    """The method-tagged AUX mirror is deliberately NOT composed.

    Only the PRIMARY '<stem>_tabulated.txt' carries the source file; the
    RCV-IRV / RCV-RR companions beside it hold just the round-by-round report.
    Composing those too would duplicate the source in every sibling.
    """
    src = tmp_path / "star_center_squeeze.yaml"
    src.write_text(STAR_WITH_AUX, encoding="utf-8")
    r = _run(src)
    assert r.returncode == 0, r.stdout + r.stderr

    # The primary mirror IS composed (STAR path).
    primary = _mirror_of(src)
    assert primary.exists()
    assert "SOURCE FILE:     " + src.name in primary.read_text(encoding="utf-8")

    aux = _aux_mirror_of(src, "RCV-IRV")
    if not aux.exists():          # pyrankvote missing, or the methods agreed
        pytest.skip("no RCV-IRV divergence mirror produced in this environment")
    aux_text = aux.read_text(encoding="utf-8")
    assert "SOURCE FILE:" not in aux_text, "aux mirror must not carry the header"
    assert "ballots: |-" not in aux_text, "aux mirror must not embed the source"
    assert "RCV" in aux_text, "aux mirror should hold the RCV-IRV report"
