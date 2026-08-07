# 06_Other/RCV_IRV — RCV-IRV: the ranked ballot, counted by instant runoff

*Rank the candidates 1st, 2nd, 3rd… then count in rounds — eliminate the last-place candidate and transfer their ballots, until someone holds a majority of what's still active.*

<img src="img/rcv_irv_ballot_example.png" width="460" alt="A Ranked Choice Voting ballot: five candidates — Andre, Blake, Carmen, David, Ella — in rows, with columns 1st through 5th and exactly one bubble filled per row. This voter ranked Andre 1st, Carmen 2nd, David 3rd, Blake 4th and Ella 5th. Instructions at top: rank candidates in order of preference; equal ranks are not allowed; candidates left blank are ranked last. Footer: votes are counted in rounds; a candidate with a majority of remaining votes is elected, otherwise the candidate with the fewest votes is eliminated; in each round your vote goes to the remaining candidate you ranked highest; if your vote is unable to transfer, it is discarded.">

*The ballot ([Equal Vote](https://www.equal.vote/voting_methods)) — the same five candidates as the [STAR](../../01_STAR/README.md), [Approval](../../04_Approval/README.md) and [Ranked Robin](../../05_Ranked_Robin/README.md) ballots, so the four can be read side by side. Two printed lines carry most of what the pages below argue about. **"Equal ranks are not allowed"** — the very same ranked paper, counted by Ranked Robin, lets you rank two candidates equally; that restriction is IRV's, not the ballot's. And the footer's closing sentence, **"If your vote is unable to transfer, it is discarded"** — [exhausted ballots](concepts/RCV_IRV_exhausted_ballots.md), conceded on the ballot itself, and the reason IRV's "majority" is a majority of the ballots still active rather than of everyone who voted.*

A basic runnable RCV-IRV election and the vendored `pyrankvote`-based engine that counts ranked (`A>C>B`) or score ballots round by round.

**New to RCV-IRV?** The concept pages for this method live in [`concepts/`](concepts/README.md) — start with [Is it RCV or IRV?](concepts/RCV_or_IRV_whats_the_right_word.md) (the terminology that makes the rest read precisely), then [RCV-IRV (Hare)](concepts/RCV-IRV-Hare.md) for the method itself and [center squeeze](concepts/RCV_IRV_center_squeeze.md) for the critique. Everything below is the **runnable example and the engine**. <!-- terminology-ok: bare RCV is inside a linked page title -->

| Case | Page | YAML |
|---|---|---|
| RCV-IRV — a basic ranked-ballot example (3 candidates) | [page](cases/cases_pages/RCV_ballot_example.md) | [`RCV_ballot_example.yaml`](cases/RCV_ballot_example.yaml) |
| Parallel universes — one count, two legal answers (an elimination tie where PUT elects two) | [page](cases/cases_pages/put_two_universes_c3_b4.md) | [`put_two_universes_c3_b4.yaml`](cases/put_two_universes_c3_b4.yaml) |
| Batch elimination empties the field — the perfect cycle (3 voters; Hare *and* Coombs both run out of candidates) | [page](cases/cases_pages/batch_all_out_cycle_c3_b3.md) | [`batch_all_out_cycle_c3_b3.yaml`](cases/batch_all_out_cycle_c3_b3.yaml) |
| …with a Condorcet winner sitting there (one ballot changed; batch IRV still ties three ways, Coombs elects Amy) | [page](cases/cases_pages/batch_all_out_condorcet_c3_b3.md) | [`batch_all_out_condorcet_c3_b3.yaml`](cases/batch_all_out_condorcet_c3_b3.yaml) |
| …and in round *two*, with Pareto keeping the unanimously-last candidate out of the tie | [page](cases/cases_pages/batch_all_out_round2_c4_b6.md) | [`batch_all_out_round2_c4_b6.yaml`](cases/batch_all_out_round2_c4_b6.yaml) |

The three `batch_all_out_*` cases back [Batch elimination — what happens when the batch is *everyone*](../../07_Concepts/topics/ties/batch_elimination.md).

The engine lives in [`RCV_IRV_tabulation_engine/`](RCV_IRV_tabulation_engine/README.md); full audit mirrors are in `RCV_IRV_tabulated/`.
