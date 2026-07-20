# Exercise 5 — The squeezed bridge-builder

*A club elects its president. Two wings can't stand each other's candidate — and there's Brook, whom everyone can live with. Every single voter scores Brook a 3 or better. Run the same nine opinions as ranked ballots under RCV-IRV and as score ballots under STAR: do both counts find the bridge-builder?*

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/6bry7c) · **[results ↗](https://bettervoting.com/6bry7c/results)** (election `6bry7c`, Test ID BV2192 — STAR, RCV-IRV, and Ranked Robin races on the same opinions: the squeeze happens live).

**You practice:** the **[center squeeze](../../00_start_here/RCV_IRV/RCV_IRV_center_squeeze.md)** mechanism — predicting *when* first-choice elimination discards a consensus candidate — and how a scoring round reads the support that first choices can't see.

Work each part on paper before opening its solution. The YAML at the bottom is runnable; its `expected_winners` key is regression-tested, and the `_tabulated` mirror is the full audit report.

## The ballots

Nine voters, three candidates, scores 0–5 (rows are candidates, columns are voter blocs):

| | ×4 voters | ×3 voters | ×1 voter | ×1 voter |
|---|:---:|:---:|:---:|:---:|
| **Avi** | 5 | 0 | 3 | 0 |
| **Brook** | 3 | 3 | 5 | 5 |
| **Cole** | 0 | 5 | 0 | 3 |

Avi's wing (4 voters), Cole's wing (3 voters), and two Brook-first voters who lean opposite ways. For RCV-IRV, rank each column by its scores.

## Your task

- **(a)** Count first choices. Then run **RCV-IRV**: who is eliminated first, where do their votes go, who wins?
- **(b)** Now run **STAR**: scoring round, finalists, runoff. Who wins?
- **(c)** Check Brook against each rival head-to-head. What is Brook, in Condorcet terms — and which of your two winners agrees with that verdict?
- **(d)** The squeeze needed specific conditions. Change ONE number in the table so that RCV-IRV *does* elect Brook. What does your fix reveal about what the squeeze depends on?

## Solutions

<details>
<summary><b>(a) RCV-IRV — Brook is eliminated first; Avi wins</b></summary>

First choices: Avi 4, Cole 3, **Brook 2** — the candidate everyone accepts is *nobody's* first choice but two. IRV eliminates Brook immediately. Brook's two voters split: one transfers to Avi (scored 3), one to Cole (scored 3). Final round: **Avi 5, Cole 4 — Avi wins.** The 3 Cole-wing voters, who scored Avi zero, get their least-acceptable outcome; Brook's broad 3s were never looked at. That is the center squeeze.

</details>

<details>
<summary><b>(b) STAR — Brook, 5–4</b></summary>

```text
Scoring Round
 The two highest-scoring candidates advance to the next round.
   Brook         -- 31 -- First place
   Avi           -- 23 -- Second place
   Cole          -- 18
 Brook and Avi advance.

Automatic Runoff Round
 The candidate preferred in the most head-to-head matchups wins.
   Brook         -- 5 -- First place
   Avi           -- 4
   Equal Support -- 0
 Brook wins.
   Voters with a preference: 9 of 9 (no Equal Support).
   Brook 5 (56%) vs Avi 4 (44%).
```

The scoring round is exactly where those invisible 3s count: Brook 31 (from *all nine* voters), Avi 23, Cole 18. In the runoff, Cole's whole wing prefers Brook over Avi — **Brook wins 5–4.**

</details>

<details>
<summary><b>(c) Brook is the Condorcet winner</b></summary>

Brook vs Avi: 5–4 (Cole's wing plus both Brook voters). Brook vs Cole: 6–3 (Avi's wing plus both Brook voters). **Brook beats everyone head-to-head** — the Condorcet winner — and STAR's verdict agrees while IRV's doesn't. (The engine's divergence block prints the same: `RCV-IRV = Avi`, with the note that no scores are tied, so this is a genuine method difference, not a conversion artifact.) This is the textbook pattern of Burlington 2009 and Alaska 2022 — see the [center-squeeze comparison set](../../method_comparisons/center_squeeze/README.md) for the fuller treatment.

</details>

<details>
<summary><b>(d) Break the squeeze — and see what it depends on</b></summary>

One clean fix: move one Avi-wing voter's Brook score from 3 up to *first place* (Avi 3, Brook 5). First choices become Avi 3, Cole 3, Brook 3 — the elimination tie breaks the clean story, but push it to two voters and Brook simply stops being last in first-choices, survives the first round, and then beats either rival in the final. The reveal: the squeeze depends on **first-choice count alone deciding who survives** — Brook's actual support (nine voters at 3+) never mattered, only the accident of how many put Brook *strictly first*. Any repair must route around that bottleneck, which is precisely what a scoring round is.

</details>

## Reading this fairly

The squeeze is the rare "whoops" that passes the whole [four-part test](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md): structural (a whole region of spatial electorates, not a knife-edge), sincere (no strategy anywhere above), realistic (two wings + a bridge-builder is ordinary politics), and really happened (Burlington 2009, Alaska 2022). The fairness note runs the other way: STAR is not squeeze-*proof* in some absolute sense — it simply doesn't gate survival on first choices; its own honest limits live in [exercise 1](ex01_two_districts.md) and [exercise 2](ex02_tenth_ballot.md).

## Run it yourself

```
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/cases/ex05_center_squeeze.yaml
```

Source: [ex05_center_squeeze.yaml](cases/ex05_center_squeeze.yaml). Full audit report: [mirror](cases/cases_tabulated/ex05_center_squeeze_tabulated.txt).

---

**Where this comes from.** Original to this repo (ballots and cast); the mechanism it drills is the classic center squeeze — concept home [RCV-IRV center squeeze](../../00_start_here/RCV_IRV/RCV_IRV_center_squeeze.md), live comparison set [method_comparisons/center_squeeze](../../method_comparisons/center_squeeze/README.md) (BV2137).

*Back to [the exercises set](README.md) · curriculum home: [Voting 301](../../00_start_here/curriculum/CURRICULUM_301.md)*

# file: ex05_center_squeeze.md
