# Minority winner — a third wins Choose-One, but the majority's choice wins STAR

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/2p33qq) · **[results ↗](https://bettervoting.com/2p33qq/results)** (election `2p33qq`, Test ID BV2215).

**One line:** under Choose-One, a candidate can **win with a third of the vote** while two-thirds wanted someone else. Read the whole ballot instead, and the winner is the candidate a majority is actually glad about. This is the repo's canonical example of the minority (plurality) winner — small enough to hold in your head.

---

## The setup

100 voters, three candidates for one seat: **Ada, Ben, Cleo.**

- **Ada** has a passionate base — a third of the room loves her.
- **Ben** has a passionate base too — another third loves him.
- **Cleo** is nobody's fiery favorite, but *everybody's easy second choice* — the one the whole room is fine with.

Here's how the 100 voters feel, scored 0–5:

| Voters | Ada | Ben | Cleo |
|---:|:--:|:--:|:--:|
| 34 | 5 | 0 | 4 |
| 33 | 0 | 5 | 4 |
| 33 | 2 | 1 | 5 |

## What Choose-One does

Choose-One counts **only your top pick.** So it only sees the first choices:

| Candidate | First choices | |
|---|:--:|:--|
| **Ada** | **34** | ← wins (34%) |
| Ben | 33 | |
| Cleo | 33 | |

**Ada wins with 34%.** But look again at the scores: **66 of the 100 voters rated Ada a 0 or a 1.** Two-thirds of the room did *not* want her — they just split their first choices between Ben and Cleo, so Ada's devoted third was enough to win. That's a **minority winner**, and it's the everyday failure of Choose-One in any race with more than two candidates.

## What reading the whole ballot does

Now count the *same* ballots with a method that reads all of them:

- **[STAR](../../00_start_here/STAR_Voting/STAR_start_here.md):** Cleo leads the scoring round with **433**, then wins the automatic runoff over Ada **66–34**. → **Cleo.**
- **[Ranked Robin](../../00_start_here/RCV_Ranked_Robin/why_ranked_robin.md):** Cleo beats Ada head-to-head (66–34) *and* Ben (67–33) — she's the **Condorcet winner**. → **Cleo.**

Both find **Cleo** — the candidate most people are genuinely happy with.

## The line-up

| Method | What it reads | Winner |
|---|---|:--:|
| **Choose-One (Plurality)** | first choices only | Ada — *34%* |
| **[Ranked Robin](../../00_start_here/RCV_Ranked_Robin/why_ranked_robin.md)** | every head-to-head | ✅ **Cleo** |
| **[STAR](../../00_start_here/STAR_Voting/STAR_start_here.md)** | scores, then a runoff | ✅ **Cleo** |

## The one big idea

Nobody voted strategically. Nobody changed their opinion. The entire difference is **how much of the ballot the method reads:**

> Choose-One sees only your *favorite*, so a passionate minority can win while the broadly-liked choice — everybody's easy second — is invisible to it. STAR and Ranked Robin read your *whole* ballot, so the candidate a majority actually prefers is the one who wins.

That's the case for a better ballot and a fuller count, in one small election. (It can get starker: with a bigger field, Choose-One winners can take office on 10–20%. A third is just the most common, most believable version.)

---

*See the same lens across every method: [same opinions, every method](../../00_start_here/topics/same_opinions_every_method.md). The concept page: [Choose-One / Plurality](../../00_start_here/topics/plurality.md). Full engine detail: [`bv2215_2p33qq_minority_winner_tabulated.txt`](minority_winner_tabulated/bv2215_2p33qq_minority_winner_tabulated.txt) · run it: [`bv2215_2p33qq_minority_winner.yaml`](bv2215_2p33qq_minority_winner.yaml).*
