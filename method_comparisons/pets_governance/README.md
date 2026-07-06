# pets_governance — one electorate elects a pet government five ways

A single 22-voter electorate (a 13-voter **Furry** majority + a 9-voter **Others** minority) fills **six positions by six methods**, to show the majoritarian-vs-proportional divide on one ballot set. All six run on BetterVoting (Bloc STAR = STAR with 3 winners; Bloc Approval = Approval with 2 winners; Bloc Plurality/SNTV = Plurality with 2 winners — all via BV's `runBlocTabulator`) and all six are cross-checked against the LH engine.

| Position | Method | Seats | Winners | src |
|----------|--------|:---:|---------|:--:|
| Mayor | Ranked Robin | 1 | Dog | [`.yaml`](pets_gov_ranked_robin.yaml) |
| Council | Bloc STAR | 3 | Dog, Fish, Cat *(majority sweep)* | [`.yaml`](pets_gov_bloc_star.yaml) |
| Committee | Approval | 2 | Dog, Cat | [`.yaml`](pets_gov_approval.yaml) |
| Council (PR) | STAR-PR | 3 | Bird, Dog, Fish *(minority seated)* | [`.yaml`](pets_gov_star_pr.yaml) |
| Delegates | STV | 3 | Dog, Bird, Cat *(minority seated)* | [`.yaml`](pets_gov_stv.yaml) |
| Neighborhood Reps | Bloc Plurality (SNTV) | 2 | Dog, Bird *(minority seated)* | [`.yaml`](pets_gov_bloc_plurality.yaml) |

**The lesson:** give the same 59/41 electorate 3 seats and Bloc STAR hands the majority all three, while STV and STAR-PR seat the minority. Majoritarian vs proportional, side by side.

→ **Full lesson:** [pets_gov_five_positions.md](pets_gov_five_positions.md)

# file: README.md
