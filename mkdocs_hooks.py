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
"""

from __future__ import annotations

import posixpath
import re
from pathlib import Path

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
        "majority_sweep.md",
        "score_leader_no_seat.md",
        "bloc_tiebreaks.md",
        SPINE_BREAK,
        "bloc_star_vs_other_bloc_methods.md",
        "bloc_honest_limits.md",
        "glossary_bloc_star.md",
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
