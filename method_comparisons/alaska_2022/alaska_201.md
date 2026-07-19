# Alaska 2022 · 201 — the vote math, round by round

*You've read the [plain-language 101](alaska_101.md). Now we count it exactly: the IRV transfers, the exhausted ballots, the head-to-head grid, and the two pieces of vocabulary that name what happened — **Condorcet winner** and **center squeeze**. All numbers are the [reduced 200-voter model](README.md); the real election is the same story ~943× bigger.*

Run it: [`bv2213_k3fmwv_alaska_2022.yaml`](bv2213_k3fmwv_alaska_2022.yaml) · live BV counts: [results ↗](https://bettervoting.com/k3fmwv/results).

---

## The ballots

Every voter's ranking, as nine groups (a "preference profile"). Read `Palin>Begich>Peltola` as "ranked Palin 1st, Begich 2nd, Peltola 3rd"; a single name is a **bullet** ballot that ranked only that candidate:

| Voters | Ranking |
|---:|:---|
| 50 | Peltola > Begich > Palin |
| 25 | Peltola *(only)* |
| 5 | Peltola > Palin > Begich |
| 36 | Palin > Begich > Peltola |
| 23 | Palin *(only)* |
| 4 | Palin > Peltola > Begich |
| 29 | Begich > Palin > Peltola |
| 16 | Begich > Peltola > Palin |
| 12 | Begich *(only)* |

200 voters. Add up the first names in each row: **Peltola 80, Palin 63, Begich 57.**

## RCV-IRV, counted

**Round 1** — first-choice totals:

| | Votes | |
|---|---:|---|
| Peltola | 80 | hopeful |
| Palin | 63 | hopeful |
| **Begich** | **57** | **fewest → eliminated** |

**Transfer Begich's 57 ballots** to each voter's next choice still standing:

- `Begich > Palin > Peltola` (29) → **Palin**
- `Begich > Peltola > Palin` (16) → **Peltola**
- `Begich` only (12) → no next choice → **exhausted** (leaves the count)

**Final round:**

| | Votes | |
|---|---:|---|
| **Peltola** | 80 + 16 = **96** | **elected** |
| Palin | 63 + 29 = **92** | |
| *(exhausted)* | 12 | |

Peltola wins **96–92**. Notice the denominator: 96 out of 200 ballots cast is only **48%** — a "majority" of the *surviving* 188 ballots, not of everyone. Those 12 exhausted ballots quietly shrank the finish line. (More on that in [301](alaska_301.md).)

## The head-to-head grid

Now the other question: every one-on-one matchup. Read each cell as **for – equal – against** (from the row candidate's view):

```
                    |    Peltola    |    Begich     |     Palin     |
        Peltola  >  |      ---      | 84 - 23 - 93  | 96 - 12 - 92  |
        Begich   >  | 93 - 23 - 84  |     ---       |107 - 25 - 68  |
        Palin    >  | 92 - 12 - 96  | 68 - 25 -107  |     ---       |
```

Read the **Begich** row:

- **Begich vs Peltola: 93 – 84** → Begich wins. (The right wing, plus Begich's own voters, prefer the center candidate to the left one.)
- **Begich vs Palin: 107 – 68** → Begich wins big. (The left wing prefers the center candidate to the right one.)

Begich wins **every** matchup. A candidate who beats each rival head-to-head is the **[Condorcet winner](../../00_start_here/topics/condorcet/)** — the "beats-everyone," consensus candidate. Alaska *had* one (Begich), and RCV-IRV **didn't elect him.** That's a **Condorcet failure**.

## Naming the mechanism: center squeeze

Why did IRV miss him? Look back at Round 1: Begich had the fewest *first* choices, so he was eliminated **before** any head-to-head mattered. The broadly-liked centrist is knocked out early precisely because "everyone's acceptable second choice" earns few *firsts*. That specific pattern — the middle candidate eliminated between two wings despite beating both head-to-head — is the **[center squeeze](../../00_start_here/topics/center_squeeze/README.md)**. It is an **IRV-specific** flaw: it comes from eliminating on first-choice counts, not from ranked ballots themselves.

## The same ballots, four ways

Because the model carries scores too, we can count the identical electorate four ways:

| Method | What it rewards | Winner |
|---|---|:---:|
| **Choose-One (Plurality)** | most 1st choices | Peltola (80) |
| **RCV-IRV (Hare)** | most 1st choices, with elimination | Peltola (96–92) |
| **Ranked Robin** | most head-to-head wins | **Begich** |
| **STAR** | highest scores, then a head-to-head runoff | **Begich** |

The two methods that eliminate/count on **first choices** pick Peltola; the two that read the **whole ballot** pick the Condorcet winner, Begich. IRV is the lone method here that fails him — the center-squeeze signature. (Ranked Robin uses the *same ranked ballots* as IRV; only the counting rule differs.)

---

## Challenge your understanding

<details><summary><strong>Q1.</strong> Recompute the final round: after Begich is eliminated, where do his 57 ballots go, and what's the final tally?</summary>

Begich's ballots: 29 go to Palin (`Begich>Palin>…`), 16 go to Peltola (`Begich>Peltola>…`), and 12 exhaust (bullet `Begich` only). Final: Peltola 80+16 = **96**, Palin 63+29 = **92**. Peltola wins 96–92, with 12 ballots exhausted.
</details>

<details><summary><strong>Q2.</strong> From the grid, who is the Condorcet winner, and what are the two margins that prove it?</summary>

**Begich.** He beats **Peltola 93–84** and **Palin 107–68** — a majority in each one-on-one matchup, so he beats *everyone*. That's the definition of a Condorcet winner.
</details>

<details><summary><strong>Q3.</strong> Peltola "won a majority" in the final round. Why is calling her a majority winner misleading?</summary>

Her 96 votes are a majority only of the **188 ballots still active** after 12 exhausted. Against all **200** ballots cast she has **48%**. Ballot exhaustion shrinks the denominator, so IRV's "majority" can be a minority of the actual electorate — a *majoritarian failure*.
</details>

<details><summary><strong>Q4.</strong> Ranked Robin uses the exact same ranked ballots as RCV-IRV, yet elects a different winner. How is that possible?</summary>

Because they *count* the ballots differently. RCV-IRV eliminates on first-choice counts round by round (which cuts Begich in Round 1). Ranked Robin instead tallies every head-to-head matchup and elects whoever wins the most — which is Begich, who wins both. Same ballots, different tabulation, different winner. "RCV" names the ballot; "IRV" and "Ranked Robin" are two ways to count it.
</details>

<details><summary><strong>Q5.</strong> Which of the four methods failed the Condorcet winner, and what's the name for the pattern?</summary>

**Choose-One** and **RCV-IRV** both failed him (both elected Peltola). For IRV specifically, the pattern — a broadly-preferred centrist eliminated early on first-choice counts despite beating everyone head-to-head — is the **center squeeze**.
</details>

**Ready for the hard part?** [301 — the full pathology set, and is this even fair to STAR?](alaska_301.md)
