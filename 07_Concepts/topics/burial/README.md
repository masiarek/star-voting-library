# Topic: Burial (sinking a rival you actually like)

**Topic hub — a cross-method view.** Burial is voting a strong rival **below candidates you honestly prefer less**, to knock them out of a comparison they would otherwise win. Your favorite stays on top — that's what separates burial from favorite betrayal — so it feels like a free move, and the whole question is whether the count lets it pay.

> **The one idea to take away:** *burial is not Ranked Robin's private wart.* It is the strategy available against **any** method that reads a rival's position relative to other candidates — Condorcet, Borda, and (in its score form) STAR. What differs is the price: how many voters must coordinate, how much they risk, and — for the Condorcet family — **which completion rule** the count uses when the burial manufactures a cycle. The method that most nearly escapes it is the one this library criticizes most, **RCV-IRV**, and it escapes for an unflattering reason: it doesn't read your lower ranks at all until your higher ones are eliminated.

In the [Equal Vote taxonomy of insincere votes](../strategic_voting.md#the-four-kinds-of-insincere-vote), burial is **weak insincerity** — it distorts the *order* of candidates you don't lead with, while [favorite betrayal](../../../01_STAR/01_Learn/properties_and_limits/favorite_betrayal_voting_301.md) (strong insincerity) distorts the top of the ballot. Formally, a method is open to burial only if it fails **[later-no-harm](../../GLOSSARY.md)**: if a lower ranking can never hurt your favorite, moving a rival down can never help them either.

## Which methods it works on — and where each is treated

| Method | Buriable? | Why | Full page |
|--------|:---:|-----|-----------|
| **Ranked Robin / Copeland** | ❌ yes — its named risk | purely ordinal: sink a rival below weaker candidates and a matchup flips, often manufacturing a cycle the record-tiebreak then settles | [RR honest limits §3](../../../05_Ranked_Robin/01_Learn/RCV_RR_honest_limits.md#3-fails-later-no-harm-open-to-burial) · [the worked pair](../../../05_Ranked_Robin/03_Criteria/burial/README.md) |
| **Margin-based Condorcet** (Minimax, Ranked Pairs, Schulze) | ⚠️ harder | they read *how much* each matchup was won by, so a thin manufactured cycle is resolved on numbers the buriers can't cheaply fake | [Alaska 2022, buried](../../../method_comparisons/condorcet_burial_alaska/README.md) · [Minimax](../../voting_paradoxes/minimax.md) |
| **Borda** | ❌ yes, notoriously | every rank is worth points, so burying is plain arithmetic — the classic **Dark Horse** | [The Dark Horse](../../../method_comparisons/dark_horse_borda/README.md) |
| **STAR** | ⚠️ possible, rarely pays | fails later-no-harm, so scoring a strong second 0 can help your favorite reach the runoff — but the runoff can then hand the win to the candidate you buried | [STAR's honest limits](../../../01_STAR/01_Learn/properties_and_limits/STAR_honest_limits.md) · [criteria failures](../../../01_STAR/01_Learn/properties_and_limits/star_criteria_failures.md) · [FAQ](../../../01_STAR/01_Learn/getting_started/STAR_FAQ.md#q-does-star-fail-later-no-harm-should-i-bury-a-strong-second-choice) |
| **RCV-IRV (Hare)** | ✅ largely no | satisfies later-no-harm — your 3rd choice is never read while your 1st is alive, so there's nothing to gain by mis-ordering below the top. IRV's exposure is *compromising* and [center squeeze](../center_squeeze/) instead | [Which RCV-IRV?](../../../06_Other/RCV_IRV/concepts/variants/RCV_IRV_variants.md) |
| **Approval / Score** | ✅ n/a (Approval) | Approval has no order to invert; withholding support is [bullet voting](../../../04_Approval/01_Learn/approval_honest_limits.md), a different strategy with a different cure | [Approval's honest limits](../../../04_Approval/01_Learn/approval_honest_limits.md) |

The pattern worth naming: **later-no-harm and Condorcet compliance can't both be had** (a small impossibility result you can feel here). IRV buys burial-resistance by ignoring most of your ballot; Condorcet methods buy the head-to-head winner by reading all of it, and pay for that with burial. STAR sits between, and pays a smaller price than either.

## Runnable here — burial worked on four different methods

| Case | Method attacked | What it shows |
|---|---|---|
| [Burial in Ranked Robin — the sincere/buried pair](../../../05_Ranked_Robin/03_Criteria/burial/README.md) | Ranked Robin | 15 of 42 voters rank the Condorcet winner last, manufacture a cycle, and win the record tie ([sincere](../../../05_Ranked_Robin/03_Criteria/burial/cases/cases_pages/bv2208_7q6by8_burial_sincere.md) · [buried](../../../05_Ranked_Robin/03_Criteria/burial/cases/cases_pages/bv2209_fxhw6g_burial_pays.md)) — triple-checked, deterministic on both engines |
| [Even Condorcet methods can be buried — Alaska 2022](../../../method_comparisons/condorcet_burial_alaska/README.md) | Condorcet, on real numbers | rb-j's attack on the actual Alaska special: bury Begich, manufacture a cycle. **The attack's success depends entirely on the completion method** — margin-based rules shrug it off, a Hare/runoff completion falls for it ([buried ballots](../../../method_comparisons/condorcet_burial_alaska/cases/cases_pages/alaska_buried_c3_b200.md)) |
| [Manipulability — the textbook P₃ profile](../../../method_comparisons/manipulability_p3/README.md) | Copeland *and* STAR | Zwicker's own illustration of single-voter manipulability is an attack on Copeland; the page runs the same profile against STAR, where [two voters bury their 4th choice](../../../method_comparisons/manipulability_p3/cases/cases_pages/p3_manip_star.md) and elect their favorite, and against [a milder no-burial variant](../../../method_comparisons/manipulability_p3/cases/cases_pages/p3_manip_compromise_rr.md) |
| [FairVote's white-paper burials](../../../method_comparisons/fairvote_star_whitepaper/README.md) | STAR (score burial) | the critics' own constructions, reproduced: [Washington 2010](../../../method_comparisons/fairvote_star_whitepaper/cases/cases_pages/bv2232_24b623_wa_2010_burial.md) — *the squeeze works on STAR, but IRV resists it* — and [French 2017](../../../method_comparisons/fairvote_star_whitepaper/cases/cases_pages/bv2230_2hqmrd_french_2017_burial.md), where every faction scores Macron 0 |

## What a burial actually costs

Every page above lands on the same three facts, which is why this library treats burial as a **real but expensive** attack rather than a routine one:

- **It needs a large, disciplined bloc sitting inside the victim's majorities.** In the Ranked Robin pair that's 15 of 42 voters — over a third of the electorate — coordinating, with decent polling, and willing to rank a candidate they genuinely like dead last.
- **It backfires when mis-aimed.** Bury into the wrong cycle and you elect the buriers' *third* choice. In STAR the buried candidate can simply win the runoff you pushed them into.
- **It leaves fingerprints.** Sincere ballots showed no cycle; the buried ballots do. A cycle appearing in a race whose polling showed a clear head-to-head winner *is* the anomaly, and the printed round-robin table is where an auditor would catch it.

And the even-handed framing this repo keeps returning to: **no method is strategy-proof** — [Gibbard–Satterthwaite](../gibbard_satterthwaite_theorem.md) forbids it. The honest comparison isn't "which method has no wart," it's *which warts are systematic and which need a heist*. Burial is a heist. Center squeeze is a Tuesday.

Closely related: [strategic voting](../strategic_voting.md) (the four-kinds taxonomy) · [the five strategic pathologies](../strategic_pathologies.md) (where the Dark Horse row hides this mechanism) · [center squeeze](../center_squeeze/) (IRV's systematic wart, the contrast case) · [cycle resolution](../../../05_Ranked_Robin/01_Learn/cycle_resolution.md) (what happens after a burial succeeds) · [the Smith set](../smith_set.md). Glossary: [`burial (weak insincerity)`](../../GLOSSARY.md).

---

*This is a **topic hub** (cross-method index). The authoritative write-ups live in the per-method folders linked above. See [the topics index](../) for the other topic hubs.*

# file: README.md
