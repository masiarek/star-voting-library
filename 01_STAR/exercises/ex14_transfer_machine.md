# Exercise 14 — The transfer machine

*A nine-member book club buys **two** novels, by ranked ballot under **STV** — the proportional cousin of RCV-IRV. Five members adore Austen; one champions Brontë; three want Camus. Your job is to be the counting machine: compute the quota, elect, transfer the surplus, eliminate, transfer again — and follow one single ballot through the whole journey to see where its vote finally lands.*

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/tk776t) (election `tk776t`, Test ID BV2201) — **but don't expect numbers there: this election found a live BV bug — now diagnosed.** BetterVoting's STV tabulator crashes on any count that ends with a *sole remaining hopeful* reaching quota (this one does), while its other STV races compute fine — see [A live bug, found — and diagnosed](#a-live-bug-found--and-diagnosed) below. The seats on this page are the LH engine's.

**You practice:** STV's two moving parts — the **Droop quota** and the **transfer** (surplus and elimination) — the mechanics behind every "no vote is wasted" claim, done by hand at whiteboard scale. (Method home: [STV](../../06_Other/STV/README.md); the score-ballot counterpart is [exercise 12](ex12_bloc_vs_proportional.md).)

Work each part on paper before opening its solution. The YAML is runnable; the `_tabulated` mirror is the full report.

## The ballots

Nine ranked ballots, four novelists, two seats:

| count | ranking |
|:---:|---|
| ×5 | Austen > Brontë > Camus > Dickens |
| ×1 | Brontë > Camus |
| ×3 | Camus > Dickens |

## Your task

- **(a)** Compute the **Droop quota** for 9 voters and 2 seats. Why that formula and not "half"?
- **(b)** **Round 1:** count first choices. Who is elected, what is the surplus, and — transferring fractionally — what does each standing candidate now hold?
- **(c)** Nobody else reaches quota. Run the **eliminations** until the second seat fills. Narrate where every transferred vote goes.
- **(d)** Follow ONE of the five Austen ballots from the moment it was cast to the final result. How much of it elected Austen? Where did the rest end up?
- **(e)** The Austen bloc is 5 of 9 voters and got 1 of 2 seats; the Camus camp is 3 of 9 and got the other. Is that proportional? Check against the quota — and name what *would* have happened under a Bloc-style count.

## Solutions

<details>
<summary><b>(a) Droop quota = 4</b></summary>

Droop = ⌊9 ÷ (2+1)⌋ + 1 = **4**. The logic: at most *two* candidates can each hold 4 votes out of 9 (4+4=8 ≤ 9, but 4+4+4 > 9) — so reaching 4 makes a seat mathematically safe, and no third rival can match both winners. "Half" is the single-winner special case of the same formula: ⌊V/2⌋+1.

</details>

<details>
<summary><b>(b) Round 1 — Austen elected; her surplus of 1 rides to Brontë</b></summary>

```text
 2 seats; Droop quota = 4 (44.4% of 9).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Austen             5  Elected
Camus              3  Hopeful
Bronte             1  Hopeful
Dickens            0  Hopeful
```

Austen holds 5 ≥ 4: **elected**, with a surplus of 5 − 4 = 1. Fractional (Gregory) transfer: all five Austen ballots move to their next choice at weight 1/5 each — five ballots × 0.2 = **1.0 vote to Brontë**. Standing after round 1: Brontë 1 + 1 = **2**, Camus **3**, Dickens **0**.

</details>

<details>
<summary><b>(c) The eliminations — the surplus keeps moving until it lands on Camus</b></summary>

No hopeful holds 4, so the machine eliminates from the bottom. **Dickens (0)** goes first — nothing to transfer (no ballot ranks him top). Then **Brontë (2)**: her pile transfers to each ballot's next standing choice — her own full ballot (Brontë > Camus) goes to **Camus**, and the five one-fifth fractions from Austen's surplus *continue down their rankings* to **Camus** too. Camus: 3 + 1 + 1 = **5 ≥ 4 — elected. Seats: Austen and Camus.** (The engine's vendored STV report prints the first round and the final table — seats confirmed; the intermediate arithmetic above is standard fractional STV, which is exactly the drill.)

</details>

<details>
<summary><b>(d) One ballot's journey</b></summary>

Take any one of the five `Austen > Brontë > Camus > Dickens` ballots. **4/5 of it** was spent electing Austen (five ballots jointly paying the quota of 4). The remaining **1/5** transferred to Brontë; when Brontë was eliminated, that same fifth continued to **Camus** — and became part of the vote that elected him. Final ledger for this single ballot: 0.8 votes → Austen (seated), 0.2 votes → Camus (seated), 0.0 wasted. That is the "transferable" in Single Transferable Vote: a ballot is a *ranked to-do list with a budget*, spent top-down until it's used up — the honest version of the no-wasted-vote slogan. (The dishonest version ignores that rankings can run out mid-journey: a truncated ballot's remainder simply [exhausts](../../00_start_here/RCV_IRV/RCV_IRV_exhausted_ballots.md) — here every transfer found a next name, but that's a property of these ballots, not of STV.)

</details>

<details>
<summary><b>(e) The proportionality check</b></summary>

With quota 4, the 5-voter Austen bloc funds exactly one seat (and its leftover 1 vote correctly *failed* to buy Brontë a second); the 3-voter Camus camp — just under quota on its own — reaches a seat with the transferred remainders. One seat per ~4 voters: **proportional to the room**, as designed. A Bloc-style count on these preferences would hand the Austen majority *both* seats ([exercise 12](ex12_bloc_vs_proportional.md)'s sweep, in ranked clothing). STV is the ranked-ballot route to the same proportional philosophy as Allocated Score — the side-by-side is worked in [STV vs STAR-PR](../../00_start_here/proportional_representation/stv/proportional_stv_vs_star.md), and the family map lives at [electing more than one](../../00_start_here/topics/electing_more_than_one.md).

</details>

## A live bug, found — and diagnosed

Making this exercise live turned it into a bug report. BetterVoting accepted the election and all nine ballots (`tk776t`, BV2201) — but its STV tabulator returns a server error when computing results (`{"error":"Error (a5f1af00)"}`-style, fresh ID per attempt). The bisection ran to ground the same day, with permanent public elections as the lab notebook — the full write-up, evidence table, and ready-to-file issue live at **[the sole-survivor STV crash](../../06_Other/STV/bv_stv_sole_survivor_crash/README.md)**. The short version:

- **Truncation acquitted.** A fully-ranked twin — same nine voters, trailing rankings no transfer ever reaches — fails identically (`bj8dfc`, BV2202; repo home [ex14_two_novels_fullranks.yaml](ex14_two_novels_fullranks.yaml), LH-verified to the same seats).
- **The `enable_write_in` flag acquitted.** A probe with the key omitted from the race object — the one config difference from BV's older, working STV races — crashes identically (`gvtg2h`, BV2203).
- **The shape acquitted, the endgame convicted.** A control with *identical config* (STV, 2 seats, 4 candidates) whose seats fill while two hopefuls still stand **computes fine** (`39py93`, BV2204) — and a minimal 1-seat, 6-voter election whose eliminations leave one candidate standing **crashes** (`8xwx43`, BV2205).
- **Root cause, in BV's own source.** This exercise's count ends with Camus reaching quota as the *sole remaining hopeful*. BetterVoting's `IRV.ts` elect-branch then redistributes his surplus over an **empty** candidate list, and `distributeVotes` runs `remainingCandidates.reduce(…)` with no initial value — `[].reduce(f)` throws `TypeError`. A sole survivor *below* quota is rescued by the fill-remaining-seats shortcut; only the at-quota sole survivor crashes. (Their own `STV.test.ts` is this same 9-voter shape with a benign endgame — the gap in one test.)

One more symptom for the report: the BV UI *export* of both elections silently omits the `Results` section entirely (Election + Ballots only) — the frozen exports beside these YAMLs archive the ballots and await a re-export once the tabulator is fixed. Until BV fixes it, the seats come from the LH engine (or any STV engine you point at these nine ballots), and the live elections stand as the reproduction set. It is also this set's best accidental lesson: *methods* are math, *implementations* are software — both need testing, which is what this repo's triple-check habit is for. The tidy design — every STV moving part firing exactly once — is precisely what walked the count into an endgame that big real-world fields almost never reach. The exercise wasn't unlucky; it was thorough.

## Reading this fairly

A tidy electorate: full rankings (nothing exhausts), one surplus, one meaningful elimination — chosen so every moving part fires exactly once. Real STV counts inherit RCV-IRV's operational caveats ([central tabulation](../../00_start_here/GLOSSARY.md), exhaustion under rank limits) alongside the genuine proportionality shown here; the balanced comparison with the score-ballot PR family is [STV vs STAR-PR](../../00_start_here/proportional_representation/stv/proportional_stv_vs_star.md).

## Run it yourself

```
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/ex14_two_novels.yaml
```

Source: [ex14_two_novels.yaml](ex14_two_novels.yaml). Full report: [mirror](exercises_tabulated/ex14_two_novels_tabulated.txt).

---

**Where this comes from.** Original to this repo (ballots and cast — novelists as candidates, so the ranked ballot reads like a bookshelf). Concept homes: [STV](../../06_Other/STV/README.md), [STV vs STAR-PR](../../00_start_here/proportional_representation/stv/proportional_stv_vs_star.md).

*Back to [the exercises set](README.md) · curriculum home: [Voting 301](../../00_start_here/curriculum/CURRICULUM_301.md)*

# file: ex14_transfer_machine.md
