# The sole-survivor STV crash — a live BetterVoting bug, bisected and diagnosed

**The finding:** BetterVoting's STV tabulator throws a server error on any election whose eliminations leave exactly **one** remaining hopeful who then **reaches quota**. The elect-branch removes the winner from the candidate list and redistributes their surplus over an *empty* list — and `distributeVotes` reduces over that empty array with no initial value, which JavaScript rejects (`TypeError: Reduce of empty array with no initial value`). The results page shows `{"error":"Error (…)"}` with a fresh ID per attempt.

Found by [exercise 14](../../../01_STAR/exercises/ex14_transfer_machine.md) going live (2026-07-17), bisected with permanent public elections as the lab notebook, then confirmed in BetterVoting's open-source tabulator code.

## The evidence table

Seven elections, five of them created for this investigation. Every crash and every success is predicted by one rule: **does the count ever elect the last remaining hopeful at/above quota?**

| Election | Test ID | Shape | Endgame | Result |
|---|---|---|---|---|
| [`ywckmg`](https://bettervoting.com/ywckmg/results) | BV2137 | 1 seat, 3 cand, 100 voters | winner elected with a hopeful standing | ✅ computes |
| [`kcf8vf`](https://bettervoting.com/kcf8vf/results) | BV2134 | 3 seats, 6 cand, 22 voters | hopefuls remain / shortcut fill | ✅ computes |
| [`tk776t`](https://bettervoting.com/tk776t/results) | BV2201 | 2 seats, 4 cand, 9 voters | Camus elected as sole survivor | 💥 error |
| [`bj8dfc`](https://bettervoting.com/bj8dfc/results) | BV2202 | same, fully ranked | identical count | 💥 error |
| [`gvtg2h`](https://bettervoting.com/gvtg2h/results) | BV2203 | same, `enable_write_in` key **omitted** | identical count | 💥 error |
| [`39py93`](https://bettervoting.com/39py93/results) | BV2204 | 2 seats, 4 cand, 13 voters — config identical to BV2201 | both seats fill with two hopefuls **standing** | ✅ computes (Angelou + Cummings) |
| [`8xwx43`](https://bettervoting.com/8xwx43/results) | BV2205 | **1 seat**, 3 cand, 6 voters | Ash elected as sole survivor | 💥 error |

Repo case files: [bv2203_gvtg2h_flag_probe.yaml](cases/bv2203_gvtg2h_flag_probe.yaml) · [bv2204_39py93_control_standing_hopefuls.yaml](cases/bv2204_39py93_control_standing_hopefuls.yaml) · [bv2205_8xwx43_minimal_sole_survivor.yaml](cases/bv2205_8xwx43_minimal_sole_survivor.yaml) — each LH-tabulated (mirrors in `bv_stv_sole_survivor_crash_tabulated/`), so the seats BetterVoting *should* return are on record.

## How the bisection ran

**Step 1 — config diff.** The full race-object diff between the crashing pair (BV2201/2202) and the working STV races came down to a single key: crashers carry `enable_write_in: false`, workers lack the key entirely (they predate the create-script setting it). Election-level settings identical. Suspects: the flag, or the 2-seat/4-candidate/9-voter shape.

**Step 2 — the flag probe (BV2203, `gvtg2h`).** The ex14 ballots byte-for-byte with the key omitted (the create script grew an `enable_write_in: None` → omit option for this). Verified absent in the created race object. **Still crashes** (`cc9625bb`) — flag acquitted, and with it the "some race-config delta" theory: the probe's config now matches the working elections.

**Step 3 — read the code.** With config out, the ballots' *count* had to be the trigger. BetterVoting's tabulator is open source — STV lives in [`IRV.ts`](https://github.com/Equal-Vote/bettervoting/blob/f52f050733f1/packages/backend/src/Tabulators/IRV.ts) (`IRV_STV`, `proportional = true`). Tracing ex14's nine ballots: Austen elected round 1 (surplus → Brontë), Dickens then Brontë eliminated, and in round 4 **Camus is the only candidate left**, holding 5 ≥ quota 4. The elect-branch fires:

```ts
if (proportional) {
    remainingCandidates.shift();                       // list is now EMPTY
    let fractionalSurplus = new Fraction(maxVotes.sub(quota)).div(maxVotes)
    …
    distributeVotes(remainingCandidates, candidateVoteLists, winningCandidateVotes, …)
}
```

and inside `distributeVotes` ([line 180](https://github.com/Equal-Vote/bettervoting/blob/f52f050733f1/packages/backend/src/Tabulators/IRV.ts#L180)):

```ts
let topCandidate = remainingCandidates.reduce((top, c) =>
    mapZero(v.marks[top.id]) < mapZero(v.marks[c.id]) ? top : c)   // [].reduce(f) → TypeError
```

`[].reduce(f)` with no initial value throws — the server's generic error handler turns it into the opaque `Error (…)` ID.

The near-miss branch explains the working elections: a sole survivor **below** quota is elected by the fill-remaining-seats shortcut (`remainingCandidates.length <= nWinners - elected`, [line 136](https://github.com/Equal-Vote/bettervoting/blob/f52f050733f1/packages/backend/src/Tabulators/IRV.ts#L136)), which skips surplus redistribution entirely. Only the **at-quota** sole survivor takes the fatal path.

**Step 4 — confirm from both directions.**

- **Control (BV2204, `39py93`):** config identical to the crasher — STV, 2 seats, 4 candidates, write-ins off — but 13 ballots whose seats both fill by quota while two hopefuls still stand (no candidate is ever eliminated). Prediction: computes. **Computes** — Angelou + Cummings, matching the LH engine. Shape acquitted; endgame convicted.
- **Minimal crasher (BV2205, `8xwx43`):** 1 seat, 3 candidates, 6 fully deterministic ballots (`3×Ash`, `2×Birch>Ash`, `1×Cedar`; quota 4; Cedar out, Birch out, Ash reaches 5 alone). Prediction: errors. **Errors** (`13617b56`) — so the bug needs neither multi-seat, nor truncation, nor any config quirk. Every rankable STV election is exposed; even `nWinners = 1`.

## Why their own tests never caught it

BetterVoting's [`STV.test.ts`](https://github.com/Equal-Vote/bettervoting/blob/f52f050733f1/packages/backend/src/Tabulators/STV.test.ts) has exactly one test — and it is the *same shape* as exercise 14 (9 voters, 2 seats, 4 candidates). Its endgame differs: Bob reaches quota while Carol still stands (her `hareScores` end `[1,1,1]` — never eliminated). The sole-survivor finish has zero coverage. A one-test gap, and the exact test to add is the BV2205 ballot set above.

## Suggested fix (for the issue)

Either guard the redistribution — in the elect-branch, skip `distributeVotes` when `remainingCandidates.length === 0` (the votes are spent; if tracked, count the residue as exhausted) — or make `distributeVotes` total: exhaust every ballot when no candidates remain instead of reducing over an empty array. Adding the BV2205 ballots to `STV.test.ts` pins it.

## Ready-to-file issue

```markdown
Title: STV tabulator crashes when the last remaining candidate reaches quota
       (Reduce of empty array in distributeVotes)

**Symptom.** GET /API/ElectionResult/{id} returns 500 `{"error":"Error (…)"}` for
some STV elections. Live reproductions (permanent, public, ballots castable):

- https://bettervoting.com/tk776t/results  (2 seats, 4 candidates, 9 voters — error IDs a5f1af00 / 3e037088 …)
- https://bettervoting.com/bj8dfc/results  (same, fully-ranked ballots)
- https://bettervoting.com/gvtg2h/results  (same, enable_write_in key omitted — flag ruled out)
- https://bettervoting.com/8xwx43/results  (minimal: 1 seat, 3 candidates, 6 voters)

Control that computes: https://bettervoting.com/39py93/results — config identical
to tk776t (STV / 2 seats / 4 candidates / write-ins off), endgame different.

**Cause.** packages/backend/src/Tabulators/IRV.ts — when eliminations leave exactly
one hopeful and that candidate reaches quota, the proportional elect-branch does
`remainingCandidates.shift()` (list now empty) and then redistributes the surplus:
distributeVotes(remainingCandidates=[], …). Inside distributeVotes (line ~180):

    let topCandidate = remainingCandidates.reduce((top, c) => …)   // no initial value

`[].reduce(f)` throws `TypeError: Reduce of empty array with no initial value`.
A sole survivor BELOW quota is rescued by the fill-remaining-seats branch (line
~136), which skips redistribution — only the at-quota sole survivor crashes.

Minimal repro ballots (8xwx43): 3×(A), 2×(B>A), 1×(C), 1 seat. Quota 4. C out,
B out (both transfer/exhaust), A alone reaches 5 ≥ 4 → crash.

**Fix suggestion.** Skip the surplus redistribution when remainingCandidates is
empty (votes are spent / exhausted), or make distributeVotes exhaust all ballots
when no candidates remain. Test gap: STV.test.ts's single test is this same
9-voter shape but with a benign endgame (Carol never eliminated) — adding the
8xwx43 ballots as a second test pins the fix.
```

## The story, and the moral

Exercise 14 was designed so every STV moving part fires exactly once — quota, surplus, two eliminations, a final quota election. That tidiness is precisely what walks the count into the sole-survivor finish, which real-world STV elections (big fields, standing also-rans) almost never reach. The exercise wasn't unlucky; it was *thorough*, and thoroughness is what found the edge. Methods are math, implementations are software — both need testing. That's the [triple-check habit](../../../00_start_here/tabulation_engines/cross_checking_with_pref_voting.md), doing its job.

*Found from [exercise 14 — the transfer machine](../../../01_STAR/exercises/ex14_transfer_machine.md) · STV method home: [06_Other/STV](../README.md)*

# file: README.md
