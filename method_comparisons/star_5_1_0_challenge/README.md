# Does STAR collapse to IRV under strategic "5-1-0" voting? — rb-j's challenge, counted

*Robert Bristow-Johnson (**rb-j**), a longtime Condorcet advocate and the analyst of [Burlington 2009](../burlington_2009/), posed a sharp challenge on r/EndFPTP: a rational STAR voter with preferences A > B > C will score **`A:5, B:1, C:0`** — and if everyone votes that way, STAR behaves like IRV and [center-squeezes](../center_squeeze/) the Condorcet winner the same way. This page takes the argument seriously, runs it, and reports what's true, what's overstated, and where the honest line is. Short version: **the mechanism is real — and his "the 1s contribute little" is not.***

→ Related: [strategic voting](../../00_start_here/topics/strategic_voting.md) · [favorite betrayal (301)](../../00_start_here/STAR_Voting/properties_and_limits/favorite_betrayal_voting_301.md) · [STAR's honest limits](../../00_start_here/STAR_Voting/properties_and_limits/STAR_honest_limits.md) · real cases: [Alaska 2022](../alaska_2022/), [Burlington 2009](../burlington_2009/).

**▶ Live on BetterVoting** (the 5-1-0 elections each carry a **STAR** race and an **RCV-IRV** race on the same voter preferences, side by side): sincere → **[results ↗](https://bettervoting.com/2kcwbw/results)** (`2kcwbw`, BV2221) · thin-moderate 5-1-0 → **[results ↗](https://bettervoting.com/rfyk46/results)** (`rfyk46`, BV2222) · real-moderate 5-1-0 → **[results ↗](https://bettervoting.com/dyh93j/results)** (`dyh93j`, BV2223).

---

## The argument (steelmanned)

You prefer **A**, you're fine with the moderate **B**, you loathe **C**. How should you fill in a STAR ballot?

- Give **A a 5** and **C a 0** — easy. The only question is B.
- In the automatic runoff, your B-vs-C preference is worth **exactly one vote** whether you scored B a 1 or a 4 — you can't give B *more* than "I prefer B to C." So **a 1 is all B needs** to beat C in a runoff that A doesn't reach.
- But raising B in the *scoring round* can bump B **past your own favorite A** into the runoff. If your goal is "A wins," you want A — not B — in that runoff, so you keep B as low as possible.

So the rational ballot is **5-1-0**: max your favorite, give the lesser-evil the *minimum* insurance, zero the enemy. rb-j's conclusion: score B higher **only** if you already fear A can't beat C but B can — which is exactly the [center-squeeze](../center_squeeze/) case. Under universal 5-1-0, "the first round cares essentially only about the top-scored ballot," so STAR's finalists are basically the first-choice leaders — and the broadly-liked moderate gets squeezed out, just like under IRV.

It's a tight argument. So we ran it.

## What the engine says

One 1-D electorate, **Beth is the Condorcet winner** (she beats Ana 52–48 and Cole 53–47), tabulated five ways:

| Electorate | Ballot | Method | Winner | CW elected? |
|---|---|---|:--:|:--:|
| **Thin moderate** (48 / 47 / 5) | sincere (poles score Beth a 3) | STAR | **Beth** | ✅ |
| Thin moderate | **strategic 5-1-0** | STAR | **Ana** (pole) | ❌ |
| Thin moderate | ranked | RCV-IRV | **Ana** (pole) | ❌ |
| **Real moderate** (40 / 35 / 25) | **strategic 5-1-0** | STAR | **Beth** | ✅ |
| Real moderate | ranked | RCV-IRV | **Ana** (pole) | ❌ |

Watch the scoring round do the work.

**Sincere STAR** ([`s1`](cases/bv2221_2kcwbw_sincere.yaml)) — the poles genuinely rate the moderate a 3, so she leads:

```
Scoring Round:  Beth 310 · Ana 250 · Cole 235   → Beth & Ana advance
Automatic Runoff:  Beth 52 vs Ana 48            → Beth wins  (the Condorcet winner)
```

**Strategic 5-1-0, thin moderate** ([`s2`](cases/bv2222_rfyk46_510_thin_star.yaml)) — now the moderate gets only 1s from the poles and collapses below both:

```
Scoring Round:  Ana 245 · Cole 235 · Beth 120   → Ana & Cole advance  (Beth squeezed out)
Automatic Runoff:  Ana 53 vs Cole 47            → Ana wins  (a pole — NOT the CW)
```

That is **identical** to RCV-IRV on the same electorate ([`s3`](cases/bv2222_rfyk46_510_thin_irv.yaml)): Beth has the fewest first-choices (5), is eliminated first, and Ana wins 53–47. **So rb-j's core claim is confirmed:** under coordinated 5-1-0 with a thin moderate base, STAR center-squeezes exactly like IRV — and yes, [Burlington 2009](../burlington_2009/) or [Alaska 2022](../alaska_2022/) voted 5-1-0 would fail under STAR too. We don't dodge that; it's ["strategy-resistant, not strategy-proof"](../../00_start_here/topics/strategic_voting.md) made concrete.

## Where the argument overstates itself

The claim that carries all the weight is *"the 1 scores contribute little."* **They don't.** Give the moderate a **real first-choice base** and run the *identical* 5-1-0 strategy ([`s4`](cases/bv2223_dyh93j_510_real_star.yaml)):

```
Scoring Round:  Ana 225 · Beth 200 · Cole 175   → Ana & Beth advance  (Beth made it — on 1s)
Automatic Runoff:  Beth 60 vs Ana 40            → Beth wins  (the Condorcet winner)
```

Beth's 75 "insignificant" 1s (plus her 25 fives) lifted her to 200 — past Cole — and into a runoff she wins. **Under the same strategic ballot, STAR elects the Condorcet winner here while RCV-IRV eliminates her** ([`s5`](cases/bv2223_dyh93j_510_real_irv.yaml) → Ana, 65–35). So:

**"Everyone votes 5-1-0 ⇒ STAR = IRV" is false as a general statement.** 5-1-0 STAR fails only in a *sub-region* — a moderate whose base is thin enough that even the pooled 1s can't lift them past a pole. Outside that region the 1s carry real weight, and 5-1-0 STAR is strictly **more** moderate-friendly than IRV. STAR degraded-by-strategy is still not IRV.

## The honest bottom line

- **Conceded, squarely:** STAR is not strategy-proof (no method is — Gibbard). Under *coordinated* 5-1-0 min-max voting **and** a thin moderate base, STAR can fail the Condorcet winner just as IRV does. rb-j is right about the mechanism.
- **But it's a strategic-equilibrium argument, not a sincere-ballot one.** On sincere ballots STAR elects the CW ([`s1`](cases/bv2221_2kcwbw_sincere.yaml)); the failure needs universal coordination on min-max, a thin moderate base, *and* accurate anticipation of who can beat whom. Misjudge it and 5-1-0 backfires — starving a moderate you needed can hand the seat to the candidate you loathe.
- **And the "1s are noise" premise is wrong** ([`s4`](cases/bv2223_dyh93j_510_real_star.yaml)): they lift moderates into runoffs, which is precisely why STAR ≠ IRV even under the strategic ballot.
- **The 0-5-0 escalation** rb-j floats (bullet-vote the moderate, abandon your doomed favorite) is [favorite betrayal](../../00_start_here/STAR_Voting/properties_and_limits/favorite_betrayal_voting_301.md) — which STAR permits and doesn't deny. But it demands even more information and coordination, and the [FBC simulation](../../06_Other/simulations/) finds attempted betrayal **backfires ~98% of the time** under STAR. "You *can* betray your favorite" and "betrayal *pays*" are different claims; STAR's case rests on the second being rare.

So the fair verdict: rb-j has found a genuine edge of STAR's strategy space and named it precisely — credit to him. What the counting adds is the boundary of that edge (thin base only) and the correction that STAR-under-5-1-0 is *IRV-like, not IRV-identical*. The Condorcet answer — "just always elect the CW" — carries its own bill: cycles need a completion method (there's no canonical one), and the CW can be a weakly-supported compromise. That's a values trade, honestly stated, not a knockout for either side.

## The runnable cases

| File | Electorate · ballot | Method | → |
|---|---|---|---|
| [`s1`](cases/bv2221_2kcwbw_sincere.yaml) | thin moderate · sincere | STAR | Beth (CW) |
| [`s2`](cases/bv2222_rfyk46_510_thin_star.yaml) | thin moderate · 5-1-0 | STAR | Ana |
| [`s3`](cases/bv2222_rfyk46_510_thin_irv.yaml) | thin moderate · ranked | RCV-IRV | Ana |
| [`s4`](cases/bv2223_dyh93j_510_real_star.yaml) | real moderate · 5-1-0 | STAR | Beth (CW) |
| [`s5`](cases/bv2223_dyh93j_510_real_irv.yaml) | real moderate · ranked | RCV-IRV | Ana |

*Source of the argument: rb-j (Robert Bristow-Johnson), r/EndFPTP, "the restricted case of 3 significant candidates" (2026). Cast renamed (Ana/Beth/Cole) for a clean spatial example; Beth is the center. Every winner above is the engine's, reproducible from the files. BetterVoting's own STAR and IRV counts **agree on every race** (frozen `_bv_export.json` beside the yamls) — including `dyh93j`, where the same 5-1-0 ballots elect **Beth under STAR yet Ana under IRV**, live.*
