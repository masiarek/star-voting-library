# IRV Non-Monotonicity — When *More* Support Makes You Lose

**One line:** under **RCV-IRV**, giving the eventual winner **more** first-choice support can cause them to **lose** — and moving a loser **down** can make them **win**. This isn't a glitch; it's baked into eliminate-and-transfer.

> **Applies to:** [Hare](RCV-IRV-Hare.md) **and the other sequential-elimination variants** — [BTR](variants/RCV-IRV-BTR.md), [Coombs](variants/RCV-IRV-Coombs.md), and [Baldwin/Nanson](variants/RCV-IRV-Baldwin-Nanson.md) are non-monotonic too, because *eliminate-and-transfer* is the cause. (So this is **not** Hare-specific the way [center squeeze](RCV_IRV_center_squeeze.md) is.) The non-eliminating Condorcet methods like [Ranked Robin](../RCV_Ranked_Robin/ranked_robin.md) are **monotonic**. See [Which RCV-IRV?](variants/RCV_IRV_variants.md).

> Why this page matters: most people are never told this. "Rank your honest favorite first, it can't backfire" is the core promise of IRV — and non-monotonicity is the case where that promise breaks. It's the single most underappreciated structural problem with the method.

→ STAR doesn't have this failure — see [`STAR is monotone`](../STAR_Voting/properties_and_limits/STAR_monotonicity.md). Glossary: [`monotonicity`](../GLOSSARY.md).

---

## What "monotone" means

A voting method is **monotone** if **ranking a candidate higher can never cause them to lose**, and ranking them lower can never cause them to win. It's the most basic sanity check you'd expect from any election: support should help, not hurt.

**RCV-IRV fails it.** STAR (and any additive, summable method) passes it.

## Why IRV fails it

IRV doesn't add support up — it **eliminates** the candidate with the fewest first-choices, round by round, and transfers their ballots. The winner depends entirely on **who gets eliminated, and in what order.**

That's the trap: changing how many first-choices a candidate has changes *who is eliminated first* — which changes *who their ballots transfer to* — which can flip the final result **backwards**. Adding support to your favorite can knock out the opponent who would have lost to them, leaving behind the opponent who beats them.

## Worked example — run it yourself

The classic 3-candidate case, as two elections that differ by **one change**: 4 voters raise X from second to first.

→ [`monotonicity_irv_before.yaml`](../../method_comparisons/monotonicity/cases/monotonicity_irv_before.yaml) · [`monotonicity_irv_after.yaml`](../../method_comparisons/monotonicity/cases/monotonicity_irv_after.yaml)

```
BEFORE                              AFTER  (4 voters raise X: Y>Z → X>Y)
  12: X>Y                             16: X>Y
  12: Y>Z                              8: Y>Z
  10: Z>X                             10: Z>X
R1: X12  Y12  Z10  → Z eliminated    R1: X16  Y8  Z10  → Y eliminated
    Z>X transfers → X 22             Y>Z transfers → Z 18
    ✅ X WINS                          ❌ X LOSES — Z wins
```

X went from **12 first-choices and a win** to **16 first-choices and a loss** — and *nothing else changed*. The four extra first-place votes for X eliminated Y instead of Z; Y's ballots flowed to Z; Z then beat X. (Verified on the RCV-IRV engine: X elected with 22 before, Z elected with 18 after.)

## How often does this happen? Not rare

- A spatial-model study (**Ornstein & Norman, *Public Choice* 2014**) estimates a **lower bound of ~15%** monotonicity failure in *competitive* three-candidate IRV races — and the rate climbs as the race gets closer. This is a structural hazard of elimination, not a freak coincidence.

## Two real-world flavors (both have happened — and both are runnable here)

Per a study of US RCV-IRV elections 2004–2022 (Graham-Squire & McCune, arXiv 2301.12075). Each has a dedicated page with a **before/after pair you can run** and the Ranked Robin contrast:

- **Upward paradox ("more is less") — [Alaska 2022 (US House special)](../../method_comparisons/monotonicity/upward_monotonicity_alaska.md).** Had ~6,000 Palin-only voters instead ranked the *winner* Peltola first, Peltola would have **lost** — those extra first-place votes eliminate Palin first, and Begich then beats Peltola. Raising the winner defeats the winner. (Ranked Robin elects the Condorcet winner Begich both times, unmoved.)
- **Downward paradox ("less is more") — [San Francisco 2020 (D7 Supervisor)](../../method_comparisons/monotonicity/downward_monotonicity_sf.md).** Shifting the *loser* Engardio **down** on ~800 ballots would have made him **win** — the shift eliminates Melgar first (by 3 votes), and Engardio then beats Nguyen. Less support, more victory. (Ranked Robin elects the Condorcet winner Melgar both times.)

(See also the [Alaska 2022 case study](case_studies/RCV_IRV_alaska_2022.md) for the full election.)

## A textbook real election

**Burlington, VT 2009 (mayor).** Kiss won, but the result was **non-monotonic** — and it was also a [center squeeze](RCV_IRV_center_squeeze.md): the Condorcet winner Montroll (who beat every rival head-to-head) was eliminated early. Voters who ranked Kiss *lower* could have made him win. Burlington **repealed IRV in 2010** over this race.

## A sharper critique — and where it overreaches (reading advocacy critically)

A well-known argument from **rangevoting.org** ([*"The logic behind IRV is flawed"*](https://www.rangevoting.org/IrvLogicBogus.html), after Blake Cretney) puts the point aggressively: IRV advocates spend their breath arguing that *most* first-choices ≠ best — then, without justification, IRV *eliminates* on *fewest* first-choices, as if fewest first-choices = worst. And IRV is "not self-consistent": use IRV to pick who to eliminate and you can eliminate the IRV *winner*. Range/Score voting, by contrast, **is** self-consistent — drop the lowest-scored candidate and the score winner still wins.

**The kernel is right — and this page is the proof.** IRV's fewest-first-choices elimination *is* the mechanical root of center squeeze and non-monotonicity, and there's a genuine tension between IRV's anti-plurality rhetoric and its plurality-based first cut. We agree, and demonstrate it above.

**But it overreaches three ways, and the fairness cuts our way too:**
- **It strawmans IRV's premise.** IRV doesn't claim "fewest first-choices = worst"; it claims "fewest *current* support can't win *this round*, so transfer those voters' next preference" — ordinary runoff logic. The *result* can still cut the best candidate (the valid complaint), but that's not what IRV *asserts*.
- **"Not self-consistent" is a method-class distinction, not "bogus logic."** Self-consistency is a property of **additive** methods (drop the lowest total, the winner's total is untouched); elimination methods lack it because eliminating a candidate *transfers* votes. That's an argument *for* additive methods, not proof IRV is irrational.
- **The "magician's trick" framing** imputes deliberate deception — polemic, not argument.

**Disclose the lean:** rangevoting.org is **Warren Smith / the Center for Range Voting** — the most aggressive pro-**Range** advocacy source (advocacy-adjacent; strong for mechanics, weak for verdicts — see [how to read the sources](../topics/how_to_learn_about_voting_methods.md)). And note it cuts against **STAR** as well: STAR's *scoring round* is additive/self-consistent, but its **runoff** is a non-additive pairwise step, so a Range purist levels the same charge at STAR. This isn't a pro-STAR argument — it's a Score-maximalist jab at *every* method with an elimination or runoff. We include it because the library checks pro-Range anti-IRV arguments by the same standard it checks the [pro-RCV ones](../../method_comparisons/fairvote_star_whitepaper/).

## Don't confuse it with Later-No-Harm

A frequent mix-up: **monotonicity** asks "can *raising* a candidate ever hurt them?" **Later-No-Harm** asks "can adding a *lower* preference ever hurt your *top* choice?" They're different criteria. IRV **passes** Later-No-Harm but **fails** monotonicity; STAR is the opposite shape. (Worked out in [Favorite Betrayal — Does *Only* RCV Avoid It?](../STAR_Voting/properties_and_limits/favorite_betrayal_voting_301.md).)

→ More source notes: **RCV-IRV monotonicity** group in [LINKS — source-of-truth registry](../LINKS.md).

Sources: [Ornstein & Norman 2014 (Public Choice)](https://link.springer.com/article/10.1007/s11127-013-0118-2), [Graham-Squire & McCune, RCV in the US 2004–2022 (arXiv)](https://arxiv.org/pdf/2301.12075.pdf), [Burlington 2009 (Wikipedia)](https://en.wikipedia.org/wiki/2009_Burlington_mayoral_election), [monotonicity criterion (Wikipedia)](https://en.wikipedia.org/wiki/Monotonicity_criterion).
