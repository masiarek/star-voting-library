# Cross-checking Proportional STAR against BetterVoting's own fixtures

*The strongest kind of agreement: BetterVoting's unit tests for Allocated Score, cast as real BetterVoting elections, and re-counted by an engine nobody at Equal Vote wrote.*

**Level: 301 · deep dive**

→ the method: [STAR-PR](../../01_Learn/STAR_PR/README.md) · the case this resolved: [BV2130](../../02_Examples/bv2130_presidential_board_star_pr.md) · the paradox these clean counts made findable: [Alabama](../alabama_paradox/README.md)

---

## Why this exists

For a long time the library had exactly one BetterVoting-backed Proportional STAR case — [BV2130](../../02_Examples/bv2130_presidential_board_star_pr.md), a 51-candidate, 102-ballot presidential board — and **it disagreed with our engine** on the last of seven seats. That is a bad place to be: with one contaminated data point you cannot tell whether the two implementations of Allocated Score differ, or whether something else does.

These two elections settle it. They are **BetterVoting's own test fixtures** for the method, taken from [`packages/backend/src/Tabulators/AllocatedScore.test.ts`](https://github.com/Equal-Vote/bettervoting/blob/main/packages/backend/src/Tabulators/AllocatedScore.test.ts), cast as live public elections, and counted independently by Larry Hastings' `starvote`.

| Case | BV election | Seats | BetterVoting elects | LH `allocated` elects | |
|---|---|--:|---|---|:--:|
| **Fractional surplus** | [`kk2gxj` ↗](https://bettervoting.com/kk2gxj/results) | 2 | Allison, Doug | Allison, Doug | ✅ |
| **Fewer voters than seats** | [`hk27tk` ↗](https://bettervoting.com/hk27tk/results) | 3 | Allison, Bill, Carmen | Allison, Bill, Carmen | ✅ |

Both exports report **`nAbstentions: 0`** — every ballot counted, by both engines, on both sides. That matters, and the next section says why.

## What this proved about BV2130

BV2130's seat-7 disagreement had two standing hypotheses: an implementation difference in Allocated Score, or a near-tie broken at random. **These fixtures killed the first one.** If the two implementations of the method disagreed, they would disagree here — on the method author's own tests. They don't.

That left the input, and the input was the answer: BetterVoting's export for BV2130 reports `nTallyVotes: 100` against the ballot set's **102**. Two ballots were discarded as abstentions ([#1478](https://github.com/Equal-Vote/bettervoting/issues/1478)), the Hare quota is `voters ÷ seats`, so a different ballot count means a different quota — 14.2857 against 14.5714 — applied in *every* round. The error compounds across six seats and flips the seventh.

**So the engines agree; they were handed different elections.** These two clean cases are what made that provable rather than suspected.

## The fixtures, and what each is for

### Fractional surplus (`kk2gxj`, 2 seats, 12 ballots)

Allison has **eight** top-level supporters, but with 12 voters and 2 seats a seat costs **six**. The whole quota therefore comes from inside her 5-star group, and no rule about which of eight identical ballots to spend would be defensible — so none is applied. Each of the eight keeps `1 − 6/8 = 0.25` of its weight.

That is [fractional surplus handling](../../01_Learn/STAR_PR/README.md), and this fixture is the reason it exists: **voters who scored a winner identically are spent identically.** Without it, four of those eight ballots would be fully consumed and four fully preserved, decided by nothing but list order.

<!-- report:bkk2gxj_fractional_surplus -->
```text
--- Allocated Score Voting Method (2 winners) ---

[Allocated Score Voting]
 Tabulating 12 ballots to fill 2 seats.
Count × Allison,Bill,Carmen,Doug
    7 ×       5,   5,     1,   0
    3 ×       0,   0,     4,   5
    1 ×       5,   4,     4,   0
    1 ×       0,   0,     0,   3

[Allocated Score Voting: Round 1]
 The highest-scoring candidate wins a seat.
   Allison       -- 40 -- First place
   Bill          -- 39
   Carmen        -- 23
   Doug          -- 18
 Allison wins a seat.

[Allocated Score Voting: Round 1: Ballot allocation round]
 Allocating 6 ballots.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 1]
 Allocating 8 ballots at score 5.
 This allocation overfills the quota.  Returning fractional surplus.
 Allocating only 75.00% of these ballots.
 Keeping these ballots, but multiplying their weights by 1/4.
 8 ballots reweighted from 1 to 1/4.

[Allocated Score Voting: Round 2]
 The highest-scoring candidate wins a seat.
   Doug          -- 18     -- First place
   Carmen        -- 14+3/4
   Bill          --  9+3/4
 Doug wins a seat.

[Allocated Score Voting: Winners — Allocated Score Voting Method (2 winners)]
 Allison
 Doug
```
<!-- /report -->

### Fewer voters than seats (`hk27tk`, 3 seats, 2 ballots)

Two voters, three seats. A degenerate election, and deliberately so: it exists to prove the tabulator does something sane when the quota (`2 ÷ 3 ≈ 0.67`) is smaller than a single ballot, rather than dividing by zero, looping, or seating nobody. Both engines fill all three seats.

Worth knowing that Allocated Score refuses `seats = 1` outright — the method is defined for multi-winner races — so the degenerate end of its range is tested here rather than assumed.

<!-- report:bhk27tk_fewer_voters_than_seats -->
```text
--- Allocated Score Voting Method (3 winners) ---

[Allocated Score Voting]
 Tabulating 2 ballots to fill 3 seats.
Allison,Bill,Carmen,Doug
      5,   5,     0,   0
      5,   4,     3,   0

[Allocated Score Voting: Round 1]
 The highest-scoring candidate wins a seat.
   Allison       -- 10 -- First place
   Bill          --  9
   Carmen        --  3
   Doug          --  0
 Allison wins a seat.

[Allocated Score Voting: Round 1: Ballot allocation round]
 Allocating 2/3 ballots.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 1]
 Allocating 2 ballots at score 5.
 This allocation overfills the quota.  Returning fractional surplus.
 Allocating only 33.33% of these ballots.
 Keeping these ballots, but multiplying their weights by 2/3.
 2 ballots reweighted from 1 to 2/3.

[Allocated Score Voting: Round 2]
 The highest-scoring candidate wins a seat.
   Bill          -- 6 -- First place
   Carmen        -- 2
   Doug          -- 0
 Bill wins a seat.

[Allocated Score Voting: Round 2: Ballot allocation round]
 Allocating 2/3 ballots.

[Allocated Score Voting: Round 2: Ballot allocation round: Round 1]
 Allocating 1 ballot at score 10/3.
 These ballots carry a remaining weight of 2/3.

[Allocated Score Voting: Round 3]
 Tabulating 1 remaining ballots.
Allison,Bill,Carmen,Doug
      5,   5,     0,   0
      5,   4,     3,   0

[Allocated Score Voting: Winners — Allocated Score Voting Method (3 winners)]
 Allison
 Bill
 Carmen
```
<!-- /report -->

## Why "their tests, our engine" is worth more than agreement on our own cases

A method's own test suite encodes what its authors *meant*, including the edge cases they thought to guard. Reproducing it in an independent implementation is a stronger claim than agreeing on cases we designed ourselves — we cannot accidentally test only the behaviours we happened to implement.

It also cuts the other way, and should be said: these fixtures are BetterVoting's, so they test what BetterVoting thought to test. Agreement here does **not** mean the two engines agree everywhere — only that they agree on the method's specified behaviour, including its documented edge cases. Where they might still part company is exactly what the [Alabama paradox](../alabama_paradox/README.md) work explores.

## Run them yourself

```bash
.venv/bin/python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 03_STAR_PR/03_Criteria/bv_fixture_crosscheck/cases/bkk2gxj_fractional_surplus.yaml
```

| Case | Seats | Files |
|---|--:|---|
| Fractional surplus | 2 | [page](cases/cases_pages/bkk2gxj_fractional_surplus.md) · [yaml](cases/bkk2gxj_fractional_surplus.yaml) · [frozen BV export](cases/bkk2gxj_fractional_surplus_bv_export.json) |
| Fewer voters than seats | 3 | [page](cases/cases_pages/bhk27tk_fewer_voters_than_seats.md) · [yaml](cases/bhk27tk_fewer_voters_than_seats.yaml) · [frozen BV export](cases/bhk27tk_fewer_voters_than_seats_bv_export.json) |

## See also

- [BV2130 — the case this resolved](../../02_Examples/bv2130_presidential_board_star_pr.md)
- [The Alabama paradox in Proportional STAR](../alabama_paradox/README.md) — where the engines' *shared* behaviour turns out to be the surprising part
- [STAR-PR — the three methods](../../01_Learn/STAR_PR/README.md) — quota vs divisor, and what each buys
- [#1478](https://github.com/Equal-Vote/bettervoting/issues/1478) — the discarded-ballot defect that made BV2130 diverge
