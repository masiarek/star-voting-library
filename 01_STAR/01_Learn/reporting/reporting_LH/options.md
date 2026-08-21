# LH reporting options — the defaults, `--full`, and the rare override

**Level: reference · deep dive**

**One line:** the engine decides **what the on-screen report shows** with a built-in set of house defaults — case files carry **no `options:` block** (dropped repo-wide 2026-08-09); a file *can* still set one to override a default, but that is reserved for the option-demo files and deliberate special renders. Display only — none of this ever changes the *result*.

→ Up: [How the LH engine reports](README.md) · hub: [STAR Reporting](../README.md) · house policy: [CLAUDE.md — working guidance for this repo](../../../../CLAUDE.md).

---

## The defaults (what a plain run shows)

Running any case file with no options at all gives the house render:

* the **finalists-only Preference Matrix** — automatically **omitted** for multi-winner races (a "Top 2 Finalist" grid is a single-winner concept) and for 2-candidate races (it would just echo the runoff);
* the self-reconciling **runoff summary** (`Voters with a preference: N of TOTAL …`);
* ballots **collapsed** (`count × scores`, most common first);
* **short headers** (`brief`), and the `[Divergence from STAR]` block whenever methods disagree — that one always prints;
* **hidden**: the scenario description (it's right there in the file), the `[Condorcet Winner]` line, and the `[Score Distribution]` table;
* **Ranked Robin**: the full pairwise table prints by default (the round-robin table *is* the method); the Smith-set block stays a separate opt-in.

The saved `_tabulated.txt` mirror ignores all of this and always renders everything.

## Want everything on screen? `--full`

```bash
.venv/bin/python STARVote_LH_tabulation_engine/starvote_larry_hastings.py <case>.yaml --full
```

`--full` puts the mirror's everything-on render on screen: full N×N matrix, Condorcet lines, score distribution, the description, and the expanded "Runoff math" funnel.

## The knobs, option by option (for the rare override)

A file may still set any of these under `options:` — the file always wins over the defaults. In this repo that's reserved for the option-demo files ([`04b_c4_b3_display-options-all.yaml`](../../../02_Examples/cases/04b_c4_b3_display-options-all.yaml) and the engine's `options_examples.yaml`) and deliberate special renders.

| Option | Default | What it adds/removes from the report | Deep dive |
|---|---|---|---|
| `show_matrix` | `true`* | the **Preference Matrix** (`For – Equal Support – Against`) | [matrix](matrix.md) |
| `matrix_finalists_only` | `true` | `true` = only the two finalists' row/col; `false` = full N×N grid | [matrix](matrix.md) |
| `show_condorcet` | `false` | the `[Condorcet Winner]` line and whether it matches the STAR winner | [matrix](matrix.md) |
| `show_score_counts` | `false` | the `[Score Distribution]` table (per-score counts, Total, Avg) | [score distribution](score_distribution.md) |
| `show_description` | `false` | the `scenario_description` echoed above the count | — |
| `show_runoff_percent` | `true` | the `Voters with a preference: N of TOTAL …` line | [runoff percentages](../../the_count/runoff_percentages.md) |
| `brief` | `true` | `true` collapses repeated section headers so the report is shorter | [brief (with/without)](brief.md) |
| `collapse_ballots` | `true` | `false` lists every ballot; `true` groups identical ones as `count × scores` | — |
| `count_separator` | `"×"` | the glyph in the collapsed count (`×`, `:`, `x`…) | — |
| `show_smith_set` | `false` | **Ranked Robin only** — the `--- Smith Set ---` block (who is still in contention, and whether the winner is inside it) | [Smith set](../../../../07_Concepts/topics/smith_set.md) |
| `show_irv` | — | vestigial: the `[Divergence from STAR]` block now always prints; the key is only accepted so old blocks still parse | — |

\* auto-off for multi-winner and 2-candidate races, as above. For Ranked Robin, `show_matrix` governs the full pairwise table (default on; `false` gives the compact echo).

## Two things that never change with options

1. **The winner and all the numbers** — options only hide or show sections, never alter the tabulation.
2. **The `_tabulated.txt` mirror** — it always forces every analysis on (full matrix, Condorcet, score counts, IRV, the runoff funnel), so the saved audit copy is complete regardless of what the on-screen report chose to show.

The defaults and auto-gates are locked by [`tests/test_default_render.py`](../../../../STARVote_LH_tabulation_engine/tests/test_default_render.py); the full report section-by-section is [Reading a STAR report](../../../../07_Concepts/tabulation_engines/LH_starvote/reading_a_star_report.md).
