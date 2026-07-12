"""
test_readme_index_complete.py
=============================
Some folders keep a README that is meant to be an EXHAUSTIVE index of their
generated pages (the teaching progression's front door). A new page added to
`<folder>_pages/` but forgotten in that README goes silently missing — the exact
bug that dropped `bv2184_fyy886_lunch_vote` from `01_STAR/_main`. This test makes
that impossible to commit for the allowlisted folders.

The scan lives in STARVote_LH_tabulation_engine/tools_adam/scripts/check_repo_hygiene.py
(`check_pages_indexed`, driven by `INDEX_COMPLETE_DIRS`) so the warn-only
pre-commit report and this blocking test can never disagree.
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


def test_index_readmes_list_every_page():
    mod = _load_hygiene()
    unlisted = mod.check_pages_indexed()
    assert not unlisted, (
        f"{len(unlisted)} page(s) missing from an index-complete README:\n" +
        "\n".join(f"  {readme}  <-  {page} not linked" for readme, page in unlisted) +
        "\n(Add the page to the README's arc, or drop the folder from "
        "INDEX_COMPLETE_DIRS in check_repo_hygiene.py if it's no longer an "
        "exhaustive index.)"
    )
