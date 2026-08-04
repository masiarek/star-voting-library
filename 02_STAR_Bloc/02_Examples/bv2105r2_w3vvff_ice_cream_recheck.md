# BV2105-r2 — the partial ballot, re-counted a year later

<!-- case-meta:start — managed by build_yaml_pages.py; edit the YAML, not these lines -->
**Method:** [Bloc STAR (multi-winner, majoritarian)](../../03_STAR_PR/01_Learn) · **2 seats** · **Expected winners:** Chocolate, Strawberry · [full count →](cases/cases_pages/bv2105r2_w3vvff_ice_cream_recheck.md)
<!-- case-meta:end -->

*A deliberate re-run of [BV2105](bv2105_r4dqvd_ice_cream_bloc.md) (`r4dqvd`) on **exactly the same four ballots**, cast again on 2026-08-04 so they are counted by **today's** tabulator. The question it settles: a year on, does BetterVoting still file a real partial ballot as an abstention? **It does.** The fresh election returns `nTallyVotes 2 / nAbstentions 2`, identical to 2025.*

> **What this case is NOT about.** The library used to attribute this miscount to [bettervoting#1056](https://github.com/Equal-Vote/bettervoting/issues/1056). That was a mis-citation, corrected 2026-08-04. **#1056 is a different defect on the same demo election** — a `401` blocking JSON/CSV download and Race Details, introduced by the Editable Ballots work ([#979](https://github.com/Equal-Vote/bettervoting/issues/979)) and correctly closed via [#1058](https://github.com/Equal-Vote/bettervoting/issues/1058). They share only the BV2105 test-document name. The counting defect on this page is a separate bug, filed 2026-08-04 as **[#1478](https://github.com/Equal-Vote/bettervoting/issues/1478)** on the strength of this election ([report archive](bv2105r2_bv_github_issue.md)).

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/w3vvff) · **[results ↗](https://bettervoting.com/w3vvff/results)** (election `w3vvff`).

Reference file: [`bv2105r2_w3vvff_ice_cream_recheck.yaml`](cases/bv2105r2_w3vvff_ice_cream_recheck.yaml). Frozen export: [`bv2105r2_w3vvff_ice_cream_recheck_bv_export.json`](cases/bv2105r2_w3vvff_ice_cream_recheck_bv_export.json).

## Why a second election was needed

The obvious move is to re-fetch `r4dqvd` and read its numbers. That doesn't work, and the reason is worth stating because it applies to every closed BV election in this library:

**`r4dqvd` is `closed`.** Re-fetching it today does return `nTallyVotes 2 / nAbstentions 2` — but a closed election's stored `ElectionResult` may simply be the tally computed back in 2025. The re-fetch cannot distinguish *"the bug is still live"* from *"we are reading a year-old result."* Only ballots cast **through today's tabulator** can.

**No other case in the library answers it either.** The discriminating ballot is one whose non-blank marks are **all equal** — here a single `1` — because that is exactly what [#884](https://github.com/Equal-Vote/bettervoting/issues/884)'s all-equal rule treats as an abstention. Sweeping every frozen export in the repo turns up only one other 2026-minted election with a partial ballot, [BV215](../../01_STAR/03_Criteria/none_of_the_above/bv215_26khr3_nota_wins.md) (`26khr3`), and its partial is `Ada 5, Bruno 1, blank` — **two distinct marks**, so it is counted either way and settles nothing.

Hence a fresh mint, same ballots.

## The election

Bloc STAR, 3 flavors, **2 seats**, 4 ballots — one of each *kind* of ballot:

```
Vanilla,Chocolate,Strawberry
5,5,5     an all-5s ballot (loves everything)
-,-,-     fully blank — a TRUE abstention
1,-,-     Vanilla=1, the rest blank — a REAL (partial) vote   ← the probe
2,5,4     a full ballot
```

Winners **Chocolate, Strawberry**, and they were never in question — Chocolate takes seat 1, seat 2 is a Vanilla/Strawberry runoff tie broken by score (Strawberry 9 > Vanilla 8). The winner path is not what this election measures. **The count is.**

## The result: still broken

| Quantity | BV2105 (`r4dqvd`, 2025) | **BV2105-r2 (`w3vvff`, today)** | LH engine |
|---|:--:|:--:|:--:|
| Winners | Chocolate, Strawberry | Chocolate, Strawberry | Chocolate, Strawberry ✓ |
| `nTallyVotes` | 2 | **2** | **3** ✗ |
| `nAbstentions` | 2 | **2** | **1** ✗ |
| Vanilla `score` | 3 | **3** | total **8**, avg **2.7** ✗ |

The two BetterVoting columns are identical. The `1,-,-` ballot is still filed as an abstention alongside the genuinely blank one, and Vanilla's reported figure is still an average over **2** ballots rather than 3 — the single `1` never enters the sum. (BV floors the average for display: Strawberry's 9/2 shows as `4`, Vanilla's 7/2 as `3`.)

### Is this a bug, or the documented policy?

Worth stating fairly, because it cuts against the simple reading. [#884](https://github.com/Equal-Vote/bettervoting/issues/884) established that a ballot whose marks are **all equal** counts as an abstention. A ballot bearing a *single* mark is **trivially** all-equal, so it falls through the same test — meaning this may be the policy working exactly as written, not a coding slip.

The argument that it is nonetheless wrong: **BetterVoting's own tally treats a blank as 0.** So `Vanilla 1, blank, blank` is not a ballot with one mark and two unknowns — it is a ballot reading Vanilla 1, Chocolate 0, Strawberry 0, which strictly prefers Vanilla to both. Under the all-equal rule *as applied to the scores it actually counts*, that ballot is not all-equal at all, and it plainly expresses a preference. Note the scope: this concerns partial ballots whose non-blank marks are all equal. Partial ballots with two or more distinct marks count correctly.

## The LH report (the correct count)

<!-- report:bv2105r2_w3vvff_ice_cream_recheck -->
```text
[Divergence from STAR]
  STAR                   = Chocolate
  Choose-One (Plurality) = Vanilla   (differs from STAR)
  RCV-IRV                = Vanilla   (differs from STAR)
  Note: 1 of 4 ballots (25%) had equal non-zero scores, so their ranks were
        decided by candidate priority order. The RCV-IRV result may be an
        artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/bv2105r2_w3vvff_ice_cream_recheck_RCV-IRV_tabulated.txt

--- Bloc STAR Voting Method (2 winners) ---

[Bloc STAR]
 Tabulating 4 ballots to fill 2 seats. Note: 1 of 4 ballots is marked as an abstention.
Vanilla,Chocolate,Strawberry
      5,        5,         5
      -,        -,         -
      1,        -,         -
      2,        5,         4
  ('-' = left blank / abstained; '0' = scored zero — both count as 0 stars.)

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Chocolate     -- 10 -- First place
   Strawberry    --  9 -- Second place
   Vanilla       --  8
 Chocolate and Strawberry advance.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Chocolate     -- 1 -- First place
   Strawberry    -- 0
   Equal Support -- 3
 Chocolate wins.
   Runoff math:
     4  ballots cast
   − 3  Equal Support (no preference between the two finalists)
     ─
     1  voters with a preference  (majority = 1)
           Chocolate 1 (100%)  ·  Strawberry 0 (0%)

──────────────────────────────────────────────────

[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Strawberry    -- 9 -- First place
   Vanilla       -- 8 -- Second place
 Strawberry and Vanilla advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Strawberry    -- 1 -- Tied for first place
   Vanilla       -- 1 -- Tied for first place
   Equal Support -- 2
 There's a two-way tie for first.

[Bloc STAR: Round 2: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Strawberry    -- 9 -- First place
   Vanilla       -- 8
 Strawberry wins.

[Bloc STAR: Winners — Bloc STAR Voting Method (2 winners)]
 Chocolate
 Strawberry
```
<!-- /report -->

LH counts **4 ballots, 1 abstention** — only the fully-blank row — and gives Vanilla a real `1`, for a total of 8.

## Does it change a winner?

Not here. The discarded ballot only helped Vanilla, who loses seat 2 either way, so this is a **reporting/counting** defect rather than a wrong result. But the ballot was *cast*, and a cast ballot dropped from the tally can flip a closer election — which is the whole reason the case is kept rather than filed as cosmetic.

## Related

- [BV2105 — the original (2025)](bv2105_r4dqvd_ice_cream_bloc.md) — same ballots, the run this one re-checks.
- [BV15 — Plurality abstain (bettervoting#740)](../../01_STAR/04_Real_Elections/pet_real_bv_election/bv15_4h89vj_plurality_abstain.md) — the mirror-image defect: abstentions *dropped from* displayed turnout.
- [The BV abstain / blank / zero issue index](../../07_Concepts/tabulation_engines/BV/abstain_issues_index.md) — how #884, #1053, #1090 and this one fit together.
- [Abstention vs a zero vs "None of the Above"](../../01_STAR/01_Learn/properties_and_limits/abstention_vs_zero_vs_nota.md) — the concept behind all of them.
- [02_STAR_Bloc README](README.md) · [BV registry](../../07_Concepts/YAML_test_case_index/BV_registry.md).
