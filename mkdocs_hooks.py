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
"""

from __future__ import annotations

import re

# Multi-word names first, so "ranked robin" is settled before the single-word
# pass looks at "rr". Keys are matched case-insensitively as whole words.
PHRASES = {
    "ranked robin": "Ranked Robin",
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


def _retitle(items) -> None:
    for item in items:
        if item.is_section:
            # unpad first: it can expose a lowercase acronym at the front.
            item.title = fix_acronyms(unpad(item.title))
            _retitle(item.children)


def on_nav(nav, config, files):
    _retitle(nav.items)
    return nav
