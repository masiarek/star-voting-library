# 05_Ranked_Robin / 02_Examples — the worked intro

**This folder holds the two starting cases — the intro election, taught on the [Ranked Robin front door](../README.md), and the tiny ballot-reading case behind [a blank is ranked last](../01_Learn/rr_blank_means_last.md).** In the intro election the consensus candidate that **plurality** overlooks wins the round-robin outright, because RR compares every pair head-to-head instead of counting only first choices. Its walkthrough lives on the front door (ballots, every matchup, the Copeland record, and the honest RCV-IRV footnote); here are the runnable files and their full reports.

| Case (page) | What it shows | src |
|---|---|:--:|
| [the consensus center wins](cases/cases_pages/ranked_robin_consensus_center.md) | RR elects the broadly-preferred center (3–0 head-to-head) over the two poles that hold more first choices | [`.yaml`](cases/ranked_robin_consensus_center.yaml) |
| [a blank is ranked last](cases/cases_pages/rr_blank_is_last_c4_b3.md) | RR reads only the preference order, never the rank number: a candidate ranked explicitly last and the same candidate left blank count identically (Dan loses every matchup 3–0 either way) | [`.yaml`](cases/rr_blank_is_last_c4_b3.yaml) |
| [the smallest round-robin](cases/cases_pages/ranked_robin_intro_c3_b7.md) | 3 candidates, 7 ballots — the first-choice leader (Ada, 3 of 7) finishes last and Ben wins 2–0; small enough that the whole report fits on a screen, which is why the [lesson](../01_Learn/ranked_robin.md) embeds it rather than pasting one | [`.yaml`](cases/ranked_robin_intro_c3_b7.yaml) |

Up: [05_Ranked_Robin — Ranked Robin (RCV-RR / Copeland)](../README.md) · the method taught: [Ranked Robin (RCV-RR)](../01_Learn/ranked_robin.md) · where RR and IRV genuinely part ways: [rr_vs_irv_plurality](rr_vs_irv_plurality/README.md) (the Tennessee center squeeze)

# file: README.md
