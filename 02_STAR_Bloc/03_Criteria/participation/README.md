# Participation — voting made this voter's council worse

**One line:** a voter turns up, scores the candidates honestly, and ends up with a council their own ballot rates **lower** than the one they would have got by staying home — because the support they gave their favourite pushed that favourite into the **seat-2 runoff**, where a candidate they scored **0** won it.

**▶ Live on BetterVoting:** BV2264 [vote](https://bettervoting.com/j3hqvb) · **[results ↗](https://bettervoting.com/j3hqvb/results)** (election `j3hqvb`) — the council six voters elect · BV2265 [vote](https://bettervoting.com/th3pbp) · **[results ↗](https://bettervoting.com/th3pbp/results)** (election `th3pbp`) — the same six plus the joiner.

→ The method: [Bloc STAR](../../01_Learn/bloc_star.md) · the concession list this belongs on: [honest limits](../../01_Learn/bloc_honest_limits.md) · the single-winner paradox page: [no-show](../../../07_Concepts/voting_paradoxes/no_show.md)

**Level: 301 · deep dive** Two elections, same 4 candidates, 2 seats. The second is the first plus one ballot.

---

## The two elections

Four candidates — **Ada, Bruno, Cleo, Dov** — for a **two-seat** board, scored 0–5.

### Before: six voters

| # | Ada | Bruno | Cleo | Dov |
|---|:--:|:--:|:--:|:--:|
| 1 | 3 | 5 | 1 | 3 |
| 2 | 4 | 5 | 2 | 4 |
| 3 | 4 | 0 | 1 | 4 |
| 4 | 2 | 2 | 5 | 1 |
| 5 | 3 | 1 | 1 | 1 |
| 6 | 5 | 0 | 1 | 5 |

**Seat 1** — scores Ada 21, Dov 18, Bruno 13, Cleo 11; Ada and Dov advance; runoff **Ada 2 – Dov 0** (4 voters express no preference between them). **Ada is seated.**

**Seat 2** — Ada is removed and the same ballots are re-counted: Dov 18, Bruno 13, Cleo 11; Dov and Bruno advance; runoff **Bruno 3 – Dov 2** (1 Equal Support). **Bruno is seated.**

**Council: Ada and Bruno.**

### After: the same six, plus one

A seventh voter arrives. Their honest ballot: **Ada 3, Bruno 2, Cleo 5, Dov 0** — Cleo is their favourite, Dov the one candidate they cannot stand.

| # | Ada | Bruno | Cleo | Dov |
|---|:--:|:--:|:--:|:--:|
| 1–6 | *as above* | | | |
| **7** | **3** | **2** | **5** | **0** |

**Seat 1** — scores Ada 24, Dov 18, Cleo 16, Bruno 15; runoff **Ada 3 – Dov 0** (4 Equal Support). **Ada is seated**, exactly as before.

**Seat 2** — Ada removed: Dov 18, **Cleo 16**, Bruno 15. Cleo has passed Bruno by one point and takes the second finalist slot. Runoff **Dov 4 – Cleo 2** (1 Equal Support). **Dov is seated.**

**Council: Ada and Dov.**

## What just happened

By their own ballot, the new voter rates the two possible councils like this:

| | Ada | + partner | total |
|---|:--:|---|:--:|
| The council they would have got by **staying home** | 3 | Bruno **2** | **5** |
| The council they got by **voting** | 3 | Dov **0** | **3** |

Their ballot changed exactly one thing that mattered: it lifted **Cleo** from 11 points to 16, which was enough to push Cleo past **Bruno** into the seat-2 runoff. Bruno — whom this voter scored 2, and who beat Dov in that runoff before — was no longer on the ballot at that stage. Dov, whom they scored **0**, beat Cleo comfortably and took the seat.

**Helping your favourite reach the runoff is what handed the seat to the candidate you scored zero.** Nothing here is strategic and no ballot is insincere; the seventh voter simply voted.

## Why it is worth a case

- **It is a participation failure — the [no-show paradox](../../../07_Concepts/voting_paradoxes/no_show.md) — in cardinal, multi-winner form.** The library's other no-show cases are all ranked-ballot ones (Burlington, Felsenthal Ex.4, the RCV-IRV pair), and in the Felsenthal pair **STAR is the method that doesn't move**. That reads as "STAR is fine here," and for one seat it largely is. For several seats it isn't.
- **The mechanism is specific to Bloc STAR**, not inherited from STAR. Each seat rebuilds the finalist pair from what is left, so a ballot that cannot change seat 1 gets a second, independent chance to change seat 2 — and there is no reweighting step to absorb it. Compare [STAR-PR](../../../03_STAR_PR/README.md), where support already spent on a seated winner is discounted.
- **The honest framing.** Every deterministic voting method with more than two candidates can be embarrassed like this ([Gibbard](../../../07_Concepts/topics/gibbard_satterthwaite_theorem.md)), and no rung of the tie-break ladder is involved here — this is the count working as designed. What the case establishes is the *shape* of Bloc STAR's failure, so it can be described accurately instead of denied or exaggerated.

## Run them yourself

Both elections are live on BetterVoting and reproduced independently in the LH engine; **BV and LH agree exactly**, all seats decided with `tieBreakType: none` and every ballot counted (`nTallyVotes` 6 and 7).

| Case | Voters | Council | Read · run |
|---|:--:|---|---|
| **BV2264** — the control | 6 | Ada, Bruno | [count](cases/cases_pages/bv2264_j3hqvb_council_before_joiner.md) · [yaml](cases/bv2264_j3hqvb_council_before_joiner.yaml) · [results ↗](https://bettervoting.com/j3hqvb/results) |
| **BV2265** — the joiner votes | 7 | Ada, **Dov** | [count](cases/cases_pages/bv2265_th3pbp_joiner_council_worse.md) · [yaml](cases/bv2265_th3pbp_joiner_council_worse.yaml) · [results ↗](https://bettervoting.com/th3pbp/results) |

Frozen exports sit beside each yaml as `…_bv_export.json`.

## Related

- [Honest limits](../../01_Learn/bloc_honest_limits.md) — where this sits among the four limits Bloc STAR adds to STAR's own
- [The score leader can win no seat](../../01_Learn/score_leader_no_seat.md) — the other case where the runoff step, not the scores, decides everything
- [Seat order](../seat_order/) · [the committee spoiler](../committee_spoiler/) — the folder's other two criteria
- [Reading the runoff percentages](../../../01_STAR/01_Learn/the_count/runoff_percentages.md) — why seat 1 above runs on 2 of 6 voters and seat 2 on 5 of 6

# file: README.md
