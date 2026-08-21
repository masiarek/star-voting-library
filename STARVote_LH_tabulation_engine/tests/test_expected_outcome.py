"""
test_expected_outcome.py
========================
Guards `expected_outcome:` — the answer key for the two results a winner list
structurally cannot express.

`expected_winners:` names WHO won. It has no way to say that the count completed
and seated **nobody** (a quorum failure), or that the engine must **refuse** the
file outright. So the two cases in this library whose entire point is one of
those carried no answer key at all, and asserted nothing that any engine could
check — noted as the residue in 07_Concepts/tabulation_engines/rust_kernel_scope.md.

A key nothing enforces is a comment. These tests run the CLI and hold the engine
to what the file claims:

    expected_outcome: no_winner   ->  exits 0, declares no winner, names nobody
    expected_outcome: rejected    ->  exits 1, counts nothing, prints no traceback

Discovery is BY THE KEY, so a case added later is covered without touching this
file. The shape of the key itself (legal values, and not contradicting
`expected_winners:`) is linted separately by
check_repo_hygiene.check_expected_outcome, which test_contradicting_key_is_linted
below calls directly.
"""

import subprocess
import sys
from pathlib import Path

import pytest

yaml = pytest.importorskip("yaml")

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
CLI = ENGINE_DIR / "starvote_larry_hastings.py"


def _cases_with(outcome):
    """Every teaching case file declaring `expected_outcome: <outcome>`."""
    out = []
    for p in sorted(REPO_ROOT.rglob("*.yaml")):
        s = str(p.relative_to(REPO_ROOT))
        if s.startswith((".claude", ".venv", "site/", "node_modules")) or "_tabulated" in s:
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if "expected_outcome:" not in text:
            continue
        try:
            data = yaml.safe_load(text)
        except Exception:
            continue
        if isinstance(data, dict) and data.get("expected_outcome") == outcome:
            out.append(p)
    return out


NO_WINNER = _cases_with("no_winner")
REJECTED = _cases_with("rejected")


def _run(path):
    return subprocess.run(
        [sys.executable, str(CLI), str(path)],
        capture_output=True, text=True, cwd=str(ENGINE_DIR),
    )


def test_the_key_is_actually_in_use():
    """If both lists empty, every assertion below passes vacuously."""
    assert NO_WINNER, "no case declares expected_outcome: no_winner"
    assert REJECTED, "no case declares expected_outcome: rejected"


@pytest.mark.parametrize("path", NO_WINNER, ids=lambda p: p.name)
def test_no_winner_case_completes_and_seats_nobody(path):
    """The count RUNS — this is not an error — and elects no one."""
    proc = _run(path)
    assert proc.returncode == 0, (
        f"{path.name} claims no_winner, which means the count completes; "
        f"the engine exited {proc.returncode}:\n{proc.stdout}\n{proc.stderr}"
    )
    assert "No winner" in proc.stdout, (
        f"{path.name} claims no_winner but the report never says so:\n{proc.stdout}"
    )


@pytest.mark.parametrize("path", NO_WINNER, ids=lambda p: p.name)
def test_no_winner_case_names_no_candidate_as_elected(path):
    """The weaker claim above would pass on a report that ALSO crowned someone.

    A quorum failure that still printed a winner line is exactly the bug this
    case exists to prevent, so check the report does not announce one.
    """
    proc = _run(path)
    banners = [ln for ln in proc.stdout.splitlines()
               if ln.strip().startswith(("Winner —", "Winners —", "Winner:", "Winners:"))]
    assert not banners, f"{path.name} claims no_winner but announced: {banners}"


def test_the_winner_detector_is_not_vacuous():
    """Meta-test, in the spirit of tests/test_harness_selfcheck.py.

    The check above passes when it finds NO winner banner — which is also what
    it would do if the banner's wording changed and the matcher silently stopped
    matching anything. So prove the matcher still fires on an election that
    definitely elects somebody.
    """
    case = REPO_ROOT / "01_STAR" / "02_Examples" / "cases" / "09_c4_b100_tennessee-capital.yaml"
    proc = _run(case)
    banners = [ln for ln in proc.stdout.splitlines()
               if ln.strip().startswith(("Winner —", "Winners —", "Winner:", "Winners:"))]
    assert banners, (
        "the winner-banner matcher found nothing on a case that elects Nashville — "
        "the report's wording changed and test_no_winner_case_names_no_candidate_as_elected "
        f"is now vacuous:\n{proc.stdout}"
    )


@pytest.mark.parametrize("path", REJECTED, ids=lambda p: p.name)
def test_rejected_case_is_refused_cleanly(path):
    """Exit 1, a plain-language reason, and no traceback.

    'The engine must refuse this' is a real claim about behaviour, and the
    no-traceback half matters as much as the exit code: the house rule is that
    a bad file gets an explanation, never a stack dump.
    """
    proc = _run(path)
    assert proc.returncode == 1, (
        f"{path.name} claims rejected but the engine exited {proc.returncode} "
        f"and counted it:\n{proc.stdout[-600:]}"
    )
    combined = proc.stdout + proc.stderr
    assert "Traceback" not in combined, f"{path.name} was refused with a traceback:\n{combined}"
    assert "Error" in combined, f"{path.name} was refused with no explanation:\n{combined}"


@pytest.mark.parametrize("path", REJECTED, ids=lambda p: p.name)
def test_rejected_case_writes_no_tabulated_mirror(path):
    """A refused file must leave no artifact claiming it was counted."""
    mirror_dir = path.parent / f"{path.parent.name}_tabulated"
    mirror = mirror_dir / f"{path.stem}_tabulated.txt"
    assert not mirror.exists(), (
        f"{path.name} claims rejected but a mirror exists at {mirror} — "
        "either the engine counted it, or a stale artifact needs deleting"
    )


def test_outcome_reaches_the_election_contract():
    """The key is only useful if it survives into the machine-readable form."""
    sys.path.insert(0, str(ENGINE_DIR))
    import election_json

    for path in NO_WINNER:
        doc = election_json.build(path)
        assert doc["expected"] == {"outcome": "no_winner"}, path.name
    for path in REJECTED:
        doc = election_json.build(path)
        assert doc["expected"] == {"outcome": "rejected"}, path.name


def _hygiene():
    import importlib.util
    hygiene_path = ENGINE_DIR / "tools_adam" / "scripts" / "check_repo_hygiene.py"
    spec = importlib.util.spec_from_file_location("hygiene_outcome", hygiene_path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["hygiene_outcome"] = mod
    spec.loader.exec_module(mod)
    return mod


def test_corpus_has_no_contradicting_key():
    """The lint, run over the real tree.

    NOTE this is a gate only because THIS test calls it. The pre-commit hook
    runs check_repo_hygiene.py as `... || true`, so nothing the script reports
    can fail a commit on its own — a check nobody calls from a test prints a
    green line and enforces nothing.
    """
    mod = _hygiene()
    assert not mod.check_expected_outcome(), "the corpus itself has a bad key"
    assert set(mod.EXPECTED_OUTCOMES) == {"elected", "no_winner", "rejected"}


# (source, should_flag) — every way the key can be written wrong, and two ways
# it can be written right.
_PROBES = [
    ("expected_outcome: no_winner\nexpected_winners: [Ada]\n", True),   # contradiction
    ("expected_outcome: rejected\nexpected_winners: [Ada]\n", True),    # contradiction
    ("expected_outcome: elected\n", True),                              # elects whom?
    ("expected_outcome: nobody_won\n", True),                           # not a legal value
    ("expected_outcome: no_winner\n", False),                           # fine
    ("expected_winners: [Ada]\n", False),                               # key absent: fine
]


@pytest.mark.parametrize("body,should_flag", _PROBES,
                         ids=[f"{'flag' if f else 'ok'}-{i}" for i, (_, f) in enumerate(_PROBES)])
def test_the_lint_is_not_vacuous(tmp_path, body, should_flag):
    """Prove the detector actually detects — the hole the test above leaves.

    `test_corpus_has_no_contradicting_key` passes when the lint returns nothing,
    which is also what it would do if the lint were broken into always returning
    nothing. So feed it each malformed shape and require the right verdict for
    each. Same posture as tests/test_harness_selfcheck.py, and the same lesson
    that came out of the BV results-link check being shipped ungated.

    `_yaml_teaching_files` is patched to a tmp file, so this touches no file in
    the repo — which matters in a checkout several sessions are committing from.
    """
    mod = _hygiene()
    probe = tmp_path / "probe.yaml"
    probe.write_text(body + "ballots: |-\n  Ada,Ben\n  5,2\n", encoding="utf-8")
    mod._yaml_teaching_files = lambda: [str(probe)]

    found = mod.check_expected_outcome()
    assert bool(found) == should_flag, (
        f"lint returned {found!r} for:\n{body}"
    )
