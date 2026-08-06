"""
test_md_links.py
================
Every relative link in a tracked Markdown file must resolve to a real file or
folder. Folder reorganizations silently break these (a 2026-07 reorg left 85+
dangling links); this test makes that class of breakage impossible to commit.

The scan itself lives in STARVote_LH_tabulation_engine/tools_adam/scripts/check_repo_hygiene.py (`check_links`) so the
warn-only pre-commit report and this blocking test can never disagree.

Deliberate placeholders — link a screenshot you haven't captured yet as
`img/REPLACE_<what>.png` — are skipped by convention.
"""
import importlib.util
import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
HYGIENE = REPO_ROOT / "STARVote_LH_tabulation_engine" / "tools_adam" / "scripts" / "check_repo_hygiene.py"


def _load_hygiene():
    spec = importlib.util.spec_from_file_location("check_repo_hygiene", HYGIENE)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["check_repo_hygiene"] = mod
    spec.loader.exec_module(mod)
    return mod


def test_all_relative_md_links_resolve():
    mod = _load_hygiene()
    broken = mod.check_links()
    assert not broken, (
        f"{len(broken)} broken relative Markdown link(s):\n" +
        "\n".join(f"  {f}  ->  ({raw})" for f, raw in broken) +
        "\n(Fix the path, or use the img/REPLACE_*.png placeholder convention "
        "for screenshots not yet captured.)"
    )


def test_no_bare_folder_links():
    """`[label](folder/)` must name the README.md explicitly.

    The bare form resolves on GitHub and on the built site, so it reads as fine
    from two of the three surfaces — but MkDocs does not rewrite it ("left as
    is" in the build log), so the raw href ships and the published page 404s,
    and a local Markdown viewer can't open it either. 635 links were landing
    dead on the site before the 2026-08 sweep; this stops the next one.
    """
    mod = _load_hygiene()
    bare = mod.check_folder_links()
    assert not bare, (
        f"{len(bare)} bare folder link(s) — name the README.md:\n" +
        "\n".join(f"  {rel}  ->  ({raw})   use ({fixed})" for rel, raw, fixed in bare)
    )


def test_folder_link_check_is_not_vacuous():
    """Prove the gate above can actually fail.

    A checker that silently matches nothing passes forever and protects
    nothing — the same reason tests/test_harness_selfcheck.py exists. This
    writes each bad spelling into the repo, confirms it is caught, and confirms
    the correct spelling and a fenced example are NOT caught.
    """
    mod = _load_hygiene()
    probe = REPO_ROOT / "07_Concepts" / "topics" / "_folder_link_probe.md"
    probe.write_text(
        "# probe\n"
        "[a](../../04_Approval/)\n"
        "[b](../../04_Approval)\n"
        "[c](../../04_Approval/#x)\n"
        "[d](../../04_Approval/README.md)\n"
        "`[e](../../04_Approval/)`\n",
        encoding="utf-8",
    )
    try:
        hits = [(raw, fixed) for rel, raw, fixed in mod.check_folder_links()
                if rel.endswith("_folder_link_probe.md")]
    finally:
        probe.unlink()
    raws = sorted(r for r, _ in hits)
    assert raws == ["../../04_Approval", "../../04_Approval/", "../../04_Approval/#x"], (
        f"expected all three bare spellings caught and nothing else, got {raws}"
    )
    assert dict(hits)["../../04_Approval/#x"] == "../../04_Approval/README.md#x", (
        "the #anchor must survive the suggested rewrite"
    )


def test_no_new_hand_pasted_engine_reports():
    """A long engine report on a companion page must be embedded, not pasted.

    Pasted output has nothing behind it, so it silently stops matching the
    engine — which is how the BV1815 page ended up showing a report format the
    engine had stopped emitting. Embedding the `_tabulated` mirror tracks the
    engine for free; a deliberate compression is fine but has to say `abridged`
    on the fence so a reader knows it isn't verbatim.
    """
    mod = _load_hygiene()
    pasted = mod.check_pasted_reports()
    assert not pasted, (
        f"{len(pasted)} companion page(s) with a hand-pasted engine report:\n" +
        "\n".join(f"  {rel}\n      {msg}" for rel, msg in pasted)
    )


def test_grandfather_list_stays_empty():
    """The burn-down finished; the exemption list is not a parking lot.

    All 34 pre-existing pasted reports were converted, so there is no page this
    rule can't be applied to. Re-populating the list would mean a new page
    pasted a report and the exemption was widened instead of the report embedded.
    """
    mod = _load_hygiene()
    assert not mod.PASTED_REPORT_GRANDFATHERED, (
        "PASTED_REPORT_GRANDFATHERED is non-empty: "
        + ", ".join(sorted(mod.PASTED_REPORT_GRANDFATHERED))
    )
