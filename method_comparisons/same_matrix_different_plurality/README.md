# Same matrix, different plurality — three electorates the pairwise table cannot tell apart

*Three 12-ballot electorates. **Identical** pairwise results — every head-to-head count, every margin, the same Condorcet winner, the same Borda scores. Ranked Robin, Minimax, Ranked Pairs and Kemeny cannot tell them apart, and must all return the same winner on all three. **Choose-One returns a different winner on each — one per candidate.** That is the whole of [what a method reads](../../07_Concepts/topics/what_a_method_reads.md), demonstrated in ballots you can count by hand.*

**Level: 301 · deep dive** Concept: [what a method reads](../../07_Concepts/topics/what_a_method_reads.md) · [summability](../../07_Concepts/topics/summability/README.md) · [the C1/C2/C3 tiers](../../07_Concepts/topics/condorcet/condorcet_reading_list.md). **LH-only** — the lesson is the *contrast across three electorates*, which a single BetterVoting election cannot show.

---

## The three electorates

Same cast throughout (Ada, Ben, Cal) — it's one election with the ballots rearranged, so a new cast would imply a different election.

| | Ballots (12 each) | First choices | Choose-One winner |
|---|---|---|:---:|
| **P1** | 4× Ada>Ben>Cal · 4× Cal>Ben>Ada · 2× Ben>Cal>Ada · 1× Ben>Ada>Cal · 1× Ada>Cal>Ben | Ada 5, Cal 4, Ben 3 | **Ada** |
| **P2** | 2× Ada>Ben>Cal · 2× Cal>Ben>Ada · 3× Ben>Ada>Cal · 2× Ben>Cal>Ada · 1× Ada>Cal>Ben · 2× Cal>Ada>Ben | Ben 5, Cal 4, Ada 3 | **Ben** |
| **P3** | 3× Ada>Ben>Cal · 3× Cal>Ben>Ada · 3× Ben>Ada>Cal · 1× Ben>Cal>Ada · 2× Cal>Ada>Ben | Cal 5, Ben 4, Ada 3 | **Cal** |

## The pairwise table — the same one, three times

All three electorates produce this, exactly:

```
Round-Robin — every pair, head-to-head (For – Against):
   Ben  beats Ada   7 – 5
   Ada  ties  Cal   6 – 6
   Ben  beats Cal   7 – 5
```

Verified: the three reports are byte-identical on those lines. So **Ranked Robin elects Ben in all three** — and so would Minimax, Ranked Pairs, Schulze and Kemeny, because there is nothing in their input that differs.

Borda too. A Borda score is just a row of that table added up: with margins Ada −2, Ben +4, Cal −2, the scores are **Ada 11, Ben 14, Cal 11** in every one of the three electorates ([why that identity holds](../../06_Other/other_ranked_methods/borda.md)).

## Why the ballots differ but the table doesn't

The trick is that **a ballot and its exact mirror image cancel out pairwise.** `Ada>Ben>Cal` and `Cal>Ben>Ada` together put one vote on each side of every head-to-head — every count and every margin is untouched. But they do *not* cancel in the first-choice tally: one hands a first preference to Ada, the other to Cal. Swap mirror pairs in and out and you can move the plurality winner anywhere you like while the pairwise table sits perfectly still.

That is not a quirk of these particular ballots. It's the structural fact: **first-choice counts are not recoverable from the pairwise matrix.**

## What this does and does not show

**It shows** that Choose-One's winner is not a function of the pairwise data — the sense in which plurality sits outside the matrix ([Fishburn C3](../../07_Concepts/topics/what_a_method_reads.md)). It makes [vote splitting](../split_voting/README.md) precise rather than rhetorical: in P1 and P3 the plurality winner isn't even the candidate a majority prefers head-to-head.

**It does not show** that plurality is "more complex," or that reading less is a defect in itself. Choose-One publishes the *smallest* possible precinct summary — one number per candidate — and is the cheapest method here to audit. The tiers classify *which* statistic a rule reads, not how big it is or how hard it is to count; the two ideas come apart at exactly this method ([summability](../../07_Concepts/topics/summability/README.md)).

**Note P2**, where plurality happens to agree with everyone else and elects Ben. Nothing forces the disagreement — the point is that plurality is *free* to differ, not that it always does.

## Run it

```bash
.venv/bin/python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/same_matrix_different_plurality/cases/same_matrix_p1_ranked_robin.yaml
```

| Electorate | Ranked Robin | Choose-One |
|---|---|---|
| P1 | [`…p1_ranked_robin.yaml`](cases/same_matrix_p1_ranked_robin.yaml) → Ben | [`…p1_plurality.yaml`](cases/same_matrix_p1_plurality.yaml) → Ada |
| P2 | [`…p2_ranked_robin.yaml`](cases/same_matrix_p2_ranked_robin.yaml) → Ben | [`…p2_plurality.yaml`](cases/same_matrix_p2_plurality.yaml) → Ben |
| P3 | [`…p3_ranked_robin.yaml`](cases/same_matrix_p3_ranked_robin.yaml) → Ben | [`…p3_plurality.yaml`](cases/same_matrix_p3_plurality.yaml) → Cal |

The Choose-One files encode each ballot as a single `1` — which is exactly what a Choose-One ballot *is*, and makes visible what it discards.

## Related

- [What a method reads](../../07_Concepts/topics/what_a_method_reads.md) — the concept page this case backs
- [Copeland vs Borda margins](../copeland_vs_borda_margins/README.md) — the C1-vs-C2 contrast (direction only, vs direction plus size)
- [The cycle–cocycle decomposition](../../07_Concepts/topics/cycle_cocycle_decomposition.md) · [summability](../../07_Concepts/topics/summability/README.md) · [the spoiler effect](../../07_Concepts/topics/spoiler_effect.md)
