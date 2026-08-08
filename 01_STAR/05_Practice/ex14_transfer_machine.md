# Exercise 14 — The transfer machine

*A nine-member book club buys **two** novels, by ranked ballot under **STV** — the proportional cousin of RCV-IRV. Five members adore Austen; one champions Brontë; three want Camus. Your job is to be the counting machine: compute the quota, elect, transfer the surplus, eliminate, transfer again — and follow one single ballot through the whole journey to see where its vote finally lands.*

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/tk776t) (election `tk776t`, Test ID BV2201) — **but don't expect numbers there: this election found a live BV bug — now diagnosed.** BetterVoting's STV tabulator crashes on any count that ends with a *sole remaining hopeful* reaching quota (this one does), while its other STV races compute fine — see [A live bug, found — and diagnosed](#a-live-bug-found-and-diagnosed) below. The seats on this page are the LH engine's.

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
- **(f)** Now count it again with the **exact** Droop quota, 9 ÷ 3 = 3.00 — the one the engine applies. Redo the surplus, the transfer weight, and the eliminations. What changes? What doesn't?

## Solutions

<details>
<summary><b>(a) Hand-count Droop quota = 4</b></summary>

Droop = ⌊9 ÷ (2+1)⌋ + 1 = **4**. The logic: at most *two* candidates can each hold 4 votes out of 9 (4+4=8 ≤ 9, but 4+4+4 > 9) — so reaching 4 makes a seat mathematically safe, and no third rival can match both winners. "Half" is the single-winner special case of the same formula: ⌊V/2⌋+1.

**One thing to know before you count.** "The Droop quota" names *two* published formulas, one vote apart, and this exercise walks the hand-count one. The theory literature (Woodall) and most software — including the engine behind this page — use the **exact** form with no rounding, 9 ÷ 3 = **3.00**. Both are standard; they seat the same two novels here; they move different numbers to get there. Work parts (b)–(e) with **4**, then read [(f)](#f) for the same count at 3.00. The engine's header prints both so a hand-checker is never stranded:

```text title="Abridged for the lesson — the header only"
 2 seats; quota = 3.00 (exact Droop, votes/(seats+1)) — 33.3% of 9.
 Elected at >= quota, and every surplus is measured from it.
 (Hand-count Droop, floor(9/3)+1 = 4, is a different but equally standard rule.)
```

</details>

<details>
<summary><b>(b) Round 1 — Austen elected; her surplus of 1 rides to Brontë</b></summary>

First choices — and this table is the same whichever quota you use, because nothing has moved yet:

```text title="Abridged for the lesson — round 1 only"
ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Austen             5  Elected
Camus              3  Hopeful
Bronte             1  Hopeful
Dickens            0  Hopeful
```

Austen holds 5 ≥ 4: **elected**, with a surplus of 5 − 4 = **1**. Fractional (Gregory) transfer: all five Austen ballots move to their next choice at weight 1/5 each — five ballots × 0.2 = **1.0 vote to Brontë**. Standing after round 1: Brontë 1 + 1 = **2**, Camus **3**, Dickens **0**.

The surplus is where the two quotas part company, and it is worth seeing why the arithmetic is forced. A winner keeps *exactly a quota* and passes on the rest, so the quota you chose in (a) sets both numbers: keep 4, pass 1, transfer at 0.2 per ballot. Take the exact quota instead and Austen keeps 3, passes **2**, and each ballot moves at 0.4 — [part (f)](#f) runs that count to the end. Neither is a rounding slip; they are two rulebooks.

</details>

<details>
<summary><b>(c) The eliminations — the surplus keeps moving until it lands on Camus</b></summary>

No hopeful holds 4, so the machine eliminates from the bottom. **Dickens (0)** goes first — nothing to transfer (no ballot ranks him top). Then **Brontë (2)**: her pile transfers to each ballot's next standing choice — her own full ballot (Brontë > Camus) goes to **Camus**, and the five one-fifth fractions from Austen's surplus *continue down their rankings* to **Camus** too. Camus: 3 + 1 + 1 = **5 ≥ 4 — elected. Seats: Austen and Camus.**

That is the drill, and it is a correct STV count. It is *not* the count the engine ran: under the exact quota, Brontë reaches 3.00 on the bigger surplus and the second seat fills without a single elimination — see [(f)](#f). Both roads end at Austen and Camus.

</details>

<details>
<summary><b>(d) One ballot's journey</b></summary>

Take any one of the five `Austen > Brontë > Camus > Dickens` ballots. **4/5 of it** was spent electing Austen (five ballots jointly paying the quota of 4). The remaining **1/5** transferred to Brontë; when Brontë was eliminated, that same fifth continued to **Camus** — and became part of the vote that elected him. Final ledger for this single ballot: 0.8 votes → Austen (seated), 0.2 votes → Camus (seated), 0.0 wasted. That is the "transferable" in Single Transferable Vote: a ballot is a *ranked to-do list with a budget*, spent top-down until it's used up — the honest version of the no-wasted-vote slogan. (The dishonest version ignores that rankings can run out mid-journey: a truncated ballot's remainder simply [exhausts](../../06_Other/RCV_IRV/concepts/RCV_IRV_exhausted_ballots.md) — here every transfer found a next name, but that's a property of these ballots, not of STV.)

**The tidy ledger is the hand count's, and it is worth knowing that the exact-quota count is less tidy.** There the ballot pays 0.6 to Austen and sends 0.4 to Brontë — who is never eliminated, because the seats fill first. That 0.4 comes to rest on a candidate who does not win. Nothing was stolen from the voter: Camus already had the second seat sewn up, so the transfer would have changed nothing. But "0.0 wasted" is a claim about *this* rulebook and this electorate, not a theorem about STV, and [(f)](#f) is the reason to say so out loud.

</details>

<details>
<summary><b>(e) The proportionality check</b></summary>

With quota 4, the 5-voter Austen bloc funds exactly one seat (and its leftover 1 vote correctly *failed* to buy Brontë a second); the 3-voter Camus camp — just under quota on its own — reaches a seat with the transferred remainders. One seat per ~4 voters: **proportional to the room**, as designed. A Bloc-style count on these preferences would hand the Austen majority *both* seats ([exercise 12](ex12_bloc_vs_proportional.md)'s sweep, in ranked clothing). STV is the ranked-ballot route to the same proportional philosophy as Allocated Score — the side-by-side is worked in [STV vs STAR-PR](../../method_comparisons/stv_vs_star_pr/README.md), and the family map lives at [electing more than one](../../07_Concepts/topics/electing_more_than_one.md).

The verdict survives the quota switch, and gets cleaner: at 3.00 the Camus camp's three voters are *exactly* one quota, so they buy their seat outright rather than on remainders. Five voters is 1.67 quotas — one seat, with change that cannot fund a second. Proportional under either rulebook.

</details>

## (f) The same nine ballots at the exact quota {#f}

*Not a spoiler — the reconciliation. Work (a)–(e) first, then read this.*

Set the quota to 9 ÷ 3 = **3.00** and run it again. Round 1 is unchanged (nothing has moved yet), but everything after it is different: Austen keeps 3 instead of 4, so her surplus is **2**, and the five ballots move at **0.4** each. Brontë lands on 1 + 2 = **3.00** — level with Camus. One seat is left and the two are tied; Brontë and Dickens are set aside as unable to catch Camus, and Camus takes the last seat as the only hopeful still standing. **No candidate is ever eliminated, and no elimination transfer ever runs.**

| | hand-count quota **4** | exact quota **3.00** |
|---|---|---|
| Austen keeps / passes on | 4 / **1** | 3 / **2** |
| transfer weight per Austen ballot | 0.2 | **0.4** |
| Brontë after the surplus | 2 | **3.00** — tied with Camus |
| eliminations | Dickens, then Brontë | **none** |
| how the second seat fills | Camus climbs to 5 ≥ 4 | Camus is the last hopeful for the last seat |
| one Austen ballot's ledger | 0.8 Austen + 0.2 Camus | 0.6 Austen + **0.4 Brontë** (unseated) |
| **seats** | **Austen + Camus** | **Austen + Camus** |

Read the last row first, then the rest. Two published, in-use definitions of "the Droop quota" disagree about nearly every number in the count and agree about the only thing being decided. That is the honest shape of [fork 1](../../06_Other/STV/README.md#where-it-genuinely-gets-complicated): the quota choice is real, it can decide a seat in principle, and it decides nothing in any of the ten STV elections in this library — each one was re-counted under both quotas to check. It is also why the engine's header stopped naming one quota and applying another.

Watch the Brontë row, though. She is *rejected* holding the same 3.00 that seats Camus, which looks wrong until you see that only one seat remained and they finished level. A tie for the last seat is the one place where the rulebook, not the electorate, picks the winner — here `pyrankvote` breaks it deterministically on second choices. Real STV codes write that rung down in law, and this is a good election to notice that they have to.

## A live bug, found — and diagnosed

Making this exercise live turned it into a bug report. BetterVoting accepted the election and all nine ballots (`tk776t`, BV2201) — but its STV tabulator returns a server error when computing results (`{"error":"Error (a5f1af00)"}`-style, fresh ID per attempt). The bisection ran to ground the same day, with permanent public elections as the lab notebook — the full write-up, evidence table, and ready-to-file issue live at **[the sole-survivor STV crash](../../06_Other/STV/bv_stv_sole_survivor_crash/README.md)**. The short version:

- **Truncation acquitted.** A fully-ranked twin — same nine voters, trailing rankings no transfer ever reaches — fails identically (`bj8dfc`, BV2202; repo home [ex14_two_novels_fullranks.yaml](cases/ex14_two_novels_fullranks.yaml), LH-verified to the same seats).
- **The `enable_write_in` flag acquitted.** A probe with the key omitted from the race object — the one config difference from BV's older, working STV races — crashes identically (`gvtg2h`, BV2203).
- **The shape acquitted, the endgame convicted.** A control with *identical config* (STV, 2 seats, 4 candidates) whose seats fill while two hopefuls still stand **computes fine** (`39py93`, BV2204) — and a minimal 1-seat, 6-voter election whose eliminations leave one candidate standing **crashes** (`8xwx43`, BV2205).
- **Root cause, in BV's own source.** This exercise's count ends with Camus reaching quota as the *sole remaining hopeful*. BetterVoting's `IRV.ts` elect-branch then redistributes his surplus over an **empty** candidate list, and `distributeVotes` runs `remainingCandidates.reduce(…)` with no initial value — `[].reduce(f)` throws `TypeError`. A sole survivor *below* quota is rescued by the fill-remaining-seats shortcut; only the at-quota sole survivor crashes. (Their own `STV.test.ts` is this same 9-voter shape with a benign endgame — the gap in one test.)

One more symptom for the report: the BV UI *export* of both elections silently omits the `Results` section entirely (Election + Ballots only) — the frozen exports beside these YAMLs archive the ballots and await a re-export once the tabulator is fixed. Until BV fixes it, the seats come from the LH engine (or any STV engine you point at these nine ballots), and the live elections stand as the reproduction set. It is also this set's best accidental lesson: *methods* are math, *implementations* are software — both need testing, which is what this repo's triple-check habit is for. The tidy design — every STV moving part firing exactly once — is precisely what walked the count into an endgame that big real-world fields almost never reach. The exercise wasn't unlucky; it was thorough.

## Reading this fairly

A tidy electorate: full rankings (nothing exhausts), one surplus, one meaningful elimination — chosen so every moving part fires exactly once. Real STV counts inherit RCV-IRV's operational caveats ([central tabulation](../../07_Concepts/GLOSSARY.md), exhaustion under rank limits) alongside the genuine proportionality shown here; the balanced comparison with the score-ballot PR family is [STV vs STAR-PR](../../method_comparisons/stv_vs_star_pr/README.md).

## Run it yourself

```
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/05_Practice/cases/ex14_two_novels.yaml
```

Every fence on this page is abridged for the lesson. Want the whole count — the header, both rounds and the Smith set? See the full LH report → [ex14_two_novels.md](cases/cases_pages/ex14_two_novels.md). Source: [ex14_two_novels.yaml](cases/ex14_two_novels.yaml); raw [mirror](cases/cases_tabulated/ex14_two_novels_tabulated.txt).

---

**Where this comes from.** Original to this repo (ballots and cast — novelists as candidates, so the ranked ballot reads like a bookshelf). Concept homes: [STV](../../06_Other/STV/README.md), [STV vs STAR-PR](../../method_comparisons/stv_vs_star_pr/README.md).

*Back to [the exercises set](README.md) · curriculum home: [Voting 301](../../07_Concepts/curriculum/CURRICULUM_301.md)*

# file: ex14_transfer_machine.md
