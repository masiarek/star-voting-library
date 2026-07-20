# Even Condorcet methods can be buried — Alaska 2022, and why the completion method matters

*rb-j (Robert Bristow-Johnson), arguing the Condorcet case on r/EndFPTP, walked through a **burial** attack on the real [Alaska 2022](../alaska_2022/) numbers: a bloc of Peltola voters insincerely rank the Condorcet winner **Begich** last, manufacturing a cycle to knock him out. His own honest finding — which this page reproduces and verifies — is that **the attack's success depends entirely on the completion method.** Margin-based Condorcet methods (MinMax, Schulze, Ranked Pairs) shrug it off; a runoff/Hare completion falls for it. The deeper lesson is the even-handed one this repo keeps landing on: **no method is strategy-proof — not even Condorcet.***

→ Related: [Alaska 2022 (the honest case)](../alaska_2022/) · [the 5-1-0 challenge](../star_5_1_0_challenge/) (STAR's strategy edge) · [strategic voting](../../00_start_here/topics/strategic_voting.md) · [Gibbard–Satterthwaite](../../00_start_here/topics/gibbard_satterthwaite_theorem.md) · [Condorcet](../../00_start_here/topics/condorcet/) · [burial vs Ranked Robin](../../05_Ranked_Robin/burial/).

---

## Sincere: Begich is the Condorcet winner

The real Alaska special, reduced to a faithful 200-voter model (Peltola / Begich / Palin), as ranked ballots ([`alaska_sincere`](cases/alaska_sincere_c3_b200.yaml)). Head-to-head:

```
Begich  beats Peltola  +9
Begich  beats Palin    +39
Peltola beats Palin    +4
→ Begich is the Condorcet winner
```

Every Condorcet method elects **Begich**. Only **RCV-IRV** elects **Peltola** — it eliminates Begich first for having the fewest first-choices ([the center squeeze](../../00_start_here/RCV_IRV/RCV_IRV_center_squeeze.md); the whole point of the [Alaska case](../alaska_2022/)).

## The burial: 20 voters rank the winner last

Now the attack. Of the 50 sincere `Peltola > Begich > Palin` voters, **20 bury Begich** — insincerely voting `Peltola > Palin > Begich` ([`alaska_buried`](cases/alaska_buried_c3_b200.yaml)). Peltola is still their favorite; they've only pushed Begich beneath Palin to sabotage him. That one move flips a single pairwise:

```
Begich  beats Peltola  +9      (unchanged)
Peltola beats Palin    +4      (unchanged)
Palin   beats Begich   +1      ← was Begich +39; the burial flipped it
→ cycle: Begich > Peltola > Palin > Begich, no Condorcet winner
```

## The completion methods split (verified with `pref_voting`)

| Method | Sincere | **Buried** |
|---|:--:|:--:|
| **MinMax** (margins) | Begich | **Begich** ✅ resists |
| **Ranked Pairs** (margins) | Begich | **Begich** ✅ resists |
| **Schulze** (beat-path) | Begich | **Begich** ✅ resists |
| **Condorcet-Hare / Top-Two-Runoff** | Begich | **Peltola** ❌ burial wins |
| RCV-IRV (plain, no Condorcet check) | Peltola | Peltola |

Why the margin-based methods hold: in the manufactured cycle, the **weakest defeat is Palin's +1 over Begich** — exactly because the buriers only *barely* dragged Begich under Palin. MinMax, Schulze, and Ranked Pairs all discard that weakest link, so Begich still wins and **the strategy backfires** (its cost: 20 voters risked helping elect Palin). But **Condorcet-Hare / TTR** — when no Condorcet winner exists, run a top-two/IRV among the survivors — eliminates Begich for his thin first-choice count and hands the seat to **Peltola**: the burial succeeds.

## The honest bottom line

- **Conceded — and it's rb-j's own point:** Condorcet methods are **not strategy-proof.** Burial can manufacture a cycle to unseat the Condorcet winner. That's [Gibbard](../../00_start_here/topics/gibbard_satterthwaite_theorem.md) again — *every* deterministic method is manipulable, Condorcet included. So "just elect the Condorcet winner" is not a clean escape from strategy; it relocates the strategy to *cycle creation*.
- **The completion method is the whole ballgame.** Among Condorcet methods, **margin-based completion (MinMax/Schulze/Ranked Pairs) is markedly more burial-resistant** than a Hare/runoff completion — because a burial that only *just* creates a cycle leaves a tell-tale weak defeat the margin methods throw out. If you're going to run a Condorcet method, this is a real argument for the margin-based ones.
- **Keep it in proportion.** Real honest cycles are **very rare** — by FairVote's own count, about **2 of ~500** RCV elections. And burial is *risky*: misjudge the margins and you elect your less-preferred candidate. This is a reason to *choose the completion method well*, not a reason to fear Condorcet methods — just as STAR's [5-1-0 edge](../star_5_1_0_challenge/) is a strategy sub-region, not a reason to fear STAR. Every method has its strategic seam; honesty is naming them and their bounds.

## Reproduce it

```
# RCV-IRV (both -> Peltola), via the LH engine:
python3 STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/condorcet_burial_alaska/cases/alaska_buried_c3_b200.yaml
# The Condorcet completion methods (MinMax/Schulze/Ranked Pairs/Hare) are verified
# with pref_voting — the sincere→Begich, buried→{Begich for margins, Peltola for Hare}
# split above is its output.
```

*Source of the argument: rb-j (Robert Bristow-Johnson), r/EndFPTP, on the Alaska August 2022 special. Numbers reduced ~943:1 to a 200-voter teaching model (the same faithful profile as [alaska_2022](../alaska_2022/), after Graham-Squire & McCune); the burial threshold (20 of 50) and every completion-method winner were verified with the LH engine and `pref_voting`.*
