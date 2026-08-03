"""
test_pages_indexed.py
=====================
A folder whose README is meant to be a COMPLETE index of its cases must actually
list every one of them. Adding a case is two steps — drop the YAML in, regenerate
the mirrors — and the third step (add the row) is the one that gets forgotten; the
new case then exists, tabulates, and is reachable only from a sibling case page's
"More cases in this set" footer, while the folder's own front door says it isn't
there. That happened to 05_Ranked_Robin/02_Examples (rr_blank_is_last_c4_b3), to
03_STAR_PR/02_Examples (bv2130_bvhchj_party_plurality) and, earlier, to 01_STAR/02_Examples
(bv2184_fyy886_lunch_vote).

The scan lives in tools_adam/scripts/check_repo_hygiene.py (`check_pages_indexed`)
so the warn-only pre-commit report and this blocking test can never disagree —
the same arrangement test_md_links.py uses for the link half.

Scope is the INDEX_COMPLETE_DIRS allowlist in that module, not every folder: most
READMEs are narrative and link a representative subset on purpose. Enroll a folder
only when its README is meant to be exhaustive.
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


def test_index_complete_readmes_list_every_case():
    mod = _load_hygiene()
    missing = mod.check_pages_indexed()
    assert not missing, (
        f"{len(missing)} case(s) missing from an index README:\n" +
        "\n".join(f"  {rel}\n      {msg}" for rel, msg in missing) +
        "\n(Add a row for each, or drop the folder from INDEX_COMPLETE_DIRS if "
        "its README is not meant to be exhaustive.)"
    )


def test_every_allowlisted_folder_actually_resolves():
    """The allowlist must not contain a folder the checker can't find.

    check_pages_indexed() reports an unresolvable entry as a failure rather than
    skipping it, which is what test_index_complete_readmes_list_every_case would
    catch. This test states the same requirement directly, because the silent
    skip is precisely how this gate sat inert: its one entry pointed at a
    `_main_pages/` directory that the cases/cases_pages/ layout never created.
    """
    mod = _load_hygiene()
    unresolved = []
    for rel_folder, rel_index in mod.INDEX_COMPLETE_DIRS.items():
        folder = REPO_ROOT / rel_folder
        readme = REPO_ROOT / rel_index if rel_index else folder / "README.md"
        if mod._cases_pages_dir(str(folder)) is None:
            unresolved.append(f"{rel_folder}: no generated-pages directory")
        if not readme.is_file():
            unresolved.append(f"{rel_folder}: indexing README missing ({readme})")
    assert not unresolved, (
        "INDEX_COMPLETE_DIRS entries that resolve to nothing (the gate would be "
        "checking zero cases):\n" + "\n".join(f"  {u}" for u in unresolved)
    )
