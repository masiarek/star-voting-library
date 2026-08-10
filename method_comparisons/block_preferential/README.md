# Block preferential voting — the same ranked ballots, three ways to fill two seats

*Twelve members of a bakery co-op, four candidates, **two seats**. A 7-member majority (58%) and a 5-member minority (42%). Nobody changes their mind between counts — only the counting rule changes, and the board changes with it.*

**The lesson:** [block preferential voting](../../06_Other/RCV_IRV/concepts/variants/RCV-IRV-block-preferential.md) — instant runoff run once per seat — is **majoritarian**, not proportional. It reads the identical ranked ballot as [STV](../../06_Other/STV/README.md) and returns the same board as plain [plurality block voting](../multi_member_plurality/README.md): a clean sweep. What moves a seat is the **quota**, not the ballot.

## The electorate

| Voters | Ranking |
|:--:|---|
| 5 | Almond > Brioche > Croissant > Danish |
| 2 | Brioche > Almond > Croissant > Danish |
| 5 | Croissant > Danish > Almond > Brioche |

Majority faction = Almond + Brioche (7). Minority faction = Croissant + Danish (5).

## The three counts

| Count | Method | Winners | Majority : minority | Read · run |
|---|---|---|:--:|:--|
| **Block preferential, seat 1** | RCV-IRV on the full field | Almond (7 of 12 after transfers) | — | [page](cases/cases_pages/bpv_bakery_seat1_c4_b12.md) · [yaml](cases/bpv_bakery_seat1_c4_b12.yaml) |
| **Block preferential, seat 2** | RCV-IRV, Almond struck from every ballot | Brioche (7 of 12, round 1) | **2 : 0** | [page](cases/cases_pages/bpv_bakery_seat2_c3_b12.md) · [yaml](cases/bpv_bakery_seat2_c3_b12.yaml) |
| **Plurality block voting** | ranks discarded, mark 2 | Almond, Brioche | **2 : 0** | [page](cases/cases_pages/bpv_bakery_block_plurality_c4_b12.md) · [yaml](cases/bpv_bakery_block_plurality_c4_b12.yaml) |
| **STV** | same ranked ballots, Droop quota | Almond, **Croissant** | **1 : 1** | [page](cases/cases_pages/bpv_bakery_stv_c4_b12.md) · [yaml](cases/bpv_bakery_stv_c4_b12.yaml) |

The first two rows are **one election**: a block-preferential count is N sequential IRV counts, and the LH engine has no `voting_method: BlockPreferential`, so the set encodes each seat as the IRV count it actually is. That is not a workaround — it is the method's definition, written out.

## What each row shows

- **Seat 1** is unremarkable IRV. Danish (0 first preferences) and Brioche (2) cannot catch either leader and are eliminated; Brioche's two ballots move to Almond, who reaches 7 of 12.
- **Seat 2** is where block preferential voting parts company with STV. Almond is struck from every ballot — including the five that just elected him — and those five voters count again **at full strength**. Their second preference was Brioche. Nothing was spent, so the same seven people decide the second seat too.
- **Plurality block voting** discards the rankings entirely and returns the same board. The ranked ballot bought a more sophisticated count and an identical result.
- **STV** spends the majority's ballots on the seat they won. Almond and Croissant each hold 5 first preferences against a Droop quota of 4 (the engine's exact form; the hand-count rule `⌊12/3⌋ + 1 = 5` agrees here), so both are seated in round one and the minority takes a seat.

## Honest limits of this set

- **Four candidates, two seats, twelve voters** — the smallest field that shows the mechanism. It demonstrates that the sweep *happens*, not how often; adoption data, not a constructed case, is what would answer "how often."
- **The minority here is cohesive and the majority is cohesive.** That is the condition under which block preferential voting sweeps, and it is also the condition under which STV protects. Split either faction internally and both results get more interesting.
- **No BetterVoting backing.** BV has no block-preferential method, and encoding it as two separate single-winner IRV races would misrepresent it as two elections rather than one count. LH-only by design.

## See also

- The concept page: [RCV-IRV (Block Preferential)](../../06_Other/RCV_IRV/concepts/variants/RCV-IRV-block-preferential.md)
- [Which RCV-IRV?](../../06_Other/RCV_IRV/concepts/variants/RCV_IRV_variants.md) — the whole sequential-elimination family
- [Block vs Limited vs SNTV](../multi_member_plurality/README.md) — the plurality half of the same class
- [Bloc STAR among the at-large methods](../../02_STAR_Bloc/01_Learn/bloc_star_vs_other_bloc_methods.md) — the majoritarian family on one table
- [STV](../../06_Other/STV/README.md) · [STAR-PR](../../03_STAR_PR/README.md) — the proportional alternatives
- [Electing more than one, simply](../../07_Concepts/topics/electing_more_than_one.md) — the majoritarian/proportional fork, which comes before any of this
