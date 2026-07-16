# `starvote_larry_hastings.py` — presentation wrapper

A thin presentation/automation layer over the vendored `starvote` engine (see `FORK_NOTES.md`). The engine does the tabulation; this script handles how elections are **loaded, run, displayed, and saved**. It never duplicates engine logic — it `import starvote` and feeds it ballots.

Use it to run a single election file, or use `tools_adam/tabulate_all.py` to run every illustration at once.

## Quick start

```bash
# Run one election file (YAML or starvote CSV)
python starvote_larry_hastings.py "elections_illustrations/99_01 tennessee_capital.yaml"

# Run every election under elections_illustrations/ and write results
python tools_adam/tabulate_all.py
```

Color is shown automatically in a real terminal and in PyCharm's run console. Set `NO_COLOR=1` to force plain output anywhere.

## Election file format

A `.yaml`/`.yml` file supplies the ballots plus a few optional fields. The loader tolerates flat files, a single `election:` wrapper, or a `races:` list.

```yaml
election_title: Tennessee Capital — classic STAR example
scenario_description: |-
  Free-text context, printed as a header above the results.

num_winners: 1          # -> seats
voting_method: STAR     # see "Methods" below

options:                # all optional; see "Display options"
  show_matrix: true
  matrix_finalists_only: true

ballots: |-
  Memphis,Nashville,Chattanooga,Knoxville
  42: 5, 4, 3, 2        # "weight: scores" — 42 identical ballots
  26: 2, 5, 4, 3
```

- **`election_title`** and **`scenario_description`** print as a header above the tabulation (also accepts `race_description` / `election_description`).
- Ballots may use `weight: scores` (e.g. `42: 5,4,3,2`) to stand in for many identical ballots. Empty cells and marker characters count as score 0.

### Methods (`voting_method`)

| Value | Method | Winners |
|-------|--------|---------|
| `STAR` / `star` | STAR Voting | single (`num_winners: 1`) |
| `bloc` / `bloc star` | Bloc STAR | multi (`num_winners: >= 2`) |
| `allocated` | Allocated Score Voting (proportional STAR) | multi |
| `sss` | Sequentially Spent Score | multi |
| `rrv` | Reweighted Range Voting | multi |

A method/seat mismatch (single-winner method with `num_winners > 1`, or a multi-winner method with `num_winners: 1`) is rejected with an explanatory error.

## Display options

Set under `options:` (top level or per race). All are booleans unless noted.

| Option | Default | Effect |
|--------|---------|--------|
| `show_matrix` | off | Show the Runoff (Preference) Matrix — the head-to-head / pairwise grid. |
| `matrix_finalists_only` | off | Restrict the matrix to just the two finalists (the decisive runoff matchup). Requires `show_matrix`. |
| `show_condorcet` | off | Show the `[Condorcet Winner]` line. |
| `show_score_counts` | off | Show the per-candidate `[Score Distribution]` table. |
| `brief` | on | Collapse repetitive `[STAR Voting: …]` section headers into plain sub-headings. |
| `collapse_ballots` | on | On-screen report identical ballots as `count × scores` (most common first) instead of one row each. |
| `count_separator` | `×` | Separator for the collapsed count: `×`, `:`, or `x`/`X` (all round-trip to valid input). |

## Output conventions

- **Equal Support** is the relabeled "no preference" bucket in the runoff, shown as `Equal Support -- N` (plain — the aka is documented once in GLOSSARY.md). ("Equal Support" is the Equal Vote Coalition's term.)
- **Runoff colors** mirror the matrix legend: the winner's count is green (For), the other finalist's is red (Against), and Equal Support is blue (Equal Support). A tie is left neutral until it resolves; tiebreaker rounds (raw scores) are uncolored.
- **Round separators**: in multi-round methods (e.g. Bloc STAR) a faint rule is drawn before each new round after the first, grouping the output into blocks.
- **Winner line** restates the method and winner count, e.g. `Winner (STAR Voting Method — single winner)` or `Winners (Bloc STAR Method — 3 winners)`.
- **Setup line** (multiwinner): the base engine's standalone `Want to fill N seats.` is folded into the ballot-count line, so the two "size of this election" facts sit together — `Tabulating 4 ballots to fill 3 seats.` Single-winner output is unchanged. (Done in the wrapper's `custom_print`; the vendored engine is untouched.)
- **`[Score Distribution]`** (with `show_score_counts`): a per-candidate star histogram, captioned `(how many ballots gave each star rating)`, with a `Score` corner label and a `===` rule row so the `5 4 3 2 1 0` header reads unmistakably as star values. The **Avg** column is computed from an *exact rational* and rounded **half-up** to one decimal (not float `/` + `{:.1f}`, which rounds half-to-even and would print an exact `1.25` as `1.2`). See [Score Distribution & averages](../00_start_here/STAR_reporting/score_distribution_and_averages.md).

## Change log — wrapper display (this is *our* code, not the vendored engine)

> For the **full consolidated list** of all LH changes (methods, reports, fixes across the whole engine, not just display), see **[`LH_ENGINE_CHANGES.md`](LH_ENGINE_CHANGES.md)**. The entries below are the wrapper's *display-layer* edits specifically.

Behavioral edits to `starvote_larry_hastings.py`'s presentation layer. The vendored `starvote/` core stays pristine (see [`FORK_NOTES.md`](FORK_NOTES.md)); these never touch it.

- **Ranked Robin equal-rankings (`A=B>C`) — parser fix** — `run_ranked_robin`'s ranked-ballot reader now splits each `>` rank level on `=`, so tied candidates share a rank and are scored as *Equal Support* against each other (exactly how Ranked Robin treats a tie). Previously the parser split only on `>`, so a level like `Ava=Bianca=Cedric` was mis-read as a *single phantom candidate* by that literal name — inflating the field and electing the wrong winner. Strict ballots (every level a singleton) are byte-for-byte unchanged. Equal ranking is a core Ranked Robin feature, so this lets the engine read the weak orders RR is defined on natively (e.g. the [electowiki worked example](https://electowiki.org/wiki/Ranked_Robin)). Guarded by `tests/test_ranked_robin.py::test_equal_rankings_are_ties`.
- **`[Score Distribution]` header + exact-rational half-up average** — `Score` corner label, `===` rule row, star-rating caption, and the Avg float→`Decimal`/`ROUND_HALF_UP` fix. ([full write-up](../00_start_here/STAR_reporting/score_distribution_and_averages.md))
- **Multiwinner setup line** — merged `Want to fill N seats.` into `Tabulating N ballots to fill N seats.`
- Earlier: `[Lot-decided tie — rare]` callout; validator accepts `voting_method: Bloc STAR`.

## Saved `_tabulated` files

Every run of a file also writes a plain-text copy into a sibling **mirror folder** whose name is the source folder + `_tabulated`, with the file itself also suffixed `_tabulated`:

```
elections_illustrations/Multi_winner/foo.yaml
  -> elections_illustrations/Multi_winner_tabulated/foo_tabulated.txt
elections_illustrations/bar.yaml
  -> elections_illustrations_tabulated/bar_tabulated.txt
```

Each `_tabulated.txt` contains:

1. A header recording the source name and the tabulated name:

   ```
   ======================================================================
   SOURCE FILE:     bar.yaml
   TABULATED FILE:  bar_tabulated.txt
   ======================================================================
   ```

   (No timestamps, deliberately: the mirrors are committed to git, so regenerating them on any machine yields a byte-identical file whenever the tabulation content is unchanged. Git history is the record of when a mirror last changed.)
2. The original election file, copied verbatim.
3. A `TABULATION RESULTS` section.

**Important:** the saved file is always rendered with the **full, most explanatory** output (every analysis on, full N×N matrix, non-brief headers), regardless of the file's own `options:`. Only the **on-screen** output honors the file's options. This keeps the on-screen demo clean while the saved record is complete. (The console no longer prints a "tabulated copy" path, to avoid distracting an audience.)

Add `--save` to additionally embed an `expected_results:` block (winners + plain-text report) back into the source YAML.

## Batch runner — `tools_adam/tabulate_all.py`

```bash
python tools_adam/tabulate_all.py            # scans elections_illustrations/
python tools_adam/tabulate_all.py --root other/folder
```

It finds every election file (skipping `*_tabulated` mirrors), **wipes** the `_tabulated` mirror folders so output always reflects current inputs, then runs each file (each writing its full `_tabulated.txt`). Wiping is best-effort: on filesystems that block deletion it warns instead of crashing and overwrites in place.

## Example library (`elections_illustrations/`)

- `Single_winner/` — STAR basics (1–3 candidates / ballots), voting styles (bullet vote, protest vote).
- `Multi_winner/` — minimal Bloc STAR, and proportional examples (`allocated`, `sss`, `rrv`) sharing the same ballots so you can compare how a cohesive minority earns a seat that Bloc STAR would deny.
- Top level — the Tennessee classic, plus display-option demos (`with_options.yaml`, `with_options2.yaml`).
