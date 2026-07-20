# 3-2-1 Voting

**3-2-1 Voting** (designed by [Jameson Quinn](../../00_start_here/topics/in_memoriam_jameson_quinn.md) of the [Center for Election Science](https://electionscience.org)) is a rated method that reaches a winner in three named steps. Voters rate each candidate **Good**, **OK**, or **Bad**:

1. **Semifinalists** — the **3** candidates with the most *Good* ratings.
2. **Finalists** — of those 3, the **2** with the fewest *Bad* ratings.
3. **Winner** — of those 2, the one rated higher on more ballots (a virtual head-to-head runoff).

The name is the countdown: **3** semifinalists → **2** finalists → **1** winner. It's a *reference* method here for comparison — **not** one of the three [Equal Vote Coalition](https://www.equal.vote) methods ([STAR, Approval, Ranked Robin](../../00_start_here/topics/choosing_among_evc_methods.md)) — kept in `06_Other/` alongside RCV-IRV, Range, and STV.

## The engine (and why it's here)

**No off-the-shelf, cleanly-licensed 3-2-1 tabulator exists.** BetterVoting, the LH `starvote` engine, `pref_voting`, `abcvoting`, and `pyrankvote` all lack it. The only authoritative implementation is Quinn's `V321` class in the Center for Election Science's [`vse-sim`](https://github.com/electionscience/vse-sim) — but that repo carries **no LICENSE** (so it can't be vendored) and is coupled to a Monte-Carlo simulation framework.

3-2-1 is a *published, documented* method, so [`three_two_one_tabulation.py`](three_two_one_tabulation.py) is a **clean-room implementation of the public spec** ([electowiki](https://electowiki.org/wiki/3-2-1_voting)) — and it is **verified to reproduce every one of Quinn's own `V321` doctest vectors**:

```
$ python three_two_one_tabulation.py --selftest
  vector 1: winner=2 expected=2 OK
  vector 2: winner=1 expected=1 OK
  vector 3: winner=1 expected=1 OK
  vector 4: winner=0 expected=0 OK
  vector 5: winner=0 expected=0 OK
3-2-1 engine reproduces Jameson Quinn's V321 doctest vectors ✓
```

So "faithful" here means *matches the published rules **and** the inventor's reference test cases* — not a homegrown guess. (This is LH-only for cross-check: there's no second engine to verify against, which is exactly why the doctest vectors matter.)

### Ballot encoding — and blanks

Good = **2**, OK = **1**, Bad = **0**. A **blank / unmarked** candidate counts as **Bad** — the natural 3-2-1 reading (you didn't rate them, so they aren't Good or OK). This matches the repo's convention that all markers tabulate as 0.

### Known gaps (documented, not faked)

This matches Quinn's `V321.results()`, which runs the plain 3-step. The full electowiki spec adds two guard rules that `V321` itself does **not** apply:

- **Dark-horse rule** — the 3rd semifinalist must have ≥ half the *Good* count of the 1st, else the top two go straight to finalists. Available via `apply_dark_horse=True`, but **off by default** so results match the verified reference.
- **Party-clone rule** — the 3rd semifinalist can't share a party with both others. **Omitted**: our ballots carry no party data, so we document the gap rather than fake it.

## Worked example — Tennessee, blank = Bad

[`321_tennessee_blank_encoding_c4_b100.yaml`](cases/321_tennessee_blank_encoding_c4_b100.yaml): the classic Tennessee-capital electorate (100 voters, four cities) as 3-2-1 ballots, with each faction's *Bad* ratings left **blank**.

```
$ python three_two_one_tabulation.py 321_tennessee_blank_encoding_c4_b100.yaml

--- 3-2-1 Voting ---
Ratings tally (Good / OK / Bad):
   Memphis        Good   42 | OK    0 | Bad   58
   Nashville      Good   26 | OK   74 | Bad    0
   Chattanooga    Good   15 | OK   43 | Bad   42
   Knoxville      Good   17 | OK   41 | Bad   42

Step 1 — Semifinalists (most Good): Memphis (42), Nashville (26), Knoxville (17)
Step 2 — Finalists (fewest Bad): Nashville (Bad 0), Knoxville (Bad 42)
Step 3 — Runoff: Nashville 68 vs Knoxville 17 (15 rated equal)

Winner — 3-2-1 Voting: Nashville
```

The teaching point: **Memphis has the most first-choice support (42) and would win Choose-One**, but 3-2-1's *fewest-Bad* step eliminates it — Memphis is Bad (blank) on **58** ballots. The consensus capital **Nashville**, never rated Bad by anyone, wins. That's the same "centrist consensus" result most non-plurality methods give on this electorate, reached here through the Good→Bad→runoff filter.

## Properties

- **Passes the Relaxed Majority Criterion** (like STAR and IRV; unlike Score/Approval) — see [Majority Criterion](../../00_start_here/topics/majority_criterion/README.md).
- **Strategy-resistant** in Quinn's [Voter Satisfaction Efficiency](https://electionscience.github.io/vse-sim/) simulations — it's one of the methods where honesty is the practical best play (see [strategic voting](../../00_start_here/topics/strategic_voting.md)).
- A **rated** method with a small 3-level scale, and a runoff-style final step (a distant cousin of STAR's score-then-runoff).

**See also:** [Choosing among the Equal Vote methods](../../00_start_here/topics/choosing_among_evc_methods.md) · [Strategic voting](../../00_start_here/topics/strategic_voting.md) · [electowiki: 3-2-1 voting](https://electowiki.org/wiki/3-2-1_voting) · [Jameson Quinn — Make All Votes Count](https://medium.com/@jameson.quinn/make-all-votes-count-part-2-single-winner-5a2fb47123d5)
