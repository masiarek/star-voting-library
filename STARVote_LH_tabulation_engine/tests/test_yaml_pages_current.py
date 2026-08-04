"""
test_yaml_pages_current.py
==========================
The generated Markdown pages (`<folder>/<folder>_pages/<stem>.md`) must match
what `STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py` would produce from the current YAMLs and
`_tabulated` mirrors — same pattern as the YAML-index staleness test, so the
pages can never silently drift from their sources.

If this fails, regenerate:

    python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py
"""
import importlib.util
import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
SCRIPT = REPO_ROOT / "STARVote_LH_tabulation_engine" / "tools_adam" / "scripts" / "build_yaml_pages.py"


def _load():
    spec = importlib.util.spec_from_file_location("build_yaml_pages", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["build_yaml_pages"] = mod
    spec.loader.exec_module(mod)
    return mod


def test_pages_exist_and_are_current():
    mod = _load()
    stale, orphans = mod.check()
    msg = []
    if stale:
        msg.append(f"{len(stale)} stale/missing page(s):")
        msg += [f"  {Path(p).relative_to(REPO_ROOT)}" for p in stale[:10]]
    if orphans:
        msg.append(f"{len(orphans)} orphan page(s) (source YAML gone):")
        msg += [f"  {Path(p).relative_to(REPO_ROOT)}" for p in orphans[:10]]
    assert not stale and not orphans, (
        "\n".join(msg) + "\nRegenerate with: python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py"
    )


def test_companion_meta_blocks_are_current():
    """Hand-authored pages that shadow a case carry an up-to-date `case-meta` block.

    The prose on those pages is the author's; the block under the H1 is not — it
    is rebuilt from the YAML, so changing `num_winners` or `voting_method` there
    can't leave a companion page quietly stating the old value.
    """
    mod = _load()
    stale = mod.check_companions()
    assert not stale, (
        f"{len(stale)} companion page(s) with a missing/outdated case-meta block:\n"
        + "\n".join(f"  {Path(p).relative_to(REPO_ROOT)}" for p in stale[:10])
        + "\nRegenerate with: python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py"
    )


def test_ballot_blocks_are_current():
    """Hand-authored pages that ask for ballot art show the current art.

    A lesson page marks the spot with `<!-- ballots:<stem> -->`; this script
    fills it from the case YAML and the drawn images. Edit the ballots and the
    pictures move — the block on the lesson has to move with them.
    """
    mod = _load()
    stale = mod.check_ballot_blocks()
    assert not stale, (
        f"{len(stale)} page(s) with an outdated ballot block:\n"
        + "\n".join(f"  {Path(p).relative_to(REPO_ROOT)}" for p in stale[:10])
        + "\nRegenerate with: python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py"
    )


def test_report_blocks_are_current():
    """Hand-authored pages that embed a count show the current count.

    The page marks the spot with `<!-- report:<stem> -->` and the generator
    pastes in that case's generated report. Pasting (rather than a `--8<--`
    include) is what makes the report visible on GitHub as well as on the site;
    this test is what keeps the paste from going stale, which is the failure
    mode the include was adopted to avoid.
    """
    mod = _load()
    stale = mod.check_report_blocks()
    assert not stale, (
        f"{len(stale)} page(s) with an outdated report block:\n"
        + "\n".join(f"  {Path(p).relative_to(REPO_ROOT)}" for p in stale[:10])
        + "\nRegenerate with: python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py"
    )


def test_no_snippet_report_includes_remain():
    """No page falls back to the site-only `--8<-- "…:report"` include.

    It renders on MkDocs and prints as a literal line of text on GitHub, so a
    page using it shows no report at all to a GitHub reader. `_notes/` is
    exempt: it documents the old idiom.
    """
    offenders = []
    for p in REPO_ROOT.rglob("*.md"):
        parts = set(p.relative_to(REPO_ROOT).parts)
        if parts & {"site", "_notes"} or any(s.startswith(".") for s in parts):
            continue
        if p.name in ("CLAUDE.md", "AGENTS.md"):
            continue
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.startswith("--8<--") and line.rstrip().endswith(':report"'):
                offenders.append(f"{p.relative_to(REPO_ROOT)}: {line.strip()}")
    assert not offenders, (
        "site-only report include(s) — replace with <!-- report:<stem> --> / "
        "<!-- /report --> and regenerate:\n" + "\n".join(offenders[:10])
    )


def test_discovery_not_vacuous():
    mod = _load()
    assert len(mod.expected_pages()) >= 50, "page discovery collapsed"
    assert len(mod.expected_companions()) >= 40, "companion discovery collapsed"
    assert len(mod.pages_with_ballot_blocks()) >= 4, "ballot-block discovery collapsed"
    assert len(mod.pages_with_report_blocks()) >= 60, "report-block discovery collapsed"
