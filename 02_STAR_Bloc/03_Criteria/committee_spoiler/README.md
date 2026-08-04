# The committee spoiler — a candidate who wins nothing changes who does

**One line:** the same seven ballots elect **Cyrus and Ari** with three candidates on the ballot, and **Cyrus and Bea** once **Dane** is added — and Dane wins no seat. A candidate who cannot win still decides who sits in the second chair.

**▶ Live on BetterVoting:** BV2267 [vote](https://bettervoting.com/my9jd9) · **[results ↗](https://bettervoting.com/my9jd9/results)** (election `my9jd9`) — three candidates · BV2268 [vote](https://bettervoting.com/6m3gxq) · **[results ↗](https://bettervoting.com/6m3gxq/results)** (election `6m3gxq`) — the same ballots with Dane added.

→ The method: [Bloc STAR](../../01_Learn/bloc_star.md) · the single-winner version: [IIA & the cycle spoiler](../../../01_STAR/03_Criteria/iia_cycle_spoiler/README.md)

**Level: 301 · deep dive.** Two elections, 2 seats each, seven voters who never change their minds about anyone.

---

## The two elections

### Three candidates: Ari, Bea, Cyrus

| # | Ari | Bea | Cyrus |
|---|:--:|:--:|:--:|
| 1 | 5 | 3 | 3 |
| 2 | 0 | 3 | 4 |
| 3 | 1 | 0 | 1 |
| 4 | 0 | 5 | 2 |
| 5 | 4 | 2 | 4 |
| 6 | 1 | 0 | 1 |
| 7 | 0 | 3 | 2 |

**Seat 1** — scores Cyrus 17, Bea 16, Ari 11; runoff **Cyrus 4 – Bea 2** (1 Equal Support). **Cyrus is seated.**
**Seat 2** — Cyrus removed: Bea 16, Ari 11; runoff **Ari 4 – Bea 3**. **Ari is seated.**

**Council: Cyrus and Ari.**

### The same ballots, plus a fourth candidate: Dane

Every existing score is untouched; the voters simply also say what they think of Dane.

| # | Ari | Bea | Cyrus | **Dane** |
|---|:--:|:--:|:--:|:--:|
| 1 | 5 | 3 | 3 | **0** |
| 2 | 0 | 3 | 4 | **2** |
| 3 | 1 | 0 | 1 | **5** |
| 4 | 0 | 5 | 2 | **1** |
| 5 | 4 | 2 | 4 | **1** |
| 6 | 1 | 0 | 1 | **5** |
| 7 | 0 | 3 | 2 | **3** |

**Seat 1** — scores Cyrus 17, **Dane 17**, Bea 16, Ari 11. Dane's arrival pushes *Bea* out of the finalist pair; runoff **Cyrus 4 – Dane 3**. **Cyrus is seated** — the same winner as before.
**Seat 2** — Cyrus removed: **Dane 17**, Bea 16, Ari 11. Dane and Bea advance; **Ari, who won this seat a moment ago, is not even a finalist.** Runoff **Bea 4 – Dane 2** (1 Equal Support). **Bea is seated.**

**Council: Cyrus and Bea. Dane wins nothing.**

## What it shows

Dane takes no seat in either round and loses both runoffs he reaches — yet his presence swaps **Ari** off the council for **Bea**. This is a failure of **independence of irrelevant alternatives** at the level of the *committee*: the set of winners depends on a candidate who is not one of them.

Two things make the Bloc version different from the [single-winner one](../../../01_STAR/03_Criteria/iia_cycle_spoiler/README.md):

- **No Condorcet cycle is needed.** The single-winner spoiler case has to arrange a genuine cycle before a non-winner can flip the result. Here the mechanism is plain arithmetic: each seat rebuilds the finalist pair from the candidates still standing, so an also-ran with a competitive *score* can occupy a finalist slot at seat 2 and crowd out the candidate who would have won it. Dane never has to be liked — he only has to score well enough to make the pair.
- **The spoiler gets N chances, not one.** A candidate eliminated from contention for seat 1 is still on the ballot for seat 2, and every subsequent seat. The more seats, the more finalist pairs there are to disturb.

The practical reading, for anyone choosing rules rather than studying them: **who else runs changes the composition of a Bloc STAR body, even when those candidates lose.** That is true of nearly every method — it is worth knowing which shape it takes here, and knowing that it does not require anything exotic like a cycle to happen.

## Run them yourself

Both are live on BetterVoting and reproduced independently in the LH engine; **BV and LH agree exactly**, `nTallyVotes 7` on both, `tieBreakType: none` at every seat.

| Case | Candidates | Council | Read · run |
|---|:--:|---|---|
| **BV2267** — the control | 3 | Cyrus, **Ari** | [count](cases/cases_pages/bv2267_my9jd9_council_before_dane.md) · [yaml](cases/bv2267_my9jd9_council_before_dane.yaml) · [results ↗](https://bettervoting.com/my9jd9/results) |
| **BV2268** — Dane runs | 4 | Cyrus, **Bea** | [count](cases/cases_pages/bv2268_6m3gxq_spoiler_changes_council.md) · [yaml](cases/bv2268_6m3gxq_spoiler_changes_council.yaml) · [results ↗](https://bettervoting.com/6m3gxq/results) |

Frozen exports sit beside each yaml as `…_bv_export.json`.

## Related

- [Participation](../participation/) — the other case on this folder where a change that cannot touch seat 1 decides seat 2
- [Seat order](../seat_order/) — the council is a set, not a podium
- [Residual vote-splitting](../../../01_STAR/01_Learn/properties_and_limits/residual_vote_splitting.md) — what STAR does and does not fix about extra candidates
- [Honest limits](../../01_Learn/bloc_honest_limits.md) · [Bloc STAR among the at-large methods](../../01_Learn/bloc_star_vs_other_bloc_methods.md) — where SNTV's version of this problem is much worse

# file: README.md
