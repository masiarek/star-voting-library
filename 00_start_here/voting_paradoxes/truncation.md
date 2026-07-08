# The Truncation paradox — when ranking less gets you more

*The **Truncation paradox** (preference-truncation): a voter obtains a **better** outcome by ranking only some of the candidates than by revealing their full, sincere ordering.* (A **conditional** paradox in Felsenthal's taxonomy: the one changed datum is how much of the ballot a group of voters fills in.)

→ Glossary: [`truncation`](../GLOSSARY.md) · Felsenthal's taxonomy: [README](README.md)

## The live demonstration (a pair of elections)

Nurmi's example (Felsenthal 2010, §A6, Example 16), run for real: [BV2162](../../method_comparisons/felsenthal_paradoxes/bv2162_4htk44_nurmi_truncation.md) — 103 voters rank all four candidates and RCV-IRV elects **A** (missing the Condorcet winner B). [BV2163](../../method_comparisons/felsenthal_paradoxes/bv2163_74j6vv_nurmi_truncation.md) — the 17 `D>C>B>A` voters rank **only D**; their exhausted ballots change the elimination order and **B** wins, whom they prefer to A. Honesty cost them; silence paid.

The paradox strikes other counting families too, each through its own machinery: **Borda** — [BV2160 (Fishburn's example)](../../method_comparisons/felsenthal_paradoxes/bv2160_r6qc8h_fishburn_borda_truncation.md), where truncating a rival denies them points (worked on paper; no Borda tabulator on BV/LH); **successive elimination** — [Example 12's worked table](successive_elimination.md); and it lurks in [BV2159 (Brams' IRV sampler)](../../method_comparisons/paradoxes_and_whoops/bv2159_f4cjpy_brams_irv_pathologies.md).

## Where it comes from

Truncation is powerful wherever a ballot's lower ranks can *hurt* its upper ranks. Under RCV-IRV a lower preference becomes a live vote once transfers reach it — in BV2162 the 17 voters' second choice (C) soaked up their transfers and thereby shielded A from elimination-order justice; withholding it let C die early. Under Borda every listed rival collects points from your ballot, so leaving a strong rival unranked is a direct attack. Pairwise (Ranked Robin) and score (STAR) counting are far more truncation-resistant — on the Nurmi pair both elect B with full *and* truncated ballots — though no ranked method is perfectly immune in all profiles.

## Why it matters

"Rank as many as you like — more information helps" is the standard advice on ranked ballots. A method where the strategically savvy *shorten* their ballots turns ballot completion into a sucker's move, and it biases outcomes toward factions with better strategic coordination. Note the practical echo: real RCV-IRV elections show heavy truncation, and this paradox says some of it may be rational.
