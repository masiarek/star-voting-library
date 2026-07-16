# How to Read a STAR Result Report (201)

**One line:** the engine prints a full **audit report** — matrix, divergence check, plain-English summary, both rounds, winner. A 101 voter only needs the last three lines; this page walks through the *whole* thing, section by section, so you can read (and trust) any STAR result.

→ The phenomenon this example shows: [Runoff Reversal](../../../01_STAR/runoff_overturns_leader/). Curriculum: [201.1 — Reading the results](../../CURRICULUM.md). This text report is the engine's half of a pair — the other is BetterVoting's visual display of the same race: [BetterVoting and the LH engine](../bettervoting_and_the_engine.md). The engine upstream: [`larryhastings/starvote` on GitHub](https://github.com/larryhastings/starvote) · [`starvote` on PyPI](https://pypi.org/project/starvote/).

---

## Start with the ballots (the input)

Always read the **input first**. This is `05_c3_b5_low-scores-bv1265.yaml` — a real BetterVoting election, 5 voters, 3 candidates (A, B, C), scored 0–5:

```
A, B, C
0, 0, 4
2, 0, 0
0, 2, 3
2, 0, 0
2, 2, 0
```

Everything below is *computed from these five rows* — nothing else goes in.

## The full report

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |    * A     |   * C     |
-----------------------------------------
         * A > |    ---     |3 - 0 - 2  |
         * C > | 2 - 0 - 3  |   ---     |

[Divergence from STAR]
  STAR     = A
  Approval = C   (differs from STAR)

[Runoff Reversal]
 - Score Round Winner(s) = (C)
 - Runoff Round Winner   = (A)
  Candidate C earned the highest total score, but
  Candidate A won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

Scoring Round
 The two highest-scoring candidates advance to the next round.
   C             -- 7 -- First place
   A             -- 6 -- Second place
   B             -- 4
 C and A advance.

Automatic Runoff Round
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 3 -- First place
   C             -- 2
   Equal Support -- 0
 A wins.

Winner — STAR Voting Method (single winner)
 A
```

## Reading it, section by section

**1. Runoff (Preference) Matrix.** The head-to-head table — the summable, auditable heart of the count (see [STAR is summable](../../STAR_Voting/properties_and_limits/STAR_summability.md)). Each cell reads **For – Equal Support – Against** for the *row* candidate vs the *column* candidate. So `A > … | 3 - 0 - 2` means: in A-vs-C, **3** ballots scored A over C, **0** scored them equal, **2** scored C over A. The `*` marks the two **Finalists** (A and C). Read the winner's row: A beats C 3–2, so A wins their head-to-head.

**2. [Divergence from STAR].** A quick cross-check: does another method — Choose-One (Plurality), RCV-IRV, **Approval**, Ranked Robin, or Condorcet — elect someone other than the STAR winner? The block hides the methods that agree and shows only those that diverge. Here only Approval diverges: `STAR = A` but `Approval = C` — counting each ballot's **≥3** scores as approvals (C is approved twice; A and B never clear the bar) picks **C**. That's a hint the score leader and the runoff winner may part ways — but the actual reversal test is the *next* block. (Note: the Approval count is a threshold count, **not** the same as "most total stars" — the score sum shown in the Scoring Round. They point the same way here, but they're different tallies.)

**3. [Runoff Reversal].** The plain-English summary, and the one sentence to quote: *"C earned the highest total score, but A won the automatic runoff — not a malfunction, STAR working as designed: the runoff elects the finalist preferred by the majority (of voters with a preference)."* This is the whole lesson in two lines — score leader ≠ winner, because the runoff applies a majority check between the two finalists. (This block was formerly headed "Majority Preference Enforcement Principle"; renamed to match the [glossary term](../../GLOSSARY.md) — and because the old name overclaimed: STAR does *not* satisfy the formal majority criterion, the guarantee is majority preference *between the finalists*.)

**4. [Scoring Round](../../STAR_Voting/the_count/STAR_Scoring_Round.md).** Add every candidate's stars: **C 7, A 6, B 4**. The two highest — **C and A** — become the Finalists; **B is out**. (This is one of the only three lines a first-time voter needs.)

**5. [Automatic Runoff Round](../../STAR_Voting/the_count/STAR_Automatic_Runoff.md).** Now compare *only* the two finalists. Each ballot is one full vote for whichever of C/A it scored higher: **A 3, C 2**, and **Equal Support 0** (no ballot scored A and C the same). **A wins.** Note the engine uses *Equal Support* — the house term for a genuine no-preference ballot, **not** "equal" in the loose sense. With `options: { show_runoff_percent: true }` (always on in the `_tabulated` copy), the engine also prints the winner's share of the **decided** voters — the percentage that actually settles the runoff. What that number means, and why its denominator excludes Equal Support, is the [runoff percentages](../../STAR_Voting/the_count/runoff_percentages.md) page.

**6. Winner.** **A** — the finalist more voters preferred, even though C led on score.

## When to show which part

| Audience | Show |
|----------|------|
| **101** — first-time voter | Scoring Round + Automatic Runoff Round + Winner (3 blocks) |
| **201** — official / auditor | + the Preference Matrix and the Majority Preference summary |
| **301** — debater / theorist | + [Divergence from STAR], Condorcet checks, score distribution, tiebreakers |

That's the point of the minimal on-screen report plus the always-full `_tabulated.txt`: the report scales to the reader. The full report for *any* example lives in its `_tabulated.txt` sibling; step-by-step method comparison is in [STAR vs RCV-IRV, step by step](../../topics/tabulation_star_vs_irv.md).
