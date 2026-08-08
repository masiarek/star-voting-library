"""Build-time fixes for the auto-generated left sidebar. Registered as `hooks:` in mkdocs.yml.

A hook, not a plugin, on purpose: it ships as one file in the repo and adds no
entry to the `docs` dependency group, so `uv.lock` and the `properdocs` pin
audit are untouched.

## Acronym casing in nav section labels

The sidebar's *section* labels are the only titles nobody authors: MkDocs
derives them from the folder name by turning `_`/`-` into spaces and then
`.capitalize()`-ing the result **only when the folder name is all lowercase**
(mkdocs/structure/nav.py). So `01_STAR` arrives as "01 STAR" untouched, while
`rr_tiebreaks` becomes "Rr tiebreaks" and `star_vs_rr_divergence` becomes
"Star vs rr divergence" — the same acronym rendered three ways down one
sidebar. Page titles are unaffected: those come from each file's own `# H1`.

Renaming the folders would fix it at the source and is the convention the
numbered top-level folders already follow — but it would move every published
URL underneath them, and this repo's URLs are permanent (they are quoted in
BetterVoting election descriptions that can never be edited after an election
goes live). Correcting the label at build time changes no URL and needs no
`redirect_maps` entry.

Keep `TERMS` narrow. It rewrites whole words only, so `STARVote` and `starvote`
are safe, but a folder whose name genuinely contains one of these as an English
word would be shouted at too.

## Underscore-prefixed folders

The same `_` → space step turns the house `_main` folders (one per method, the
core case set, underscored so it sorts to the top of a file listing) into a
label that *starts with a space* — and `.capitalize()` then lands on that space
and does nothing, so the sidebar shipped a blank-looking " main" indented out of
line with its siblings. Stripping the padding and applying MkDocs' own
capitalize-if-all-lowercase rule to what's left gives "Main", which is what the
folder would have rendered as without the prefix. The prefix keeps doing its
sorting job on disk; only the label changes.

## Folders that already carry a capital

The capitalize step is all-or-nothing: MkDocs applies it only when the *whole*
folder name is lowercase. So one capital anywhere suppresses it for the entire
label, and `reporting_BV` / `silly_two_cand_STAR` shipped with a lowercase first
word standing under sentence-cased siblings. `capitalize_first()` raises just
that first character; the deliberate capitals further in are left alone.

## Labels no casing rule can reach

`SECTIONS` maps a derived title to a replacement outright — the escape hatch for
folder names that aren't a cased version of what the reader should see, like the
generated SCREAMING_SNAKE divergence buckets.

## Reading order in the sidebar

MkDocs' automatic nav sorts **alphabetically**, files before folders, uppercase
before lowercase. For a reference tree that is fine; for a *lesson* tree it is
actively misleading — `01_STAR/01_Learn` shipped with "Welcome to STAR Voting"
third, under the ballot page and a history page, because `STAR_s` sorts after
`STAR_b` and `STAR_h`. The sidebar is the only sequence signal a reader gets,
and the alphabet was writing it.

`NAV_ORDER` states the intended order for the folders that have one, keyed by
the folder's repo-relative path and listing children by their **on-disk name**
(a file name, or the sub-folder a section opens). Anything not listed keeps its
alphabetical position, after everything that is — so adding a page never needs
an edit here, it just lands at the bottom of its section until someone places
it. A folder's own `README.md` stays pinned first whatever the list says: the
theme's `navigation.indexes` requires the index page at `children[0]`, and
demoting it would silently break the section's landing link.

Ordering here rather than by renaming files to `01_`, `02_`… is the same
trade-off the casing rules above make: a number in a filename is a number in a
permanent URL, and inserting one lesson later would move a run of them.

`SPINE_BREAK` splits a list into a numbered **lesson spine** and an unnumbered
reference shelf below it. Items before the break get a `N. ` prefix in the
sidebar; items after get none, because a number promises a next one and
"Reference" is not step 7 of anything. Numbering a *page* also sets that page's
`<title>` — see `_page_title` — which is why the spine is kept short and made of
mostly sections.

## Site-ownership verification files at the site root

Search engines verify who owns a site by asking for a file at its root with a
name they choose (`google<token>.html` for Google Search Console). The file has
to ship verbatim, at the root, under that exact name — nothing else counts.

Two things in this repo quietly eat such a file, and both fail *silently*, which
is what makes them worth a docstring:

1. **`.gitignore` has a root-level `/*.html` guard**, so the file is never even
   committed. `git add` reports success-by-saying-nothing and the push carries
   no file. (Fixed there with a matching `!` exception, not here.)
2. **`mkdocs-same-dir` drops every non-document file in the root of `docs_dir`.**
   Its `on_files` keeps a root file only if it is Markdown, JS, CSS, or named
   exactly `CNAME`. That rule is right — `docs_dir` is the repo root, so it is
   what stops `pyproject.toml` and `uv.lock` shipping as site content — but a
   verification file is in the same class as the `CNAME` it special-cases, and
   is not on the list. The file is therefore absent from the built site with no
   warning: MkDocs never knew about it, so it has nothing to warn about.

`on_files` below re-admits it after the plugin has run (hooks are appended to
the plugin collection, so their events fire last). MkDocs' own
`copy_static_files` then copies it through untouched — `.html` is a "static
page", copied byte-for-byte rather than rendered, so the token reaches Google
exactly as issued.

The glob is deliberately narrow: only root-level `google*.html`. Widening it to
all root `.html` would re-admit precisely the build artefacts the plugin and the
`.gitignore` guard both exist to keep out. Add a sibling pattern here if another
search engine's verification is ever needed. Guarded by
`tests/test_search_console_file.py`.

## Keeping internal pages out of search results

`CLAUDE.md` is house conventions for contributors and agents. It is a real page
that 19 others link to — `readme.md` and `CONTRIBUTING.md` among them — so it
has to stay built and clickable, and `exclude_docs` (the route `AGENTS.md`
takes) is not available: dropping it would 404 all 19 links and fail
`mkdocs build --strict`. But it is the wrong thing to hand a voter who searched
for STAR voting, and it is a thousand lines of dense, keyword-rich terminology
prose, which is exactly the shape of page that surfaces for a niche query.

`not_in_nav` does not help: it hides a page from the sidebar, not from Google.
Nor does removing it from `sitemap.xml` — a sitemap is a discovery hint, not an
index gate, and a page linked from 19 others is discovered regardless. The only
thing that actually keeps a page out of results is a `noindex` robots meta tag.

So `on_post_page` stamps one. Material has no `page.meta.robots` support to hang
this on (checked — no `robots` anywhere in its templates), and a `custom_dir`
override would mean shadowing a theme template across future Material upgrades
for the sake of one line, so the tag is injected into `<head>` directly.

`on_post_build` then removes the same pages from `sitemap.xml`, because the two
signals must agree: listing a `noindex` URL in a sitemap is contradictory, and
Search Console reports it under "Submitted URL marked noindex" as an error
rather than ignoring it. Half this fix is worse than none.

Note `noindex, follow` rather than `noindex, nofollow` — the page should not be
listed, but the links it makes to real pages should still pass through.

To publish one of these again, delete it from `NOINDEX_PAGES`. Nothing else
changes: the page is built, linked and rendered on GitHub either way. Guarded by
`tests/test_noindex_pages.py`.
"""

from __future__ import annotations

import gzip
import posixpath
import re
import xml.etree.ElementTree as ET
from pathlib import Path

# Root-level files that must ship verbatim to the site root even though
# mkdocs-same-dir drops root non-documents. See the module docstring.
SITE_VERIFICATION_GLOB = "google*.html"

# Pages that stay built, linked and clickable but must not appear in search
# results, keyed by src_uri. See the module docstring.
NOINDEX_PAGES = {"CLAUDE.md"}

SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"

# Canonical URLs of the pages stamped this build, collected by on_post_page so
# on_post_build can strip exactly those from the sitemap. Reset per build
# because `mkdocs serve` reuses the process across rebuilds.
_noindex_urls: set[str] = set()

# Folders whose children have a reading order, keyed by repo-relative path.
# Values are on-disk names — a file name, or the folder a section opens.
# `SPINE_BREAK` ends the numbered run; everything below it is reference.
SPINE_BREAK = "--- reference below ---"

NAV_ORDER: dict[str, list[str]] = {
    # The STAR lesson tree. Spine: what STAR is → the ballot you fill out → how
    # it is counted → doing it yourself → the awkward corners. Then the shelf:
    # the FAQ/objections bucket, result reporting, glossary and resources, and
    # the history, which is context rather than a step.
    "01_STAR/01_Learn": [
        "STAR_start_here.md",
        "voting_styles",
        "the_count",
        "hands_on",
        "Tie_Breaking_STAR",
        "properties_and_limits",
        SPINE_BREAK,
        "getting_started",
        "reporting",
        "reference",
        "STAR_history.md",
    ],
    # The Bloc lesson tree. Spine: the count → the sweep that defines the
    # method → the surprise that is NOT the sweep → how a tie travels between
    # seats. Then the shelf: the family comparison, the limits, the glossary.
    # Alphabetical order would open the folder on "honest limits", which is
    # the last thing a newcomer should meet.
    "02_STAR_Bloc/01_Learn": [
        "bloc_star.md",
        "bloc_star_ballot.md",
        "bloc_ballot_language.md",
        "majority_sweep.md",
        "over_50_percent.md",
        "score_leader_no_seat.md",
        "bloc_tiebreaks.md",
        SPINE_BREAK,
        "bloc_star_vs_other_bloc_methods.md",
        "bloc_honest_limits.md",
        "at_large_and_the_vra.md",
        "glossary_bloc_star.md",
    ],
    # What the word promises comes before the machinery that delivers it:
    # alphabetical order would open this folder on the STAR_PR method folder
    # and bury "what proportional actually means" at the bottom, which is the
    # page that stops a reader over-claiming for the rest.
    "03_STAR_PR/01_Learn": [
        "proportional_to_what.md",
        "star_pr_faq.md",
        "what_proportional_means.md",
        "STAR_PR",
        "simulating_pr.md",
    ],
    # The three tabulations, recommended-first rather than alphabetical:
    # Allocated Score is Equal Vote's pick and the one this library actually
    # exercises, SSS is the other quota method, RRV the divisor outlier.
    # `the_math_…` stays last — it is the shared theory under all three.
    "03_STAR_PR/01_Learn/STAR_PR": [
        "allocated_score.md",
        "sequentially_spent_score.md",
        "reweighted_range_voting.md",
        "the_math_behind_proportional_star.md",
    ],
    # Divergences before the single-method write-up: "the methods disagree"
    # is the question a reader arrives with once they know there are three.
    "03_STAR_PR/02_Examples": [
        "method_divergences",
        "bv2130_presidential_board_star_pr.md",
    ],
    "03_STAR_PR/02_Examples/method_divergences": [
        "three_neighbors.md",
        "two_officers.md",
    ],
    # 58 loose pages plus 9 hubs, and alphabetical put "Advocacy organizations"
    # and "AI advice" above "spoiler effect" and "Condorcet" purely by spelling.
    # SPINE_BREAK comes FIRST on purpose: this orders without numbering, because
    # a topic shelf is not a lesson spine and "3. Spoiler effect" would promise a
    # step 4. Everything unlisted keeps its alphabetical slot underneath, so
    # adding a topic still needs no edit here.
    "07_Concepts/topics": [
        SPINE_BREAK,
        # the meta-questions this folder's own index opens with
        "what_makes_a_good_winner.md",
        "what_makes_a_voting_method_good.md",
        "Why_STAR_Voting.md",
        "our_voting_system_is_broken.md",
        # what people actually arrive looking for
        "spoiler_effect.md",
        "center_squeeze",
        "condorcet",
        "majority_criterion",
        # more than one seat
        "electing_more_than_one.md",
        "comparing_multiwinner_methods.md",
        # the remaining cross-method hubs, before the flat pages
        "monotonicity",
        "participation",
        "summability",
        "ties",
        "burial",
        "districting",
    ],
    # The two Condorcet-efficiency pages are a pair — the measured rates, then why
    # field size moves them — and plain alphabetical order files four unrelated
    # claim-checks between them. No numbering (SPINE_BREAK first): this is a shelf,
    # not a spine. Everything unlisted keeps its alphabetical slot underneath.
    "07_Concepts/topics/condorcet": [
        SPINE_BREAK,
        "condorcet_efficiency_measured.md",
        "why_more_candidates_miss.md",
    ],
}

# Runs before TERMS, so "ranked robin" is settled before the single-word pass
# looks at "rr". This is also where punctuation a folder name cannot carry gets
# put back — every value here matches the H1 of the folder's own README, which
# is the naming authority. Keys match case-insensitively as whole words.
PHRASES = {
    "ranked robin": "Ranked Robin",
    "split cycle": "Split Cycle",
    "hands on": "Hands-on",
    "postit": "Post-it",
    # `06_Other` sits in the sidebar among five folders named for a method, and
    # alone among them it names a leftover instead — "Other" reads as a junk
    # drawer rather than "the other methods". The folder cannot be renamed:
    # a published BetterVoting description points at 06_Other/Plurality and
    # cannot be edited. Keyed on the number so the word "other" is left alone
    # everywhere else (`other_ranked_methods` must stay as it is).
    "06 other": "06 Other methods",
}

# Acronyms and proper nouns that folder names spell in lowercase. Whole words
# only, which is what keeps the election-ID folders intact: `bv2138` never
# matches `bv`, so "No condorcet bv2138" becomes "No Condorcet bv2138".
TERMS = {
    "rr": "RR",
    "irv": "IRV",
    "star": "STAR",
    "rcv": "RCV",
    "stv": "STV",
    "bv": "BV",
    "condorcet": "Condorcet",
    "borda": "Borda",
    "iia": "IIA",
    "sntv": "SNTV",
    # The library spells itself all-lowercase, but the ABC is an acronym
    # (approval-based committee rules), and MkDocs' sentence-casing turns the
    # folder into "Abcvoting", which reads as a word nobody can pronounce.
    "abcvoting": "ABCvoting",
}

# Whole labels that no casing rule can reach, keyed by the title MkDocs derives.
# The five divergence buckets are SCREAMING_SNAKE folders written by
# build_divergence_index.py, so MkDocs leaves them shouting; these are the same
# human names that generator already prints for them (its BUCKET_TITLE), copied
# rather than imported because the docs build must not depend on the engine's
# tooling being importable. tests/test_nav_labels.py fails if the two drift.
SECTIONS = {
    "APPROVAL OR MINOR": "Only Approval differs",
    "CYCLE OR THREE WAY": "Cycle / three-way split",
    "IRV DIFFERS ARTIFACT": "RCV-IRV differs — tie-break artifact",
    "IRV OUTLIER RR WITH STAR": "RCV-IRV is the outlier (center squeeze)",
    "STAR OUTLIER RR WITH IRV": "STAR is the outlier",
}

_PHRASE_RE = re.compile(
    r"\b(?:%s)\b" % "|".join(re.escape(p) for p in PHRASES), re.IGNORECASE
)
_TERM_RE = re.compile(
    r"\b(?:%s)\b" % "|".join(re.escape(t) for t in TERMS), re.IGNORECASE
)


def unpad(title: str) -> str:
    """Drop the padding a leading/trailing `_` leaves behind, then re-apply
    MkDocs' capitalize-if-all-lowercase rule that the padding defeated."""
    stripped = title.strip()
    if stripped == title:
        return title
    return stripped.capitalize() if stripped.islower() else stripped


def fix_acronyms(title: str) -> str:
    """Return `title` with known acronyms and proper nouns cased canonically."""
    title = _PHRASE_RE.sub(lambda m: PHRASES[m.group(0).lower()], title)
    return _TERM_RE.sub(lambda m: TERMS[m.group(0).lower()], title)


def capitalize_first(title: str) -> str:
    """Uppercase a leading lowercase letter, leaving the rest alone.

    MkDocs skips its capitalize step for any folder name that already carries a
    capital anywhere, so `reporting_BV` and `silly_two_cand_STAR` ship with a
    lowercase first word under siblings that are all sentence-cased. Only the
    first character moves — the deliberate capitals further in must survive.
    """
    return title[:1].upper() + title[1:] if title[:1].islower() else title


def clean(title: str) -> str:
    """The whole label pipeline for one section, in order."""
    # unpad first: it can expose a lowercase acronym at the front.
    title = unpad(title)
    if title in SECTIONS:
        return SECTIONS[title]
    return capitalize_first(fix_acronyms(title))


def _retitle(items) -> None:
    for item in items:
        if item.is_section:
            item.title = clean(item.title)
            _retitle(item.children)


# --- reading order -------------------------------------------------------

_H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.M)


def _descendant_srcs(item, out: list[str]) -> None:
    if item.is_page:
        if item.file is not None:
            out.append(item.file.src_uri)
    else:
        for child in item.children or ():
            _descendant_srcs(child, out)


def folder_of(item) -> str:
    """The repo folder a nav item stands for.

    A page's own directory; for a section, the directory every page beneath it
    shares. Taking the common prefix rather than the first child's directory is
    what keeps a section with sub-sections (`reporting/`, which holds
    `reporting_BV/` and `reporting_LH/`) reporting itself and not its first
    grandchild's folder.
    """
    if item.is_page:
        return posixpath.dirname(item.file.src_uri) if item.file else ""
    srcs: list[str] = []
    _descendant_srcs(item, srcs)
    if not srcs:
        return ""
    common: list[str] = []
    for segments in zip(*(posixpath.dirname(s).split("/") for s in srcs)):
        if len(set(segments)) != 1:
            break
        common.append(segments[0])
    return "/".join(common)


def order_key(item, folder: str) -> str:
    """The on-disk name `item` is listed under in `NAV_ORDER`."""
    if item.is_page:
        return posixpath.basename(item.file.src_uri) if item.file else ""
    sub = folder_of(item)
    if not sub.startswith(folder + "/" if folder else ""):
        return ""
    return sub[len(folder) + 1 :].split("/")[0] if folder else sub.split("/")[0]


def _page_title(page) -> str:
    """The title MkDocs *will* derive for `page` — needed before it derives it.

    `on_nav` runs before a single page is read, so `page.title` is still None
    for every page that doesn't set one in meta, and there is nothing to prefix
    a number onto. So read the `# H1` the same place MkDocs will. Whatever we
    set here survives: MkDocs' own `_set_title()` returns early once `title` is
    not None, which is also why this shows up in the page's `<title>` tag and in
    search results, not only in the sidebar.
    """
    if page.title:
        return str(page.title)
    try:
        text = Path(page.file.abs_src_path).read_text(encoding="utf-8")
    except OSError:
        return page.file.name.replace("_", " ")
    match = _H1_RE.search(text)
    return match.group(1).strip() if match else page.file.name.replace("_", " ")


def _number(item, n: int) -> None:
    item.title = f"{n}. {item.title if item.is_section else _page_title(item)}"


def _apply_order(items: list, folder: str) -> None:
    order = NAV_ORDER.get(folder)
    if not order:
        return
    named = [name for name in order if name != SPINE_BREAK]
    rank = {name: i for i, name in enumerate(named)}
    spine = order[: order.index(SPINE_BREAK)] if SPINE_BREAK in order else order
    number = {name: i + 1 for i, name in enumerate(spine)}

    # `navigation.indexes` renders children[0] as the section's own landing
    # link, so the folder README is not orderable — it is the section.
    is_pinned = [bool(it.is_page and getattr(it, "is_index", False)) for it in items]
    pinned = [it for it, p in zip(items, is_pinned) if p]
    rest = [it for it, p in zip(items, is_pinned) if not p]
    # Unlisted items sort after listed ones, keeping their alphabetical order.
    rest.sort(key=lambda it: rank.get(order_key(it, folder), len(rank)))
    items[:] = pinned + rest

    for item in items:
        n = number.get(order_key(item, folder))
        if n:
            _number(item, n)


def _order(items: list, folder: str) -> None:
    _apply_order(items, folder)
    for item in items:
        if item.is_section:
            _order(item.children, folder_of(item))


def on_nav(nav, config, files):
    _retitle(nav.items)
    _order(nav.items, "")
    return nav


def on_pre_build(config):
    """`mkdocs serve` reuses the process, so per-build state must be cleared."""
    _noindex_urls.clear()


def on_post_page(output, page, config):
    """Stamp `noindex` on internal pages. See the module docstring."""
    if page.file.src_uri not in NOINDEX_PAGES:
        return output

    if page.canonical_url:
        _noindex_urls.add(page.canonical_url)

    # Material offers no page.meta.robots to hang this on, and a custom_dir
    # override would shadow a theme template for the sake of one line.
    return output.replace(
        "<head>",
        '<head>\n    <meta name="robots" content="noindex, follow">',
        1,
    )


def on_post_build(config):
    """Strip the noindex pages from sitemap.xml — the signals must agree."""
    if not _noindex_urls:
        return

    site_dir = Path(config["site_dir"])
    sitemap = site_dir / "sitemap.xml"
    if not sitemap.is_file():
        return

    ET.register_namespace("", SITEMAP_NS)
    tree = ET.parse(sitemap)
    root = tree.getroot()

    removed = 0
    for url in list(root.findall(f"{{{SITEMAP_NS}}}url")):
        loc = url.find(f"{{{SITEMAP_NS}}}loc")
        if loc is not None and (loc.text or "").strip() in _noindex_urls:
            root.remove(url)
            removed += 1

    if not removed:
        return

    tree.write(sitemap, encoding="utf-8", xml_declaration=True)

    # MkDocs writes both; a stale .gz would still be advertising the URL we
    # just removed. mtime=0 keeps the artefact byte-reproducible.
    gz = site_dir / "sitemap.xml.gz"
    if gz.is_file():
        with gzip.GzipFile(gz, mode="wb", mtime=0) as f:
            f.write(sitemap.read_bytes())


def on_files(files, config):
    """Re-admit root-level site-verification files. See the module docstring."""
    from mkdocs.structure.files import File

    docs_dir = Path(config["docs_dir"])
    present = {f.src_uri for f in files}

    for path in sorted(docs_dir.glob(SITE_VERIFICATION_GLOB)):
        if not path.is_file() or path.name in present:
            continue
        files.append(
            File(
                path.name,
                src_dir=str(docs_dir),
                dest_dir=config["site_dir"],
                use_directory_urls=config["use_directory_urls"],
            )
        )
    return files
