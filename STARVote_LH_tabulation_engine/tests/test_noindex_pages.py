"""
test_noindex_pages.py
=====================
Internal pages must stay built and linkable, but out of search results.

WHY. `CLAUDE.md` is house conventions for contributors and agents. Nineteen
pages link to it, so it cannot be dropped from the build — but it is the wrong
result to hand someone who searched for STAR voting, and it is a thousand lines
of dense terminology prose, which is the shape of page that surfaces for a niche
query.

The fix has two halves that MUST move together (`mkdocs_hooks.py`):

1. a `noindex` robots meta tag — the only thing that actually keeps a page out
   of results, since a page linked from 19 others is discovered with or without
   a sitemap entry; and
2. removal from `sitemap.xml`, because Search Console reports a sitemapped
   `noindex` URL under "Submitted URL marked noindex" as an *error*.

Half of it is worse than none: tag-only produces that error, sitemap-only does
nothing at all. Hence a test that asserts both, plus the `follow` half of the
directive — the page should not be listed, but the links it makes to real pages
should still pass through.
"""
import gzip
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
sys.path.insert(0, str(REPO_ROOT))

import mkdocs_hooks as hooks  # noqa: E402

SITE_URL = "https://masiarek.github.io/star-voting-library/"


class _FakeFile:
    def __init__(self, src_uri):
        self.src_uri = src_uri


class _FakePage:
    def __init__(self, src_uri, canonical_url):
        self.file = _FakeFile(src_uri)
        self.canonical_url = canonical_url


MATERIAL_HEAD = '<!doctype html>\n<html lang="en">\n  <head>\n    <title>x</title>\n  </head>\n'


def test_noindex_list_is_not_empty():
    """A silently-emptied list would make every other test here vacuous."""
    assert hooks.NOINDEX_PAGES, "NOINDEX_PAGES is empty — nothing is protected"


@pytest.mark.parametrize("src_uri", sorted(hooks.NOINDEX_PAGES))
def test_listed_page_exists_on_disk(src_uri):
    """A stale entry protects nothing and hides the fact that it protects nothing."""
    assert (REPO_ROOT / src_uri).is_file(), (
        f"NOINDEX_PAGES names {src_uri}, which no longer exists. "
        "Remove the entry or fix the path."
    )


@pytest.mark.parametrize("src_uri", sorted(hooks.NOINDEX_PAGES))
def test_page_gets_noindex_tag(src_uri):
    hooks.on_pre_build({})
    out = hooks.on_post_page(
        MATERIAL_HEAD, _FakePage(src_uri, SITE_URL + "CLAUDE.html"), {}
    )
    assert 'name="robots"' in out, f"{src_uri} was not stamped"
    assert "noindex" in out
    # follow, not nofollow: unlisted, but its links to real pages still count.
    assert "nofollow" not in out, "should be `noindex, follow`"
    assert out.count('name="robots"') == 1, "stamped more than once"


def test_ordinary_page_is_untouched():
    hooks.on_pre_build({})
    page = _FakePage("01_STAR/README.md", SITE_URL + "01_STAR/README.html")
    assert hooks.on_post_page(MATERIAL_HEAD, page, {}) == MATERIAL_HEAD


def test_sitemap_loses_exactly_the_noindex_urls(tmp_path):
    """The two halves must agree, or GSC reports an error on the mismatch."""
    keep = SITE_URL + "01_STAR/README.html"
    drop = SITE_URL + "CLAUDE.html"

    sitemap = tmp_path / "sitemap.xml"
    sitemap.write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<urlset xmlns="{hooks.SITEMAP_NS}">\n'
        f"<url><loc>{keep}</loc></url>\n"
        f"<url><loc>{drop}</loc></url>\n"
        "</urlset>\n",
        encoding="utf-8",
    )
    gz = tmp_path / "sitemap.xml.gz"
    gz.write_bytes(gzip.compress(sitemap.read_bytes()))

    hooks.on_pre_build({})
    hooks.on_post_page(MATERIAL_HEAD, _FakePage(sorted(hooks.NOINDEX_PAGES)[0], drop), {})
    hooks.on_post_build({"site_dir": str(tmp_path)})

    root = ET.parse(sitemap).getroot()
    locs = [e.text for e in root.iter(f"{{{hooks.SITEMAP_NS}}}loc")]
    assert locs == [keep], f"expected only {keep!r}, got {locs!r}"

    # The .gz is served too — a stale copy would still advertise the URL.
    gz_locs = [
        e.text
        for e in ET.fromstring(gzip.decompress(gz.read_bytes())).iter(
            f"{{{hooks.SITEMAP_NS}}}loc"
        )
    ]
    assert gz_locs == [keep], f"sitemap.xml.gz is stale: {gz_locs!r}"


def test_sitemap_untouched_when_nothing_stamped(tmp_path):
    """No stamped pages must mean no rewrite — not an emptied sitemap."""
    body = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<urlset xmlns="{hooks.SITEMAP_NS}">\n'
        f"<url><loc>{SITE_URL}index.html</loc></url>\n"
        "</urlset>\n"
    )
    sitemap = tmp_path / "sitemap.xml"
    sitemap.write_text(body, encoding="utf-8")

    hooks.on_pre_build({})
    hooks.on_post_build({"site_dir": str(tmp_path)})

    assert sitemap.read_text(encoding="utf-8") == body
