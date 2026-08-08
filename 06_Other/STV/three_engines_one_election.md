# Three engines, one election — what a cross-check actually costs

**One line:** Two tabulators agreeing on the winner proves less than it looks like, because agreement is cheap when the settings are wrong — and the only way this library found out was to count one nine-voter book club three different ways.

**Level: 301 · deep dive**

*Prerequisite: [STV](README.md), particularly [fork 1 — which quota?](README.md#where-it-genuinely-gets-complicated). The election worked here is [exercise 14](../../01_STAR/05_Practice/ex14_transfer_machine.md).*

---

## The gap that started it

This library cross-checks itself, and it is uneven about it. [Ranked Robin](../../05_Ranked_Robin/README.md) has **three** independent counts behind every case: the engine here, [BetterVoting](../../07_Concepts/tabulation_engines/bettervoting_and_the_engine.md), and [`pref_voting`](../../07_Concepts/tabulation_engines/cross_checking_with_pref_voting.md)'s Copeland. The house rule is to run all three on every RR case, not just awkward ones, precisely because the third is what makes a result trustworthy instead of self-confirming.

STV had one and a half.

The vendored `pyrankvote` counts it. BetterVoting was supposed to be the second opinion — except BetterVoting **crashes** on any STV count whose eliminations leave a sole remaining hopeful who then reaches quota ([the sole-survivor bug](bv_stv_sole_survivor_crash/README.md), diagnosed in BV's own source). That is not an exotic shape. It is the shape of the gentlest STV election in this repo, the nine-member book club buying two novels. So the cases that most needed a witness were exactly the ones that had none, and several published seat lists rested on a single engine.

[RCTab](../../07_Concepts/tabulation_engines/rctab.md) — federally tested under the VVSG, state-certified, the software US jurisdictions run on election night — now counts all ten. **They agree**, including the two BetterVoting cannot count at all.

That is the boring half.

## Agreement is cheap if you don't pin the settings

Here is the part worth 301 attention. Before a single case was run, one setting had to be chosen correctly, and choosing it wrongly would have produced a *confident, meaningless* answer.

"The Droop quota" names two published formulas, one vote apart. RCTab does not pick for you — it exposes the choice as a config field, and documents it exactly, in its own shipped `config_file_documentation.txt`:

```text title="RCTab config_file_documentation.txt — quoted, not paraphrased"
"nonIntegerWinningThreshold" optional
  the vote threshold used to determine winners can be a non-integer
  if true,  threshold = V/(S+1) + 10^-d
  if false, threshold = floor(V/(S+1)) + 1
  where V = total number of votes; S = numberOfWinners;
  and d = decimalPlacesForVoteArithmetic
  note: only valid for multi-seat contests
```

Read that as a sentence: **this repo's fork 1 is a checkbox in production election software.** The theory literature's exact quota and the Irish/Scottish hand-count quota are both shipping, in one binary, behind one boolean.

Our engine applies the exact form — `pyrankvote` elects at `votes - 1e-6 >= V/(S+1)`, which is "strictly above `V/(S+1)` by a hair," the same shape as RCTab's `+ 10⁻ᵈ`. So the converter sets the flag **true**.

Set it `false` and RCTab would have counted an election **one whole vote different** from ours. On these ten cases it would very likely still have named the same winners — the seats are robust to the quota here — and the cross-check would have reported ten green ticks while comparing two different elections. A disagreement, if one had surfaced, would have been about *configuration*, and someone would have gone hunting for a bug in a tabulator that was working perfectly.

**This is the general shape of the thing.** A cross-check is not "run it somewhere else and see if the name matches." It is: make the two systems answer the *same question*, prove you have done so, and only then compare. Everything before the comparison is the actual work.

There is a smaller version of the same trap one layer down. Our engine could not have told you which quota it applied — until August 2026 its report header printed `Droop quota = 4` while the count used 3.00. The information needed to configure the cross-check correctly did not exist in our own output. Fixing the header was not cosmetic; it was the precondition.

## What the third engine actually bought

Now the interesting half, and the reason "two engines agree" is a weaker claim than "three engines were compared."

Count the book club three ways — hand count at quota 4, our engine at 3.00, RCTab at 3.0001 — and every intermediate number moves while the seats never do:

| | hand count, quota **4** | ours, exact **3.00** | RCTab, exact **3.0001** |
|---|---|---|---|
| Austen keeps / passes on | 4 / 1 | 3 / 2 | 3.0001 / 1.9999 |
| transfer weight per ballot | 0.2 | 0.4 | 0.3999 |
| Brontë after the surplus | 2 | **3.00** — ties Camus | **2.9995** — just short |
| eliminations | Dickens, then Brontë | **none** | Dickens, then Brontë |
| second seat fills by | Camus climbs to 5 | Camus is the last hopeful left | Camus climbs to 5.9995 |
| **seats** | **Austen + Camus** | **Austen + Camus** | **Austen + Camus** |

Look at the eliminations row. Our engine is the odd one out — it finishes with **no elimination round at all**.

With two engines, the obvious reading is that the exact quota causes it: the bigger surplus lifts Brontë to exactly 3.00, she ties Camus, the seats fill, nobody is eliminated. That reading is wrong, and it was written into this library's pages for a day before RCTab contradicted it.

RCTab uses **the same exact quota** and eliminates normally. The difference is the epsilon. RCTab's bar sits at `V/(S+1) + 10⁻ᵈ` = 3.0001, so Austen keeps 3.0001, passes on 1.9999, and Brontë arrives at **2.9995** — strictly short of Camus, and duly eliminated in the ordinary way. `pyrankvote`'s bar is the bare `V/(S+1)` = 3.00, so Brontë arrives at *exactly* 3.00, ties Camus, and is disposed of by a "reject candidates who cannot change the result" shortcut rather than by elimination.

So there were **two forks stacked on top of each other**, and they had been read as one:

1. **Which quota** — `⌊V/(S+1)⌋+1` vs `V/(S+1)`. A rulebook question, documented, real, and the one this repo already knew about.
2. **How the bar is compared, and what happens at a dead tie** — `>` vs `≥`, an epsilon, and whether a candidate who cannot win is *eliminated* or *set aside*. An implementation question, undocumented, and invisible until a third implementation disagreed about it while agreeing about fork 1.

Two engines can only ever tell you *that* they differ. Three can tell you **which of two stacked causes** is responsible, because RCTab held the quota fixed and varied the tie handling — a controlled experiment nobody designed, available for the price of a second cross-check.

## What to take from it

- **A green tick is a claim about your configuration as much as about your arithmetic.** Record which settings made the comparison legitimate, next to the result. If the setting is not written down, the agreement is not reproducible.
- **Engines that agree on winners routinely disagree on everything else.** Seats are the least sensitive thing a tabulator produces. If a teaching page quotes an intermediate figure — a surplus, a transfer weight, a round-by-round standing — that figure belongs to *one* engine and should say so.
- **Prefer the count that is auditable to the count that is convenient.** RCTab writes its threshold, its tiebreaks and its transfers into an audit log because a jurisdiction has to defend them. Our engine's tie shortcut is a reasonable optimisation that appears nowhere in its output — and it is what produced the anomaly above.
- **Methods are math; implementations are software.** Both need testing. The [sole-survivor crash](bv_stv_sole_survivor_crash/README.md) was a bug in software that implements STV correctly on paper; the vanishing elimination round is a quirk of software that computes the right winner. Neither is a fact about single transferable vote.
- **Robustness is worth stating explicitly.** All ten STV elections here seat the same people under either quota, and agree with RCTab. That is a stronger sentence than "our engine says so," and it is the sentence a debater can actually use.

## Run it yourself

```bash
export RCTAB_HOME=/path/to/RCTab.app        # or an unpacked release
.venv/bin/python STARVote_LH_tabulation_engine/tools_adam/rctab_tabulation_engine/rctab_crosscheck.py 01_STAR/05_Practice/cases/ex14_two_novels.yaml
```

Add `--hand-count-quota` to count the same ballots under `⌊V/(S+1)⌋+1` and watch the middle column of that table turn into the left one. Tool, flags and findings: [`rctab_tabulation_engine/`](../../STARVote_LH_tabulation_engine/tools_adam/rctab_tabulation_engine/README.md).

---

*Up: [STV](README.md) · the engine: [RCTab](../../07_Concepts/tabulation_engines/rctab.md) · the drill: [exercise 14](../../01_STAR/05_Practice/ex14_transfer_machine.md) · the bug: [sole-survivor crash](bv_stv_sole_survivor_crash/README.md) · curriculum: [Voting 301](../../07_Concepts/curriculum/CURRICULUM_301.md)*

# file: three_engines_one_election.md
