# Seat order — the candidate who beats everyone is seated second

**One line:** in this two-seat election **Anika** beats every other candidate head-to-head — including **Dev**, who takes seat 1 — and is seated **second**. Under Bloc STAR "first seated" means *won the first runoff*, not *most preferred*, and the difference is visible on the same seven ballots.

→ The method: [Bloc STAR](../../01_Learn/bloc_star.md) · the single-winner version of the same tension: [three notions of "winner"](../../../01_STAR/01_Learn/properties_and_limits/STAR_three_winner_notions.md)

**Level: 201.** One election, 4 candidates, 7 voters, 2 seats — small enough to check the pairwise table by hand.

---

## The election

Four candidates — **Anika, Bo, Cora, Dev** — for **two seats**, scored 0–5.

| # | Anika | Bo | Cora | Dev |
|---|:--:|:--:|:--:|:--:|
| 1 | 4 | 2 | 3 | 2 |
| 2 | 1 | 5 | 5 | 5 |
| 3 | 4 | 3 | 0 | 3 |
| 4 | 5 | 4 | 0 | 3 |
| 5 | 4 | 2 | 2 | 3 |
| 6 | 1 | 1 | 4 | 3 |
| 7 | 2 | 5 | 1 | 5 |

**Seat 1** — scores **Dev 24**, **Bo 22**, Anika 21, Cora 15. The top two advance, so Anika misses the runoff by a single point. Runoff **Dev 2 – Bo 1**, with 4 voters expressing no preference between them. **Dev is seated.**

**Seat 2** — Dev is removed and the same ballots are re-counted: Bo 22, Anika 21, Cora 15. Runoff **Anika 4 – Bo 2** (1 Equal Support). **Anika is seated.**

**Council: Dev, then Anika.**

## The pairwise table — Anika beats all three

| Matchup | For | Against | Equal Support |
|---|:--:|:--:|:--:|
| Anika vs Bo | **4** | 2 | 1 |
| Anika vs Cora | **5** | 2 | 0 |
| **Anika vs Dev** | **4** | **3** | 0 |

Anika is the **Condorcet winner** — preferred by a majority to every rival, one at a time — and she is seated *after* Dev, whom she beats 4–3. No tie is broken anywhere in this election; both seats are decided outright by the ballots.

## Why it matters, and why it is not a scandal

**It matters because seat order is often not cosmetic.** Plenty of bodies attach something to finishing first: the chair, the mayoralty, the longer term, the tie-breaking vote, the top line on the ballot next cycle. If your rules say "the top vote-getter becomes chair," this election hands the chair to the candidate a majority likes *less* than the person seated behind them. That is a rules-design question — the count is doing exactly what it was told — and this is the receipt to have in hand when the question comes up.

**It is not a scandal because both of them win.** Run these same ballots for **one** seat and it is an ordinary [STAR Condorcet failure](../../../01_STAR/01_Learn/properties_and_limits/STAR_three_winner_notions.md): Anika misses the top two by a point and loses outright. The second seat *rescues* her. Multi-winner elections are more forgiving of a narrow scoring-round miss than single-winner ones — a genuinely good thing to be able to show, and the honest other half of this page.

What the case pins down is the precise claim: **Bloc STAR seats winners in the order its runoffs finish, and that order is not a preference ranking.** Announce the council as a set, not a podium, unless your rules really mean the podium.

## Related

- [The score leader can win no seat](../../01_Learn/score_leader_no_seat.md) — the sharper form: leading every scoring round and taking nothing
- [Participation](../participation/) · [the committee spoiler](../committee_spoiler/) — the folder's other two criteria
- [Ties, seat by seat](../../01_Learn/bloc_tiebreaks.md) — the other way seat order stops being cosmetic: a seat-1 tie can change *who* wins seat 2
- [Honest limits](../../01_Learn/bloc_honest_limits.md) · [Bloc STAR among the at-large methods](../../01_Learn/bloc_star_vs_other_bloc_methods.md)

# file: README.md
