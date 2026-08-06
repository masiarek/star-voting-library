# 05_Ranked_Robin/03_Criteria — where Ranked Robin is tested

Ranked Robin's usual answer is easy: whoever beats everyone head-to-head wins. This folder is about the cases that **probe** that — the strategic attack it is most vulnerable to, the defense it is best known for, and what happens at the edge where the rule runs out.

Same discipline as the STAR side: every claim is a runnable election, and the failures are shown as loudly as the passes. Prose companions live in [`01_Learn/`](../01_Learn/README.md).

| Set | What it shows |
|---|---|
| [Burial](burial/README.md) | **The signature strategic wart of Condorcet methods** — rank the frontrunner *last*, manufacture a cycle, win on the record. A sincere election a compromise wins cleanly, then the coordinated lie that takes it from her. (Side by side with Borda, STAR and IRV → [the burial topic hub](../../07_Concepts/topics/burial/README.md).) |
| [Clone independence](clone_independence/README.md) | **Ranked Robin's headline defense:** adding near-identical candidates shouldn't change the winner. The LH-only pair showing teaming on paper, then the BV-backed pair (BV2142/BV2143) where the engine and BetterVoting resolve the resulting cycle differently. |
| [Tie-breaks](rr_tiebreaks/README.md) | The edge: when Copeland scores tie, how the engine resolves it, and where that resolution **differs** from BetterVoting. |

---

**Related:** what the rule actually is → [02_Examples](../02_Examples/README.md) · the honest-limits prose → [Ranked Robin's limits](../01_Learn/RCV_RR_honest_limits.md) · cycle handling → [cycle resolution](../01_Learn/cycle_resolution.md).
