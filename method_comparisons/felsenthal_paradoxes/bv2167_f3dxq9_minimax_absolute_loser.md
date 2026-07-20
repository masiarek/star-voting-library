# BV2167 — Minimax elects the absolute loser: losing to everyone, narrowly

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/f3dxq9) · **[results ↗](https://bettervoting.com/f3dxq9/results)** (election `f3dxq9`).

11 voters, four candidates. **D loses every single head-to-head 5–6** and a majority rank D dead last — yet the Condorcet/Minimax procedure elects **D**, because D's *worst* loss is the *smallest*. The sharpest "wrong winner" in Felsenthal's whole appendix. Live races: **STAR → B**, **Choose-One → D** (agreeing with Minimax, for opposite reasons).

## Source

Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / LSE, revised 26 May 2010; Appendix §A10 ("Demonstrating Paradoxes Afflicting the Condorcet (aka Minimax or Simpson-Kramer) Procedure"), **Example 29**. Full §A10 treatment: [minimax.md](../../00_start_here/voting_paradoxes/minimax.md).

## The election

```
No. of voters    Preference ordering
      2          D > A > C > B
      3          D > B > A > C
      3          C > B > A > D
      1          B > A > C > D
      2          A > C > B > D
```

Pairwise: **B>A 7–4, A>C 8–3, C>B 7–4** — a top cycle among A, B, C — and **D loses to each of them 5–6**. D is the Condorcet loser *and* the absolute loser (ranked last by 6 of 11).

## Minimax, worked (the paper paradox)

With no Condorcet winner, Minimax elects the candidate whose **worst pairwise loss margin is smallest**: A's worst is 7 (vs B), B's is 7 (vs C), C's is 8 (vs A) — and **D's is 6** (all three losses). **D elected.** Losing to everyone *narrowly* beats winning twice and losing once *badly* — the [Condorcet loser](../../00_start_here/voting_paradoxes/condorcet_loser_paradox.md) and [absolute loser](../../00_start_here/voting_paradoxes/absolute_loser_paradox.md) paradoxes inside a genuine Condorcet method. Contrast **Copeland** (Ranked Robin's rule, most pairwise *wins*): D has zero wins and can never top a Copeland count — the two cycle-breakers differ in kind, not taste (see [cycle_resolution.md](../../00_start_here/RCV_Ranked_Robin/cycle_resolution.md)).

## Agreement

| Race | BetterVoting | LH engine | Agree? |
|---|---|---|---|
| STAR (5/4/2/1 map: 34/35/32/31; runoff B beats A 7–4) | **B** | B | ✓ |
| Choose-One (Plurality) | **D** (5 of 11) | D | ✓ |
| Minimax *(paper only)* | — | D (worst loss 6 vs 7/7/8) | n/a |

Choose-One and Minimax converge on the absolute loser from opposite directions — one counts only D's five committed fans, the other only D's narrow defeats. STAR elects a top-cycle member. No Ranked Robin race (the A/B/C Copeland tie → BV random) and no IRV race (a random transfer tie), per the freezability rule.

Files: [star yaml](cases/bv2167_f3dxq9_star.yaml) · [plurality yaml](cases/bv2167_f3dxq9_plurality.yaml) · [frozen export](cases/bv2167_f3dxq9_bv_export.json) · mirrors: [star](cases/cases_tabulated/bv2167_f3dxq9_star_tabulated.txt), [plurality](cases/cases_tabulated/bv2167_f3dxq9_plurality_tabulated.txt).
