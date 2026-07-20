# Exercise 9 — Game night: nobody is unbeatable

*Ten friends rank four board games for the club's game night. When the count is done, every one of the top three games loses some head-to-head matchup — rock, paper, scissors, with a fourth game everyone ranks last. If nobody beats everybody, who deserves to win? Predict what Ranked Robin does before you peek — including every rung of its ladder.*

**You practice:** filling in a pairwise matrix from ranked ballots · detecting that **no [Condorcet winner](../../00_start_here/GLOSSARY.md) exists** · walking [Ranked Robin](../../00_start_here/RCV_Ranked_Robin/ranked_robin_vs_condorcet.md)'s tiebreak ladder (most wins → total margin) to a *deterministic* answer inside a cycle.

Work each part on paper before opening its solution. The YAML at the bottom is runnable; the `_tabulated` mirror is the full audit report. This is the set's one **ranked-ballot** exercise — the ballots are `Azul>Boggle>Catan>Dominion`-style rankings, not scores.

## The ballots

Ten voters, four games:

| | ×4 voters | ×3 voters | ×3 voters |
|---|---|---|---|
| ranking | Azul > Boggle > Catan > Dominion | Boggle > Catan > Azul > Dominion | Catan > Azul > Boggle > Dominion |

## Your task

- **(a)** Fill in the full pairwise table: for each pair, how many voters rank one above the other?
- **(b)** Is there a Condorcet winner? A Condorcet loser?
- **(c)** Compute each game's win–loss record. What's the problem?
- **(d)** Ranked Robin's ladder is: most pairwise wins, then **total win margin**, then lot order. Walk it. Who wins game night — and does the lot ever fire?
- **(e)** Why is this exercise deliberately **not** backed by a live BetterVoting election, when most of this set is?

## Solutions

<details>
<summary><b>(a) The pairwise table</b></summary>

Azul beats Boggle **7–3** (the ×4 bloc plus the Catan bloc, which ranks Azul above Boggle). Boggle beats Catan **7–3** (the ×4 bloc plus its own). Catan beats Azul **6–4** (the Boggle and Catan blocs together). And all three beat Dominion **10–0**.

```text
             |     Azul     |   Boggle    |   Catan     |  Dominion   |
-----------------------------------------------------------------------
      Azul > |     ---      | 7 -  0 -  3 | 4 -  0 -  6 |10 -  0 -  0 |
    Boggle > |  3 -  0 -  7 |    ---      | 7 -  0 -  3 |10 -  0 -  0 |
     Catan > |  6 -  0 -  4 | 3 -  0 -  7 |    ---      |10 -  0 -  0 |
  Dominion > |  0 -  0 - 10 | 0 -  0 - 10 | 0 -  0 - 10 |    ---      |
```

</details>

<details>
<summary><b>(b) No Condorcet winner — one very clear Condorcet loser</b></summary>

Azul → Boggle → Catan → Azul is a genuine **cycle**: each of the three loses exactly one matchup, so *no one beats everyone* — there is no Condorcet winner to elect. Dominion, losing all three matchups 0–10, is the **Condorcet loser**. The three cyclists are precisely the [Smith set](../../00_start_here/topics/smith_set.md) — the smallest club that beats everyone outside it.

</details>

<details>
<summary><b>(c) The records — a three-way tie at the top</b></summary>

Azul 2–1, Boggle 2–1, Catan 2–1, Dominion 0–3. "Most pairwise wins" alone cannot decide — the cycle has manufactured a three-way tie. This is the moment every Condorcet-family method must say what it does next.

</details>

<details>
<summary><b>(d) The ladder — margins decide, the lot never fires</b></summary>

```text
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Azul       2–1–0         2     +12  Boggle, Dominion
    2  Boggle     2–1–0         2     +10  Catan, Dominion
    3  Catan      2–1–0         2      +8  Azul, Dominion
    4  Dominion   0–3–0         0     -30  —

Winner — Ranked Robin (RCV-RR): Azul
```

Total win margins: Azul (+4 −2 +10) = **+12**, Boggle (−4 +4 +10) = **+10**, Catan (−4 +2 +10) = **+8**. Azul's one loss is the *narrowest* (6–4) and its win the widest (7–3), so Azul tops the margin rung — **Azul wins, deterministically**; the lot rung is never reached. The engine's own note points out this is exactly where Condorcet methods diverge from each other — Minimax, Ranked Pairs, and Schulze each resolve cycles their own way: [cycle resolution](../../00_start_here/RCV_Ranked_Robin/cycle_resolution.md).

</details>

<details>
<summary><b>(e) Why LH-only</b></summary>

BetterVoting's Ranked Robin breaks a **three-way** wins tie at *random* (its ladder is wins → two-way head-to-head → random — the caveat documented on the repo's BV2142 clone case), so a BV run of this election could name any of the three cyclists and can't be frozen as a stable teaching result. The LH engine's wins → **margin** → lot ladder is deterministic here, so the exercise lives where its answer is reproducible. The two engines' tiebreak ladders are compared in [rr_tiebreak_lh_vs_bv](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md).

</details>

## Reading this fairly

Cycles among top candidates are real but rare in large electorates (and this one is engineered to be perfectly tidy). The honest takeaways: "elect the Condorcet winner" is an incomplete instruction — a method must also say what happens when there isn't one — and different completions genuinely elect different candidates, which is a *choice*, not an error. The [four-part test](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md) applies to cycle horror-stories as much as anything else.

## Run it yourself

```
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/cases/ex09_game_night_cycle.yaml
```

Source: [ex09_game_night_cycle.yaml](cases/ex09_game_night_cycle.yaml). Full audit report: [mirror](cases/cases_tabulated/ex09_game_night_cycle_tabulated.txt).

---

**Where this comes from.** Original to this repo (ballots and cast — the candidates are board games so the cycle reads as fun, not politics). Concept homes: [Ranked Robin vs Condorcet](../../00_start_here/RCV_Ranked_Robin/ranked_robin_vs_condorcet.md), [cycle resolution](../../00_start_here/RCV_Ranked_Robin/cycle_resolution.md), and the worked [Smith-set case](../../05_Ranked_Robin/condorcet_vs_ranked_robin/cases/cases_pages/04_smith_set_c4_b7.md).

*Back to [the exercises set](README.md) · curriculum home: [Voting 301](../../00_start_here/curriculum/CURRICULUM_301.md)*

# file: ex09_game_night_cycle.md
