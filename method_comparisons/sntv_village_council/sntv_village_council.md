# Village Council by SNTV — a concentrated minority wins a seat

*A clean, standalone look at the one property that made SNTV famous: with a single vote per voter, a disciplined minority can win representation a majority would otherwise sweep. Nine residents, two council seats.*

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/y3tvxm) · **[results ↗](https://bettervoting.com/y3tvxm/results)** (election `y3tvxm`, Test ID **BV2136**). Frozen export: [`sntv_village_council_y3tvxm_bv_export.json`](sntv_village_council_y3tvxm_bv_export.json).

## The election

Two factions, three candidates, **2 seats**, SNTV (one vote each; the top two win):

```text
Nora,Omar,Priya
3 × Nora     (Downtown majority, split)
2 × Omar     (Downtown majority, split)
4 × Priya    (Riverside minority, concentrated)
```

- **Downtown** is the majority (5 of 9) but **splits** its votes: Nora 3, Omar 2.
- **Riverside** is the minority (4 of 9) but **concentrates**: Priya 4.

## Result

```text
--- SNTV (single non-transferable vote) — 2 winners ---
First-choice votes (most votes fill the seats):
   Priya     4  <- Elected
   Nora      3  <- Elected
   Omar      2

Winners — SNTV, 2 seats: Priya (4), Nora (3)
```

**Priya tops the poll** and wins a seat next to Nora; Omar just misses. The 44% minority earns 1 of 2 seats — rough proportionality. Under **Block Voting** (each voter marks both seats) the 5-voter majority would take *both* seats and shut Riverside out; SNTV's single vote is exactly what opens the door — provided the minority concentrates. That vote-management pressure is why SNTV was used for multi-member districts (Japan, Taiwan) before STV.

## On BetterVoting (BV2136)

Reproduced natively as BV **multi-winner Plurality** (`Plurality` + `num_winners: 2`, election [`y3tvxm`](https://bettervoting.com/y3tvxm/results)). **BV elects the same two — Priya and Nora — confirming LH.** This is SNTV running directly on BetterVoting: single mark per voter, the top two by first-choice count win. No Approval workaround needed (that's only for the multi-mark Block/Limited variants).

## See also

- The full family — Block vs. Limited vs. SNTV: [multi_member_plurality](../multi_member_plurality/) · how BV runs it: [running_on_bettervoting.md](../multi_member_plurality/running_on_bettervoting.md)
- References: [SNTV (Wikipedia)](https://en.wikipedia.org/wiki/Single_non-transferable_vote) · [SNTV (electowiki)](https://electowiki.org/wiki/Single_non-transferable_vote)
- Proportional alternatives: [STV](../../06_Other/STV/) · [STAR-PR](../../03_STAR_PR/)
