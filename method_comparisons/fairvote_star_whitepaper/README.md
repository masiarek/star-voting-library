# FairVote's official position on STAR, claim-checked

*In July 2018 FairVote — the leading Ranked-Choice-Voting advocacy group — published a white paper, **"Explaining FairVote's position on STAR Voting"** (Rob Richie & Drew Spencer Penrose), laying out why it backs RCV over STAR. It's the canonical opposition document, and most of its claims are **checkable**. This page quotes each, concedes the ones that are **true** (STAR does fail some criteria — and here's why we think the trade is worth it), **runs** the strategic examples on a live engine, and **flags** the ones that were already false when the ink was wet. Same discipline as the [FairVote Condorcet claim-check](../../00_start_here/topics/condorcet/fairvote_condorcet_claim_check.md) — and, as there, the fairness cuts toward our own side too.*

**▶ Live on BetterVoting:** French 2017 [honest ↗](https://bettervoting.com/7j2bqf/results) · [burial ↗](https://bettervoting.com/2hqmrd/results) (BV2229/2230) — Washington 2010 [honest ↗](https://bettervoting.com/b4yr3v/results) · [burial ↗](https://bettervoting.com/24b623/results) (BV2231/2232).

→ Related: [Favorite Betrayal (LNH vs FBC)](../../00_start_here/STAR_Voting/properties_and_limits/favorite_betrayal_voting_301.md) · [the 5-1-0 challenge](../star_5_1_0_challenge/) · [STAR's honest limits](../../00_start_here/STAR_Voting/properties_and_limits/STAR_honest_limits.md) · [are equal-score votes discounted?](../../00_start_here/STAR_Voting/reference/are_equal_score_votes_discounted.md).

---

## The claims that are TRUE — conceded

FairVote is a serious critic, and several of its points are simply correct. Pretending otherwise would fail this repo's own [fairness rule](../paradoxes_and_whoops/reading_these_fairly.md).

- **STAR fails Later-No-Harm.** True — scoring a second candidate can help defeat your favorite. *But this is the whole disagreement.* FairVote lists LNH-failure as a **flaw**; STAR's camp — including STAR's co-inventor [Clay Shentrup, "Later-no-harm is a bug, not a feature"](https://medium.com/@ClayShentrup/later-no-harm-72c44e145510) — argues LNH is *the very property that forces [center squeeze](../center_squeeze/)*: guaranteeing your backup can never help your favorite is mathematically the same as guaranteeing a broadly-liked compromise can't be rescued. RCV keeps LNH and pays for it in Burlington and Alaska. Worked in full on the [favorite-betrayal page](../../00_start_here/STAR_Voting/properties_and_limits/favorite_betrayal_voting_301.md).
- **STAR fails the majority-favorite and mutual-majority criteria** (in constructed cases); RCV satisfies both. True and conceded — see [STAR's honest limits](../../00_start_here/STAR_Voting/properties_and_limits/STAR_honest_limits.md) and [residual vote-splitting](../../00_start_here/STAR_Voting/properties_and_limits/residual_vote_splitting.md). These are rare, constructed failures, not everyday behavior.
- **There is no single "honest" 0–5 score** the way there's an honest ranking. A fair philosophical point — scoring asks *how much*, which is genuinely a judgment call. The repo agrees the scale is a modeling choice ([are equal-score votes discounted?](../../00_start_here/STAR_Voting/reference/are_equal_score_votes_discounted.md)); the counter is that real STAR elections show ~90% of voters using the full range comfortably ([STAR history](../../00_start_here/STAR_Voting/STAR_history.md)).

And FairVote makes one **concession in STAR's favor** worth keeping: STAR *cannot elect the Condorcet loser* (the runoff prevents it), unlike plurality, score, and approval. They're right, and it's a real STAR strength.

## The strategic examples — RUN, not just argued

The white paper's most concrete claim is that STAR's strategy incentives let a coordinated faction **bury a strong centrist** out of the runoff. It gives two examples. We modelled both — honest ballots *and* the exact burial FairVote describes.

### The 2017 French election

FairVote: with four ~20% candidates and Macron the broadly-preferred centrist, rival factions could score Macron 0 (and inflate the other wings) to keep him out of the runoff.

| | STAR | RCV-IRV |
|---|:--:|:--:|
| **Honest** ([`french_2017_honest`](cases/cases_pages/bv2229_7j2bqf_french_2017_honest.md)) | **Macron** (351; runoff 51–49) | **Macron** |
| **Coordinated burial** ([`french_2017_strategic`](cases/cases_pages/bv2230_2hqmrd_french_2017_burial.md)) | Mélenchon (Macron → 130, squeezed) | **Le Pen** |

**Conceded:** the burial works under STAR — Macron, the Condorcet winner, is squeezed out. **But read the honest full picture:** it required *every* rival faction to bury Macron **and rate its ideological enemies a 4** — a risky, wildly-coordinated conspiracy. Honest STAR elects Macron. And RCV-IRV on the *same* strategic ballots elects **Le Pen** — a worse miss. The asymmetry the white paper never states: **STAR squeezes the center only under coordinated strategy; IRV squeezes it under sincere voting** ([Burlington](../burlington_2009/README.md), [Alaska](../alaska_2022/)).

### The 2010 Washington State Senate race

FairVote: anti-Berkey groups boosted the long-shot conservative Rieger to squeeze the moderate Berkey; under STAR they'd score Harper 5, Rieger 4, Berkey 0.

| | STAR | RCV-IRV |
|---|:--:|:--:|
| **Honest** ([`wa_2010_honest`](cases/cases_pages/bv2231_b4yr3v_wa_2010_honest.md)) | **Berkey** (385; runoff 60–40) | **Berkey** |
| **Coordinated burial** ([`wa_2010_strategic`](cases/cases_pages/bv2232_24b623_wa_2010_burial.md)) | Harper (Berkey → 225, squeezed) | **Berkey** — resists! |

**This one cuts fairly against STAR, and we keep it that way:** the burial works under STAR (Berkey squeezed, Harper wins), and RCV-IRV on the same ballots **still elects Berkey** — the manipulation STAR fell for, IRV happened to resist. That's a real point for IRV *in this case*. The honest balance: (1) honest STAR elects Berkey; (2) the burial needs the Harper faction to rate a conservative a 4, which could backfire and elect Rieger; (3) IRV's resistance here is incidental to elimination order, and doesn't rescue it from squeezing centrists when voters are **honest**. One method needs a conspiracy to squeeze the center; the other does it sincerely.

## The claims that were already OVERCLAIMED

- **"RCV elects the Condorcet winner in practice."** The paper leans on *"over 100 Bay Area RCV elections, every one elected the Condorcet winner."* But **[Burlington 2009](../burlington_2009/README.md) — a real RCV Condorcet failure — predated this 2018 paper by nine years**, and the claim is carefully scoped to *the Bay Area*. That's a [criterion-built-to-fit](../../00_start_here/topics/condorcet/) tell; **[Alaska 2022](../alaska_2022/)** later refuted it outright. RCV does **not** satisfy the Condorcet criterion, in theory or in the field — a fact available when the paper was written.
- **The "nullifying ballots" framing.** Equal-Support voters (who score both finalists the same) are described as having their votes "set aside." That's precisely the framing our [are equal-score votes discounted?](../../00_start_here/STAR_Voting/reference/are_equal_score_votes_discounted.md) page rebuts: their scores *are* counted (they helped choose the finalists); they simply decline to tip a pairing they rated equally — exactly like leaving a down-ballot race blank.
- **"STAR has no track record."** True in 2018; dated now. STAR has run binding public elections since the 2020 Independent Party of Oregon primary ([history](../../00_start_here/STAR_Voting/STAR_history.md)).

## Net assessment

FairVote's white paper is a *good-faith, serious* critique — the best-argued opposition to STAR there is — and its criterion claims are **largely accurate**: STAR does fail Later-No-Harm, the majority-favorite criterion, and mutual majority, and it *can* be strategically manipulated to squeeze a centrist. We concede all of that. The disagreement is threefold: (1) whether **LNH is a virtue** — FairVote assumes yes; STAR's whole design says it's the bug that causes center squeeze; (2) whether STAR's **strategic** vulnerability is comparable to IRV's **sincere** one — it isn't, and the French/WA runs show honest STAR electing the centrist both times; and (3) the paper's one **empirical** claim, that RCV reliably elects the Condorcet winner, was already contradicted by Burlington when written and is now refuted by Alaska. Read every white paper — FairVote's and STAR's — with the ballots in hand.

## The demo elections

All four are LH-verified *and* live on BetterVoting.

| Case | Winner | Live results | Page |
|---|:--:|---|---|
| French 2017 — honest | Macron | [BV2229 ↗](https://bettervoting.com/7j2bqf/results) | [page](cases/cases_pages/bv2229_7j2bqf_french_2017_honest.md) |
| French 2017 — burial | Mélenchon | [BV2230 ↗](https://bettervoting.com/2hqmrd/results) | [page](cases/cases_pages/bv2230_2hqmrd_french_2017_burial.md) |
| Washington 2010 — honest | Berkey | [BV2231 ↗](https://bettervoting.com/b4yr3v/results) | [page](cases/cases_pages/bv2231_b4yr3v_wa_2010_honest.md) |
| Washington 2010 — burial | Harper | [BV2232 ↗](https://bettervoting.com/24b623/results) | [page](cases/cases_pages/bv2232_24b623_wa_2010_burial.md) |

*Both scenarios are simplified teaching models of the real fields (French: the ~20%-each four-way; Washington: Berkey / Harper / Rieger), built to reproduce the exact dynamic FairVote's white paper describes. Source of the critique: Richie & Penrose, FairVote, July 2018 — an advocacy document, checked here the same way this repo checks its own side's advocacy.*
