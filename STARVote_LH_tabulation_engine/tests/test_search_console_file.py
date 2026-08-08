"""
test_search_console_file.py
===========================
A search engine's site-ownership file must reach the published site root.

WHY. Google Search Console verifies ownership by fetching one file at the site
root under a name it issued (`google<token>.html`). Two mechanisms in this repo
swallow that file, and BOTH fail silently — which is how the first attempt got
committed, pushed, and deployed while the URL stayed a 404:

1. `.gitignore` carries a root-level `/*.html` guard (it keeps one-off ballot
   HTML out of the repo). `git add` on an ignored path prints nothing and stages
   nothing, so the push looks clean and carries no file.
2. `mkdocs-same-dir` drops every non-document file in the root of `docs_dir` —
   correct in general, since `docs_dir` IS the repo root here, but it means
   MkDocs never learns the file exists and so never warns that it didn't ship.

Neither failure is visible in a build log, in `git status`, or in `mkdocs build
--strict`. The only signal is Google's own VERIFY button failing, days later,
with nothing in the repo to point at. Hence this test.

If verification is ever moved to the DNS-TXT or meta-tag method and the file is
deleted, these tests skip rather than fail.
"""
import subprocess
import sys
from pathlib import Path

import pytest

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
sys.path.insert(0, str(REPO_ROOT))

import mkdocs_hooks as hooks  # noqa: E402

VERIFICATION_FILES = sorted(REPO_ROOT.glob(hooks.SITE_VERIFICATION_GLOB))


def _skip_if_absent():
    if not VERIFICATION_FILES:
        pytest.skip(
            f"no {hooks.SITE_VERIFICATION_GLOB} at the repo root — "
            "site ownership is not verified by file"
        )


def test_verification_file_is_not_git_ignored():
    """The `/*.html` guard must carry a matching `!` exception."""
    _skip_if_absent()
    for path in VERIFICATION_FILES:
        result = subprocess.run(
            ["git", "check-ignore", "-v", path.name],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        # check-ignore exits 0 (and names the rule) only when the path IS ignored.
        assert result.returncode != 0, (
            f"{path.name} is ignored by {result.stdout.strip()!r}. "
            "It can never be committed, so the site can never serve it. "
            "Add a `!` exception in .gitignore."
        )


def test_verification_file_is_tracked():
    """Present on disk but untracked means the deploy carries nothing."""
    _skip_if_absent()
    for path in VERIFICATION_FILES:
        result = subprocess.run(
            ["git", "ls-files", "--error-unmatch", path.name],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, (
            f"{path.name} exists at the repo root but is not tracked by git. "
            "Run `git add` on it — CI builds the committed tree, not yours."
        )


def test_hook_readmits_verification_file():
    """mkdocs-same-dir drops root non-documents; the hook must put this one back."""
    _skip_if_absent()
    from mkdocs.structure.files import Files

    # Files() as mkdocs-same-dir leaves it: root non-documents already stripped.
    files = Files([])
    config = {
        "docs_dir": str(REPO_ROOT),
        "site_dir": str(REPO_ROOT / "site"),
        "use_directory_urls": False,
    }

    result = hooks.on_files(files, config)
    admitted = {f.src_uri for f in result}

    for path in VERIFICATION_FILES:
        assert path.name in admitted, (
            f"{path.name} was not re-admitted to the build. It would be absent "
            "from the published site with no warning anywhere in the build log."
        )


def test_hook_is_idempotent_and_narrow():
    """Re-admitting must not duplicate files, nor widen to other root HTML."""
    _skip_if_absent()
    from mkdocs.structure.files import Files

    config = {
        "docs_dir": str(REPO_ROOT),
        "site_dir": str(REPO_ROOT / "site"),
        "use_directory_urls": False,
    }

    once = hooks.on_files(Files([]), config)
    twice = hooks.on_files(once, config)
    names = [f.src_uri for f in twice]
    assert len(names) == len(set(names)), f"hook duplicated files: {names}"

    # Only the verification file(s) — never the ballot/preview HTML the
    # `/*.html` guard and the same-dir plugin both exist to keep out.
    assert set(names) == {p.name for p in VERIFICATION_FILES}, (
        "the hook admitted something other than the verification file(s): "
        f"{sorted(set(names))}"
    )
