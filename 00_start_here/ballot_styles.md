# Alternate ballot styles — one voter, three ballots

*The same voter's opinion, expressed on three different ballots: **Ranking**, **Yes/No** (Approval), and **Scoring**. Seeing them side by side is the clearest way to grasp what each ballot **captures** and what it **throws away**.*

→ The core distinction — order vs. strength: [scores vs. ranks](scores_and_ranks/scores_vs_ranks.md) · why Approval & STAR aren't "RCV": [scoring methods vs. ranked voting](scoring-methods-vs-ranked-voting.md)

![Three ballot styles side by side for the same five candidates (Andre, Blake, Carmen, David, Ella): a Ranking ballot with a 1st–5th grid, a Yes/No (Approval) ballot with one filled or open bubble per candidate, and a Scoring ballot rating each candidate 0 (Worst) to 5 (Best)](img/ballot_styles_ranking_yesno_scoring.png)

---

## The three ballots

Meet one voter deciding among five candidates — Andre, Blake, Carmen, David, Ella. Here is how that *same* opinion looks on each ballot style (● = the mark the voter made).

**Ranking** — put the candidates in order, 1st through 5th. One mark per column, one per row.

| Candidate | 1st | 2nd | 3rd | 4th | 5th |
|---|:--:|:--:|:--:|:--:|:--:|
| Andre | ● | ○ | ○ | ○ | ○ |
| Blake | ○ | ○ | ○ | ● | ○ |
| Carmen | ○ | ● | ○ | ○ | ○ |
| David | ○ | ○ | ● | ○ | ○ |
| Ella | ○ | ○ | ○ | ○ | ● |

**Yes/No** — approve each candidate, or don't. One bit per candidate.

| Candidate | Approve? |
|---|:--:|
| Andre | ● approve |
| Blake | ○ no |
| Carmen | ● approve |
| David | ● approve |
| Ella | ○ no |

**Scoring** — rate each candidate from 0 (worst) to 5 (best), independently. Equal scores allowed.

| Candidate | Score (0–5) |
|---|:--:|
| Andre | 5 |
| Blake | 1 |
| Carmen | 4 |
| David | 4 |
| Ella | 0 |

## The same opinion, three ways

Line them up and the trade-offs jump out:

| Candidate | Ranking | Yes/No | Score 0–5 |
|---|:--:|:--:|:--:|
| Andre | 1st | ● | 5 |
| Blake | 4th | ○ | 1 |
| Carmen | 2nd | ● | 4 |
| David | 3rd | ● | 4 |
| Ella | 5th | ○ | 0 |

- **Ranking** records *order* but not *distance*. It's forced to call Carmen "2nd" and David "3rd" even though the voter rates them **the same (both 4)** — a distinction the ranked ballot can't express (no equal ranks on a strict ballot). It also spaces every rung equally, so it can't show that the drop from David (3rd) to Blake (4th) is a cliff while 1st→2nd→3rd is a gentle slope.
- **Yes/No** is a single **threshold**: one bit per candidate. It cleanly separates the three the voter likes from the two they don't, but it loses *all* order and strength *within* each group — Andre and David read identical, and so do Blake and Ella.
- **Scoring** keeps both **order and strength**, and **[allows ties](scores_and_ranks/strict_vs_weak_ranks.md)**: Carmen = David = 4, Andre a clear 5, Blake a grudging 1, Ella a 0 — and if a tied pair turn out to be the two finalists, that tie counts as [Equal Support](GLOSSARY.md) in STAR's runoff. It's the most expressive of the three, and Yes/No is just scoring at 1-bit resolution (the [fidelity ladder](scores_and_ranks/fidelity_ladder.md): **Approval → Range → STAR**).

## Which methods read which ballot

| Ballot style | Cardinal or ordinal? | Methods that use it |
|---|:--:|---|
| Ranking | ordinal | [RCV-IRV](RCV_IRV/RCV-IRV-Hare.md), STV, Condorcet ([Ranked Robin](RCV_Ranked_Robin/ranked_robin.md)), Borda, Bucklin |
| Yes/No | cardinal (1-bit) | [Approval](Approval_Voting/approval_voting.md) |
| Scoring | cardinal (graded, e.g. 0–5) | [Score / Range](Range_Voting/range_voting.md), [STAR](STAR_Voting/STAR_start_here.md) (a [hybrid](STAR_Voting/STAR_hybrid_nature.md) — score ballot **+ runoff**) |

The ballot is *what the voter marks*; the **tabulation** is *how it's counted* — and the same ballot can be counted more than one way (a ranked ballot by IRV, Ranked Robin, or STV). See [ballot vs tabulation](what_is_a_voting_method.md) and the [glossary](GLOSSARY.md).

# file: ballot_styles.md
