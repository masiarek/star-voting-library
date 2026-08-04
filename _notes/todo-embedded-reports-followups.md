# TODO — follow-ups from the embed-the-report work (2026-08-04)

Working notes to pick up later. Not site content — `mkdocs.yml`'s `exclude_docs` drops the whole `/_notes` folder. Delete sections as they're done.

Context: a question about why `02_STAR_Bloc/02_Examples/bv1815_bloc_3c2s_basic.html` showed no method or seat count turned into a repo-wide pass on hand-pasted engine reports. Everything below is **pushed and CI-green**; this file exists so the next session doesn't have to re-derive it.

## What shipped

Two mechanisms, both enforced by tests, both documented in `CLAUDE.md`:

1. **`case-meta` block on companion pages** (`d5156331`, `6688d776`). A case with both a generated page and a hand-authored companion (`<set>/<stem>.md`) now gets a method / seats / expected-winners line plus a full-count link under its H1, written by `build_yaml_pages.py` between `<!-- case-meta:start -->` / `<!-- case-meta:end -->`. Prose outside the markers is never touched. **Don't hand-edit inside the markers or restate those facts beside them** — change the YAML and rerun the generator. Gated by `test_companion_meta_blocks_are_current`.

2. **The paste gate** (`a95279f9`, `d009e8fa`, `ba5be085`, `73178b0f`). A ≥8-line engine-shaped fence on a hand-authored page must be either a `:report` include or labelled abridged. Gated by `test_md_links.py::test_no_new_hand_pasted_engine_reports`; `PASTED_REPORT_GRANDFATHERED` is empty and `test_grandfather_list_stays_empty` keeps it that way.

To show a count, write this **bare** — not inside a fence, the include brings its own:

```
--8<-- "<set>/cases/cases_pages/<stem>.md:report"
```

`build_yaml_pages.py` wraps each generated page's report fence in `[start:report]` / `[end:report]` for this. Include the **generated page, not the `_tabulated` mirror** — the mirror drags in its ~50-line YAML echo, and for `Runoff_08_ca_governor_reversal_gvdy42` that is 785 lines.

Scale: 98 fences became includes (87 of them were showing output the engine had stopped emitting, mostly pre-dating the bracketed `[STAR Voting: …]` headers); 20 were labelled as the deliberate abridgements they always were.

> **SUPERSEDED the same day.** The include block above is history — don't write a new one.
> `pymdownx.snippets` is a **MkDocs** extension, so `--8<-- "…:report"` renders the count on
> the site and prints as a **line of literal text on GitHub**. Adam hit it from the GitHub
> side on `bv2105r2_w3vvff_ice_cream_recheck.md`: heading, then `--8<-- "…"`, then no report.
> All 96 includes across 77 pages became generated blocks instead —
>
> ```
> <!-- report:<stem> -->
> <!-- /report -->
> ```
>
> — filled by `build_yaml_pages.py` with the very bytes the include used to pull (the fence
> between `SNIPPET_START`/`SNIPPET_END` on the generated page), so the site renders exactly
> what it did before and GitHub now renders it too. Drift is gated by
> `test_report_blocks_are_current`; a new include fails `test_no_snippet_report_includes_remain`;
> `check_pasted_reports` skips fences inside the markers. Everything the original work bought
> — one source of truth, no stale copies — is kept; only the delivery mechanism changed.
> Snippets **remain correct** for whole-file embeds inside a fence (`.yaml`, `_tabulated`),
> where GitHub degrades to a visible placeholder in a code block rather than to broken prose.

## 1. Three malformed `**Level:**` tags in `02_STAR_Bloc/03_Criteria/`

`check_repo_hygiene.py` reports these and nothing else:

```
02_STAR_Bloc/03_Criteria/committee_spoiler/README.md:9   **Level: 301 · deep dive.**
02_STAR_Bloc/03_Criteria/participation/README.md:9       **Level: 301 · deep dive.**
02_STAR_Bloc/03_Criteria/seat_order/README.md:9          **Level: 201.**
```

The trailing `.` has to sit *after* the closing `**`, and `seat_order` is missing its audience half. Wanted shape: `**Level: 201 · for presenters**`. Not gated by a test, so CI stays green either way — it only shows in the hygiene run.

## 2. Two pages whose excerpt is authorial, not machine-tracked

These are correctly labelled and the gate is satisfied, but nothing verifies their contents:

- `07_Concepts/tabulation_engines/LH_starvote/reading_a_star_report.md` — the block is annotated line-by-line; that *is* the page.
- `method_comparisons/symmetric_centrist_all_methods/bv2171_h93tm4_all_methods.md` — shows only the `[Divergence from STAR]` block, deliberately.

If either ever needs to become machine-tracked, the move is the one used for the Ranked Robin lesson in `8b99d501`: add the backing case, then include `:report`. Beware the index cost — see §4.

## 3. An annotated fence is NEVER convertible

Worth restating because it was learned the hard way: replacing a fence with an include **deletes the `←` margin notes**, and those are the lesson. Nine were destroyed that way and restored from history in `ba5be085`. If a block carries `←`, a `#` aside, or `·`-joined tallies, it gets `title="Abridged for the lesson — not verbatim engine output"` and stays. Same for a curated excerpt: the selection is authorial.

## 4. Adding a case regenerates shared indexes — mind whose work is in the tree

`test_yaml_index_current` gates `07_Concepts/YAML_test_case_index/README.md`, so a new case forces a `regen_all.py` run, and that sweeps up **every** case file on disk — including anything uncommitted. To regenerate cleanly while other work is in flight:

```bash
git worktree add -q --detach /tmp/clean HEAD && cp <new-case>.yaml /tmp/clean/<set>/cases/
```

then run `regen_all.py` inside `/tmp/clean`, copy back only the index files, and `git worktree remove --force /tmp/clean`. Also: cases in an `INDEX_COMPLETE_DIRS` folder need a row in that folder's README or `check_pages_indexed` fails.

## 5. Two commits carry work they don't describe

`af232b6a` ("Add the 'over 50%' pair") contains ~500 files of the embed conversion; `8b99d501` and `c517a124` likewise carry the Ranked Robin case and the vote-splitting refresh. A `git add -A` in this clone picked up an agent's working tree mid-session. Nothing was lost and everything was verified afterwards, but `git log --follow` on those paths will point at the wrong message. History was left alone because your own work is mixed into the same commits.

**Practical rule for this clone:** it is a live working copy for both of us. Stage by explicit path, and run `git diff -- <path>` before staging — `git add <path>` still stages the whole file, including someone else's in-flight hunk sitting in it.
