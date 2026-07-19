# Pairwise Counting — Every Ballot Is a Tiny Matrix

*How the preference matrix actually gets built: one ballot at a time. Once you see that each ballot is already a little head-to-head table, the matrix — and why it's precinct-summable — stops being mysterious.*

→ **Level: Voting 201** — Curriculum [201.1](../CURRICULUM.md) (reading the results) · Glossary: [`preference matrix`](../GLOSSARY.md) · the summability payoff: [Summability topic hub](summability/)

---

## Two terms, one thing (a verb and a noun)

- **Pairwise counting** is the *process*: for every **pair** of candidates, tally each ballot's verdict — does this ballot support A over B, B over A, or neither?
- The **preference matrix** is the *artifact* that process produces: the table holding those tallies for every pair.

They are the same idea seen as verb and noun. The artifact goes by **many** names — **preference matrix**, **pairwise matrix**, **pairwise-comparison matrix**, **head-to-head table**, and, on [Wikipedia](https://en.wikipedia.org/wiki/Condorcet_method#Pairwise_counting_and_matrices), **beats matrix**, **tournament matrix**, or **outranking matrix**. When it holds the *summed* tallies for the whole electorate it's the **sum matrix**. The LH engine prints it as the **"Runoff (Preference) Matrix"** with the legend **For – Equal Support – Against**. All the same table. ([electowiki](https://electowiki.org/wiki/Pairwise_counting) calls the process "pairwise counting"; we use its mechanics pages here while noting it's an advocacy-adjacent wiki.)

> **Seen the "strange" Wikipedia matrix?** That article shows a *single ballot* written as a 0/1 grid (1 = the row candidate beats the column candidate), then *adds* the ballots into a **sum matrix**. That two-step — one ballot is a matrix, and matrices add — is exactly what this page builds below, and it's why the count is **[precinct-summable](summability/)**.

## The one idea: a ballot is already a matrix

You don't need the whole electorate to start a preference matrix — **a single ballot is one**. Take the first voter of the canonical [Ann, Bob, Cal election](../../01_STAR/_main/_main_pages/bv2187_qrw6wb_ann-bob-cal.md) (3 voters × 3 candidates, [registered canonical #1](../tips/TIPS_canonical_elections.md) — [live on BetterVoting](https://bettervoting.com/qrw6wb/results)). She scored **Ann 5, Bob 4, Cal 0**. Written as her own tiny matrix (For – Equal Support – Against, row vs column):

```text
Voter 1 (Ann 5, Bob 4, Cal 0)
        |    Ann    |    Bob    |    Cal    |
  Ann > |    ---    | 1 - 0 - 0 | 1 - 0 - 0 |
  Bob > | 0 - 0 - 1 |    ---    | 1 - 0 - 0 |
  Cal > | 0 - 0 - 1 | 0 - 0 - 1 |    ---    |
```

Her 5 beats the 4, so this ballot is one vote **For Ann over Bob** — even though she likes Bob too. Here's the one thing *not* to misread: that **`1` is a count, not a margin** — it is *not* 5 − 4. Look at **Ann over Cal** (5 vs 0), which is *also* just `1`: the cell records only *whether* one candidate is higher, never *by how much*. A 5-vs-4 and a 5-vs-0 are each exactly **one vote For**. (That intensity is thrown away *here* on purpose — which is why STAR keeps the score totals too, right alongside this matrix.) Every cell is just "which did this ballot put higher?"

**Counting the election = adding the ballots' matrices.** Here are all three ballots' pair verdicts, and their sum:

| Ballot (Ann, Bob, Cal) | Ann vs Bob | Ann vs Cal | Bob vs Cal |
|---|:--:|:--:|:--:|
| Voter 1 — 5, 4, 0 | **Ann** (5>4) | **Ann** (5>0) | **Bob** (4>0) |
| Voter 2 — 3, 5, 2 | **Bob** (5>3) | **Ann** (3>2) | **Bob** (5>2) |
| Voter 3 — 0, 3, 5 | **Bob** (3>0) | **Cal** (5>0) | **Cal** (5>3) |
| **Sum (For – Equal Support – Against)** | Ann: 1 – 0 – 2 | Ann: 2 – 0 – 1 | Bob: 2 – 0 – 1 |

That bottom row **is** the preference matrix. Here it is straight from the LH engine (the [full report](../../01_STAR/_main/_main_tabulated/bv2187_qrw6wb_ann-bob-cal_tabulated.txt) of [`bv2187_qrw6wb_ann-bob-cal.yaml`](../../01_STAR/_main/bv2187_qrw6wb_ann-bob-cal.yaml)):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Ann    |  * Bob    |    Cal    |
-----------------------------------------------------
       * Ann > |    ---     |1 - 0 - 2  |2 - 0 - 1  |
       * Bob > | 2 - 0 - 1  |   ---     |2 - 0 - 1  |
         Cal > | 1 - 0 - 2  |1 - 0 - 2  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Bob — matches the STAR winner
```

Reading it: **Bob beats Ann 2–1 and beats Cal 2–1**, so Bob wins every head-to-head — the [Condorcet winner](condorcet/). And look at the Bob-vs-Ann cell: **2 – 0 – 1 is exactly STAR's Automatic Runoff** (Bob preferred on 2 ballots, Ann on 1). The runoff isn't a separate computation — it's **one cell of this matrix**.

If a ballot puts a pair **equal** — the same score, or both blank — that ballot lands in the middle **Equal Support** bucket for that pair (none happen to occur here). No verdict is ever lost: every ballot counts For, Against, or Equal Support on every pair, which is what makes the matrix self-reconciling in an audit.

## Ranked or scored — same construction

The matrix doesn't care which ballot style fed it, only *order*:

- **Scored ballot (0–5):** higher score = For. Strength is deliberately thrown away — a 5-vs-4 and a 5-vs-0 are each one vote For (that's why STAR keeps the score totals *too*).
- **Ranked ballot (A>B>C):** higher rank = For. An unranked candidate counts below every ranked one; two unranked (or equal-ranked, where allowed) candidates are Equal Support for that pair.

## Why this one idea earns its keep

1. **It's the auditable heart of the count.** The matrix is a small fixed-size table anyone can recompute from the ballots — the annotated tour of a full report is [How to Read a STAR Result Report](../tabulation_engines/LH_starvote/reading_a_star_report.md), and the display demo is [`04b_c4_b3_display-options-all`](../../01_STAR/_main/_main_pages/04b_c4_b3_display-options-all.md) (`show_matrix`).
2. **[Ranked Robin](../RCV_Ranked_Robin/ranked_robin.md) reads its whole result off it** — most head-to-head wins takes the seat. The matrix isn't a supporting exhibit there; it *is* the tally.
3. **It's why these counts are [summable](summability/).** The election's matrix is the sum of the ballots' matrices — so a precinct's matrix is just a partial sum, and precinct tables **add** to the statewide result. That's the worked two-district demo in [Ranked Robin is summable](../RCV_Ranked_Robin/RCV_RR_summability.md) and [STAR is summable](../STAR_Voting/properties_and_limits/STAR_summability.md), and the very thing [IRV's count can't do](../RCV_IRV/RCV_IRV_lack_of_summability.md): IRV has no per-ballot artifact that adds — its rounds depend on everyone else's ballots.

## Further afield (301): write-ins and bookkeeping variants

Real election offices hit a wrinkle: a **write-in** candidate discovered mid-count has no row or column yet. electowiki's [pairwise counting](https://electowiki.org/wiki/Pairwise_counting#Example_without_numbers) page works through the administrative fixes — retrofitting the new candidate's cells, and a "negative counting" variant that records only the *upsets* to cut bookkeeping. Clever, but it changes nothing conceptually: every variant still ends at the same summed matrix. File under election administration, not voting theory.

---

## Cross-references

- [Ann, Bob, Cal — the canonical leading example](../../01_STAR/_main/_main_pages/bv2187_qrw6wb_ann-bob-cal.md) — the election used above (frozen ballots; [canonical registry](../tips/TIPS_canonical_elections.md))
- [How the count works — STAR vs RCV-IRV, step by step](tabulation_star_vs_irv.md) — the two counts this matrix feeds and contrasts
- [Summability topic hub](summability/) · [Ranked Robin is summable](../RCV_Ranked_Robin/RCV_RR_summability.md) — the precinct-level payoff
- [The math behind Condorcet](../RCV_Ranked_Robin/the_math_behind_condorcet.md) — the 301 sequel: the matrix as a *graph* (tournaments, Smith set, cycles)
- Glossary: [`preference matrix`, `Equal Support`, `summability`](../GLOSSARY.md)
