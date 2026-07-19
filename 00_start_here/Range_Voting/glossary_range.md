# Glossary — Range / Score Voting

Method-specific terms for **Range (Score)** voting. Shared, cross-method vocabulary lives in the [main glossary](../GLOSSARY.md).

- **Range / Score voting** — grade each candidate on a fixed scale (e.g. 0–5); the highest **total score** wins. No runoff, no elimination. STAR's score round without the automatic runoff; Approval at more than 1 bit. → [Range / Score Voting](range_voting.md); engine [the Range engine](../../06_Other/Range/Range_tabulation_engine/)
- **Exaggeration / min-max strategy** — Range's central weakness: a voter often does best giving only max/min, which collapses Range toward Approval. STAR adds the runoff specifically to make honest scoring safer.
- **Scale granularity** — how many rungs the scale offers (0–5 vs 0–9…). When top contenders are bunched, the granularity can change the winner. → [Scale granularity can flip the winner (a 301 case)](../scores_and_ranks/scale_granularity_flips_the_winner.md)

*Range is a non-EVC method (this library teaches it for honest comparison). Shared criteria — monotonicity, the Majority criterion, the Equal Vote criterion — are in the [main glossary](../GLOSSARY.md#properties-criteria).*

# file: glossary_range.md
