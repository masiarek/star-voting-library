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
"""

from __future__ import annotations

import re

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


def on_nav(nav, config, files):
    _retitle(nav.items)
    return nav
