---
search:
  exclude: true
---

# Minneapolis 2017 Mayor — the head-to-head check: right winner, wrong runner-up

*Generated from [`minneapolis_2017_ranked_robin.yaml`](../minneapolis_2017_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn/README.md) · **1 seat** · **Expected winner:** Jacob Frey

**Official tie-break (lot) order:** Jacob Frey > Betsy Hodges > Tom Hoch > Raymond Dehn > Nekima Levy-Pounds > Charlie Gers > Aswar Rahman > Al Flowers > L.A. Nik > David Rosenfeld > Captain Jack Sparrow > Gregg A. Iverson > Ronald Lischeid > David John Wilson > Troy Benjegerdes > Ian Simpson > Christopher Zimmerman > Theron Preston Washington > Undeclared Write-ins — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

Reproduced from the 2017 Minneapolis mayoral cast vote record published by
RCV Lab (rcv-lab.org), converted from the city's ESS export. A REAL election
at full size: 105,928 ballots, 18 candidates plus Undeclared Write-ins, and
Minneapolis' three-rank limit. Nothing is sampled or rounded — all 2,479
distinct rankings are here as weighted blocs.

THE CONVERSION follows the published RCTab rules file exactly, and four
independent numbers confirm it landed right:

    first choices    26,104 / 20,122 / 18,905 / 18,100 / 15,715  (match)
    blank ballots    1,369                                       (match)
    skipped-rank     38                                          (match)
    final round      Frey 46,704 vs Dehn 34,970                  (match)

Those rules, and what they cost: an `overvote` skips to the next rank rather
than killing the ballot (269 ballots); a repeated candidate is ignored rather
than exhausting (4,213); and a SECOND consecutive skipped rank truncates the
ballot there. That last one sounds brutal and almost never is — of 13,456
ballots hitting it, 13,418 were simply trailing blanks with nothing after
them. Only **38** actually discarded a later choice, which is exactly the
`skippedRankings` figure the source reports.

THE SAME BALLOTS, COUNTED AS RANKED ROBIN, to ask the question the
elimination rounds never ask: who beats whom?

THE GOOD NEWS FOR RCV-IRV. Jacob Frey is the Condorcet winner outright —
18 wins, 0 losses, beating every one of the eighteen others head-to-head. IRV
elected him. There is no center squeeze here, no cycle anywhere in the
tournament, and the whole field sorts into one clean transitive line. On the
largest real election in this library, the instant runoff got the winner
right, and this file is the evidence rather than a claim.

THE PART WORTH KNOWING ANYWAY. IRV's elimination order is not a strength
order, and here the two come apart at second place:

    by head-to-head strength   Frey > Hodges > Hoch > Dehn > Levy-Pounds
    IRV's last one standing    Frey, then ... Raymond Dehn

Dehn is the FOURTH-strongest of the five by head-to-head, yet he is the one
left in the final pair, because Hodges and Hoch were eliminated before him on
first-choice counts. Both would have beaten him:

    Betsy Hodges beats Raymond Dehn   37,513 - 35,133
    Tom Hoch     beats Raymond Dehn   40,644 - 36,737

So "runner-up" under RCV-IRV means "last one eliminated", not
"second-strongest" — and a reader who takes the final-round margin as a
measure of how close the election was is reading the wrong pair. Frey beats
Hodges by 8,122 and Dehn by 11,734, so the reported final margin actually
OVERSTATES his lead over the strongest challenger.

This costs RCV-IRV nothing on the winner and should not be inflated into a
scandal. It is the ordinary, structural consequence of eliminating on first
choices, and it is exactly what the round-robin table is for.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
4636:Jacob Frey
3410:Raymond Dehn>Nekima Levy-Pounds>Betsy Hodges
3192:Betsy Hodges
2854:Tom Hoch
2676:Jacob Frey>Tom Hoch>Betsy Hodges
2520:Jacob Frey>Tom Hoch
2189:Tom Hoch>Jacob Frey
2187:Nekima Levy-Pounds>Raymond Dehn>Betsy Hodges
2115:Raymond Dehn>Betsy Hodges>Nekima Levy-Pounds
2069:Tom Hoch>Jacob Frey>Betsy Hodges
1908:Betsy Hodges>Raymond Dehn>Nekima Levy-Pounds
1875:Jacob Frey>Tom Hoch>Raymond Dehn
1472:Tom Hoch>Jacob Frey>Raymond Dehn
1466:Betsy Hodges>Nekima Levy-Pounds>Raymond Dehn
1418:Jacob Frey>Betsy Hodges>Tom Hoch
1334:Nekima Levy-Pounds>Betsy Hodges>Raymond Dehn
1302:Jacob Frey>Tom Hoch>Nekima Levy-Pounds
1188:Betsy Hodges>Jacob Frey>Tom Hoch
1181:Raymond Dehn>Nekima Levy-Pounds>Jacob Frey
1097:Tom Hoch>Jacob Frey>Nekima Levy-Pounds
1078:Jacob Frey>Raymond Dehn>Tom Hoch
1078:Nekima Levy-Pounds
942:Nekima Levy-Pounds>Raymond Dehn>Jacob Frey
940:Betsy Hodges>Tom Hoch>Jacob Frey
848:Betsy Hodges>Jacob Frey>Nekima Levy-Pounds
838:Betsy Hodges>Raymond Dehn>Jacob Frey
834:Tom Hoch>Raymond Dehn>Jacob Frey
822:Jacob Frey>Betsy Hodges
819:Raymond Dehn
796:Raymond Dehn>Jacob Frey>Nekima Levy-Pounds
792:Betsy Hodges>Nekima Levy-Pounds>Jacob Frey
790:Jacob Frey>Raymond Dehn>Betsy Hodges
776:Tom Hoch>Betsy Hodges>Jacob Frey
766:Raymond Dehn>Nekima Levy-Pounds>Tom Hoch
761:Jacob Frey>Betsy Hodges>Nekima Levy-Pounds
750:Raymond Dehn>Jacob Frey>Betsy Hodges
746:Nekima Levy-Pounds>Jacob Frey>Betsy Hodges
746:Raymond Dehn>Betsy Hodges>Jacob Frey
744:Nekima Levy-Pounds>Betsy Hodges>Jacob Frey
743:Raymond Dehn>Nekima Levy-Pounds
711:Jacob Frey>Raymond Dehn>Nekima Levy-Pounds
701:Jacob Frey>Nekima Levy-Pounds>Betsy Hodges
694:Jacob Frey>Nekima Levy-Pounds>Tom Hoch
677:Jacob Frey>Betsy Hodges>Raymond Dehn
671:Betsy Hodges>Jacob Frey>Raymond Dehn
669:Betsy Hodges>Jacob Frey
660:Raymond Dehn>Jacob Frey>Tom Hoch
659:Nekima Levy-Pounds>Raymond Dehn>Tom Hoch
656:Raymond Dehn>Tom Hoch>Jacob Frey
578:Betsy Hodges>Raymond Dehn
575:Tom Hoch>Betsy Hodges
571:Nekima Levy-Pounds>Betsy Hodges
560:Jacob Frey>Nekima Levy-Pounds>Raymond Dehn
555:Raymond Dehn>Tom Hoch>Nekima Levy-Pounds
551:Tom Hoch>Nekima Levy-Pounds>Jacob Frey
537:Betsy Hodges>Tom Hoch
525:Nekima Levy-Pounds>Jacob Frey>Tom Hoch
521:Nekima Levy-Pounds>Raymond Dehn
519:Nekima Levy-Pounds>Jacob Frey>Raymond Dehn
502:Betsy Hodges>Nekima Levy-Pounds
486:Raymond Dehn>Betsy Hodges
481:Betsy Hodges>Nekima Levy-Pounds>Tom Hoch
481:Raymond Dehn>Tom Hoch>Betsy Hodges
456:Betsy Hodges>Tom Hoch>Nekima Levy-Pounds
454:Tom Hoch>Raymond Dehn>Nekima Levy-Pounds
449:Nekima Levy-Pounds>Tom Hoch>Jacob Frey
436:Betsy Hodges>Raymond Dehn>Tom Hoch
417:Nekima Levy-Pounds>Betsy Hodges>Tom Hoch
408:Raymond Dehn>Betsy Hodges>Tom Hoch
401:Tom Hoch>Raymond Dehn>Betsy Hodges
378:Betsy Hodges>Tom Hoch>Raymond Dehn
372:Tom Hoch>Betsy Hodges>Nekima Levy-Pounds
363:Tom Hoch>Nekima Levy-Pounds>Betsy Hodges
360:Nekima Levy-Pounds>Tom Hoch>Betsy Hodges
350:Jacob Frey>Nekima Levy-Pounds
330:Jacob Frey>Raymond Dehn
328:Charlie Gers
327:Nekima Levy-Pounds>Tom Hoch>Raymond Dehn
324:Tom Hoch>Raymond Dehn
314:Tom Hoch>Nekima Levy-Pounds>Raymond Dehn
302:Tom Hoch>Betsy Hodges>Raymond Dehn
295:Jacob Frey>Tom Hoch>Aswar Rahman
278:Nekima Levy-Pounds>Jacob Frey
269:Tom Hoch>Nekima Levy-Pounds
268:Jacob Frey>Tom Hoch>Captain Jack Sparrow
262:Tom Hoch>Jacob Frey>Captain Jack Sparrow
260:Raymond Dehn>Jacob Frey
258:Tom Hoch>Jacob Frey>Gregg A. Iverson
251:Tom Hoch>Jacob Frey>Aswar Rahman
245:Raymond Dehn>Nekima Levy-Pounds>Al Flowers
245:Raymond Dehn>Nekima Levy-Pounds>David Rosenfeld
233:Raymond Dehn>Nekima Levy-Pounds>Captain Jack Sparrow
231:Raymond Dehn>Tom Hoch
216:Nekima Levy-Pounds>Raymond Dehn>Al Flowers
203:Jacob Frey>Tom Hoch>Gregg A. Iverson
200:Nekima Levy-Pounds>Raymond Dehn>Aswar Rahman
196:Nekima Levy-Pounds>Betsy Hodges>Al Flowers
195:Raymond Dehn>Nekima Levy-Pounds>Aswar Rahman
195:Tom Hoch>Jacob Frey>Al Flowers
192:Nekima Levy-Pounds>Tom Hoch
189:Jacob Frey>Tom Hoch>Al Flowers
188:L.A. Nik
174:Tom Hoch>Jacob Frey>Charlie Gers
153:Nekima Levy-Pounds>Raymond Dehn>David Rosenfeld
146:Aswar Rahman
144:Nekima Levy-Pounds>Al Flowers>Betsy Hodges
143:Al Flowers
141:Betsy Hodges>Jacob Frey>Gregg A. Iverson
137:Nekima Levy-Pounds>Betsy Hodges>Aswar Rahman
137:Tom Hoch>Jacob Frey>L.A. Nik
134:Jacob Frey>Tom Hoch>Charlie Gers
131:Betsy Hodges>Nekima Levy-Pounds>Al Flowers
131:Betsy Hodges>Nekima Levy-Pounds>Aswar Rahman
127:Nekima Levy-Pounds>Al Flowers
123:Nekima Levy-Pounds>Raymond Dehn>Captain Jack Sparrow
110:Betsy Hodges>Tom Hoch>Al Flowers
107:Nekima Levy-Pounds>Al Flowers>Raymond Dehn
105:Jacob Frey>Nekima Levy-Pounds>Aswar Rahman
104:Jacob Frey>Betsy Hodges>Aswar Rahman
101:Jacob Frey>Betsy Hodges>Gregg A. Iverson
100:Raymond Dehn>Betsy Hodges>Al Flowers
97:Nekima Levy-Pounds>Aswar Rahman>Betsy Hodges
97:Nekima Levy-Pounds>Jacob Frey>Aswar Rahman
97:Tom Hoch>Charlie Gers
95:Nekima Levy-Pounds>Jacob Frey>Al Flowers
93:Nekima Levy-Pounds>Al Flowers>Tom Hoch
91:Tom Hoch>Nekima Levy-Pounds>Aswar Rahman
91:Tom Hoch>Raymond Dehn>Al Flowers
90:Jacob Frey>Tom Hoch>L.A. Nik
89:Jacob Frey>Tom Hoch>David John Wilson
88:Captain Jack Sparrow
86:Nekima Levy-Pounds>Tom Hoch>Al Flowers
86:Tom Hoch>Jacob Frey>David John Wilson
86:Undeclared Write-ins
84:Tom Hoch>Aswar Rahman>Jacob Frey
83:Tom Hoch>Raymond Dehn>Aswar Rahman
81:Jacob Frey>Betsy Hodges>Captain Jack Sparrow
80:Betsy Hodges>Jacob Frey>Aswar Rahman
80:Gregg A. Iverson
80:Ronald Lischeid
79:Nekima Levy-Pounds>Al Flowers>Aswar Rahman
78:Raymond Dehn>Betsy Hodges>Captain Jack Sparrow
75:Betsy Hodges>Aswar Rahman
75:Betsy Hodges>Gregg A. Iverson>Jacob Frey
75:Nekima Levy-Pounds>Aswar Rahman>Raymond Dehn
75:Tom Hoch>Nekima Levy-Pounds>Al Flowers
73:Betsy Hodges>Jacob Frey>Al Flowers
73:Betsy Hodges>Tom Hoch>Aswar Rahman
72:Jacob Frey>Aswar Rahman>Tom Hoch
72:Jacob Frey>Nekima Levy-Pounds>Al Flowers
72:Nekima Levy-Pounds>Al Flowers>Jacob Frey
71:David Rosenfeld
71:Nekima Levy-Pounds>Jacob Frey>Gregg A. Iverson
70:Jacob Frey>Nekima Levy-Pounds>Captain Jack Sparrow
70:Tom Hoch>Betsy Hodges>Al Flowers
69:Jacob Frey>Gregg A. Iverson>Betsy Hodges
69:Tom Hoch>Betsy Hodges>Captain Jack Sparrow
68:Nekima Levy-Pounds>Jacob Frey>Captain Jack Sparrow
67:Nekima Levy-Pounds>Tom Hoch>Aswar Rahman
67:Tom Hoch>Raymond Dehn>Captain Jack Sparrow
66:Betsy Hodges>Aswar Rahman>Nekima Levy-Pounds
66:Betsy Hodges>Jacob Frey>Captain Jack Sparrow
65:Charlie Gers>L.A. Nik
64:David John Wilson
64:Nekima Levy-Pounds>Betsy Hodges>Captain Jack Sparrow
63:Raymond Dehn>Al Flowers>Betsy Hodges
63:Tom Hoch>Al Flowers>Raymond Dehn
62:Tom Hoch>Nekima Levy-Pounds>Captain Jack Sparrow
61:Tom Hoch>Betsy Hodges>Aswar Rahman
61:Tom Hoch>Captain Jack Sparrow
61:Tom Hoch>Raymond Dehn>Gregg A. Iverson
60:Betsy Hodges>Tom Hoch>Captain Jack Sparrow
60:Jacob Frey>Aswar Rahman
60:Jacob Frey>Raymond Dehn>Captain Jack Sparrow
60:Raymond Dehn>Betsy Hodges>Aswar Rahman
60:Tom Hoch>Al Flowers>Jacob Frey
60:Tom Hoch>Aswar Rahman
59:Betsy Hodges>Nekima Levy-Pounds>Gregg A. Iverson
59:Betsy Hodges>Raymond Dehn>Aswar Rahman
59:Nekima Levy-Pounds>Aswar Rahman
59:Nekima Levy-Pounds>Betsy Hodges>David Rosenfeld
58:Betsy Hodges>Al Flowers>Nekima Levy-Pounds
58:Betsy Hodges>Al Flowers>Tom Hoch
58:Betsy Hodges>Nekima Levy-Pounds>Captain Jack Sparrow
58:Betsy Hodges>Raymond Dehn>Al Flowers
58:Jacob Frey>Betsy Hodges>Al Flowers
57:Jacob Frey>Al Flowers>Tom Hoch
56:Jacob Frey>Aswar Rahman>Nekima Levy-Pounds
55:Nekima Levy-Pounds>Aswar Rahman>Al Flowers
55:Tom Hoch>Al Flowers>Nekima Levy-Pounds
55:Tom Hoch>Charlie Gers>Jacob Frey
54:Raymond Dehn>Aswar Rahman>Nekima Levy-Pounds
54:Raymond Dehn>Betsy Hodges>David Rosenfeld
53:Jacob Frey>Gregg A. Iverson>Tom Hoch
53:Jacob Frey>Raymond Dehn>Al Flowers
53:Tom Hoch>Aswar Rahman>Nekima Levy-Pounds
52:Raymond Dehn>Tom Hoch>Al Flowers
51:Charlie Gers>Tom Hoch>Jacob Frey
50:Betsy Hodges>Tom Hoch>Gregg A. Iverson
50:Raymond Dehn>David Rosenfeld>Nekima Levy-Pounds
50:Raymond Dehn>Jacob Frey>Captain Jack Sparrow
50:Raymond Dehn>Nekima Levy-Pounds>David John Wilson
49:Jacob Frey>Raymond Dehn>Aswar Rahman
49:Nekima Levy-Pounds>Tom Hoch>Captain Jack Sparrow
49:Raymond Dehn>Aswar Rahman>Betsy Hodges
49:Tom Hoch>L.A. Nik
48:Betsy Hodges>Al Flowers
48:Jacob Frey>Aswar Rahman>Betsy Hodges
48:Jacob Frey>Nekima Levy-Pounds>Gregg A. Iverson
48:Raymond Dehn>Al Flowers>Nekima Levy-Pounds
48:Raymond Dehn>Tom Hoch>Captain Jack Sparrow
47:Betsy Hodges>Aswar Rahman>Tom Hoch
47:Nekima Levy-Pounds>Aswar Rahman>Jacob Frey
47:Nekima Levy-Pounds>Aswar Rahman>Tom Hoch
47:Raymond Dehn>Tom Hoch>Aswar Rahman
47:Tom Hoch>Jacob Frey>Ronald Lischeid
46:Tom Hoch>Al Flowers
46:Tom Hoch>Jacob Frey>David Rosenfeld
44:Tom Hoch>Captain Jack Sparrow>David John Wilson
43:Jacob Frey>Captain Jack Sparrow
43:Tom Hoch>Aswar Rahman>Betsy Hodges
43:Tom Hoch>Charlie Gers>L.A. Nik
42:Jacob Frey>Charlie Gers
42:Jacob Frey>Tom Hoch>David Rosenfeld
42:Nekima Levy-Pounds>Raymond Dehn>David John Wilson
42:Tom Hoch>Betsy Hodges>Gregg A. Iverson
42:Tom Hoch>Jacob Frey>Undeclared Write-ins
42:Troy Benjegerdes
41:Betsy Hodges>Aswar Rahman>Al Flowers
40:Betsy Hodges>Al Flowers>Jacob Frey
40:Tom Hoch>L.A. Nik>Jacob Frey
39:Betsy Hodges>Aswar Rahman>Jacob Frey
39:Nekima Levy-Pounds>Betsy Hodges>Gregg A. Iverson
37:Raymond Dehn>Jacob Frey>Aswar Rahman
37:Tom Hoch>Aswar Rahman>Raymond Dehn
36:Charlie Gers>L.A. Nik>Ronald Lischeid
36:Charlie Gers>Tom Hoch
36:Nekima Levy-Pounds>Jacob Frey>David Rosenfeld
36:Raymond Dehn>David Rosenfeld>Captain Jack Sparrow
35:Jacob Frey>Al Flowers>Betsy Hodges
35:Jacob Frey>Betsy Hodges>David Rosenfeld
35:Tom Hoch>Gregg A. Iverson>Jacob Frey
34:Betsy Hodges>Captain Jack Sparrow
34:Betsy Hodges>Raymond Dehn>Captain Jack Sparrow
34:Jacob Frey>Gregg A. Iverson
34:Jacob Frey>Gregg A. Iverson>Nekima Levy-Pounds
34:L.A. Nik>Charlie Gers
34:Raymond Dehn>Jacob Frey>Al Flowers
34:Tom Hoch>Al Flowers>Betsy Hodges
33:Betsy Hodges>Gregg A. Iverson
33:Betsy Hodges>Gregg A. Iverson>Tom Hoch
33:Charlie Gers>Jacob Frey>Tom Hoch
33:Jacob Frey>Aswar Rahman>Raymond Dehn
33:Jacob Frey>Tom Hoch>Undeclared Write-ins
33:Raymond Dehn>Al Flowers
33:Raymond Dehn>Nekima Levy-Pounds>Undeclared Write-ins
33:Tom Hoch>Raymond Dehn>Charlie Gers
32:Betsy Hodges>Al Flowers>Raymond Dehn
32:Raymond Dehn>David Rosenfeld
32:Raymond Dehn>David Rosenfeld>Betsy Hodges
31:Aswar Rahman>Tom Hoch>Jacob Frey
31:Betsy Hodges>Gregg A. Iverson>Nekima Levy-Pounds
31:Betsy Hodges>Jacob Frey>David Rosenfeld
31:Nekima Levy-Pounds>David Rosenfeld>Raymond Dehn
31:Raymond Dehn>Aswar Rahman>Jacob Frey
31:Raymond Dehn>Jacob Frey>David Rosenfeld
30:Al Flowers>Nekima Levy-Pounds>Betsy Hodges
30:David Rosenfeld>Raymond Dehn>Nekima Levy-Pounds
30:Jacob Frey>Al Flowers
30:Jacob Frey>Betsy Hodges>Charlie Gers
30:Tom Hoch>Aswar Rahman>Al Flowers
30:Tom Hoch>Betsy Hodges>Charlie Gers
30:Tom Hoch>Charlie Gers>Captain Jack Sparrow
30:Tom Hoch>L.A. Nik>Charlie Gers
29:Betsy Hodges>Aswar Rahman>Raymond Dehn
29:Jacob Frey>Al Flowers>Nekima Levy-Pounds
29:Jacob Frey>Tom Hoch>Ian Simpson
29:Nekima Levy-Pounds>Tom Hoch>David Rosenfeld
29:Tom Hoch>Undeclared Write-ins
28:Jacob Frey>Charlie Gers>Tom Hoch
28:Nekima Levy-Pounds>David Rosenfeld>Betsy Hodges
28:Raymond Dehn>Aswar Rahman>Tom Hoch
28:Tom Hoch>Gregg A. Iverson>Raymond Dehn
28:Tom Hoch>Jacob Frey>Troy Benjegerdes
27:Aswar Rahman>Jacob Frey>Tom Hoch
27:Betsy Hodges>David Rosenfeld
27:Betsy Hodges>Tom Hoch>David John Wilson
27:Charlie Gers>Ronald Lischeid>L.A. Nik
27:Jacob Frey>Captain Jack Sparrow>David John Wilson
27:Jacob Frey>Raymond Dehn>Gregg A. Iverson
27:Nekima Levy-Pounds>Captain Jack Sparrow
27:Tom Hoch>Captain Jack Sparrow>Jacob Frey
27:Tom Hoch>Gregg A. Iverson
27:Tom Hoch>Gregg A. Iverson>Betsy Hodges
27:Tom Hoch>Nekima Levy-Pounds>Gregg A. Iverson
27:Tom Hoch>Raymond Dehn>David John Wilson
27:Tom Hoch>Raymond Dehn>L.A. Nik
26:Al Flowers>Betsy Hodges
26:Charlie Gers>Undeclared Write-ins
26:Jacob Frey>Gregg A. Iverson>Raymond Dehn
26:Nekima Levy-Pounds>Betsy Hodges>David John Wilson
26:Raymond Dehn>Al Flowers>Tom Hoch
25:David Rosenfeld>Nekima Levy-Pounds>Raymond Dehn
25:Ian Simpson
25:Raymond Dehn>Betsy Hodges>Gregg A. Iverson
24:Al Flowers>Nekima Levy-Pounds
24:Betsy Hodges>Tom Hoch>David Rosenfeld
24:Jacob Frey>Captain Jack Sparrow>Tom Hoch
24:Jacob Frey>Tom Hoch>Troy Benjegerdes
24:Raymond Dehn>Nekima Levy-Pounds>L.A. Nik
24:Tom Hoch>Captain Jack Sparrow>L.A. Nik
23:Al Flowers>Raymond Dehn>Tom Hoch
23:Betsy Hodges>Al Flowers>Aswar Rahman
23:Betsy Hodges>Captain Jack Sparrow>David John Wilson
23:Jacob Frey>Charlie Gers>Captain Jack Sparrow
23:Jacob Frey>L.A. Nik>Tom Hoch
23:Jacob Frey>Undeclared Write-ins
23:Nekima Levy-Pounds>Al Flowers>Captain Jack Sparrow
23:Raymond Dehn>Jacob Frey>Gregg A. Iverson
23:Tom Hoch>Jacob Frey>Ian Simpson
23:Tom Hoch>L.A. Nik>Captain Jack Sparrow
23:Tom Hoch>Raymond Dehn>David Rosenfeld
22:Al Flowers>Betsy Hodges>Nekima Levy-Pounds
22:Aswar Rahman>Jacob Frey>Betsy Hodges
22:Aswar Rahman>Nekima Levy-Pounds>Jacob Frey
22:Jacob Frey>Al Flowers>Raymond Dehn
22:Jacob Frey>Nekima Levy-Pounds>David John Wilson
22:Jacob Frey>Nekima Levy-Pounds>David Rosenfeld
22:Jacob Frey>Tom Hoch>Ronald Lischeid
22:Nekima Levy-Pounds>David Rosenfeld
22:Raymond Dehn>Captain Jack Sparrow
22:Raymond Dehn>Tom Hoch>David Rosenfeld
21:Aswar Rahman>Raymond Dehn>Jacob Frey
21:Charlie Gers>L.A. Nik>Ian Simpson
21:Charlie Gers>Tom Hoch>L.A. Nik
21:Jacob Frey>Betsy Hodges>David John Wilson
21:Jacob Frey>L.A. Nik
21:Nekima Levy-Pounds>Raymond Dehn>Ian Simpson
21:Nekima Levy-Pounds>Raymond Dehn>Undeclared Write-ins
21:Raymond Dehn>Al Flowers>Jacob Frey
21:Tom Hoch>Betsy Hodges>David John Wilson
21:Tom Hoch>Nekima Levy-Pounds>David John Wilson
20:Aswar Rahman>Nekima Levy-Pounds>Betsy Hodges
20:Betsy Hodges>Undeclared Write-ins
20:Charlie Gers>L.A. Nik>David John Wilson
20:Jacob Frey>Betsy Hodges>L.A. Nik
20:L.A. Nik>Jacob Frey>Tom Hoch
20:Nekima Levy-Pounds>Aswar Rahman>Captain Jack Sparrow
20:Nekima Levy-Pounds>Jacob Frey>David John Wilson
20:Raymond Dehn>Al Flowers>Aswar Rahman
20:Tom Hoch>Aswar Rahman>Captain Jack Sparrow
20:Tom Hoch>Captain Jack Sparrow>Charlie Gers
20:Tom Hoch>Ronald Lischeid
19:Al Flowers>Tom Hoch>Betsy Hodges
19:Betsy Hodges>Nekima Levy-Pounds>David John Wilson
19:Raymond Dehn>Captain Jack Sparrow>Nekima Levy-Pounds
19:Raymond Dehn>Nekima Levy-Pounds>Ian Simpson
19:Raymond Dehn>Tom Hoch>L.A. Nik
19:Tom Hoch>Al Flowers>Captain Jack Sparrow
19:Tom Hoch>Captain Jack Sparrow>Betsy Hodges
18:Al Flowers>Betsy Hodges>Jacob Frey
18:Al Flowers>Nekima Levy-Pounds>Raymond Dehn
18:Betsy Hodges>Al Flowers>Captain Jack Sparrow
18:Betsy Hodges>Jacob Frey>David John Wilson
18:Betsy Hodges>Nekima Levy-Pounds>David Rosenfeld
18:Jacob Frey>Aswar Rahman>Captain Jack Sparrow
18:Jacob Frey>Charlie Gers>L.A. Nik
18:Jacob Frey>Gregg A. Iverson>Captain Jack Sparrow
18:L.A. Nik>Tom Hoch>Jacob Frey
18:Nekima Levy-Pounds>David Rosenfeld>Aswar Rahman
18:Raymond Dehn>Jacob Frey>David John Wilson
18:Tom Hoch>Betsy Hodges>L.A. Nik
18:Tom Hoch>Betsy Hodges>Ronald Lischeid
17:Aswar Rahman>Raymond Dehn>Tom Hoch
17:Betsy Hodges>Raymond Dehn>David Rosenfeld
17:Charlie Gers>Betsy Hodges
17:Charlie Gers>L.A. Nik>Captain Jack Sparrow
17:Jacob Frey>Captain Jack Sparrow>L.A. Nik
17:Jacob Frey>Raymond Dehn>David Rosenfeld
17:Nekima Levy-Pounds>David Rosenfeld>Captain Jack Sparrow
17:Raymond Dehn>Aswar Rahman
17:Raymond Dehn>David Rosenfeld>Tom Hoch
17:Tom Hoch>Al Flowers>Aswar Rahman
17:Tom Hoch>David John Wilson>Captain Jack Sparrow
17:Tom Hoch>Nekima Levy-Pounds>David Rosenfeld
17:Tom Hoch>Nekima Levy-Pounds>L.A. Nik
16:Al Flowers>Nekima Levy-Pounds>Jacob Frey
16:Al Flowers>Nekima Levy-Pounds>Tom Hoch
16:Al Flowers>Tom Hoch>Nekima Levy-Pounds
16:Aswar Rahman>Al Flowers>Raymond Dehn
16:Aswar Rahman>Betsy Hodges>Nekima Levy-Pounds
16:Aswar Rahman>Jacob Frey>Nekima Levy-Pounds
16:Betsy Hodges>Al Flowers>Gregg A. Iverson
16:Betsy Hodges>Gregg A. Iverson>Aswar Rahman
16:Betsy Hodges>Jacob Frey>Charlie Gers
16:Betsy Hodges>Raymond Dehn>David John Wilson
16:Betsy Hodges>Raymond Dehn>Gregg A. Iverson
16:Betsy Hodges>Tom Hoch>L.A. Nik
16:Charlie Gers>Captain Jack Sparrow>L.A. Nik
16:Jacob Frey>David John Wilson
16:Jacob Frey>David John Wilson>Captain Jack Sparrow
16:Nekima Levy-Pounds>Captain Jack Sparrow>Betsy Hodges
16:Nekima Levy-Pounds>Gregg A. Iverson
16:Nekima Levy-Pounds>Raymond Dehn>Troy Benjegerdes
16:Raymond Dehn>Aswar Rahman>Al Flowers
16:Raymond Dehn>Captain Jack Sparrow>David Rosenfeld
16:Tom Hoch>David John Wilson
15:Al Flowers>Raymond Dehn>Nekima Levy-Pounds
15:Aswar Rahman>Jacob Frey>Raymond Dehn
15:Aswar Rahman>Tom Hoch
15:Betsy Hodges>Gregg A. Iverson>Al Flowers
15:Charlie Gers>Jacob Frey
15:Charlie Gers>Jacob Frey>Betsy Hodges
15:David Rosenfeld>Raymond Dehn>Betsy Hodges
15:Jacob Frey>Raymond Dehn>Charlie Gers
15:Jacob Frey>Raymond Dehn>David John Wilson
15:L.A. Nik>Charlie Gers>Ian Simpson
15:L.A. Nik>Tom Hoch
15:Nekima Levy-Pounds>Aswar Rahman>David Rosenfeld
15:Nekima Levy-Pounds>Gregg A. Iverson>Betsy Hodges
15:Nekima Levy-Pounds>Jacob Frey>Charlie Gers
15:Raymond Dehn>Aswar Rahman>Captain Jack Sparrow
15:Raymond Dehn>Betsy Hodges>Charlie Gers
15:Raymond Dehn>Captain Jack Sparrow>Betsy Hodges
15:Raymond Dehn>Tom Hoch>David John Wilson
15:Raymond Dehn>Tom Hoch>Gregg A. Iverson
15:Tom Hoch>David Rosenfeld>Betsy Hodges
14:Al Flowers>Tom Hoch
14:Al Flowers>Tom Hoch>Jacob Frey
14:Betsy Hodges>Charlie Gers
14:Betsy Hodges>David Rosenfeld>Captain Jack Sparrow
14:Captain Jack Sparrow>Tom Hoch>Jacob Frey
14:David Rosenfeld>Nekima Levy-Pounds>Betsy Hodges
14:David Rosenfeld>Raymond Dehn>Jacob Frey
14:Gregg A. Iverson>Betsy Hodges>Jacob Frey
14:Jacob Frey>Captain Jack Sparrow>Betsy Hodges
14:Jacob Frey>Nekima Levy-Pounds>L.A. Nik
14:Jacob Frey>Raymond Dehn>L.A. Nik
14:L.A. Nik>Ronald Lischeid>Charlie Gers
14:Nekima Levy-Pounds>Captain Jack Sparrow>David John Wilson
14:Nekima Levy-Pounds>Gregg A. Iverson>Jacob Frey
14:Nekima Levy-Pounds>Raymond Dehn>L.A. Nik
14:Nekima Levy-Pounds>Tom Hoch>Ronald Lischeid
14:Nekima Levy-Pounds>Undeclared Write-ins
14:Raymond Dehn>Betsy Hodges>David John Wilson
14:Tom Hoch>Captain Jack Sparrow>Al Flowers
14:Tom Hoch>Captain Jack Sparrow>David Rosenfeld
14:Tom Hoch>Charlie Gers>Betsy Hodges
14:Tom Hoch>Charlie Gers>Ian Simpson
14:Tom Hoch>David John Wilson>Jacob Frey
14:Tom Hoch>L.A. Nik>Al Flowers
13:Aswar Rahman>Raymond Dehn
13:Betsy Hodges>David Rosenfeld>Jacob Frey
13:Betsy Hodges>David Rosenfeld>Tom Hoch
13:Betsy Hodges>Gregg A. Iverson>Raymond Dehn
13:Betsy Hodges>Tom Hoch>Troy Benjegerdes
13:Charlie Gers>L.A. Nik>Undeclared Write-ins
13:Jacob Frey>Al Flowers>Captain Jack Sparrow
13:Jacob Frey>Aswar Rahman>Al Flowers
13:Jacob Frey>David Rosenfeld
13:Jacob Frey>David Rosenfeld>Captain Jack Sparrow
13:L.A. Nik>Charlie Gers>Ronald Lischeid
13:Nekima Levy-Pounds>Al Flowers>David Rosenfeld
13:Nekima Levy-Pounds>David John Wilson>Captain Jack Sparrow
13:Nekima Levy-Pounds>Tom Hoch>David John Wilson
13:Nekima Levy-Pounds>Tom Hoch>Gregg A. Iverson
13:Ronald Lischeid>Tom Hoch>Jacob Frey
13:Tom Hoch>Betsy Hodges>David Rosenfeld
13:Tom Hoch>Captain Jack Sparrow>Ian Simpson
13:Tom Hoch>Captain Jack Sparrow>Raymond Dehn
13:Tom Hoch>David John Wilson>L.A. Nik
13:Tom Hoch>Gregg A. Iverson>Captain Jack Sparrow
13:Tom Hoch>Nekima Levy-Pounds>Charlie Gers
13:Tom Hoch>Raymond Dehn>Troy Benjegerdes
12:Al Flowers>Tom Hoch>Raymond Dehn
12:Aswar Rahman>Betsy Hodges
12:Aswar Rahman>Betsy Hodges>Raymond Dehn
12:Aswar Rahman>Jacob Frey
12:Aswar Rahman>Raymond Dehn>Nekima Levy-Pounds
12:Aswar Rahman>Tom Hoch>Betsy Hodges
12:Aswar Rahman>Tom Hoch>Nekima Levy-Pounds
12:Betsy Hodges>Aswar Rahman>Captain Jack Sparrow
12:Betsy Hodges>Captain Jack Sparrow>Nekima Levy-Pounds
12:Betsy Hodges>Jacob Frey>Ronald Lischeid
12:Charlie Gers>Betsy Hodges>Jacob Frey
12:Charlie Gers>Ronald Lischeid
12:Charlie Gers>Tom Hoch>Betsy Hodges
12:David Rosenfeld>Betsy Hodges>Nekima Levy-Pounds
12:Jacob Frey>Betsy Hodges>Troy Benjegerdes
12:Jacob Frey>Betsy Hodges>Undeclared Write-ins
12:Jacob Frey>David Rosenfeld>Betsy Hodges
12:Jacob Frey>David Rosenfeld>Tom Hoch
12:Jacob Frey>Gregg A. Iverson>Al Flowers
12:Jacob Frey>L.A. Nik>Captain Jack Sparrow
12:Jacob Frey>L.A. Nik>Charlie Gers
12:Nekima Levy-Pounds>Al Flowers>Gregg A. Iverson
12:Nekima Levy-Pounds>Betsy Hodges>Charlie Gers
12:Raymond Dehn>Jacob Frey>Ian Simpson
12:Tom Hoch>Al Flowers>Charlie Gers
12:Tom Hoch>Charlie Gers>Raymond Dehn
12:Tom Hoch>David Rosenfeld
12:Tom Hoch>David Rosenfeld>Captain Jack Sparrow
12:Tom Hoch>L.A. Nik>Ronald Lischeid
11:Al Flowers>Betsy Hodges>Tom Hoch
11:Aswar Rahman>Al Flowers>Tom Hoch
11:Aswar Rahman>Nekima Levy-Pounds>Raymond Dehn
11:Betsy Hodges>Captain Jack Sparrow>Tom Hoch
11:Betsy Hodges>Gregg A. Iverson>Captain Jack Sparrow
11:Betsy Hodges>Raymond Dehn>L.A. Nik
11:Betsy Hodges>Tom Hoch>Charlie Gers
11:Betsy Hodges>Tom Hoch>Ronald Lischeid
11:Charlie Gers>L.A. Nik>Tom Hoch
11:Gregg A. Iverson>Jacob Frey>Betsy Hodges
11:Jacob Frey>Al Flowers>Aswar Rahman
11:Jacob Frey>Captain Jack Sparrow>Raymond Dehn
11:Jacob Frey>Gregg A. Iverson>Charlie Gers
11:L.A. Nik>Charlie Gers>Tom Hoch
11:L.A. Nik>Undeclared Write-ins
11:Nekima Levy-Pounds>Betsy Hodges>L.A. Nik
11:Nekima Levy-Pounds>Betsy Hodges>Undeclared Write-ins
11:Nekima Levy-Pounds>Captain Jack Sparrow>David Rosenfeld
11:Nekima Levy-Pounds>Captain Jack Sparrow>Jacob Frey
11:Nekima Levy-Pounds>David Rosenfeld>Al Flowers
11:Nekima Levy-Pounds>David Rosenfeld>Jacob Frey
11:Nekima Levy-Pounds>David Rosenfeld>Tom Hoch
11:Raymond Dehn>Al Flowers>Captain Jack Sparrow
11:Raymond Dehn>Betsy Hodges>Undeclared Write-ins
11:Raymond Dehn>Captain Jack Sparrow>Jacob Frey
11:Raymond Dehn>David Rosenfeld>David John Wilson
11:Raymond Dehn>Nekima Levy-Pounds>Ronald Lischeid
11:Raymond Dehn>Undeclared Write-ins
11:Tom Hoch>Al Flowers>L.A. Nik
11:Tom Hoch>Aswar Rahman>Gregg A. Iverson
11:Tom Hoch>Gregg A. Iverson>Al Flowers
11:Tom Hoch>L.A. Nik>Betsy Hodges
11:Tom Hoch>Raymond Dehn>Ronald Lischeid
11:Tom Hoch>Troy Benjegerdes
10:Al Flowers>Betsy Hodges>Aswar Rahman
10:Al Flowers>Jacob Frey
10:Aswar Rahman>Betsy Hodges>Jacob Frey
10:Betsy Hodges>David John Wilson
10:Betsy Hodges>David Rosenfeld>Nekima Levy-Pounds
10:Betsy Hodges>Nekima Levy-Pounds>Ian Simpson
10:Betsy Hodges>Nekima Levy-Pounds>L.A. Nik
10:Charlie Gers>Captain Jack Sparrow
10:Charlie Gers>David John Wilson>L.A. Nik
10:Charlie Gers>Raymond Dehn>Tom Hoch
10:David Rosenfeld>Nekima Levy-Pounds
10:David Rosenfeld>Nekima Levy-Pounds>Jacob Frey
10:Gregg A. Iverson>Betsy Hodges
10:Gregg A. Iverson>Betsy Hodges>Tom Hoch
10:Gregg A. Iverson>Jacob Frey>Tom Hoch
10:Jacob Frey>Al Flowers>Gregg A. Iverson
10:Jacob Frey>Aswar Rahman>Charlie Gers
10:Jacob Frey>Charlie Gers>Nekima Levy-Pounds
10:Jacob Frey>Charlie Gers>Raymond Dehn
10:Jacob Frey>Nekima Levy-Pounds>Charlie Gers
10:Jacob Frey>Nekima Levy-Pounds>Ian Simpson
10:L.A. Nik>Tom Hoch>Captain Jack Sparrow
10:Nekima Levy-Pounds>Raymond Dehn>Gregg A. Iverson
10:Nekima Levy-Pounds>Tom Hoch>L.A. Nik
10:Raymond Dehn>Al Flowers>David Rosenfeld
10:Raymond Dehn>Aswar Rahman>David Rosenfeld
10:Raymond Dehn>David Rosenfeld>Jacob Frey
10:Raymond Dehn>Jacob Frey>L.A. Nik
10:Raymond Dehn>Nekima Levy-Pounds>Charlie Gers
10:Raymond Dehn>Nekima Levy-Pounds>Troy Benjegerdes
10:Tom Hoch>Aswar Rahman>L.A. Nik
10:Tom Hoch>Captain Jack Sparrow>Aswar Rahman
10:Tom Hoch>Charlie Gers>Aswar Rahman
10:Tom Hoch>Charlie Gers>Nekima Levy-Pounds
10:Tom Hoch>Charlie Gers>Ronald Lischeid
10:Tom Hoch>Ian Simpson>Captain Jack Sparrow
10:Tom Hoch>L.A. Nik>David John Wilson
10:Tom Hoch>L.A. Nik>Nekima Levy-Pounds
10:Tom Hoch>Ronald Lischeid>Jacob Frey
10:Tom Hoch>Troy Benjegerdes>Raymond Dehn
9:Aswar Rahman>Nekima Levy-Pounds
9:Aswar Rahman>Nekima Levy-Pounds>Al Flowers
9:Betsy Hodges>Aswar Rahman>David Rosenfeld
9:Betsy Hodges>Aswar Rahman>Gregg A. Iverson
9:Betsy Hodges>Jacob Frey>L.A. Nik
9:Betsy Hodges>Nekima Levy-Pounds>Ronald Lischeid
9:Betsy Hodges>Nekima Levy-Pounds>Undeclared Write-ins
9:Captain Jack Sparrow>Jacob Frey>Betsy Hodges
9:Captain Jack Sparrow>Jacob Frey>Tom Hoch
9:Charlie Gers>Jacob Frey>Captain Jack Sparrow
9:Charlie Gers>Ronald Lischeid>Ian Simpson
9:Charlie Gers>Tom Hoch>Ronald Lischeid
9:David Rosenfeld>Betsy Hodges>Captain Jack Sparrow
9:David Rosenfeld>Captain Jack Sparrow
9:David Rosenfeld>Jacob Frey>Nekima Levy-Pounds
9:Jacob Frey>Charlie Gers>Betsy Hodges
9:L.A. Nik>Tom Hoch>Charlie Gers
9:Nekima Levy-Pounds>Al Flowers>L.A. Nik
9:Nekima Levy-Pounds>Captain Jack Sparrow>Al Flowers
9:Nekima Levy-Pounds>Gregg A. Iverson>Tom Hoch
9:Nekima Levy-Pounds>Raymond Dehn>Ronald Lischeid
9:Raymond Dehn>Captain Jack Sparrow>David John Wilson
9:Raymond Dehn>Captain Jack Sparrow>Tom Hoch
9:Raymond Dehn>David John Wilson>Captain Jack Sparrow
9:Raymond Dehn>Gregg A. Iverson>Tom Hoch
9:Raymond Dehn>Nekima Levy-Pounds>Gregg A. Iverson
9:Tom Hoch>Al Flowers>David John Wilson
9:Tom Hoch>Al Flowers>Gregg A. Iverson
9:Tom Hoch>Aswar Rahman>Charlie Gers
9:Tom Hoch>Aswar Rahman>David John Wilson
9:Tom Hoch>Captain Jack Sparrow>Nekima Levy-Pounds
9:Tom Hoch>Charlie Gers>David John Wilson
9:Tom Hoch>David John Wilson>Nekima Levy-Pounds
9:Tom Hoch>David Rosenfeld>Jacob Frey
9:Tom Hoch>David Rosenfeld>Nekima Levy-Pounds
9:Tom Hoch>Gregg A. Iverson>Aswar Rahman
9:Tom Hoch>Gregg A. Iverson>Troy Benjegerdes
9:Tom Hoch>L.A. Nik>Ian Simpson
9:Tom Hoch>Raymond Dehn>Undeclared Write-ins
9:Tom Hoch>Ronald Lischeid>Charlie Gers
9:Tom Hoch>Ronald Lischeid>L.A. Nik
8:Al Flowers>Aswar Rahman>Raymond Dehn
8:Al Flowers>Betsy Hodges>Raymond Dehn
8:Al Flowers>Jacob Frey>Tom Hoch
8:Al Flowers>Raymond Dehn
8:Al Flowers>Raymond Dehn>Betsy Hodges
8:Aswar Rahman>Betsy Hodges>Tom Hoch
8:Betsy Hodges>Captain Jack Sparrow>Charlie Gers
8:Betsy Hodges>Captain Jack Sparrow>Jacob Frey
8:Betsy Hodges>Charlie Gers>Captain Jack Sparrow
8:Betsy Hodges>Charlie Gers>David Rosenfeld
8:Betsy Hodges>Jacob Frey>Undeclared Write-ins
8:Betsy Hodges>Raymond Dehn>Troy Benjegerdes
8:Betsy Hodges>Tom Hoch>Ian Simpson
8:Captain Jack Sparrow>Charlie Gers>L.A. Nik
8:Captain Jack Sparrow>Nekima Levy-Pounds>Raymond Dehn
8:Charlie Gers>Aswar Rahman>Tom Hoch
8:Charlie Gers>L.A. Nik>Jacob Frey
8:Charlie Gers>Raymond Dehn
8:Charlie Gers>Tom Hoch>Captain Jack Sparrow
8:David John Wilson>Tom Hoch>Jacob Frey
8:Gregg A. Iverson>Jacob Frey>Nekima Levy-Pounds
8:Jacob Frey>Aswar Rahman>David John Wilson
8:Jacob Frey>Betsy Hodges>Ian Simpson
8:Jacob Frey>Captain Jack Sparrow>David Rosenfeld
8:Jacob Frey>Captain Jack Sparrow>Nekima Levy-Pounds
8:Jacob Frey>Charlie Gers>David John Wilson
8:Jacob Frey>David Rosenfeld>Raymond Dehn
8:Jacob Frey>Gregg A. Iverson>Aswar Rahman
8:L.A. Nik>Charlie Gers>David John Wilson
8:Nekima Levy-Pounds>Al Flowers>Troy Benjegerdes
8:Nekima Levy-Pounds>Captain Jack Sparrow>Raymond Dehn
8:Nekima Levy-Pounds>David Rosenfeld>David John Wilson
8:Nekima Levy-Pounds>David Rosenfeld>Ronald Lischeid
8:Nekima Levy-Pounds>L.A. Nik>Betsy Hodges
8:Nekima Levy-Pounds>Tom Hoch>Undeclared Write-ins
8:Raymond Dehn>Charlie Gers
8:Raymond Dehn>David Rosenfeld>Ronald Lischeid
8:Raymond Dehn>Jacob Frey>Charlie Gers
8:Raymond Dehn>Jacob Frey>Undeclared Write-ins
8:Raymond Dehn>Tom Hoch>Charlie Gers
8:Raymond Dehn>Tom Hoch>Ian Simpson
8:Raymond Dehn>Tom Hoch>Ronald Lischeid
8:Ronald Lischeid>L.A. Nik>Charlie Gers
8:Tom Hoch>Betsy Hodges>Ian Simpson
8:Tom Hoch>Gregg A. Iverson>Nekima Levy-Pounds
8:Tom Hoch>Gregg A. Iverson>Ronald Lischeid
8:Tom Hoch>L.A. Nik>Raymond Dehn
8:Tom Hoch>Raymond Dehn>Ian Simpson
7:Al Flowers>Aswar Rahman
7:Al Flowers>Aswar Rahman>Tom Hoch
7:Al Flowers>Jacob Frey>Betsy Hodges
7:Aswar Rahman>Al Flowers
7:Aswar Rahman>Tom Hoch>Raymond Dehn
7:Betsy Hodges>Charlie Gers>Gregg A. Iverson
7:Betsy Hodges>Charlie Gers>Ian Simpson
7:Betsy Hodges>Charlie Gers>L.A. Nik
7:Betsy Hodges>David Rosenfeld>Aswar Rahman
7:Betsy Hodges>L.A. Nik
7:Betsy Hodges>Nekima Levy-Pounds>Charlie Gers
7:Betsy Hodges>Ronald Lischeid
7:Captain Jack Sparrow>Raymond Dehn>Tom Hoch
7:Charlie Gers>Captain Jack Sparrow>David John Wilson
7:Charlie Gers>Captain Jack Sparrow>Ian Simpson
7:Charlie Gers>David John Wilson>Captain Jack Sparrow
7:Charlie Gers>Ian Simpson>L.A. Nik
7:Charlie Gers>Tom Hoch>David John Wilson
7:David Rosenfeld>Nekima Levy-Pounds>Aswar Rahman
7:David Rosenfeld>Tom Hoch>Betsy Hodges
7:Gregg A. Iverson>Betsy Hodges>Aswar Rahman
7:Gregg A. Iverson>Jacob Frey
7:Gregg A. Iverson>Tom Hoch>Betsy Hodges
7:Jacob Frey>Aswar Rahman>Gregg A. Iverson
7:Jacob Frey>Aswar Rahman>L.A. Nik
7:Jacob Frey>Captain Jack Sparrow>Gregg A. Iverson
7:Jacob Frey>Charlie Gers>Aswar Rahman
7:Jacob Frey>Charlie Gers>Gregg A. Iverson
7:Jacob Frey>David John Wilson>Tom Hoch
7:Jacob Frey>Nekima Levy-Pounds>Ronald Lischeid
7:Jacob Frey>Raymond Dehn>Troy Benjegerdes
7:Jacob Frey>Ronald Lischeid>Tom Hoch
7:Jacob Frey>Troy Benjegerdes
7:L.A. Nik>Charlie Gers>Captain Jack Sparrow
7:L.A. Nik>Ronald Lischeid>Ian Simpson
7:Nekima Levy-Pounds>Al Flowers>Charlie Gers
7:Nekima Levy-Pounds>Al Flowers>Undeclared Write-ins
7:Nekima Levy-Pounds>Jacob Frey>Ian Simpson
7:Nekima Levy-Pounds>Jacob Frey>Ronald Lischeid
7:Nekima Levy-Pounds>L.A. Nik>Captain Jack Sparrow
7:Raymond Dehn>Betsy Hodges>Ronald Lischeid
7:Raymond Dehn>David Rosenfeld>Al Flowers
7:Raymond Dehn>Jacob Frey>Troy Benjegerdes
7:Raymond Dehn>L.A. Nik
7:Ronald Lischeid>Charlie Gers>L.A. Nik
7:Tom Hoch>Aswar Rahman>Ronald Lischeid
7:Tom Hoch>Captain Jack Sparrow>Gregg A. Iverson
7:Tom Hoch>Charlie Gers>Al Flowers
7:Tom Hoch>David John Wilson>Betsy Hodges
7:Tom Hoch>David Rosenfeld>Al Flowers
7:Tom Hoch>L.A. Nik>Gregg A. Iverson
7:Tom Hoch>Nekima Levy-Pounds>Ronald Lischeid
7:Tom Hoch>Ronald Lischeid>Captain Jack Sparrow
7:Tom Hoch>Ronald Lischeid>David John Wilson
7:Troy Benjegerdes>Jacob Frey>Tom Hoch
6:Al Flowers>Captain Jack Sparrow
6:Al Flowers>Jacob Frey>Nekima Levy-Pounds
6:Al Flowers>Jacob Frey>Raymond Dehn
6:Al Flowers>Nekima Levy-Pounds>Aswar Rahman
6:Al Flowers>Nekima Levy-Pounds>Gregg A. Iverson
6:Al Flowers>Tom Hoch>Aswar Rahman
6:Aswar Rahman>Al Flowers>Betsy Hodges
6:Aswar Rahman>Tom Hoch>Al Flowers
6:Aswar Rahman>Tom Hoch>Gregg A. Iverson
6:Betsy Hodges>Al Flowers>David John Wilson
6:Betsy Hodges>Al Flowers>David Rosenfeld
6:Betsy Hodges>Captain Jack Sparrow>L.A. Nik
6:Betsy Hodges>Charlie Gers>Jacob Frey
6:Betsy Hodges>Charlie Gers>Raymond Dehn
6:Betsy Hodges>David John Wilson>Captain Jack Sparrow
6:Betsy Hodges>Gregg A. Iverson>David Rosenfeld
6:Betsy Hodges>Ian Simpson>Captain Jack Sparrow
6:Betsy Hodges>Jacob Frey>Ian Simpson
6:Betsy Hodges>Jacob Frey>Troy Benjegerdes
6:Betsy Hodges>L.A. Nik>Tom Hoch
6:Betsy Hodges>Raymond Dehn>Ian Simpson
6:Captain Jack Sparrow>Betsy Hodges>Al Flowers
6:Captain Jack Sparrow>Betsy Hodges>Raymond Dehn
6:Captain Jack Sparrow>Raymond Dehn>Betsy Hodges
6:Charlie Gers>Ian Simpson
6:Charlie Gers>Ian Simpson>Jacob Frey
6:Charlie Gers>Ian Simpson>Ronald Lischeid
6:Charlie Gers>Jacob Frey>Nekima Levy-Pounds
6:Charlie Gers>L.A. Nik>Betsy Hodges
6:Charlie Gers>Ronald Lischeid>David John Wilson
6:Charlie Gers>Ronald Lischeid>Tom Hoch
6:Charlie Gers>Tom Hoch>Aswar Rahman
6:David Rosenfeld>Betsy Hodges>Tom Hoch
6:David Rosenfeld>Nekima Levy-Pounds>Tom Hoch
6:David Rosenfeld>Raymond Dehn>Captain Jack Sparrow
6:David Rosenfeld>Raymond Dehn>Tom Hoch
6:Gregg A. Iverson>Tom Hoch>Jacob Frey
6:Jacob Frey>Betsy Hodges>Ronald Lischeid
6:Jacob Frey>Captain Jack Sparrow>Al Flowers
6:Jacob Frey>David John Wilson>Raymond Dehn
6:Jacob Frey>David Rosenfeld>Gregg A. Iverson
6:Jacob Frey>David Rosenfeld>Nekima Levy-Pounds
6:Jacob Frey>L.A. Nik>Ronald Lischeid
6:Jacob Frey>Raymond Dehn>Ian Simpson
6:Jacob Frey>Ronald Lischeid
6:L.A. Nik>Captain Jack Sparrow>Ian Simpson
6:Nekima Levy-Pounds>Al Flowers>Ronald Lischeid
6:Nekima Levy-Pounds>Aswar Rahman>Gregg A. Iverson
6:Nekima Levy-Pounds>Betsy Hodges>Ronald Lischeid
6:Nekima Levy-Pounds>Betsy Hodges>Troy Benjegerdes
6:Nekima Levy-Pounds>Captain Jack Sparrow>L.A. Nik
6:Nekima Levy-Pounds>Captain Jack Sparrow>Undeclared Write-ins
6:Nekima Levy-Pounds>Charlie Gers>Captain Jack Sparrow
6:Nekima Levy-Pounds>Charlie Gers>Raymond Dehn
6:Nekima Levy-Pounds>Raymond Dehn>Charlie Gers
6:Nekima Levy-Pounds>Ronald Lischeid
6:Nekima Levy-Pounds>Ronald Lischeid>Betsy Hodges
6:Nekima Levy-Pounds>Tom Hoch>Charlie Gers
6:Raymond Dehn>Aswar Rahman>L.A. Nik
6:Raymond Dehn>Captain Jack Sparrow>Al Flowers
6:Raymond Dehn>Captain Jack Sparrow>Undeclared Write-ins
6:Raymond Dehn>David John Wilson>Tom Hoch
6:Raymond Dehn>Gregg A. Iverson
6:Raymond Dehn>Gregg A. Iverson>Jacob Frey
6:Raymond Dehn>Gregg A. Iverson>Nekima Levy-Pounds
6:Raymond Dehn>L.A. Nik>Tom Hoch
6:Raymond Dehn>Tom Hoch>Troy Benjegerdes
6:Ronald Lischeid>Charlie Gers
6:Ronald Lischeid>L.A. Nik
6:Ronald Lischeid>Raymond Dehn>Jacob Frey
6:Ronald Lischeid>Tom Hoch>Betsy Hodges
6:Tom Hoch>Captain Jack Sparrow>Ronald Lischeid
6:Tom Hoch>Captain Jack Sparrow>Troy Benjegerdes
6:Tom Hoch>Captain Jack Sparrow>Undeclared Write-ins
6:Tom Hoch>Charlie Gers>Troy Benjegerdes
6:Tom Hoch>David John Wilson>Aswar Rahman
6:Tom Hoch>David John Wilson>Ronald Lischeid
6:Tom Hoch>David Rosenfeld>David John Wilson
6:Tom Hoch>David Rosenfeld>Raymond Dehn
6:Tom Hoch>Gregg A. Iverson>Charlie Gers
6:Tom Hoch>Ian Simpson
6:Tom Hoch>Troy Benjegerdes>Captain Jack Sparrow
6:Troy Benjegerdes>Jacob Frey>Betsy Hodges
5:Al Flowers>Betsy Hodges>Gregg A. Iverson
5:Al Flowers>Nekima Levy-Pounds>Captain Jack Sparrow
5:Al Flowers>Tom Hoch>Captain Jack Sparrow
5:Aswar Rahman>Nekima Levy-Pounds>Captain Jack Sparrow
5:Aswar Rahman>Nekima Levy-Pounds>David Rosenfeld
5:Aswar Rahman>Tom Hoch>Charlie Gers
5:Betsy Hodges>Al Flowers>L.A. Nik
5:Betsy Hodges>Aswar Rahman>Charlie Gers
5:Betsy Hodges>Aswar Rahman>L.A. Nik
5:Betsy Hodges>Aswar Rahman>Ronald Lischeid
5:Betsy Hodges>Captain Jack Sparrow>Aswar Rahman
5:Betsy Hodges>Captain Jack Sparrow>Ian Simpson
5:Betsy Hodges>Charlie Gers>Tom Hoch
5:Betsy Hodges>David John Wilson>Al Flowers
5:Betsy Hodges>David Rosenfeld>David John Wilson
5:Betsy Hodges>David Rosenfeld>Raymond Dehn
5:Betsy Hodges>Gregg A. Iverson>Charlie Gers
5:Betsy Hodges>Ian Simpson
5:Betsy Hodges>L.A. Nik>Charlie Gers
5:Betsy Hodges>L.A. Nik>Nekima Levy-Pounds
5:Betsy Hodges>Raymond Dehn>Charlie Gers
5:Betsy Hodges>Raymond Dehn>Ronald Lischeid
5:Betsy Hodges>Raymond Dehn>Undeclared Write-ins
5:Betsy Hodges>Ronald Lischeid>David John Wilson
5:Betsy Hodges>Troy Benjegerdes>Tom Hoch
5:Captain Jack Sparrow>Betsy Hodges
5:Captain Jack Sparrow>David John Wilson>Charlie Gers
5:Captain Jack Sparrow>L.A. Nik>David John Wilson
5:Captain Jack Sparrow>L.A. Nik>Jacob Frey
5:Captain Jack Sparrow>Raymond Dehn>Jacob Frey
5:Captain Jack Sparrow>Ronald Lischeid>L.A. Nik
5:Captain Jack Sparrow>Tom Hoch
5:Charlie Gers>Aswar Rahman>Jacob Frey
5:Charlie Gers>Betsy Hodges>Gregg A. Iverson
5:Charlie Gers>L.A. Nik>Troy Benjegerdes
5:David John Wilson>Jacob Frey
5:David John Wilson>Jacob Frey>Betsy Hodges
5:David Rosenfeld>Aswar Rahman>Nekima Levy-Pounds
5:David Rosenfeld>Betsy Hodges
5:David Rosenfeld>Jacob Frey
5:David Rosenfeld>Jacob Frey>Betsy Hodges
5:David Rosenfeld>Nekima Levy-Pounds>Captain Jack Sparrow
5:Gregg A. Iverson>Betsy Hodges>Captain Jack Sparrow
5:Gregg A. Iverson>Tom Hoch>Raymond Dehn
5:Ian Simpson>Jacob Frey>Tom Hoch
5:Jacob Frey>Al Flowers>David Rosenfeld
5:Jacob Frey>Aswar Rahman>David Rosenfeld
5:Jacob Frey>Aswar Rahman>Ronald Lischeid
5:Jacob Frey>Captain Jack Sparrow>Charlie Gers
5:Jacob Frey>Captain Jack Sparrow>Ian Simpson
5:Jacob Frey>Captain Jack Sparrow>Ronald Lischeid
5:Jacob Frey>Charlie Gers>Ronald Lischeid
5:Jacob Frey>David John Wilson>Al Flowers
5:Jacob Frey>David Rosenfeld>Troy Benjegerdes
5:Jacob Frey>Gregg A. Iverson>David Rosenfeld
5:Jacob Frey>Gregg A. Iverson>L.A. Nik
5:Jacob Frey>Gregg A. Iverson>Ronald Lischeid
5:Jacob Frey>L.A. Nik>Raymond Dehn
5:Jacob Frey>Raymond Dehn>Ronald Lischeid
5:Jacob Frey>Raymond Dehn>Undeclared Write-ins
5:Jacob Frey>Ronald Lischeid>Betsy Hodges
5:Jacob Frey>Troy Benjegerdes>Betsy Hodges
5:Jacob Frey>Troy Benjegerdes>Captain Jack Sparrow
5:Jacob Frey>Troy Benjegerdes>Tom Hoch
5:L.A. Nik>Al Flowers
5:L.A. Nik>Captain Jack Sparrow
5:L.A. Nik>Captain Jack Sparrow>Tom Hoch
5:L.A. Nik>Ian Simpson>Charlie Gers
5:L.A. Nik>Ian Simpson>Ronald Lischeid
5:L.A. Nik>Jacob Frey>Captain Jack Sparrow
5:L.A. Nik>Jacob Frey>Nekima Levy-Pounds
5:L.A. Nik>Jacob Frey>Raymond Dehn
5:L.A. Nik>Tom Hoch>Ronald Lischeid
5:Nekima Levy-Pounds>Al Flowers>David John Wilson
5:Nekima Levy-Pounds>Aswar Rahman>L.A. Nik
5:Nekima Levy-Pounds>Betsy Hodges>Ian Simpson
5:Nekima Levy-Pounds>Captain Jack Sparrow>Aswar Rahman
5:Nekima Levy-Pounds>Captain Jack Sparrow>Tom Hoch
5:Nekima Levy-Pounds>Charlie Gers>Jacob Frey
5:Nekima Levy-Pounds>David John Wilson>Tom Hoch
5:Nekima Levy-Pounds>Gregg A. Iverson>Charlie Gers
5:Nekima Levy-Pounds>Jacob Frey>L.A. Nik
5:Raymond Dehn>Aswar Rahman>David John Wilson
5:Raymond Dehn>Aswar Rahman>Gregg A. Iverson
5:Raymond Dehn>Betsy Hodges>Ian Simpson
5:Raymond Dehn>Betsy Hodges>L.A. Nik
5:Raymond Dehn>Betsy Hodges>Troy Benjegerdes
5:Raymond Dehn>Captain Jack Sparrow>L.A. Nik
5:Raymond Dehn>Charlie Gers>Betsy Hodges
5:Raymond Dehn>David John Wilson
5:Raymond Dehn>David Rosenfeld>Aswar Rahman
5:Raymond Dehn>L.A. Nik>Captain Jack Sparrow
5:Raymond Dehn>L.A. Nik>Ian Simpson
5:Raymond Dehn>Tom Hoch>Undeclared Write-ins
5:Ronald Lischeid>David John Wilson>Captain Jack Sparrow
5:Ronald Lischeid>Jacob Frey>Tom Hoch
5:Tom Hoch>Al Flowers>Ronald Lischeid
5:Tom Hoch>Betsy Hodges>Troy Benjegerdes
5:Tom Hoch>Charlie Gers>David Rosenfeld
5:Tom Hoch>Charlie Gers>Undeclared Write-ins
5:Tom Hoch>Ian Simpson>Jacob Frey
5:Tom Hoch>Nekima Levy-Pounds>Ian Simpson
5:Tom Hoch>Ronald Lischeid>Betsy Hodges
5:Tom Hoch>Ronald Lischeid>Gregg A. Iverson
5:Troy Benjegerdes>Jacob Frey>Nekima Levy-Pounds
5:Undeclared Write-ins>Jacob Frey>Tom Hoch
4:Al Flowers>Aswar Rahman>Betsy Hodges
4:Al Flowers>Aswar Rahman>Jacob Frey
4:Al Flowers>Gregg A. Iverson
4:Al Flowers>Jacob Frey>Captain Jack Sparrow
4:Al Flowers>Jacob Frey>Gregg A. Iverson
4:Aswar Rahman>Betsy Hodges>Al Flowers
4:Aswar Rahman>Charlie Gers
4:Aswar Rahman>David John Wilson
4:Aswar Rahman>Nekima Levy-Pounds>Tom Hoch
4:Aswar Rahman>Raymond Dehn>Al Flowers
4:Aswar Rahman>Raymond Dehn>Betsy Hodges
4:Aswar Rahman>Raymond Dehn>David Rosenfeld
4:Betsy Hodges>Al Flowers>Troy Benjegerdes
4:Betsy Hodges>Aswar Rahman>David John Wilson
4:Betsy Hodges>Aswar Rahman>Troy Benjegerdes
4:Betsy Hodges>Captain Jack Sparrow>Al Flowers
4:Betsy Hodges>Captain Jack Sparrow>David Rosenfeld
4:Betsy Hodges>Captain Jack Sparrow>Raymond Dehn
4:Betsy Hodges>David John Wilson>Nekima Levy-Pounds
4:Betsy Hodges>David John Wilson>Ronald Lischeid
4:Betsy Hodges>David Rosenfeld>Al Flowers
4:Betsy Hodges>David Rosenfeld>Charlie Gers
4:Betsy Hodges>Gregg A. Iverson>David John Wilson
4:Betsy Hodges>Gregg A. Iverson>Troy Benjegerdes
4:Betsy Hodges>L.A. Nik>Al Flowers
4:Betsy Hodges>L.A. Nik>Captain Jack Sparrow
4:Betsy Hodges>L.A. Nik>Jacob Frey
4:Betsy Hodges>Nekima Levy-Pounds>Troy Benjegerdes
4:Betsy Hodges>Ronald Lischeid>Captain Jack Sparrow
4:Betsy Hodges>Ronald Lischeid>Charlie Gers
4:Betsy Hodges>Ronald Lischeid>Ian Simpson
4:Betsy Hodges>Ronald Lischeid>Tom Hoch
4:Betsy Hodges>Tom Hoch>Undeclared Write-ins
4:Betsy Hodges>Troy Benjegerdes
4:Captain Jack Sparrow>Al Flowers
4:Captain Jack Sparrow>Betsy Hodges>Tom Hoch
4:Captain Jack Sparrow>David Rosenfeld>L.A. Nik
4:Captain Jack Sparrow>David Rosenfeld>Tom Hoch
4:Captain Jack Sparrow>Jacob Frey>Nekima Levy-Pounds
4:Captain Jack Sparrow>L.A. Nik>Ronald Lischeid
4:Captain Jack Sparrow>Nekima Levy-Pounds>Betsy Hodges
4:Captain Jack Sparrow>Nekima Levy-Pounds>Tom Hoch
4:Captain Jack Sparrow>Raymond Dehn>Nekima Levy-Pounds
4:Charlie Gers>Betsy Hodges>Tom Hoch
4:Charlie Gers>Captain Jack Sparrow>Jacob Frey
4:Charlie Gers>Captain Jack Sparrow>Tom Hoch
4:Charlie Gers>David John Wilson>Jacob Frey
4:Charlie Gers>Ian Simpson>Captain Jack Sparrow
4:Charlie Gers>Jacob Frey>Gregg A. Iverson
4:Charlie Gers>Jacob Frey>L.A. Nik
4:Charlie Gers>Jacob Frey>Raymond Dehn
4:Charlie Gers>Raymond Dehn>Betsy Hodges
4:Charlie Gers>Tom Hoch>Ian Simpson
4:Charlie Gers>Tom Hoch>Nekima Levy-Pounds
4:Charlie Gers>Troy Benjegerdes
4:David John Wilson>Captain Jack Sparrow>Ian Simpson
4:David John Wilson>Jacob Frey>Tom Hoch
4:David John Wilson>Tom Hoch>Betsy Hodges
4:David Rosenfeld>Aswar Rahman>Betsy Hodges
4:David Rosenfeld>Betsy Hodges>David John Wilson
4:David Rosenfeld>Betsy Hodges>Jacob Frey
4:David Rosenfeld>Captain Jack Sparrow>David John Wilson
4:David Rosenfeld>Captain Jack Sparrow>Raymond Dehn
4:David Rosenfeld>David John Wilson>Captain Jack Sparrow
4:David Rosenfeld>Raymond Dehn
4:David Rosenfeld>Tom Hoch>Nekima Levy-Pounds
4:David Rosenfeld>Troy Benjegerdes>Raymond Dehn
4:Gregg A. Iverson>Betsy Hodges>Al Flowers
4:Gregg A. Iverson>Betsy Hodges>Nekima Levy-Pounds
4:Gregg A. Iverson>Nekima Levy-Pounds
4:Gregg A. Iverson>Tom Hoch>Al Flowers
4:Gregg A. Iverson>Tom Hoch>Nekima Levy-Pounds
4:Ian Simpson>Troy Benjegerdes>Captain Jack Sparrow
4:Jacob Frey>Al Flowers>David John Wilson
4:Jacob Frey>Al Flowers>L.A. Nik
4:Jacob Frey>Al Flowers>Ronald Lischeid
4:Jacob Frey>Al Flowers>Troy Benjegerdes
4:Jacob Frey>Aswar Rahman>Undeclared Write-ins
4:Jacob Frey>Captain Jack Sparrow>Aswar Rahman
4:Jacob Frey>Charlie Gers>David Rosenfeld
4:Jacob Frey>David Rosenfeld>David John Wilson
4:Jacob Frey>Ian Simpson
4:Jacob Frey>Ian Simpson>Captain Jack Sparrow
4:Jacob Frey>L.A. Nik>Nekima Levy-Pounds
4:Jacob Frey>Nekima Levy-Pounds>Troy Benjegerdes
4:Jacob Frey>Nekima Levy-Pounds>Undeclared Write-ins
4:Jacob Frey>Ronald Lischeid>Charlie Gers
4:Jacob Frey>Ronald Lischeid>Ian Simpson
4:Jacob Frey>Ronald Lischeid>Nekima Levy-Pounds
4:Jacob Frey>Troy Benjegerdes>Nekima Levy-Pounds
4:Jacob Frey>Troy Benjegerdes>Raymond Dehn
4:L.A. Nik>Captain Jack Sparrow>David John Wilson
4:L.A. Nik>Charlie Gers>Jacob Frey
4:L.A. Nik>Gregg A. Iverson
4:L.A. Nik>Jacob Frey
4:L.A. Nik>Jacob Frey>Ian Simpson
4:L.A. Nik>Ronald Lischeid>Tom Hoch
4:Nekima Levy-Pounds>Al Flowers>Ian Simpson
4:Nekima Levy-Pounds>Aswar Rahman>Charlie Gers
4:Nekima Levy-Pounds>Aswar Rahman>David John Wilson
4:Nekima Levy-Pounds>Aswar Rahman>Ian Simpson
4:Nekima Levy-Pounds>Aswar Rahman>Ronald Lischeid
4:Nekima Levy-Pounds>Captain Jack Sparrow>Charlie Gers
4:Nekima Levy-Pounds>Captain Jack Sparrow>Ian Simpson
4:Nekima Levy-Pounds>Charlie Gers
4:Nekima Levy-Pounds>Charlie Gers>Betsy Hodges
4:Nekima Levy-Pounds>David John Wilson>Betsy Hodges
4:Nekima Levy-Pounds>David John Wilson>Jacob Frey
4:Nekima Levy-Pounds>David Rosenfeld>Undeclared Write-ins
4:Nekima Levy-Pounds>Gregg A. Iverson>Raymond Dehn
4:Nekima Levy-Pounds>L.A. Nik
4:Nekima Levy-Pounds>L.A. Nik>Charlie Gers
4:Nekima Levy-Pounds>L.A. Nik>Jacob Frey
4:Raymond Dehn>Al Flowers>David John Wilson
4:Raymond Dehn>Aswar Rahman>Ronald Lischeid
4:Raymond Dehn>Captain Jack Sparrow>Ian Simpson
4:Raymond Dehn>Charlie Gers>Captain Jack Sparrow
4:Raymond Dehn>Charlie Gers>L.A. Nik
4:Raymond Dehn>Charlie Gers>Nekima Levy-Pounds
4:Raymond Dehn>David John Wilson>Betsy Hodges
4:Raymond Dehn>David John Wilson>Nekima Levy-Pounds
4:Raymond Dehn>David Rosenfeld>Troy Benjegerdes
4:Raymond Dehn>Gregg A. Iverson>Betsy Hodges
4:Raymond Dehn>L.A. Nik>Betsy Hodges
4:Raymond Dehn>Ronald Lischeid
4:Ronald Lischeid>Betsy Hodges
4:Ronald Lischeid>Jacob Frey
4:Ronald Lischeid>L.A. Nik>David Rosenfeld
4:Ronald Lischeid>L.A. Nik>Ian Simpson
4:Ronald Lischeid>Tom Hoch
4:Ronald Lischeid>Tom Hoch>Raymond Dehn
4:Tom Hoch>Al Flowers>Troy Benjegerdes
4:Tom Hoch>Aswar Rahman>Troy Benjegerdes
4:Tom Hoch>Betsy Hodges>Undeclared Write-ins
4:Tom Hoch>Charlie Gers>Gregg A. Iverson
4:Tom Hoch>Gregg A. Iverson>L.A. Nik
4:Tom Hoch>Ian Simpson>Betsy Hodges
4:Tom Hoch>L.A. Nik>Aswar Rahman
4:Tom Hoch>Nekima Levy-Pounds>Troy Benjegerdes
4:Tom Hoch>Ronald Lischeid>Al Flowers
4:Tom Hoch>Ronald Lischeid>Aswar Rahman
4:Tom Hoch>Ronald Lischeid>Ian Simpson
4:Tom Hoch>Ronald Lischeid>Raymond Dehn
4:Tom Hoch>Troy Benjegerdes>Aswar Rahman
4:Tom Hoch>Undeclared Write-ins>Jacob Frey
4:Troy Benjegerdes>Nekima Levy-Pounds>Al Flowers
4:Troy Benjegerdes>Raymond Dehn>Nekima Levy-Pounds
4:Undeclared Write-ins>L.A. Nik
3:Al Flowers>Betsy Hodges>Captain Jack Sparrow
3:Al Flowers>Betsy Hodges>Troy Benjegerdes
3:Al Flowers>Captain Jack Sparrow>Raymond Dehn
3:Al Flowers>Charlie Gers>L.A. Nik
3:Al Flowers>David John Wilson>Nekima Levy-Pounds
3:Al Flowers>David Rosenfeld>Tom Hoch
3:Al Flowers>Jacob Frey>Aswar Rahman
3:Al Flowers>L.A. Nik
3:Al Flowers>Raymond Dehn>Aswar Rahman
3:Al Flowers>Raymond Dehn>Ronald Lischeid
3:Al Flowers>Tom Hoch>Troy Benjegerdes
3:Aswar Rahman>Al Flowers>Captain Jack Sparrow
3:Aswar Rahman>Al Flowers>Jacob Frey
3:Aswar Rahman>Al Flowers>Nekima Levy-Pounds
3:Aswar Rahman>Al Flowers>Ronald Lischeid
3:Aswar Rahman>Betsy Hodges>Captain Jack Sparrow
3:Aswar Rahman>Betsy Hodges>David John Wilson
3:Aswar Rahman>Betsy Hodges>Troy Benjegerdes
3:Aswar Rahman>Captain Jack Sparrow
3:Aswar Rahman>Captain Jack Sparrow>Tom Hoch
3:Aswar Rahman>Jacob Frey>Al Flowers
3:Aswar Rahman>Jacob Frey>Charlie Gers
3:Aswar Rahman>Jacob Frey>Gregg A. Iverson
3:Aswar Rahman>Nekima Levy-Pounds>Gregg A. Iverson
3:Aswar Rahman>Nekima Levy-Pounds>L.A. Nik
3:Aswar Rahman>Raymond Dehn>Captain Jack Sparrow
3:Aswar Rahman>Ronald Lischeid>Tom Hoch
3:Aswar Rahman>Tom Hoch>L.A. Nik
3:Aswar Rahman>Tom Hoch>Ronald Lischeid
3:Aswar Rahman>Troy Benjegerdes
3:Betsy Hodges>Charlie Gers>Al Flowers
3:Betsy Hodges>Charlie Gers>David John Wilson
3:Betsy Hodges>David John Wilson>Ian Simpson
3:Betsy Hodges>David John Wilson>Jacob Frey
3:Betsy Hodges>David John Wilson>Tom Hoch
3:Betsy Hodges>David Rosenfeld>Troy Benjegerdes
3:Betsy Hodges>Gregg A. Iverson>Ronald Lischeid
3:Betsy Hodges>Ian Simpson>David John Wilson
3:Betsy Hodges>Ian Simpson>Nekima Levy-Pounds
3:Betsy Hodges>L.A. Nik>David John Wilson
3:Betsy Hodges>L.A. Nik>Ronald Lischeid
3:Betsy Hodges>Ronald Lischeid>L.A. Nik
3:Betsy Hodges>Troy Benjegerdes>Captain Jack Sparrow
3:Captain Jack Sparrow>Al Flowers>Betsy Hodges
3:Captain Jack Sparrow>Al Flowers>Tom Hoch
3:Captain Jack Sparrow>Aswar Rahman>Tom Hoch
3:Captain Jack Sparrow>Betsy Hodges>Nekima Levy-Pounds
3:Captain Jack Sparrow>Charlie Gers>Jacob Frey
3:Captain Jack Sparrow>David John Wilson
3:Captain Jack Sparrow>David John Wilson>Betsy Hodges
3:Captain Jack Sparrow>David John Wilson>David Rosenfeld
3:Captain Jack Sparrow>David John Wilson>Ian Simpson
3:Captain Jack Sparrow>David John Wilson>Jacob Frey
3:Captain Jack Sparrow>David John Wilson>L.A. Nik
3:Captain Jack Sparrow>David Rosenfeld>Betsy Hodges
3:Captain Jack Sparrow>David Rosenfeld>Ian Simpson
3:Captain Jack Sparrow>David Rosenfeld>Jacob Frey
3:Captain Jack Sparrow>Ian Simpson>Charlie Gers
3:Captain Jack Sparrow>Ian Simpson>David John Wilson
3:Captain Jack Sparrow>Ian Simpson>David Rosenfeld
3:Captain Jack Sparrow>Ian Simpson>L.A. Nik
3:Captain Jack Sparrow>Jacob Frey
3:Captain Jack Sparrow>Jacob Frey>Aswar Rahman
3:Captain Jack Sparrow>Jacob Frey>L.A. Nik
3:Captain Jack Sparrow>L.A. Nik
3:Captain Jack Sparrow>L.A. Nik>Ian Simpson
3:Captain Jack Sparrow>Nekima Levy-Pounds>Aswar Rahman
3:Captain Jack Sparrow>Tom Hoch>Al Flowers
3:Captain Jack Sparrow>Tom Hoch>Betsy Hodges
3:Captain Jack Sparrow>Tom Hoch>Raymond Dehn
3:Charlie Gers>Betsy Hodges>Nekima Levy-Pounds
3:Charlie Gers>Captain Jack Sparrow>Ronald Lischeid
3:Charlie Gers>Captain Jack Sparrow>Undeclared Write-ins
3:Charlie Gers>David John Wilson>Ian Simpson
3:Charlie Gers>David John Wilson>Ronald Lischeid
3:Charlie Gers>David Rosenfeld>Ronald Lischeid
3:Charlie Gers>Gregg A. Iverson
3:Charlie Gers>Gregg A. Iverson>Ronald Lischeid
3:Charlie Gers>Ian Simpson>Tom Hoch
3:Charlie Gers>Ian Simpson>Undeclared Write-ins
3:Charlie Gers>L.A. Nik>Aswar Rahman
3:Charlie Gers>L.A. Nik>Nekima Levy-Pounds
3:Charlie Gers>Nekima Levy-Pounds>Jacob Frey
3:Charlie Gers>Raymond Dehn>Jacob Frey
3:Charlie Gers>Ronald Lischeid>Captain Jack Sparrow
3:Charlie Gers>Ronald Lischeid>Troy Benjegerdes
3:Charlie Gers>Tom Hoch>Al Flowers
3:Charlie Gers>Tom Hoch>Raymond Dehn
3:Charlie Gers>Tom Hoch>Troy Benjegerdes
3:Charlie Gers>Tom Hoch>Undeclared Write-ins
3:Charlie Gers>Troy Benjegerdes>Ronald Lischeid
3:David John Wilson>Charlie Gers
3:David John Wilson>Ian Simpson>Captain Jack Sparrow
3:David John Wilson>Jacob Frey>Captain Jack Sparrow
3:David John Wilson>Nekima Levy-Pounds>Jacob Frey
3:David John Wilson>Raymond Dehn>Jacob Frey
3:David Rosenfeld>Al Flowers>Raymond Dehn
3:David Rosenfeld>Aswar Rahman
3:David Rosenfeld>Aswar Rahman>L.A. Nik
3:David Rosenfeld>Betsy Hodges>Al Flowers
3:David Rosenfeld>Betsy Hodges>Aswar Rahman
3:David Rosenfeld>Betsy Hodges>L.A. Nik
3:David Rosenfeld>Captain Jack Sparrow>Jacob Frey
3:David Rosenfeld>David John Wilson
3:David Rosenfeld>Ian Simpson>Charlie Gers
3:David Rosenfeld>Jacob Frey>Raymond Dehn
3:David Rosenfeld>Raymond Dehn>Ian Simpson
3:David Rosenfeld>Raymond Dehn>Troy Benjegerdes
3:David Rosenfeld>Ronald Lischeid>Captain Jack Sparrow
3:David Rosenfeld>Tom Hoch
3:David Rosenfeld>Tom Hoch>Jacob Frey
3:David Rosenfeld>Tom Hoch>Ronald Lischeid
3:David Rosenfeld>Troy Benjegerdes>Betsy Hodges
3:Gregg A. Iverson>Al Flowers
3:Gregg A. Iverson>Betsy Hodges>Charlie Gers
3:Gregg A. Iverson>Betsy Hodges>David Rosenfeld
3:Gregg A. Iverson>Betsy Hodges>Raymond Dehn
3:Gregg A. Iverson>Captain Jack Sparrow>Troy Benjegerdes
3:Gregg A. Iverson>Nekima Levy-Pounds>Betsy Hodges
3:Gregg A. Iverson>Nekima Levy-Pounds>Jacob Frey
3:Gregg A. Iverson>Raymond Dehn>Betsy Hodges
3:Gregg A. Iverson>Raymond Dehn>Tom Hoch
3:Gregg A. Iverson>Troy Benjegerdes>Al Flowers
3:Ian Simpson>Charlie Gers>L.A. Nik
3:Ian Simpson>Ronald Lischeid
3:Jacob Frey>Captain Jack Sparrow>Troy Benjegerdes
3:Jacob Frey>Captain Jack Sparrow>Undeclared Write-ins
3:Jacob Frey>David John Wilson>Betsy Hodges
3:Jacob Frey>David John Wilson>Nekima Levy-Pounds
3:Jacob Frey>David John Wilson>Ronald Lischeid
3:Jacob Frey>David Rosenfeld>Aswar Rahman
3:Jacob Frey>David Rosenfeld>Charlie Gers
3:Jacob Frey>Gregg A. Iverson>David John Wilson
3:Jacob Frey>Gregg A. Iverson>Ian Simpson
3:Jacob Frey>Ian Simpson>Tom Hoch
3:Jacob Frey>L.A. Nik>Al Flowers
3:Jacob Frey>L.A. Nik>Betsy Hodges
3:Jacob Frey>Ronald Lischeid>Gregg A. Iverson
3:Jacob Frey>Troy Benjegerdes>Al Flowers
3:Jacob Frey>Troy Benjegerdes>Charlie Gers
3:Jacob Frey>Troy Benjegerdes>David John Wilson
3:Jacob Frey>Troy Benjegerdes>David Rosenfeld
3:Jacob Frey>Troy Benjegerdes>Gregg A. Iverson
3:L.A. Nik>Al Flowers>Jacob Frey
3:L.A. Nik>Aswar Rahman>Nekima Levy-Pounds
3:L.A. Nik>Betsy Hodges
3:L.A. Nik>Captain Jack Sparrow>Betsy Hodges
3:L.A. Nik>Charlie Gers>David Rosenfeld
3:L.A. Nik>Charlie Gers>Troy Benjegerdes
3:L.A. Nik>Charlie Gers>Undeclared Write-ins
3:L.A. Nik>David John Wilson>Captain Jack Sparrow
3:L.A. Nik>David Rosenfeld>Ronald Lischeid
3:L.A. Nik>Gregg A. Iverson>Jacob Frey
3:L.A. Nik>Jacob Frey>Charlie Gers
3:L.A. Nik>Jacob Frey>David John Wilson
3:L.A. Nik>Jacob Frey>Ronald Lischeid
3:L.A. Nik>Raymond Dehn>Al Flowers
3:L.A. Nik>Ronald Lischeid
3:L.A. Nik>Ronald Lischeid>Troy Benjegerdes
3:L.A. Nik>Tom Hoch>Betsy Hodges
3:L.A. Nik>Tom Hoch>Nekima Levy-Pounds
3:L.A. Nik>Troy Benjegerdes>Charlie Gers
3:L.A. Nik>Troy Benjegerdes>Ronald Lischeid
3:Nekima Levy-Pounds>Aswar Rahman>Troy Benjegerdes
3:Nekima Levy-Pounds>David John Wilson
3:Nekima Levy-Pounds>David John Wilson>Raymond Dehn
3:Nekima Levy-Pounds>David Rosenfeld>Charlie Gers
3:Nekima Levy-Pounds>David Rosenfeld>Gregg A. Iverson
3:Nekima Levy-Pounds>Gregg A. Iverson>Al Flowers
3:Nekima Levy-Pounds>Gregg A. Iverson>Aswar Rahman
3:Nekima Levy-Pounds>Gregg A. Iverson>David Rosenfeld
3:Nekima Levy-Pounds>Ian Simpson>Captain Jack Sparrow
3:Nekima Levy-Pounds>L.A. Nik>Aswar Rahman
3:Nekima Levy-Pounds>Ronald Lischeid>Captain Jack Sparrow
3:Nekima Levy-Pounds>Ronald Lischeid>Tom Hoch
3:Nekima Levy-Pounds>Troy Benjegerdes>Captain Jack Sparrow
3:Raymond Dehn>Al Flowers>Charlie Gers
3:Raymond Dehn>Al Flowers>Gregg A. Iverson
3:Raymond Dehn>Al Flowers>Ian Simpson
3:Raymond Dehn>Aswar Rahman>Charlie Gers
3:Raymond Dehn>Charlie Gers>Jacob Frey
3:Raymond Dehn>David Rosenfeld>Charlie Gers
3:Raymond Dehn>David Rosenfeld>L.A. Nik
3:Raymond Dehn>David Rosenfeld>Undeclared Write-ins
3:Raymond Dehn>Gregg A. Iverson>Al Flowers
3:Raymond Dehn>L.A. Nik>Aswar Rahman
3:Raymond Dehn>Ronald Lischeid>Captain Jack Sparrow
3:Raymond Dehn>Ronald Lischeid>Ian Simpson
3:Raymond Dehn>Troy Benjegerdes>Nekima Levy-Pounds
3:Raymond Dehn>Undeclared Write-ins>Betsy Hodges
3:Ronald Lischeid>Betsy Hodges>Al Flowers
3:Ronald Lischeid>Captain Jack Sparrow>Ian Simpson
3:Ronald Lischeid>Charlie Gers>Captain Jack Sparrow
3:Ronald Lischeid>Charlie Gers>Jacob Frey
3:Ronald Lischeid>Charlie Gers>Tom Hoch
3:Ronald Lischeid>Charlie Gers>Undeclared Write-ins
3:Ronald Lischeid>Ian Simpson
3:Ronald Lischeid>Jacob Frey>Gregg A. Iverson
3:Ronald Lischeid>Jacob Frey>Ian Simpson
3:Ronald Lischeid>Jacob Frey>Nekima Levy-Pounds
3:Ronald Lischeid>L.A. Nik>David John Wilson
3:Ronald Lischeid>L.A. Nik>Nekima Levy-Pounds
3:Ronald Lischeid>Nekima Levy-Pounds>Jacob Frey
3:Ronald Lischeid>Tom Hoch>Gregg A. Iverson
3:Ronald Lischeid>Tom Hoch>Nekima Levy-Pounds
3:Tom Hoch>Aswar Rahman>David Rosenfeld
3:Tom Hoch>Aswar Rahman>Ian Simpson
3:Tom Hoch>David John Wilson>Charlie Gers
3:Tom Hoch>David Rosenfeld>Charlie Gers
3:Tom Hoch>David Rosenfeld>Ronald Lischeid
3:Tom Hoch>Ian Simpson>David John Wilson
3:Tom Hoch>Ian Simpson>L.A. Nik
3:Tom Hoch>L.A. Nik>David Rosenfeld
3:Tom Hoch>Ronald Lischeid>Nekima Levy-Pounds
3:Tom Hoch>Ronald Lischeid>Troy Benjegerdes
3:Tom Hoch>Troy Benjegerdes>Charlie Gers
3:Tom Hoch>Troy Benjegerdes>Gregg A. Iverson
3:Tom Hoch>Troy Benjegerdes>Jacob Frey
3:Tom Hoch>Troy Benjegerdes>L.A. Nik
3:Troy Benjegerdes>Captain Jack Sparrow
3:Troy Benjegerdes>Charlie Gers>L.A. Nik
3:Troy Benjegerdes>L.A. Nik>Charlie Gers
3:Troy Benjegerdes>Nekima Levy-Pounds>Raymond Dehn
3:Troy Benjegerdes>Raymond Dehn
3:Troy Benjegerdes>Tom Hoch
3:Troy Benjegerdes>Tom Hoch>Jacob Frey
3:Undeclared Write-ins>David John Wilson
3:Undeclared Write-ins>Tom Hoch>Jacob Frey
2:Al Flowers>Aswar Rahman>Nekima Levy-Pounds
2:Al Flowers>Betsy Hodges>David Rosenfeld
2:Al Flowers>Betsy Hodges>Ian Simpson
2:Al Flowers>Betsy Hodges>L.A. Nik
2:Al Flowers>Captain Jack Sparrow>Betsy Hodges
2:Al Flowers>Captain Jack Sparrow>David John Wilson
2:Al Flowers>Captain Jack Sparrow>L.A. Nik
2:Al Flowers>Charlie Gers
2:Al Flowers>David Rosenfeld
2:Al Flowers>David Rosenfeld>Charlie Gers
2:Al Flowers>Gregg A. Iverson>Betsy Hodges
2:Al Flowers>Jacob Frey>David John Wilson
2:Al Flowers>Jacob Frey>L.A. Nik
2:Al Flowers>Nekima Levy-Pounds>Charlie Gers
2:Al Flowers>Nekima Levy-Pounds>David John Wilson
2:Al Flowers>Nekima Levy-Pounds>Ronald Lischeid
2:Al Flowers>Raymond Dehn>Charlie Gers
2:Al Flowers>Raymond Dehn>Jacob Frey
2:Al Flowers>Tom Hoch>Gregg A. Iverson
2:Al Flowers>Tom Hoch>Ian Simpson
2:Aswar Rahman>Captain Jack Sparrow>Al Flowers
2:Aswar Rahman>Captain Jack Sparrow>Betsy Hodges
2:Aswar Rahman>Captain Jack Sparrow>David John Wilson
2:Aswar Rahman>Captain Jack Sparrow>Nekima Levy-Pounds
2:Aswar Rahman>Charlie Gers>David John Wilson
2:Aswar Rahman>Charlie Gers>Ronald Lischeid
2:Aswar Rahman>Charlie Gers>Tom Hoch
2:Aswar Rahman>David Rosenfeld>Betsy Hodges
2:Aswar Rahman>Gregg A. Iverson>Betsy Hodges
2:Aswar Rahman>Gregg A. Iverson>Raymond Dehn
2:Aswar Rahman>Jacob Frey>David Rosenfeld
2:Aswar Rahman>Raymond Dehn>Ronald Lischeid
2:Aswar Rahman>Ronald Lischeid
2:Aswar Rahman>Tom Hoch>Captain Jack Sparrow
2:Aswar Rahman>Tom Hoch>David John Wilson
2:Aswar Rahman>Tom Hoch>David Rosenfeld
2:Betsy Hodges>Al Flowers>Charlie Gers
2:Betsy Hodges>Al Flowers>Ian Simpson
2:Betsy Hodges>Al Flowers>Undeclared Write-ins
2:Betsy Hodges>Captain Jack Sparrow>Ronald Lischeid
2:Betsy Hodges>David John Wilson>David Rosenfeld
2:Betsy Hodges>David John Wilson>Troy Benjegerdes
2:Betsy Hodges>David Rosenfeld>Gregg A. Iverson
2:Betsy Hodges>David Rosenfeld>Ian Simpson
2:Betsy Hodges>David Rosenfeld>Ronald Lischeid
2:Betsy Hodges>David Rosenfeld>Undeclared Write-ins
2:Betsy Hodges>Gregg A. Iverson>L.A. Nik
2:Betsy Hodges>Ian Simpson>Aswar Rahman
2:Betsy Hodges>Ian Simpson>Charlie Gers
2:Betsy Hodges>Ian Simpson>David Rosenfeld
2:Betsy Hodges>L.A. Nik>Aswar Rahman
2:Betsy Hodges>L.A. Nik>David Rosenfeld
2:Betsy Hodges>L.A. Nik>Ian Simpson
2:Betsy Hodges>Ronald Lischeid>Aswar Rahman
2:Betsy Hodges>Ronald Lischeid>David Rosenfeld
2:Betsy Hodges>Troy Benjegerdes>Al Flowers
2:Betsy Hodges>Troy Benjegerdes>Aswar Rahman
2:Betsy Hodges>Troy Benjegerdes>David Rosenfeld
2:Betsy Hodges>Troy Benjegerdes>Gregg A. Iverson
2:Betsy Hodges>Troy Benjegerdes>Jacob Frey
2:Betsy Hodges>Troy Benjegerdes>Raymond Dehn
2:Captain Jack Sparrow>Al Flowers>David John Wilson
2:Captain Jack Sparrow>Al Flowers>Jacob Frey
2:Captain Jack Sparrow>Al Flowers>Nekima Levy-Pounds
2:Captain Jack Sparrow>Al Flowers>Raymond Dehn
2:Captain Jack Sparrow>Aswar Rahman>Nekima Levy-Pounds
2:Captain Jack Sparrow>Betsy Hodges>Jacob Frey
2:Captain Jack Sparrow>Charlie Gers>David Rosenfeld
2:Captain Jack Sparrow>Charlie Gers>Ian Simpson
2:Captain Jack Sparrow>Charlie Gers>Tom Hoch
2:Captain Jack Sparrow>David John Wilson>Aswar Rahman
2:Captain Jack Sparrow>David John Wilson>Raymond Dehn
2:Captain Jack Sparrow>David John Wilson>Ronald Lischeid
2:Captain Jack Sparrow>David Rosenfeld>Aswar Rahman
2:Captain Jack Sparrow>David Rosenfeld>Charlie Gers
2:Captain Jack Sparrow>Ian Simpson
2:Captain Jack Sparrow>Ian Simpson>Ronald Lischeid
2:Captain Jack Sparrow>Jacob Frey>David John Wilson
2:Captain Jack Sparrow>Jacob Frey>David Rosenfeld
2:Captain Jack Sparrow>Jacob Frey>Ian Simpson
2:Captain Jack Sparrow>L.A. Nik>Betsy Hodges
2:Captain Jack Sparrow>L.A. Nik>Tom Hoch
2:Captain Jack Sparrow>Nekima Levy-Pounds>Jacob Frey
2:Captain Jack Sparrow>Raymond Dehn>David John Wilson
2:Captain Jack Sparrow>Raymond Dehn>L.A. Nik
2:Captain Jack Sparrow>Ronald Lischeid>Ian Simpson
2:Captain Jack Sparrow>Tom Hoch>Aswar Rahman
2:Captain Jack Sparrow>Tom Hoch>Charlie Gers
2:Captain Jack Sparrow>Tom Hoch>David Rosenfeld
2:Captain Jack Sparrow>Tom Hoch>Ian Simpson
2:Captain Jack Sparrow>Tom Hoch>Nekima Levy-Pounds
2:Captain Jack Sparrow>Troy Benjegerdes>Ronald Lischeid
2:Charlie Gers>Al Flowers>Aswar Rahman
2:Charlie Gers>Al Flowers>Jacob Frey
2:Charlie Gers>Al Flowers>Tom Hoch
2:Charlie Gers>Aswar Rahman
2:Charlie Gers>Aswar Rahman>Al Flowers
2:Charlie Gers>Aswar Rahman>Captain Jack Sparrow
2:Charlie Gers>Aswar Rahman>L.A. Nik
2:Charlie Gers>Aswar Rahman>Ronald Lischeid
2:Charlie Gers>Betsy Hodges>Captain Jack Sparrow
2:Charlie Gers>Betsy Hodges>Ian Simpson
2:Charlie Gers>Betsy Hodges>Raymond Dehn
2:Charlie Gers>Betsy Hodges>Undeclared Write-ins
2:Charlie Gers>Captain Jack Sparrow>Raymond Dehn
2:Charlie Gers>David John Wilson
2:Charlie Gers>David John Wilson>Nekima Levy-Pounds
2:Charlie Gers>David Rosenfeld>Captain Jack Sparrow
2:Charlie Gers>David Rosenfeld>Ian Simpson
2:Charlie Gers>Gregg A. Iverson>Betsy Hodges
2:Charlie Gers>Gregg A. Iverson>Tom Hoch
2:Charlie Gers>Ian Simpson>Troy Benjegerdes
2:Charlie Gers>Jacob Frey>Al Flowers
2:Charlie Gers>Jacob Frey>Aswar Rahman
2:Charlie Gers>Jacob Frey>David John Wilson
2:Charlie Gers>Jacob Frey>David Rosenfeld
2:Charlie Gers>Jacob Frey>Ian Simpson
2:Charlie Gers>L.A. Nik>Raymond Dehn
2:Charlie Gers>Nekima Levy-Pounds>Captain Jack Sparrow
2:Charlie Gers>Nekima Levy-Pounds>Raymond Dehn
2:Charlie Gers>Nekima Levy-Pounds>Tom Hoch
2:Charlie Gers>Raymond Dehn>David John Wilson
2:Charlie Gers>Raymond Dehn>L.A. Nik
2:Charlie Gers>Raymond Dehn>Nekima Levy-Pounds
2:Charlie Gers>Raymond Dehn>Troy Benjegerdes
2:Charlie Gers>Ronald Lischeid>Betsy Hodges
2:Charlie Gers>Ronald Lischeid>Jacob Frey
2:Charlie Gers>Ronald Lischeid>Undeclared Write-ins
2:Charlie Gers>Tom Hoch>Gregg A. Iverson
2:Charlie Gers>Troy Benjegerdes>David Rosenfeld
2:Charlie Gers>Undeclared Write-ins>L.A. Nik
2:David John Wilson>Al Flowers>Raymond Dehn
2:David John Wilson>Aswar Rahman>Al Flowers
2:David John Wilson>Aswar Rahman>Tom Hoch
2:David John Wilson>Betsy Hodges>Al Flowers
2:David John Wilson>Betsy Hodges>Jacob Frey
2:David John Wilson>Betsy Hodges>Raymond Dehn
2:David John Wilson>Betsy Hodges>Tom Hoch
2:David John Wilson>Captain Jack Sparrow
2:David John Wilson>Captain Jack Sparrow>Charlie Gers
2:David John Wilson>Captain Jack Sparrow>David Rosenfeld
2:David John Wilson>Captain Jack Sparrow>Jacob Frey
2:David John Wilson>Captain Jack Sparrow>Nekima Levy-Pounds
2:David John Wilson>Captain Jack Sparrow>Ronald Lischeid
2:David John Wilson>Charlie Gers>L.A. Nik
2:David John Wilson>David Rosenfeld>Ronald Lischeid
2:David John Wilson>Gregg A. Iverson
2:David John Wilson>Ian Simpson>Tom Hoch
2:David John Wilson>Jacob Frey>Aswar Rahman
2:David John Wilson>Jacob Frey>Nekima Levy-Pounds
2:David John Wilson>Jacob Frey>Raymond Dehn
2:David John Wilson>L.A. Nik>Captain Jack Sparrow
2:David John Wilson>Nekima Levy-Pounds
2:David John Wilson>Nekima Levy-Pounds>Tom Hoch
2:David John Wilson>Raymond Dehn>Betsy Hodges
2:David John Wilson>Raymond Dehn>Nekima Levy-Pounds
2:David John Wilson>Ronald Lischeid>L.A. Nik
2:David John Wilson>Tom Hoch>Captain Jack Sparrow
2:David John Wilson>Tom Hoch>Nekima Levy-Pounds
2:David John Wilson>Troy Benjegerdes
2:David Rosenfeld>Al Flowers>Nekima Levy-Pounds
2:David Rosenfeld>Al Flowers>Ronald Lischeid
2:David Rosenfeld>Aswar Rahman>Al Flowers
2:David Rosenfeld>Betsy Hodges>Gregg A. Iverson
2:David Rosenfeld>Captain Jack Sparrow>Ian Simpson
2:David Rosenfeld>Captain Jack Sparrow>Nekima Levy-Pounds
2:David Rosenfeld>Captain Jack Sparrow>Troy Benjegerdes
2:David Rosenfeld>Charlie Gers>Captain Jack Sparrow
2:David Rosenfeld>Charlie Gers>Ronald Lischeid
2:David Rosenfeld>David John Wilson>Nekima Levy-Pounds
2:David Rosenfeld>Ian Simpson>Captain Jack Sparrow
2:David Rosenfeld>Jacob Frey>Gregg A. Iverson
2:David Rosenfeld>Jacob Frey>Tom Hoch
2:David Rosenfeld>L.A. Nik>Raymond Dehn
2:David Rosenfeld>Nekima Levy-Pounds>David John Wilson
2:David Rosenfeld>Ronald Lischeid
2:David Rosenfeld>Ronald Lischeid>David John Wilson
2:David Rosenfeld>Tom Hoch>Captain Jack Sparrow
2:David Rosenfeld>Tom Hoch>Raymond Dehn
2:David Rosenfeld>Troy Benjegerdes>David John Wilson
2:Gregg A. Iverson>Al Flowers>Captain Jack Sparrow
2:Gregg A. Iverson>Al Flowers>Jacob Frey
2:Gregg A. Iverson>Aswar Rahman
2:Gregg A. Iverson>Aswar Rahman>Betsy Hodges
2:Gregg A. Iverson>Aswar Rahman>Raymond Dehn
2:Gregg A. Iverson>Betsy Hodges>David John Wilson
2:Gregg A. Iverson>Captain Jack Sparrow>Al Flowers
2:Gregg A. Iverson>Captain Jack Sparrow>Jacob Frey
2:Gregg A. Iverson>Captain Jack Sparrow>Nekima Levy-Pounds
2:Gregg A. Iverson>Charlie Gers
2:Gregg A. Iverson>Charlie Gers>Ronald Lischeid
2:Gregg A. Iverson>David Rosenfeld>Betsy Hodges
2:Gregg A. Iverson>David Rosenfeld>Captain Jack Sparrow
2:Gregg A. Iverson>David Rosenfeld>Tom Hoch
2:Gregg A. Iverson>David Rosenfeld>Troy Benjegerdes
2:Gregg A. Iverson>Jacob Frey>Al Flowers
2:Gregg A. Iverson>Jacob Frey>Captain Jack Sparrow
2:Gregg A. Iverson>Jacob Frey>David John Wilson
2:Gregg A. Iverson>Jacob Frey>David Rosenfeld
2:Gregg A. Iverson>Raymond Dehn>Al Flowers
2:Gregg A. Iverson>Raymond Dehn>Captain Jack Sparrow
2:Gregg A. Iverson>Raymond Dehn>Jacob Frey
2:Gregg A. Iverson>Raymond Dehn>Nekima Levy-Pounds
2:Gregg A. Iverson>Ronald Lischeid
2:Gregg A. Iverson>Ronald Lischeid>Charlie Gers
2:Gregg A. Iverson>Troy Benjegerdes
2:Ian Simpson>Betsy Hodges>Raymond Dehn
2:Ian Simpson>Captain Jack Sparrow>David John Wilson
2:Ian Simpson>Captain Jack Sparrow>Tom Hoch
2:Ian Simpson>Charlie Gers>Betsy Hodges
2:Ian Simpson>David John Wilson>Captain Jack Sparrow
2:Ian Simpson>Nekima Levy-Pounds>Raymond Dehn
2:Ian Simpson>Raymond Dehn>Jacob Frey
2:Ian Simpson>Raymond Dehn>Tom Hoch
2:Ian Simpson>Tom Hoch
2:Ian Simpson>Tom Hoch>Captain Jack Sparrow
2:Ian Simpson>Tom Hoch>Jacob Frey
2:Jacob Frey>Al Flowers>Charlie Gers
2:Jacob Frey>Al Flowers>Ian Simpson
2:Jacob Frey>Charlie Gers>Ian Simpson
2:Jacob Frey>Charlie Gers>Undeclared Write-ins
2:Jacob Frey>David John Wilson>Charlie Gers
2:Jacob Frey>David John Wilson>David Rosenfeld
2:Jacob Frey>David John Wilson>Ian Simpson
2:Jacob Frey>David Rosenfeld>L.A. Nik
2:Jacob Frey>David Rosenfeld>Ronald Lischeid
2:Jacob Frey>Gregg A. Iverson>Troy Benjegerdes
2:Jacob Frey>Ian Simpson>Betsy Hodges
2:Jacob Frey>Ian Simpson>L.A. Nik
2:Jacob Frey>L.A. Nik>David John Wilson
2:Jacob Frey>L.A. Nik>David Rosenfeld
2:Jacob Frey>L.A. Nik>Gregg A. Iverson
2:Jacob Frey>Ronald Lischeid>Captain Jack Sparrow
2:Jacob Frey>Ronald Lischeid>David Rosenfeld
2:Jacob Frey>Ronald Lischeid>L.A. Nik
2:Jacob Frey>Troy Benjegerdes>L.A. Nik
2:Jacob Frey>Undeclared Write-ins>Betsy Hodges
2:Jacob Frey>Undeclared Write-ins>Raymond Dehn
2:L.A. Nik>Betsy Hodges>Al Flowers
2:L.A. Nik>Betsy Hodges>Captain Jack Sparrow
2:L.A. Nik>Betsy Hodges>Charlie Gers
2:L.A. Nik>Captain Jack Sparrow>Charlie Gers
2:L.A. Nik>Captain Jack Sparrow>Ronald Lischeid
2:L.A. Nik>Charlie Gers>Gregg A. Iverson
2:L.A. Nik>David John Wilson
2:L.A. Nik>David John Wilson>Charlie Gers
2:L.A. Nik>David John Wilson>Ronald Lischeid
2:L.A. Nik>Gregg A. Iverson>Charlie Gers
2:L.A. Nik>Gregg A. Iverson>Raymond Dehn
2:L.A. Nik>Ian Simpson>Captain Jack Sparrow
2:L.A. Nik>Nekima Levy-Pounds
2:L.A. Nik>Nekima Levy-Pounds>Betsy Hodges
2:L.A. Nik>Nekima Levy-Pounds>Jacob Frey
2:L.A. Nik>Raymond Dehn>Aswar Rahman
2:L.A. Nik>Raymond Dehn>Tom Hoch
2:L.A. Nik>Ronald Lischeid>David Rosenfeld
2:L.A. Nik>Ronald Lischeid>Jacob Frey
2:L.A. Nik>Tom Hoch>Al Flowers
2:L.A. Nik>Tom Hoch>Raymond Dehn
2:L.A. Nik>Troy Benjegerdes
2:L.A. Nik>Troy Benjegerdes>David John Wilson
2:Nekima Levy-Pounds>Charlie Gers>David John Wilson
2:Nekima Levy-Pounds>Charlie Gers>Ronald Lischeid
2:Nekima Levy-Pounds>David John Wilson>Charlie Gers
2:Nekima Levy-Pounds>David Rosenfeld>Troy Benjegerdes
2:Nekima Levy-Pounds>Ian Simpson>Raymond Dehn
2:Nekima Levy-Pounds>Ian Simpson>Ronald Lischeid
2:Nekima Levy-Pounds>Jacob Frey>Troy Benjegerdes
2:Nekima Levy-Pounds>L.A. Nik>Al Flowers
2:Nekima Levy-Pounds>Ronald Lischeid>Aswar Rahman
2:Nekima Levy-Pounds>Ronald Lischeid>David John Wilson
2:Nekima Levy-Pounds>Ronald Lischeid>David Rosenfeld
2:Nekima Levy-Pounds>Ronald Lischeid>Jacob Frey
2:Nekima Levy-Pounds>Tom Hoch>Ian Simpson
2:Nekima Levy-Pounds>Tom Hoch>Troy Benjegerdes
2:Nekima Levy-Pounds>Troy Benjegerdes>Aswar Rahman
2:Nekima Levy-Pounds>Troy Benjegerdes>Betsy Hodges
2:Nekima Levy-Pounds>Troy Benjegerdes>Jacob Frey
2:Nekima Levy-Pounds>Undeclared Write-ins>Betsy Hodges
2:Nekima Levy-Pounds>Undeclared Write-ins>Raymond Dehn
2:Raymond Dehn>Al Flowers>Ronald Lischeid
2:Raymond Dehn>Al Flowers>Troy Benjegerdes
2:Raymond Dehn>Aswar Rahman>Undeclared Write-ins
2:Raymond Dehn>Captain Jack Sparrow>Aswar Rahman
2:Raymond Dehn>Captain Jack Sparrow>Gregg A. Iverson
2:Raymond Dehn>Charlie Gers>Aswar Rahman
2:Raymond Dehn>Charlie Gers>David John Wilson
2:Raymond Dehn>Charlie Gers>David Rosenfeld
2:Raymond Dehn>David John Wilson>Aswar Rahman
2:Raymond Dehn>David John Wilson>David Rosenfeld
2:Raymond Dehn>David John Wilson>Jacob Frey
2:Raymond Dehn>David John Wilson>L.A. Nik
2:Raymond Dehn>David John Wilson>Ronald Lischeid
2:Raymond Dehn>David Rosenfeld>Ian Simpson
2:Raymond Dehn>Gregg A. Iverson>David Rosenfeld
2:Raymond Dehn>Ian Simpson>Captain Jack Sparrow
2:Raymond Dehn>Ian Simpson>Ronald Lischeid
2:Raymond Dehn>Jacob Frey>Ronald Lischeid
2:Raymond Dehn>L.A. Nik>David John Wilson
2:Raymond Dehn>L.A. Nik>David Rosenfeld
2:Raymond Dehn>L.A. Nik>Gregg A. Iverson
2:Raymond Dehn>L.A. Nik>Jacob Frey
2:Raymond Dehn>L.A. Nik>Ronald Lischeid
2:Raymond Dehn>L.A. Nik>Undeclared Write-ins
2:Raymond Dehn>Ronald Lischeid>Al Flowers
2:Raymond Dehn>Ronald Lischeid>Aswar Rahman
2:Raymond Dehn>Ronald Lischeid>Betsy Hodges
2:Raymond Dehn>Ronald Lischeid>Gregg A. Iverson
2:Raymond Dehn>Ronald Lischeid>L.A. Nik
2:Raymond Dehn>Ronald Lischeid>Nekima Levy-Pounds
2:Raymond Dehn>Troy Benjegerdes
2:Raymond Dehn>Troy Benjegerdes>Jacob Frey
2:Ronald Lischeid>Aswar Rahman>Captain Jack Sparrow
2:Ronald Lischeid>Betsy Hodges>Troy Benjegerdes
2:Ronald Lischeid>Captain Jack Sparrow>Betsy Hodges
2:Ronald Lischeid>Captain Jack Sparrow>David John Wilson
2:Ronald Lischeid>Captain Jack Sparrow>L.A. Nik
2:Ronald Lischeid>Charlie Gers>Betsy Hodges
2:Ronald Lischeid>Charlie Gers>Raymond Dehn
2:Ronald Lischeid>David John Wilson>Charlie Gers
2:Ronald Lischeid>David Rosenfeld>Betsy Hodges
2:Ronald Lischeid>Gregg A. Iverson
2:Ronald Lischeid>Ian Simpson>L.A. Nik
2:Ronald Lischeid>L.A. Nik>Tom Hoch
2:Ronald Lischeid>Nekima Levy-Pounds>Betsy Hodges
2:Ronald Lischeid>Nekima Levy-Pounds>Raymond Dehn
2:Ronald Lischeid>Raymond Dehn
2:Ronald Lischeid>Raymond Dehn>Tom Hoch
2:Ronald Lischeid>Tom Hoch>Captain Jack Sparrow
2:Ronald Lischeid>Tom Hoch>Charlie Gers
2:Ronald Lischeid>Troy Benjegerdes>Al Flowers
2:Tom Hoch>Al Flowers>David Rosenfeld
2:Tom Hoch>Aswar Rahman>Undeclared Write-ins
2:Tom Hoch>David John Wilson>David Rosenfeld
2:Tom Hoch>David John Wilson>Gregg A. Iverson
2:Tom Hoch>David John Wilson>Troy Benjegerdes
2:Tom Hoch>David Rosenfeld>Aswar Rahman
2:Tom Hoch>David Rosenfeld>Gregg A. Iverson
2:Tom Hoch>David Rosenfeld>Ian Simpson
2:Tom Hoch>David Rosenfeld>L.A. Nik
2:Tom Hoch>Gregg A. Iverson>David Rosenfeld
2:Tom Hoch>Gregg A. Iverson>Ian Simpson
2:Tom Hoch>Ian Simpson>Gregg A. Iverson
2:Tom Hoch>Ian Simpson>Ronald Lischeid
2:Tom Hoch>L.A. Nik>Troy Benjegerdes
2:Tom Hoch>L.A. Nik>Undeclared Write-ins
2:Tom Hoch>Nekima Levy-Pounds>Christopher Zimmerman
2:Tom Hoch>Nekima Levy-Pounds>Undeclared Write-ins
2:Tom Hoch>Ronald Lischeid>David Rosenfeld
2:Tom Hoch>Troy Benjegerdes>Betsy Hodges
2:Tom Hoch>Troy Benjegerdes>David Rosenfeld
2:Tom Hoch>Undeclared Write-ins>Captain Jack Sparrow
2:Tom Hoch>Undeclared Write-ins>Charlie Gers
2:Tom Hoch>Undeclared Write-ins>L.A. Nik
2:Troy Benjegerdes>Aswar Rahman>Al Flowers
2:Troy Benjegerdes>Betsy Hodges>Captain Jack Sparrow
2:Troy Benjegerdes>Betsy Hodges>Nekima Levy-Pounds
2:Troy Benjegerdes>Captain Jack Sparrow>Betsy Hodges
2:Troy Benjegerdes>Captain Jack Sparrow>Ronald Lischeid
2:Troy Benjegerdes>Ian Simpson
2:Troy Benjegerdes>Ian Simpson>Charlie Gers
2:Troy Benjegerdes>Jacob Frey>Aswar Rahman
2:Troy Benjegerdes>Jacob Frey>Charlie Gers
2:Troy Benjegerdes>L.A. Nik>Captain Jack Sparrow
2:Troy Benjegerdes>L.A. Nik>Ian Simpson
2:Troy Benjegerdes>Nekima Levy-Pounds>Betsy Hodges
2:Troy Benjegerdes>Nekima Levy-Pounds>David Rosenfeld
2:Troy Benjegerdes>Raymond Dehn>David Rosenfeld
2:Troy Benjegerdes>Raymond Dehn>Jacob Frey
2:Troy Benjegerdes>Ronald Lischeid
2:Troy Benjegerdes>Ronald Lischeid>Jacob Frey
2:Troy Benjegerdes>Ronald Lischeid>L.A. Nik
2:Troy Benjegerdes>Tom Hoch>Raymond Dehn
2:Undeclared Write-ins>Al Flowers
2:Undeclared Write-ins>Captain Jack Sparrow
2:Undeclared Write-ins>Charlie Gers
2:Undeclared Write-ins>Raymond Dehn
1:Al Flowers>Aswar Rahman>Captain Jack Sparrow
1:Al Flowers>Aswar Rahman>Charlie Gers
1:Al Flowers>Aswar Rahman>David John Wilson
1:Al Flowers>Aswar Rahman>Gregg A. Iverson
1:Al Flowers>Aswar Rahman>L.A. Nik
1:Al Flowers>Aswar Rahman>Troy Benjegerdes
1:Al Flowers>Captain Jack Sparrow>David Rosenfeld
1:Al Flowers>Captain Jack Sparrow>Gregg A. Iverson
1:Al Flowers>Captain Jack Sparrow>Nekima Levy-Pounds
1:Al Flowers>Captain Jack Sparrow>Tom Hoch
1:Al Flowers>Charlie Gers>Raymond Dehn
1:Al Flowers>Charlie Gers>Tom Hoch
1:Al Flowers>David John Wilson>Captain Jack Sparrow
1:Al Flowers>David John Wilson>Ian Simpson
1:Al Flowers>David John Wilson>Jacob Frey
1:Al Flowers>David Rosenfeld>Jacob Frey
1:Al Flowers>David Rosenfeld>L.A. Nik
1:Al Flowers>David Rosenfeld>Raymond Dehn
1:Al Flowers>Gregg A. Iverson>Charlie Gers
1:Al Flowers>Gregg A. Iverson>David Rosenfeld
1:Al Flowers>Gregg A. Iverson>Ian Simpson
1:Al Flowers>Gregg A. Iverson>Raymond Dehn
1:Al Flowers>Gregg A. Iverson>Ronald Lischeid
1:Al Flowers>Gregg A. Iverson>Tom Hoch
1:Al Flowers>Ian Simpson
1:Al Flowers>Ian Simpson>Betsy Hodges
1:Al Flowers>Ian Simpson>Captain Jack Sparrow
1:Al Flowers>Ian Simpson>David John Wilson
1:Al Flowers>Ian Simpson>Ronald Lischeid
1:Al Flowers>Jacob Frey>Charlie Gers
1:Al Flowers>L.A. Nik>Jacob Frey
1:Al Flowers>L.A. Nik>Raymond Dehn
1:Al Flowers>L.A. Nik>Undeclared Write-ins
1:Al Flowers>Nekima Levy-Pounds>David Rosenfeld
1:Al Flowers>Nekima Levy-Pounds>Ian Simpson
1:Al Flowers>Nekima Levy-Pounds>Undeclared Write-ins
1:Al Flowers>Raymond Dehn>David John Wilson
1:Al Flowers>Raymond Dehn>Gregg A. Iverson
1:Al Flowers>Raymond Dehn>Ian Simpson
1:Al Flowers>Ronald Lischeid
1:Al Flowers>Ronald Lischeid>Gregg A. Iverson
1:Al Flowers>Ronald Lischeid>L.A. Nik
1:Al Flowers>Tom Hoch>Ronald Lischeid
1:Al Flowers>Troy Benjegerdes>Captain Jack Sparrow
1:Al Flowers>Troy Benjegerdes>Gregg A. Iverson
1:Al Flowers>Troy Benjegerdes>L.A. Nik
1:Al Flowers>Troy Benjegerdes>Undeclared Write-ins
1:Al Flowers>Undeclared Write-ins
1:Al Flowers>Undeclared Write-ins>Betsy Hodges
1:Aswar Rahman>Al Flowers>David John Wilson
1:Aswar Rahman>Al Flowers>Gregg A. Iverson
1:Aswar Rahman>Betsy Hodges>David Rosenfeld
1:Aswar Rahman>Betsy Hodges>Gregg A. Iverson
1:Aswar Rahman>Betsy Hodges>Ian Simpson
1:Aswar Rahman>Betsy Hodges>Undeclared Write-ins
1:Aswar Rahman>Captain Jack Sparrow>Charlie Gers
1:Aswar Rahman>Captain Jack Sparrow>Jacob Frey
1:Aswar Rahman>Captain Jack Sparrow>Troy Benjegerdes
1:Aswar Rahman>Charlie Gers>Betsy Hodges
1:Aswar Rahman>Charlie Gers>Ian Simpson
1:Aswar Rahman>Charlie Gers>Jacob Frey
1:Aswar Rahman>Charlie Gers>Troy Benjegerdes
1:Aswar Rahman>Charlie Gers>Undeclared Write-ins
1:Aswar Rahman>David John Wilson>Betsy Hodges
1:Aswar Rahman>David John Wilson>L.A. Nik
1:Aswar Rahman>David John Wilson>Raymond Dehn
1:Aswar Rahman>David John Wilson>Tom Hoch
1:Aswar Rahman>David Rosenfeld>Al Flowers
1:Aswar Rahman>David Rosenfeld>Captain Jack Sparrow
1:Aswar Rahman>David Rosenfeld>David John Wilson
1:Aswar Rahman>David Rosenfeld>L.A. Nik
1:Aswar Rahman>David Rosenfeld>Nekima Levy-Pounds
1:Aswar Rahman>David Rosenfeld>Raymond Dehn
1:Aswar Rahman>David Rosenfeld>Ronald Lischeid
1:Aswar Rahman>David Rosenfeld>Tom Hoch
1:Aswar Rahman>David Rosenfeld>Troy Benjegerdes
1:Aswar Rahman>Gregg A. Iverson
1:Aswar Rahman>Gregg A. Iverson>Captain Jack Sparrow
1:Aswar Rahman>Gregg A. Iverson>Charlie Gers
1:Aswar Rahman>Gregg A. Iverson>David John Wilson
1:Aswar Rahman>Gregg A. Iverson>Ian Simpson
1:Aswar Rahman>Gregg A. Iverson>Jacob Frey
1:Aswar Rahman>Gregg A. Iverson>Nekima Levy-Pounds
1:Aswar Rahman>Ian Simpson>Al Flowers
1:Aswar Rahman>Ian Simpson>Betsy Hodges
1:Aswar Rahman>Ian Simpson>Tom Hoch
1:Aswar Rahman>Jacob Frey>Captain Jack Sparrow
1:Aswar Rahman>Jacob Frey>L.A. Nik
1:Aswar Rahman>L.A. Nik
1:Aswar Rahman>L.A. Nik>Captain Jack Sparrow
1:Aswar Rahman>L.A. Nik>Charlie Gers
1:Aswar Rahman>L.A. Nik>Ian Simpson
1:Aswar Rahman>L.A. Nik>Raymond Dehn
1:Aswar Rahman>L.A. Nik>Troy Benjegerdes
1:Aswar Rahman>L.A. Nik>Undeclared Write-ins
1:Aswar Rahman>Nekima Levy-Pounds>Charlie Gers
1:Aswar Rahman>Nekima Levy-Pounds>David John Wilson
1:Aswar Rahman>Nekima Levy-Pounds>Ian Simpson
1:Aswar Rahman>Raymond Dehn>David John Wilson
1:Aswar Rahman>Raymond Dehn>L.A. Nik
1:Aswar Rahman>Raymond Dehn>Troy Benjegerdes
1:Aswar Rahman>Ronald Lischeid>Betsy Hodges
1:Aswar Rahman>Ronald Lischeid>Jacob Frey
1:Aswar Rahman>Ronald Lischeid>L.A. Nik
1:Aswar Rahman>Troy Benjegerdes>Betsy Hodges
1:Aswar Rahman>Troy Benjegerdes>L.A. Nik
1:Aswar Rahman>Troy Benjegerdes>Raymond Dehn
1:Aswar Rahman>Troy Benjegerdes>Tom Hoch
1:Aswar Rahman>Undeclared Write-ins
1:Betsy Hodges>Al Flowers>Ronald Lischeid
1:Betsy Hodges>Aswar Rahman>Ian Simpson
1:Betsy Hodges>Captain Jack Sparrow>Gregg A. Iverson
1:Betsy Hodges>Captain Jack Sparrow>Troy Benjegerdes
1:Betsy Hodges>Charlie Gers>Aswar Rahman
1:Betsy Hodges>Charlie Gers>Ronald Lischeid
1:Betsy Hodges>David John Wilson>Aswar Rahman
1:Betsy Hodges>David John Wilson>Charlie Gers
1:Betsy Hodges>David John Wilson>Gregg A. Iverson
1:Betsy Hodges>Gregg A. Iverson>Ian Simpson
1:Betsy Hodges>Gregg A. Iverson>Undeclared Write-ins
1:Betsy Hodges>Ian Simpson>Jacob Frey
1:Betsy Hodges>Ian Simpson>L.A. Nik
1:Betsy Hodges>Ian Simpson>Raymond Dehn
1:Betsy Hodges>Ian Simpson>Ronald Lischeid
1:Betsy Hodges>Ian Simpson>Tom Hoch
1:Betsy Hodges>L.A. Nik>Raymond Dehn
1:Betsy Hodges>Ronald Lischeid>Al Flowers
1:Betsy Hodges>Ronald Lischeid>Gregg A. Iverson
1:Betsy Hodges>Troy Benjegerdes>Ronald Lischeid
1:Betsy Hodges>Undeclared Write-ins>David Rosenfeld
1:Betsy Hodges>Undeclared Write-ins>Nekima Levy-Pounds
1:Captain Jack Sparrow>Al Flowers>Aswar Rahman
1:Captain Jack Sparrow>Al Flowers>David Rosenfeld
1:Captain Jack Sparrow>Al Flowers>Ian Simpson
1:Captain Jack Sparrow>Al Flowers>L.A. Nik
1:Captain Jack Sparrow>Aswar Rahman
1:Captain Jack Sparrow>Aswar Rahman>Al Flowers
1:Captain Jack Sparrow>Aswar Rahman>Betsy Hodges
1:Captain Jack Sparrow>Aswar Rahman>Jacob Frey
1:Captain Jack Sparrow>Aswar Rahman>Raymond Dehn
1:Captain Jack Sparrow>Aswar Rahman>Undeclared Write-ins
1:Captain Jack Sparrow>Betsy Hodges>Aswar Rahman
1:Captain Jack Sparrow>Betsy Hodges>David John Wilson
1:Captain Jack Sparrow>Betsy Hodges>Gregg A. Iverson
1:Captain Jack Sparrow>Charlie Gers>David John Wilson
1:Captain Jack Sparrow>Charlie Gers>Ronald Lischeid
1:Captain Jack Sparrow>David John Wilson>Al Flowers
1:Captain Jack Sparrow>David John Wilson>Tom Hoch
1:Captain Jack Sparrow>David Rosenfeld>David John Wilson
1:Captain Jack Sparrow>David Rosenfeld>Gregg A. Iverson
1:Captain Jack Sparrow>David Rosenfeld>Nekima Levy-Pounds
1:Captain Jack Sparrow>David Rosenfeld>Raymond Dehn
1:Captain Jack Sparrow>David Rosenfeld>Ronald Lischeid
1:Captain Jack Sparrow>Gregg A. Iverson>Betsy Hodges
1:Captain Jack Sparrow>Gregg A. Iverson>David John Wilson
1:Captain Jack Sparrow>Gregg A. Iverson>Raymond Dehn
1:Captain Jack Sparrow>Gregg A. Iverson>Troy Benjegerdes
1:Captain Jack Sparrow>Ian Simpson>Gregg A. Iverson
1:Captain Jack Sparrow>Ian Simpson>Jacob Frey
1:Captain Jack Sparrow>Ian Simpson>Troy Benjegerdes
1:Captain Jack Sparrow>Jacob Frey>Charlie Gers
1:Captain Jack Sparrow>Jacob Frey>Gregg A. Iverson
1:Captain Jack Sparrow>Jacob Frey>Raymond Dehn
1:Captain Jack Sparrow>L.A. Nik>Al Flowers
1:Captain Jack Sparrow>L.A. Nik>Aswar Rahman
1:Captain Jack Sparrow>L.A. Nik>Charlie Gers
1:Captain Jack Sparrow>L.A. Nik>David Rosenfeld
1:Captain Jack Sparrow>L.A. Nik>Gregg A. Iverson
1:Captain Jack Sparrow>L.A. Nik>Nekima Levy-Pounds
1:Captain Jack Sparrow>L.A. Nik>Raymond Dehn
1:Captain Jack Sparrow>Nekima Levy-Pounds
1:Captain Jack Sparrow>Nekima Levy-Pounds>Charlie Gers
1:Captain Jack Sparrow>Nekima Levy-Pounds>David John Wilson
1:Captain Jack Sparrow>Nekima Levy-Pounds>David Rosenfeld
1:Captain Jack Sparrow>Nekima Levy-Pounds>Gregg A. Iverson
1:Captain Jack Sparrow>Nekima Levy-Pounds>Troy Benjegerdes
1:Captain Jack Sparrow>Nekima Levy-Pounds>Undeclared Write-ins
1:Captain Jack Sparrow>Raymond Dehn
1:Captain Jack Sparrow>Raymond Dehn>Al Flowers
1:Captain Jack Sparrow>Ronald Lischeid
1:Captain Jack Sparrow>Ronald Lischeid>Charlie Gers
1:Captain Jack Sparrow>Ronald Lischeid>David John Wilson
1:Captain Jack Sparrow>Ronald Lischeid>David Rosenfeld
1:Captain Jack Sparrow>Ronald Lischeid>Jacob Frey
1:Captain Jack Sparrow>Ronald Lischeid>Nekima Levy-Pounds
1:Captain Jack Sparrow>Ronald Lischeid>Troy Benjegerdes
1:Captain Jack Sparrow>Tom Hoch>David John Wilson
1:Captain Jack Sparrow>Tom Hoch>Gregg A. Iverson
1:Captain Jack Sparrow>Tom Hoch>L.A. Nik
1:Captain Jack Sparrow>Tom Hoch>Troy Benjegerdes
1:Captain Jack Sparrow>Troy Benjegerdes>Betsy Hodges
1:Captain Jack Sparrow>Troy Benjegerdes>Ian Simpson
1:Captain Jack Sparrow>Troy Benjegerdes>L.A. Nik
1:Captain Jack Sparrow>Undeclared Write-ins>Ian Simpson
1:Charlie Gers>Al Flowers
1:Charlie Gers>Al Flowers>Captain Jack Sparrow
1:Charlie Gers>Al Flowers>L.A. Nik
1:Charlie Gers>Al Flowers>Nekima Levy-Pounds
1:Charlie Gers>Aswar Rahman>David John Wilson
1:Charlie Gers>Aswar Rahman>Ian Simpson
1:Charlie Gers>Aswar Rahman>Raymond Dehn
1:Charlie Gers>Betsy Hodges>David John Wilson
1:Charlie Gers>Betsy Hodges>David Rosenfeld
1:Charlie Gers>Betsy Hodges>L.A. Nik
1:Charlie Gers>Captain Jack Sparrow>Al Flowers
1:Charlie Gers>Captain Jack Sparrow>Aswar Rahman
1:Charlie Gers>Captain Jack Sparrow>Betsy Hodges
1:Charlie Gers>David John Wilson>Aswar Rahman
1:Charlie Gers>David John Wilson>Betsy Hodges
1:Charlie Gers>David John Wilson>David Rosenfeld
1:Charlie Gers>David John Wilson>Gregg A. Iverson
1:Charlie Gers>David John Wilson>Tom Hoch
1:Charlie Gers>David John Wilson>Troy Benjegerdes
1:Charlie Gers>David Rosenfeld
1:Charlie Gers>David Rosenfeld>Al Flowers
1:Charlie Gers>David Rosenfeld>Aswar Rahman
1:Charlie Gers>David Rosenfeld>Gregg A. Iverson
1:Charlie Gers>David Rosenfeld>Jacob Frey
1:Charlie Gers>David Rosenfeld>L.A. Nik
1:Charlie Gers>David Rosenfeld>Raymond Dehn
1:Charlie Gers>Gregg A. Iverson>David Rosenfeld
1:Charlie Gers>Ian Simpson>David John Wilson
1:Charlie Gers>Ian Simpson>David Rosenfeld
1:Charlie Gers>Ian Simpson>Nekima Levy-Pounds
1:Charlie Gers>Jacob Frey>Troy Benjegerdes
1:Charlie Gers>Jacob Frey>Undeclared Write-ins
1:Charlie Gers>L.A. Nik>Al Flowers
1:Charlie Gers>Nekima Levy-Pounds
1:Charlie Gers>Nekima Levy-Pounds>Betsy Hodges
1:Charlie Gers>Nekima Levy-Pounds>Gregg A. Iverson
1:Charlie Gers>Nekima Levy-Pounds>L.A. Nik
1:Charlie Gers>Nekima Levy-Pounds>Ronald Lischeid
1:Charlie Gers>Raymond Dehn>Al Flowers
1:Charlie Gers>Raymond Dehn>Captain Jack Sparrow
1:Charlie Gers>Raymond Dehn>Ian Simpson
1:Charlie Gers>Raymond Dehn>Ronald Lischeid
1:Charlie Gers>Ronald Lischeid>David Rosenfeld
1:Charlie Gers>Ronald Lischeid>Nekima Levy-Pounds
1:Charlie Gers>Ronald Lischeid>Raymond Dehn
1:Charlie Gers>Troy Benjegerdes>Captain Jack Sparrow
1:Charlie Gers>Troy Benjegerdes>David John Wilson
1:Charlie Gers>Troy Benjegerdes>Ian Simpson
1:Charlie Gers>Troy Benjegerdes>Jacob Frey
1:Charlie Gers>Troy Benjegerdes>L.A. Nik
1:Charlie Gers>Troy Benjegerdes>Raymond Dehn
1:Charlie Gers>Troy Benjegerdes>Tom Hoch
1:Charlie Gers>Undeclared Write-ins>Jacob Frey
1:Christopher Zimmerman>Nekima Levy-Pounds>Raymond Dehn
1:David John Wilson>Al Flowers>Captain Jack Sparrow
1:David John Wilson>Al Flowers>David Rosenfeld
1:David John Wilson>Al Flowers>Ian Simpson
1:David John Wilson>Al Flowers>Troy Benjegerdes
1:David John Wilson>Aswar Rahman
1:David John Wilson>Aswar Rahman>Betsy Hodges
1:David John Wilson>Aswar Rahman>David Rosenfeld
1:David John Wilson>Betsy Hodges>David Rosenfeld
1:David John Wilson>Captain Jack Sparrow>Al Flowers
1:David John Wilson>Captain Jack Sparrow>Aswar Rahman
1:David John Wilson>Captain Jack Sparrow>Betsy Hodges
1:David John Wilson>Captain Jack Sparrow>Gregg A. Iverson
1:David John Wilson>Captain Jack Sparrow>L.A. Nik
1:David John Wilson>Captain Jack Sparrow>Tom Hoch
1:David John Wilson>Charlie Gers>Al Flowers
1:David John Wilson>Charlie Gers>Nekima Levy-Pounds
1:David John Wilson>Charlie Gers>Ronald Lischeid
1:David John Wilson>David Rosenfeld>Al Flowers
1:David John Wilson>David Rosenfeld>Aswar Rahman
1:David John Wilson>David Rosenfeld>Captain Jack Sparrow
1:David John Wilson>David Rosenfeld>Charlie Gers
1:David John Wilson>David Rosenfeld>Troy Benjegerdes
1:David John Wilson>Gregg A. Iverson>Al Flowers
1:David John Wilson>Gregg A. Iverson>Betsy Hodges
1:David John Wilson>Gregg A. Iverson>Ian Simpson
1:David John Wilson>Ian Simpson>Betsy Hodges
1:David John Wilson>Ian Simpson>L.A. Nik
1:David John Wilson>Ian Simpson>Ronald Lischeid
1:David John Wilson>Jacob Frey>Charlie Gers
1:David John Wilson>Jacob Frey>David Rosenfeld
1:David John Wilson>L.A. Nik>Aswar Rahman
1:David John Wilson>L.A. Nik>Ian Simpson
1:David John Wilson>L.A. Nik>Troy Benjegerdes
1:David John Wilson>Nekima Levy-Pounds>Aswar Rahman
1:David John Wilson>Nekima Levy-Pounds>David Rosenfeld
1:David John Wilson>Nekima Levy-Pounds>Raymond Dehn
1:David John Wilson>Raymond Dehn
1:David John Wilson>Raymond Dehn>Aswar Rahman
1:David John Wilson>Raymond Dehn>Charlie Gers
1:David John Wilson>Raymond Dehn>Troy Benjegerdes
1:David John Wilson>Ronald Lischeid
1:David John Wilson>Ronald Lischeid>Jacob Frey
1:David John Wilson>Ronald Lischeid>Raymond Dehn
1:David John Wilson>Tom Hoch
1:David John Wilson>Tom Hoch>Al Flowers
1:David John Wilson>Tom Hoch>Aswar Rahman
1:David John Wilson>Tom Hoch>Charlie Gers
1:David John Wilson>Tom Hoch>Undeclared Write-ins
1:David John Wilson>Troy Benjegerdes>Betsy Hodges
1:David John Wilson>Troy Benjegerdes>Ian Simpson
1:David John Wilson>Troy Benjegerdes>Jacob Frey
1:David John Wilson>Troy Benjegerdes>Nekima Levy-Pounds
1:David John Wilson>Undeclared Write-ins
1:David Rosenfeld>Al Flowers
1:David Rosenfeld>Al Flowers>Jacob Frey
1:David Rosenfeld>Aswar Rahman>Gregg A. Iverson
1:David Rosenfeld>Aswar Rahman>Raymond Dehn
1:David Rosenfeld>Aswar Rahman>Ronald Lischeid
1:David Rosenfeld>Betsy Hodges>Charlie Gers
1:David Rosenfeld>Betsy Hodges>Raymond Dehn
1:David Rosenfeld>Betsy Hodges>Ronald Lischeid
1:David Rosenfeld>Captain Jack Sparrow>Aswar Rahman
1:David Rosenfeld>Captain Jack Sparrow>Ronald Lischeid
1:David Rosenfeld>Captain Jack Sparrow>Tom Hoch
1:David Rosenfeld>Captain Jack Sparrow>Undeclared Write-ins
1:David Rosenfeld>Charlie Gers
1:David Rosenfeld>Charlie Gers>L.A. Nik
1:David Rosenfeld>Charlie Gers>Raymond Dehn
1:David Rosenfeld>Charlie Gers>Tom Hoch
1:David Rosenfeld>David John Wilson>Betsy Hodges
1:David Rosenfeld>David John Wilson>L.A. Nik
1:David Rosenfeld>Gregg A. Iverson>Al Flowers
1:David Rosenfeld>Gregg A. Iverson>Captain Jack Sparrow
1:David Rosenfeld>Gregg A. Iverson>Jacob Frey
1:David Rosenfeld>Gregg A. Iverson>Raymond Dehn
1:David Rosenfeld>Ian Simpson
1:David Rosenfeld>Ian Simpson>Betsy Hodges
1:David Rosenfeld>Ian Simpson>David John Wilson
1:David Rosenfeld>Ian Simpson>Raymond Dehn
1:David Rosenfeld>Ian Simpson>Troy Benjegerdes
1:David Rosenfeld>Jacob Frey>Aswar Rahman
1:David Rosenfeld>Jacob Frey>Captain Jack Sparrow
1:David Rosenfeld>Jacob Frey>David John Wilson
1:David Rosenfeld>Jacob Frey>Undeclared Write-ins
1:David Rosenfeld>L.A. Nik
1:David Rosenfeld>L.A. Nik>Al Flowers
1:David Rosenfeld>L.A. Nik>Aswar Rahman
1:David Rosenfeld>L.A. Nik>Betsy Hodges
1:David Rosenfeld>L.A. Nik>Charlie Gers
1:David Rosenfeld>L.A. Nik>Tom Hoch
1:David Rosenfeld>L.A. Nik>Undeclared Write-ins
1:David Rosenfeld>Nekima Levy-Pounds>Al Flowers
1:David Rosenfeld>Nekima Levy-Pounds>L.A. Nik
1:David Rosenfeld>Nekima Levy-Pounds>Ronald Lischeid
1:David Rosenfeld>Nekima Levy-Pounds>Undeclared Write-ins
1:David Rosenfeld>Raymond Dehn>Al Flowers
1:David Rosenfeld>Raymond Dehn>Aswar Rahman
1:David Rosenfeld>Raymond Dehn>Charlie Gers
1:David Rosenfeld>Raymond Dehn>Gregg A. Iverson
1:David Rosenfeld>Ronald Lischeid>Betsy Hodges
1:David Rosenfeld>Ronald Lischeid>Charlie Gers
1:David Rosenfeld>Ronald Lischeid>Gregg A. Iverson
1:David Rosenfeld>Ronald Lischeid>Ian Simpson
1:David Rosenfeld>Ronald Lischeid>Jacob Frey
1:David Rosenfeld>Ronald Lischeid>Tom Hoch
1:David Rosenfeld>Tom Hoch>Aswar Rahman
1:David Rosenfeld>Tom Hoch>Charlie Gers
1:David Rosenfeld>Tom Hoch>Gregg A. Iverson
1:David Rosenfeld>Troy Benjegerdes>Gregg A. Iverson
1:David Rosenfeld>Troy Benjegerdes>Ian Simpson
1:David Rosenfeld>Undeclared Write-ins>Tom Hoch
1:Gregg A. Iverson>Al Flowers>Aswar Rahman
1:Gregg A. Iverson>Al Flowers>Betsy Hodges
1:Gregg A. Iverson>Al Flowers>David John Wilson
1:Gregg A. Iverson>Al Flowers>Ian Simpson
1:Gregg A. Iverson>Al Flowers>Raymond Dehn
1:Gregg A. Iverson>Al Flowers>Tom Hoch
1:Gregg A. Iverson>Aswar Rahman>Al Flowers
1:Gregg A. Iverson>Aswar Rahman>Tom Hoch
1:Gregg A. Iverson>Betsy Hodges>Ian Simpson
1:Gregg A. Iverson>Betsy Hodges>L.A. Nik
1:Gregg A. Iverson>Captain Jack Sparrow
1:Gregg A. Iverson>Captain Jack Sparrow>Aswar Rahman
1:Gregg A. Iverson>Captain Jack Sparrow>David Rosenfeld
1:Gregg A. Iverson>Captain Jack Sparrow>Raymond Dehn
1:Gregg A. Iverson>Captain Jack Sparrow>Tom Hoch
1:Gregg A. Iverson>Charlie Gers>Aswar Rahman
1:Gregg A. Iverson>Charlie Gers>Tom Hoch
1:Gregg A. Iverson>Charlie Gers>Troy Benjegerdes
1:Gregg A. Iverson>David John Wilson>Al Flowers
1:Gregg A. Iverson>David John Wilson>Aswar Rahman
1:Gregg A. Iverson>David Rosenfeld>Aswar Rahman
1:Gregg A. Iverson>David Rosenfeld>Jacob Frey
1:Gregg A. Iverson>Ian Simpson>Betsy Hodges
1:Gregg A. Iverson>Ian Simpson>Ronald Lischeid
1:Gregg A. Iverson>Ian Simpson>Tom Hoch
1:Gregg A. Iverson>Ian Simpson>Troy Benjegerdes
1:Gregg A. Iverson>Jacob Frey>Ian Simpson
1:Gregg A. Iverson>Jacob Frey>Raymond Dehn
1:Gregg A. Iverson>L.A. Nik
1:Gregg A. Iverson>L.A. Nik>Betsy Hodges
1:Gregg A. Iverson>L.A. Nik>Captain Jack Sparrow
1:Gregg A. Iverson>Nekima Levy-Pounds>Al Flowers
1:Gregg A. Iverson>Nekima Levy-Pounds>David Rosenfeld
1:Gregg A. Iverson>Nekima Levy-Pounds>L.A. Nik
1:Gregg A. Iverson>Nekima Levy-Pounds>Tom Hoch
1:Gregg A. Iverson>Raymond Dehn
1:Gregg A. Iverson>Raymond Dehn>David Rosenfeld
1:Gregg A. Iverson>Raymond Dehn>L.A. Nik
1:Gregg A. Iverson>Raymond Dehn>Ronald Lischeid
1:Gregg A. Iverson>Ronald Lischeid>Al Flowers
1:Gregg A. Iverson>Ronald Lischeid>Betsy Hodges
1:Gregg A. Iverson>Ronald Lischeid>L.A. Nik
1:Gregg A. Iverson>Tom Hoch
1:Gregg A. Iverson>Tom Hoch>Aswar Rahman
1:Gregg A. Iverson>Tom Hoch>Charlie Gers
1:Gregg A. Iverson>Tom Hoch>David Rosenfeld
1:Gregg A. Iverson>Tom Hoch>Ronald Lischeid
1:Gregg A. Iverson>Tom Hoch>Troy Benjegerdes
1:Gregg A. Iverson>Troy Benjegerdes>Aswar Rahman
1:Gregg A. Iverson>Troy Benjegerdes>Jacob Frey
1:Gregg A. Iverson>Troy Benjegerdes>Nekima Levy-Pounds
1:Gregg A. Iverson>Troy Benjegerdes>Tom Hoch
1:Gregg A. Iverson>Undeclared Write-ins>Captain Jack Sparrow
1:Ian Simpson>Al Flowers
1:Ian Simpson>Al Flowers>Captain Jack Sparrow
1:Ian Simpson>Aswar Rahman>Al Flowers
1:Ian Simpson>Aswar Rahman>Jacob Frey
1:Ian Simpson>Aswar Rahman>L.A. Nik
1:Ian Simpson>Aswar Rahman>Nekima Levy-Pounds
1:Ian Simpson>Aswar Rahman>Raymond Dehn
1:Ian Simpson>Aswar Rahman>Troy Benjegerdes
1:Ian Simpson>Betsy Hodges>Captain Jack Sparrow
1:Ian Simpson>Betsy Hodges>Gregg A. Iverson
1:Ian Simpson>Betsy Hodges>Nekima Levy-Pounds
1:Ian Simpson>Betsy Hodges>Tom Hoch
1:Ian Simpson>Captain Jack Sparrow
1:Ian Simpson>Captain Jack Sparrow>Charlie Gers
1:Ian Simpson>Captain Jack Sparrow>David Rosenfeld
1:Ian Simpson>Captain Jack Sparrow>L.A. Nik
1:Ian Simpson>Captain Jack Sparrow>Raymond Dehn
1:Ian Simpson>Captain Jack Sparrow>Troy Benjegerdes
1:Ian Simpson>Charlie Gers
1:Ian Simpson>Charlie Gers>Al Flowers
1:Ian Simpson>Charlie Gers>Captain Jack Sparrow
1:Ian Simpson>Charlie Gers>David Rosenfeld
1:Ian Simpson>Charlie Gers>Jacob Frey
1:Ian Simpson>Charlie Gers>Tom Hoch
1:Ian Simpson>David John Wilson>Charlie Gers
1:Ian Simpson>Gregg A. Iverson>Captain Jack Sparrow
1:Ian Simpson>Jacob Frey>Betsy Hodges
1:Ian Simpson>Jacob Frey>Captain Jack Sparrow
1:Ian Simpson>Jacob Frey>Charlie Gers
1:Ian Simpson>Jacob Frey>Raymond Dehn
1:Ian Simpson>L.A. Nik
1:Ian Simpson>L.A. Nik>Charlie Gers
1:Ian Simpson>L.A. Nik>David Rosenfeld
1:Ian Simpson>L.A. Nik>Jacob Frey
1:Ian Simpson>L.A. Nik>Raymond Dehn
1:Ian Simpson>Nekima Levy-Pounds>Betsy Hodges
1:Ian Simpson>Nekima Levy-Pounds>Charlie Gers
1:Ian Simpson>Nekima Levy-Pounds>Tom Hoch
1:Ian Simpson>Nekima Levy-Pounds>Troy Benjegerdes
1:Ian Simpson>Raymond Dehn>Gregg A. Iverson
1:Ian Simpson>Raymond Dehn>Nekima Levy-Pounds
1:Ian Simpson>Ronald Lischeid>Betsy Hodges
1:Ian Simpson>Ronald Lischeid>Captain Jack Sparrow
1:Ian Simpson>Ronald Lischeid>Charlie Gers
1:Ian Simpson>Ronald Lischeid>David John Wilson
1:Ian Simpson>Ronald Lischeid>David Rosenfeld
1:Ian Simpson>Ronald Lischeid>Jacob Frey
1:Ian Simpson>Ronald Lischeid>L.A. Nik
1:Ian Simpson>Tom Hoch>Al Flowers
1:Ian Simpson>Tom Hoch>Aswar Rahman
1:Ian Simpson>Tom Hoch>Betsy Hodges
1:Ian Simpson>Tom Hoch>David John Wilson
1:Ian Simpson>Tom Hoch>David Rosenfeld
1:Ian Simpson>Troy Benjegerdes
1:Ian Simpson>Troy Benjegerdes>Aswar Rahman
1:Ian Simpson>Troy Benjegerdes>L.A. Nik
1:Ian Simpson>Troy Benjegerdes>Tom Hoch
1:Jacob Frey>Al Flowers>Undeclared Write-ins
1:Jacob Frey>Aswar Rahman>Ian Simpson
1:Jacob Frey>Charlie Gers>Al Flowers
1:Jacob Frey>Charlie Gers>Troy Benjegerdes
1:Jacob Frey>David John Wilson>Aswar Rahman
1:Jacob Frey>David John Wilson>Gregg A. Iverson
1:Jacob Frey>David John Wilson>L.A. Nik
1:Jacob Frey>David Rosenfeld>Al Flowers
1:Jacob Frey>Gregg A. Iverson>Undeclared Write-ins
1:Jacob Frey>Ian Simpson>Al Flowers
1:Jacob Frey>Ian Simpson>Aswar Rahman
1:Jacob Frey>Ian Simpson>Charlie Gers
1:Jacob Frey>Ian Simpson>Gregg A. Iverson
1:Jacob Frey>Ian Simpson>Nekima Levy-Pounds
1:Jacob Frey>Ian Simpson>Raymond Dehn
1:Jacob Frey>Ian Simpson>Ronald Lischeid
1:Jacob Frey>Ian Simpson>Undeclared Write-ins
1:Jacob Frey>L.A. Nik>Aswar Rahman
1:Jacob Frey>L.A. Nik>Ian Simpson
1:Jacob Frey>L.A. Nik>Troy Benjegerdes
1:Jacob Frey>Ronald Lischeid>Aswar Rahman
1:Jacob Frey>Ronald Lischeid>Raymond Dehn
1:Jacob Frey>Ronald Lischeid>Undeclared Write-ins
1:Jacob Frey>Troy Benjegerdes>Aswar Rahman
1:Jacob Frey>Troy Benjegerdes>Ronald Lischeid
1:Jacob Frey>Undeclared Write-ins>Charlie Gers
1:Jacob Frey>Undeclared Write-ins>Nekima Levy-Pounds
1:Jacob Frey>Undeclared Write-ins>Tom Hoch
1:L.A. Nik>Al Flowers>Betsy Hodges
1:L.A. Nik>Al Flowers>Charlie Gers
1:L.A. Nik>Al Flowers>Ronald Lischeid
1:L.A. Nik>Aswar Rahman>Al Flowers
1:L.A. Nik>Aswar Rahman>Captain Jack Sparrow
1:L.A. Nik>Aswar Rahman>Charlie Gers
1:L.A. Nik>Aswar Rahman>David John Wilson
1:L.A. Nik>Aswar Rahman>Jacob Frey
1:L.A. Nik>Aswar Rahman>Tom Hoch
1:L.A. Nik>Betsy Hodges>Aswar Rahman
1:L.A. Nik>Betsy Hodges>David John Wilson
1:L.A. Nik>Betsy Hodges>Gregg A. Iverson
1:L.A. Nik>Betsy Hodges>Ian Simpson
1:L.A. Nik>Betsy Hodges>Nekima Levy-Pounds
1:L.A. Nik>Betsy Hodges>Raymond Dehn
1:L.A. Nik>Betsy Hodges>Tom Hoch
1:L.A. Nik>Captain Jack Sparrow>Al Flowers
1:L.A. Nik>Captain Jack Sparrow>David Rosenfeld
1:L.A. Nik>Captain Jack Sparrow>Jacob Frey
1:L.A. Nik>Captain Jack Sparrow>Nekima Levy-Pounds
1:L.A. Nik>Charlie Gers>Al Flowers
1:L.A. Nik>Charlie Gers>Betsy Hodges
1:L.A. Nik>Charlie Gers>Raymond Dehn
1:L.A. Nik>David John Wilson>Betsy Hodges
1:L.A. Nik>David John Wilson>David Rosenfeld
1:L.A. Nik>David John Wilson>Ian Simpson
1:L.A. Nik>David John Wilson>Jacob Frey
1:L.A. Nik>David John Wilson>Troy Benjegerdes
1:L.A. Nik>David Rosenfeld
1:L.A. Nik>David Rosenfeld>Betsy Hodges
1:L.A. Nik>David Rosenfeld>David John Wilson
1:L.A. Nik>David Rosenfeld>Raymond Dehn
1:L.A. Nik>Gregg A. Iverson>Tom Hoch
1:L.A. Nik>Ian Simpson
1:L.A. Nik>Ian Simpson>Gregg A. Iverson
1:L.A. Nik>Jacob Frey>Betsy Hodges
1:L.A. Nik>Nekima Levy-Pounds>Captain Jack Sparrow
1:L.A. Nik>Nekima Levy-Pounds>Ronald Lischeid
1:L.A. Nik>Nekima Levy-Pounds>Tom Hoch
1:L.A. Nik>Raymond Dehn>Jacob Frey
1:L.A. Nik>Ronald Lischeid>Al Flowers
1:L.A. Nik>Ronald Lischeid>David John Wilson
1:L.A. Nik>Tom Hoch>Aswar Rahman
1:L.A. Nik>Tom Hoch>David John Wilson
1:L.A. Nik>Tom Hoch>David Rosenfeld
1:L.A. Nik>Tom Hoch>Gregg A. Iverson
1:L.A. Nik>Tom Hoch>Ian Simpson
1:L.A. Nik>Tom Hoch>Troy Benjegerdes
1:L.A. Nik>Troy Benjegerdes>Captain Jack Sparrow
1:L.A. Nik>Troy Benjegerdes>Jacob Frey
1:L.A. Nik>Troy Benjegerdes>Tom Hoch
1:Nekima Levy-Pounds>Al Flowers>Theron Preston Washington
1:Nekima Levy-Pounds>Captain Jack Sparrow>Ronald Lischeid
1:Nekima Levy-Pounds>Captain Jack Sparrow>Troy Benjegerdes
1:Nekima Levy-Pounds>Charlie Gers>Al Flowers
1:Nekima Levy-Pounds>Charlie Gers>Aswar Rahman
1:Nekima Levy-Pounds>Charlie Gers>David Rosenfeld
1:Nekima Levy-Pounds>Charlie Gers>Gregg A. Iverson
1:Nekima Levy-Pounds>Charlie Gers>L.A. Nik
1:Nekima Levy-Pounds>Charlie Gers>Tom Hoch
1:Nekima Levy-Pounds>Charlie Gers>Undeclared Write-ins
1:Nekima Levy-Pounds>David John Wilson>Al Flowers
1:Nekima Levy-Pounds>David John Wilson>Aswar Rahman
1:Nekima Levy-Pounds>David John Wilson>David Rosenfeld
1:Nekima Levy-Pounds>David John Wilson>Ian Simpson
1:Nekima Levy-Pounds>David John Wilson>L.A. Nik
1:Nekima Levy-Pounds>David John Wilson>Ronald Lischeid
1:Nekima Levy-Pounds>David John Wilson>Troy Benjegerdes
1:Nekima Levy-Pounds>David Rosenfeld>L.A. Nik
1:Nekima Levy-Pounds>Gregg A. Iverson>Captain Jack Sparrow
1:Nekima Levy-Pounds>Gregg A. Iverson>David John Wilson
1:Nekima Levy-Pounds>Gregg A. Iverson>Ian Simpson
1:Nekima Levy-Pounds>Gregg A. Iverson>L.A. Nik
1:Nekima Levy-Pounds>Gregg A. Iverson>Ronald Lischeid
1:Nekima Levy-Pounds>Ian Simpson
1:Nekima Levy-Pounds>Ian Simpson>Al Flowers
1:Nekima Levy-Pounds>Ian Simpson>Aswar Rahman
1:Nekima Levy-Pounds>Ian Simpson>Betsy Hodges
1:Nekima Levy-Pounds>Ian Simpson>Jacob Frey
1:Nekima Levy-Pounds>Ian Simpson>L.A. Nik
1:Nekima Levy-Pounds>Ian Simpson>Tom Hoch
1:Nekima Levy-Pounds>Ian Simpson>Undeclared Write-ins
1:Nekima Levy-Pounds>L.A. Nik>David Rosenfeld
1:Nekima Levy-Pounds>L.A. Nik>Gregg A. Iverson
1:Nekima Levy-Pounds>L.A. Nik>Ian Simpson
1:Nekima Levy-Pounds>L.A. Nik>Raymond Dehn
1:Nekima Levy-Pounds>L.A. Nik>Ronald Lischeid
1:Nekima Levy-Pounds>L.A. Nik>Tom Hoch
1:Nekima Levy-Pounds>Ronald Lischeid>Al Flowers
1:Nekima Levy-Pounds>Ronald Lischeid>Gregg A. Iverson
1:Nekima Levy-Pounds>Ronald Lischeid>Ian Simpson
1:Nekima Levy-Pounds>Ronald Lischeid>Raymond Dehn
1:Nekima Levy-Pounds>Ronald Lischeid>Troy Benjegerdes
1:Nekima Levy-Pounds>Ronald Lischeid>Undeclared Write-ins
1:Nekima Levy-Pounds>Troy Benjegerdes
1:Nekima Levy-Pounds>Troy Benjegerdes>Al Flowers
1:Nekima Levy-Pounds>Troy Benjegerdes>Charlie Gers
1:Nekima Levy-Pounds>Troy Benjegerdes>David John Wilson
1:Nekima Levy-Pounds>Troy Benjegerdes>Raymond Dehn
1:Nekima Levy-Pounds>Troy Benjegerdes>Tom Hoch
1:Nekima Levy-Pounds>Undeclared Write-ins>Jacob Frey
1:Raymond Dehn>Al Flowers>L.A. Nik
1:Raymond Dehn>Aswar Rahman>Ian Simpson
1:Raymond Dehn>Aswar Rahman>Troy Benjegerdes
1:Raymond Dehn>Captain Jack Sparrow>Charlie Gers
1:Raymond Dehn>Captain Jack Sparrow>Ronald Lischeid
1:Raymond Dehn>Captain Jack Sparrow>Troy Benjegerdes
1:Raymond Dehn>Charlie Gers>Gregg A. Iverson
1:Raymond Dehn>Charlie Gers>Ian Simpson
1:Raymond Dehn>Charlie Gers>Ronald Lischeid
1:Raymond Dehn>Charlie Gers>Tom Hoch
1:Raymond Dehn>Charlie Gers>Undeclared Write-ins
1:Raymond Dehn>David Rosenfeld>Gregg A. Iverson
1:Raymond Dehn>Gregg A. Iverson>Aswar Rahman
1:Raymond Dehn>Gregg A. Iverson>Captain Jack Sparrow
1:Raymond Dehn>Gregg A. Iverson>L.A. Nik
1:Raymond Dehn>Gregg A. Iverson>Troy Benjegerdes
1:Raymond Dehn>Ian Simpson
1:Raymond Dehn>Ian Simpson>Al Flowers
1:Raymond Dehn>Ian Simpson>Betsy Hodges
1:Raymond Dehn>Ian Simpson>Charlie Gers
1:Raymond Dehn>Ian Simpson>David John Wilson
1:Raymond Dehn>Ian Simpson>Gregg A. Iverson
1:Raymond Dehn>Ian Simpson>Nekima Levy-Pounds
1:Raymond Dehn>L.A. Nik>Al Flowers
1:Raymond Dehn>L.A. Nik>Charlie Gers
1:Raymond Dehn>L.A. Nik>Nekima Levy-Pounds
1:Raymond Dehn>Ronald Lischeid>Charlie Gers
1:Raymond Dehn>Ronald Lischeid>David John Wilson
1:Raymond Dehn>Ronald Lischeid>David Rosenfeld
1:Raymond Dehn>Ronald Lischeid>Tom Hoch
1:Raymond Dehn>Ronald Lischeid>Troy Benjegerdes
1:Raymond Dehn>Troy Benjegerdes>Aswar Rahman
1:Raymond Dehn>Troy Benjegerdes>Captain Jack Sparrow
1:Raymond Dehn>Troy Benjegerdes>Charlie Gers
1:Raymond Dehn>Troy Benjegerdes>David Rosenfeld
1:Raymond Dehn>Troy Benjegerdes>Gregg A. Iverson
1:Raymond Dehn>Troy Benjegerdes>L.A. Nik
1:Raymond Dehn>Troy Benjegerdes>Ronald Lischeid
1:Raymond Dehn>Troy Benjegerdes>Tom Hoch
1:Raymond Dehn>Undeclared Write-ins>Captain Jack Sparrow
1:Raymond Dehn>Undeclared Write-ins>Nekima Levy-Pounds
1:Ronald Lischeid>Al Flowers>L.A. Nik
1:Ronald Lischeid>Aswar Rahman
1:Ronald Lischeid>Aswar Rahman>Betsy Hodges
1:Ronald Lischeid>Aswar Rahman>Charlie Gers
1:Ronald Lischeid>Aswar Rahman>Ian Simpson
1:Ronald Lischeid>Aswar Rahman>Jacob Frey
1:Ronald Lischeid>Aswar Rahman>Nekima Levy-Pounds
1:Ronald Lischeid>Aswar Rahman>Raymond Dehn
1:Ronald Lischeid>Aswar Rahman>Tom Hoch
1:Ronald Lischeid>Betsy Hodges>Charlie Gers
1:Ronald Lischeid>Betsy Hodges>David Rosenfeld
1:Ronald Lischeid>Betsy Hodges>Jacob Frey
1:Ronald Lischeid>Betsy Hodges>L.A. Nik
1:Ronald Lischeid>Betsy Hodges>Nekima Levy-Pounds
1:Ronald Lischeid>Betsy Hodges>Raymond Dehn
1:Ronald Lischeid>Captain Jack Sparrow>Aswar Rahman
1:Ronald Lischeid>Captain Jack Sparrow>Jacob Frey
1:Ronald Lischeid>Captain Jack Sparrow>Raymond Dehn
1:Ronald Lischeid>Captain Jack Sparrow>Troy Benjegerdes
1:Ronald Lischeid>Charlie Gers>David John Wilson
1:Ronald Lischeid>Charlie Gers>David Rosenfeld
1:Ronald Lischeid>Charlie Gers>Gregg A. Iverson
1:Ronald Lischeid>Charlie Gers>Ian Simpson
1:Ronald Lischeid>Charlie Gers>Nekima Levy-Pounds
1:Ronald Lischeid>David John Wilson
1:Ronald Lischeid>David John Wilson>David Rosenfeld
1:Ronald Lischeid>David John Wilson>L.A. Nik
1:Ronald Lischeid>David Rosenfeld>Al Flowers
1:Ronald Lischeid>David Rosenfeld>Aswar Rahman
1:Ronald Lischeid>David Rosenfeld>Captain Jack Sparrow
1:Ronald Lischeid>David Rosenfeld>Charlie Gers
1:Ronald Lischeid>David Rosenfeld>David John Wilson
1:Ronald Lischeid>David Rosenfeld>Tom Hoch
1:Ronald Lischeid>Gregg A. Iverson>Charlie Gers
1:Ronald Lischeid>Gregg A. Iverson>David John Wilson
1:Ronald Lischeid>Gregg A. Iverson>L.A. Nik
1:Ronald Lischeid>Gregg A. Iverson>Nekima Levy-Pounds
1:Ronald Lischeid>Gregg A. Iverson>Raymond Dehn
1:Ronald Lischeid>Ian Simpson>Betsy Hodges
1:Ronald Lischeid>Ian Simpson>David John Wilson
1:Ronald Lischeid>Ian Simpson>Jacob Frey
1:Ronald Lischeid>Ian Simpson>Tom Hoch
1:Ronald Lischeid>Jacob Frey>Al Flowers
1:Ronald Lischeid>Jacob Frey>Betsy Hodges
1:Ronald Lischeid>Jacob Frey>Captain Jack Sparrow
1:Ronald Lischeid>Jacob Frey>Charlie Gers
1:Ronald Lischeid>Jacob Frey>L.A. Nik
1:Ronald Lischeid>L.A. Nik>Captain Jack Sparrow
1:Ronald Lischeid>L.A. Nik>Troy Benjegerdes
1:Ronald Lischeid>L.A. Nik>Undeclared Write-ins
1:Ronald Lischeid>Nekima Levy-Pounds
1:Ronald Lischeid>Nekima Levy-Pounds>Captain Jack Sparrow
1:Ronald Lischeid>Nekima Levy-Pounds>Tom Hoch
1:Ronald Lischeid>Raymond Dehn>Al Flowers
1:Ronald Lischeid>Raymond Dehn>Betsy Hodges
1:Ronald Lischeid>Raymond Dehn>Captain Jack Sparrow
1:Ronald Lischeid>Raymond Dehn>Charlie Gers
1:Ronald Lischeid>Raymond Dehn>David John Wilson
1:Ronald Lischeid>Raymond Dehn>Gregg A. Iverson
1:Ronald Lischeid>Raymond Dehn>Nekima Levy-Pounds
1:Ronald Lischeid>Tom Hoch>Al Flowers
1:Ronald Lischeid>Tom Hoch>Aswar Rahman
1:Ronald Lischeid>Tom Hoch>David John Wilson
1:Ronald Lischeid>Tom Hoch>David Rosenfeld
1:Ronald Lischeid>Tom Hoch>L.A. Nik
1:Ronald Lischeid>Tom Hoch>Troy Benjegerdes
1:Ronald Lischeid>Troy Benjegerdes>Betsy Hodges
1:Ronald Lischeid>Troy Benjegerdes>Captain Jack Sparrow
1:Ronald Lischeid>Troy Benjegerdes>Gregg A. Iverson
1:Ronald Lischeid>Troy Benjegerdes>Ian Simpson
1:Ronald Lischeid>Troy Benjegerdes>Jacob Frey
1:Ronald Lischeid>Troy Benjegerdes>Raymond Dehn
1:Tom Hoch>Al Flowers>Ian Simpson
1:Tom Hoch>Al Flowers>Undeclared Write-ins
1:Tom Hoch>David John Wilson>Ian Simpson
1:Tom Hoch>David John Wilson>Undeclared Write-ins
1:Tom Hoch>David Rosenfeld>Troy Benjegerdes
1:Tom Hoch>Gregg A. Iverson>David John Wilson
1:Tom Hoch>Ian Simpson>Al Flowers
1:Tom Hoch>Ian Simpson>Charlie Gers
1:Tom Hoch>Ian Simpson>David Rosenfeld
1:Tom Hoch>Ian Simpson>Nekima Levy-Pounds
1:Tom Hoch>Ian Simpson>Raymond Dehn
1:Tom Hoch>Ian Simpson>Troy Benjegerdes
1:Tom Hoch>Ian Simpson>Undeclared Write-ins
1:Tom Hoch>Troy Benjegerdes>Al Flowers
1:Tom Hoch>Troy Benjegerdes>David John Wilson
1:Tom Hoch>Troy Benjegerdes>Ian Simpson
1:Tom Hoch>Troy Benjegerdes>Nekima Levy-Pounds
1:Tom Hoch>Troy Benjegerdes>Ronald Lischeid
1:Tom Hoch>Undeclared Write-ins>Al Flowers
1:Tom Hoch>Undeclared Write-ins>Raymond Dehn
1:Troy Benjegerdes>Al Flowers
1:Troy Benjegerdes>Al Flowers>Aswar Rahman
1:Troy Benjegerdes>Al Flowers>Betsy Hodges
1:Troy Benjegerdes>Al Flowers>Nekima Levy-Pounds
1:Troy Benjegerdes>Al Flowers>Raymond Dehn
1:Troy Benjegerdes>Al Flowers>Ronald Lischeid
1:Troy Benjegerdes>Aswar Rahman>David John Wilson
1:Troy Benjegerdes>Aswar Rahman>Raymond Dehn
1:Troy Benjegerdes>Aswar Rahman>Tom Hoch
1:Troy Benjegerdes>Betsy Hodges>Aswar Rahman
1:Troy Benjegerdes>Betsy Hodges>Gregg A. Iverson
1:Troy Benjegerdes>Betsy Hodges>Ian Simpson
1:Troy Benjegerdes>Betsy Hodges>Raymond Dehn
1:Troy Benjegerdes>Captain Jack Sparrow>David John Wilson
1:Troy Benjegerdes>Captain Jack Sparrow>L.A. Nik
1:Troy Benjegerdes>Captain Jack Sparrow>Nekima Levy-Pounds
1:Troy Benjegerdes>Captain Jack Sparrow>Raymond Dehn
1:Troy Benjegerdes>Captain Jack Sparrow>Tom Hoch
1:Troy Benjegerdes>Charlie Gers>Betsy Hodges
1:Troy Benjegerdes>Charlie Gers>Captain Jack Sparrow
1:Troy Benjegerdes>David John Wilson
1:Troy Benjegerdes>David John Wilson>Betsy Hodges
1:Troy Benjegerdes>David John Wilson>Captain Jack Sparrow
1:Troy Benjegerdes>David John Wilson>Charlie Gers
1:Troy Benjegerdes>David John Wilson>L.A. Nik
1:Troy Benjegerdes>David Rosenfeld
1:Troy Benjegerdes>David Rosenfeld>Charlie Gers
1:Troy Benjegerdes>David Rosenfeld>Jacob Frey
1:Troy Benjegerdes>Gregg A. Iverson>Aswar Rahman
1:Troy Benjegerdes>Gregg A. Iverson>Tom Hoch
1:Troy Benjegerdes>Ian Simpson>Captain Jack Sparrow
1:Troy Benjegerdes>Ian Simpson>Ronald Lischeid
1:Troy Benjegerdes>Jacob Frey>Al Flowers
1:Troy Benjegerdes>Jacob Frey>Captain Jack Sparrow
1:Troy Benjegerdes>Jacob Frey>Raymond Dehn
1:Troy Benjegerdes>Jacob Frey>Ronald Lischeid
1:Troy Benjegerdes>L.A. Nik>Betsy Hodges
1:Troy Benjegerdes>L.A. Nik>David Rosenfeld
1:Troy Benjegerdes>L.A. Nik>Ronald Lischeid
1:Troy Benjegerdes>Nekima Levy-Pounds>Aswar Rahman
1:Troy Benjegerdes>Nekima Levy-Pounds>Jacob Frey
1:Troy Benjegerdes>Raymond Dehn>Al Flowers
1:Troy Benjegerdes>Raymond Dehn>David John Wilson
1:Troy Benjegerdes>Raymond Dehn>Gregg A. Iverson
1:Troy Benjegerdes>Raymond Dehn>Ian Simpson
1:Troy Benjegerdes>Raymond Dehn>L.A. Nik
1:Troy Benjegerdes>Raymond Dehn>Tom Hoch
1:Troy Benjegerdes>Ronald Lischeid>Al Flowers
1:Troy Benjegerdes>Ronald Lischeid>Captain Jack Sparrow
1:Troy Benjegerdes>Ronald Lischeid>Ian Simpson
1:Troy Benjegerdes>Ronald Lischeid>Tom Hoch
1:Troy Benjegerdes>Tom Hoch>Aswar Rahman
1:Troy Benjegerdes>Tom Hoch>Betsy Hodges
1:Troy Benjegerdes>Tom Hoch>David John Wilson
1:Troy Benjegerdes>Tom Hoch>Gregg A. Iverson
1:Troy Benjegerdes>Tom Hoch>Nekima Levy-Pounds
1:Troy Benjegerdes>Undeclared Write-ins>Ronald Lischeid
1:Undeclared Write-ins>Betsy Hodges
1:Undeclared Write-ins>Betsy Hodges>Captain Jack Sparrow
1:Undeclared Write-ins>Betsy Hodges>Ian Simpson
1:Undeclared Write-ins>Betsy Hodges>Nekima Levy-Pounds
1:Undeclared Write-ins>Betsy Hodges>Raymond Dehn
1:Undeclared Write-ins>Betsy Hodges>Tom Hoch
1:Undeclared Write-ins>Captain Jack Sparrow>Betsy Hodges
1:Undeclared Write-ins>Captain Jack Sparrow>David John Wilson
1:Undeclared Write-ins>Captain Jack Sparrow>David Rosenfeld
1:Undeclared Write-ins>Charlie Gers>Jacob Frey
1:Undeclared Write-ins>Charlie Gers>L.A. Nik
1:Undeclared Write-ins>Charlie Gers>Ronald Lischeid
1:Undeclared Write-ins>David John Wilson>Captain Jack Sparrow
1:Undeclared Write-ins>David Rosenfeld
1:Undeclared Write-ins>David Rosenfeld>Ian Simpson
1:Undeclared Write-ins>David Rosenfeld>Troy Benjegerdes
1:Undeclared Write-ins>Gregg A. Iverson>Tom Hoch
1:Undeclared Write-ins>Gregg A. Iverson>Troy Benjegerdes
1:Undeclared Write-ins>Jacob Frey
1:Undeclared Write-ins>Jacob Frey>Al Flowers
1:Undeclared Write-ins>Jacob Frey>Aswar Rahman
1:Undeclared Write-ins>Nekima Levy-Pounds>Al Flowers
1:Undeclared Write-ins>Nekima Levy-Pounds>David John Wilson
1:Undeclared Write-ins>Raymond Dehn>Jacob Frey
1:Undeclared Write-ins>Tom Hoch>Al Flowers
1:Undeclared Write-ins>Tom Hoch>Aswar Rahman
1:Undeclared Write-ins>Tom Hoch>Betsy Hodges
1:Undeclared Write-ins>Troy Benjegerdes>Ronald Lischeid
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 104484 ballots (ranked ballots).

Ballots:
   4636 × Jacob Frey
   3410 × Raymond Dehn > Nekima Levy-Pounds > Betsy Hodges
   3192 × Betsy Hodges
   2854 × Tom Hoch
   2676 × Jacob Frey > Tom Hoch > Betsy Hodges
   2520 × Jacob Frey > Tom Hoch
   2189 × Tom Hoch > Jacob Frey
   2187 × Nekima Levy-Pounds > Raymond Dehn > Betsy Hodges
   2115 × Raymond Dehn > Betsy Hodges > Nekima Levy-Pounds
   2069 × Tom Hoch > Jacob Frey > Betsy Hodges
   1908 × Betsy Hodges > Raymond Dehn > Nekima Levy-Pounds
   1875 × Jacob Frey > Tom Hoch > Raymond Dehn
   1472 × Tom Hoch > Jacob Frey > Raymond Dehn
   1466 × Betsy Hodges > Nekima Levy-Pounds > Raymond Dehn
   1418 × Jacob Frey > Betsy Hodges > Tom Hoch
   1334 × Nekima Levy-Pounds > Betsy Hodges > Raymond Dehn
   1302 × Jacob Frey > Tom Hoch > Nekima Levy-Pounds
   1188 × Betsy Hodges > Jacob Frey > Tom Hoch
   1181 × Raymond Dehn > Nekima Levy-Pounds > Jacob Frey
   1097 × Tom Hoch > Jacob Frey > Nekima Levy-Pounds
   1078 × Jacob Frey > Raymond Dehn > Tom Hoch
   1078 × Nekima Levy-Pounds
   942 × Nekima Levy-Pounds > Raymond Dehn > Jacob Frey
   940 × Betsy Hodges > Tom Hoch > Jacob Frey
   848 × Betsy Hodges > Jacob Frey > Nekima Levy-Pounds
   838 × Betsy Hodges > Raymond Dehn > Jacob Frey
   834 × Tom Hoch > Raymond Dehn > Jacob Frey
   822 × Jacob Frey > Betsy Hodges
   819 × Raymond Dehn
   796 × Raymond Dehn > Jacob Frey > Nekima Levy-Pounds
   792 × Betsy Hodges > Nekima Levy-Pounds > Jacob Frey
   790 × Jacob Frey > Raymond Dehn > Betsy Hodges
   776 × Tom Hoch > Betsy Hodges > Jacob Frey
   766 × Raymond Dehn > Nekima Levy-Pounds > Tom Hoch
   761 × Jacob Frey > Betsy Hodges > Nekima Levy-Pounds
   750 × Raymond Dehn > Jacob Frey > Betsy Hodges
   746 × Nekima Levy-Pounds > Jacob Frey > Betsy Hodges
   746 × Raymond Dehn > Betsy Hodges > Jacob Frey
   744 × Nekima Levy-Pounds > Betsy Hodges > Jacob Frey
   743 × Raymond Dehn > Nekima Levy-Pounds
   711 × Jacob Frey > Raymond Dehn > Nekima Levy-Pounds
   701 × Jacob Frey > Nekima Levy-Pounds > Betsy Hodges
   694 × Jacob Frey > Nekima Levy-Pounds > Tom Hoch
   677 × Jacob Frey > Betsy Hodges > Raymond Dehn
   671 × Betsy Hodges > Jacob Frey > Raymond Dehn
   669 × Betsy Hodges > Jacob Frey
   660 × Raymond Dehn > Jacob Frey > Tom Hoch
   659 × Nekima Levy-Pounds > Raymond Dehn > Tom Hoch
   656 × Raymond Dehn > Tom Hoch > Jacob Frey
   578 × Betsy Hodges > Raymond Dehn
   575 × Tom Hoch > Betsy Hodges
   571 × Nekima Levy-Pounds > Betsy Hodges
   560 × Jacob Frey > Nekima Levy-Pounds > Raymond Dehn
   555 × Raymond Dehn > Tom Hoch > Nekima Levy-Pounds
   551 × Tom Hoch > Nekima Levy-Pounds > Jacob Frey
   537 × Betsy Hodges > Tom Hoch
   525 × Nekima Levy-Pounds > Jacob Frey > Tom Hoch
   521 × Nekima Levy-Pounds > Raymond Dehn
   519 × Nekima Levy-Pounds > Jacob Frey > Raymond Dehn
   502 × Betsy Hodges > Nekima Levy-Pounds
   486 × Raymond Dehn > Betsy Hodges
   481 × Betsy Hodges > Nekima Levy-Pounds > Tom Hoch
   481 × Raymond Dehn > Tom Hoch > Betsy Hodges
   456 × Betsy Hodges > Tom Hoch > Nekima Levy-Pounds
   454 × Tom Hoch > Raymond Dehn > Nekima Levy-Pounds
   449 × Nekima Levy-Pounds > Tom Hoch > Jacob Frey
   436 × Betsy Hodges > Raymond Dehn > Tom Hoch
   417 × Nekima Levy-Pounds > Betsy Hodges > Tom Hoch
   408 × Raymond Dehn > Betsy Hodges > Tom Hoch
   401 × Tom Hoch > Raymond Dehn > Betsy Hodges
   378 × Betsy Hodges > Tom Hoch > Raymond Dehn
   372 × Tom Hoch > Betsy Hodges > Nekima Levy-Pounds
   363 × Tom Hoch > Nekima Levy-Pounds > Betsy Hodges
   360 × Nekima Levy-Pounds > Tom Hoch > Betsy Hodges
   350 × Jacob Frey > Nekima Levy-Pounds
   330 × Jacob Frey > Raymond Dehn
   328 × Charlie Gers
   327 × Nekima Levy-Pounds > Tom Hoch > Raymond Dehn
   324 × Tom Hoch > Raymond Dehn
   314 × Tom Hoch > Nekima Levy-Pounds > Raymond Dehn
   302 × Tom Hoch > Betsy Hodges > Raymond Dehn
   295 × Jacob Frey > Tom Hoch > Aswar Rahman
   278 × Nekima Levy-Pounds > Jacob Frey
   269 × Tom Hoch > Nekima Levy-Pounds
   268 × Jacob Frey > Tom Hoch > Captain Jack Sparrow
   262 × Tom Hoch > Jacob Frey > Captain Jack Sparrow
   260 × Raymond Dehn > Jacob Frey
   258 × Tom Hoch > Jacob Frey > Gregg A. Iverson
   251 × Tom Hoch > Jacob Frey > Aswar Rahman
   245 × Raymond Dehn > Nekima Levy-Pounds > Al Flowers
   245 × Raymond Dehn > Nekima Levy-Pounds > David Rosenfeld
   233 × Raymond Dehn > Nekima Levy-Pounds > Captain Jack Sparrow
   231 × Raymond Dehn > Tom Hoch
   216 × Nekima Levy-Pounds > Raymond Dehn > Al Flowers
   203 × Jacob Frey > Tom Hoch > Gregg A. Iverson
   200 × Nekima Levy-Pounds > Raymond Dehn > Aswar Rahman
   196 × Nekima Levy-Pounds > Betsy Hodges > Al Flowers
   195 × Raymond Dehn > Nekima Levy-Pounds > Aswar Rahman
   195 × Tom Hoch > Jacob Frey > Al Flowers
   192 × Nekima Levy-Pounds > Tom Hoch
   189 × Jacob Frey > Tom Hoch > Al Flowers
   188 × L.A. Nik
   174 × Tom Hoch > Jacob Frey > Charlie Gers
   153 × Nekima Levy-Pounds > Raymond Dehn > David Rosenfeld
   146 × Aswar Rahman
   144 × Nekima Levy-Pounds > Al Flowers > Betsy Hodges
   143 × Al Flowers
   141 × Betsy Hodges > Jacob Frey > Gregg A. Iverson
   137 × Nekima Levy-Pounds > Betsy Hodges > Aswar Rahman
   137 × Tom Hoch > Jacob Frey > L.A. Nik
   134 × Jacob Frey > Tom Hoch > Charlie Gers
   131 × Betsy Hodges > Nekima Levy-Pounds > Al Flowers
   131 × Betsy Hodges > Nekima Levy-Pounds > Aswar Rahman
   127 × Nekima Levy-Pounds > Al Flowers
   123 × Nekima Levy-Pounds > Raymond Dehn > Captain Jack Sparrow
   110 × Betsy Hodges > Tom Hoch > Al Flowers
   107 × Nekima Levy-Pounds > Al Flowers > Raymond Dehn
   105 × Jacob Frey > Nekima Levy-Pounds > Aswar Rahman
   104 × Jacob Frey > Betsy Hodges > Aswar Rahman
   101 × Jacob Frey > Betsy Hodges > Gregg A. Iverson
   100 × Raymond Dehn > Betsy Hodges > Al Flowers
    97 × Nekima Levy-Pounds > Aswar Rahman > Betsy Hodges
    97 × Nekima Levy-Pounds > Jacob Frey > Aswar Rahman
    97 × Tom Hoch > Charlie Gers
    95 × Nekima Levy-Pounds > Jacob Frey > Al Flowers
    93 × Nekima Levy-Pounds > Al Flowers > Tom Hoch
    91 × Tom Hoch > Nekima Levy-Pounds > Aswar Rahman
    91 × Tom Hoch > Raymond Dehn > Al Flowers
    90 × Jacob Frey > Tom Hoch > L.A. Nik
    89 × Jacob Frey > Tom Hoch > David John Wilson
    88 × Captain Jack Sparrow
    86 × Nekima Levy-Pounds > Tom Hoch > Al Flowers
    86 × Tom Hoch > Jacob Frey > David John Wilson
    86 × Undeclared Write-ins
    84 × Tom Hoch > Aswar Rahman > Jacob Frey
    83 × Tom Hoch > Raymond Dehn > Aswar Rahman
    81 × Jacob Frey > Betsy Hodges > Captain Jack Sparrow
    80 × Betsy Hodges > Jacob Frey > Aswar Rahman
    80 × Gregg A. Iverson
    80 × Ronald Lischeid
    79 × Nekima Levy-Pounds > Al Flowers > Aswar Rahman
    78 × Raymond Dehn > Betsy Hodges > Captain Jack Sparrow
    75 × Betsy Hodges > Aswar Rahman
    75 × Betsy Hodges > Gregg A. Iverson > Jacob Frey
    75 × Nekima Levy-Pounds > Aswar Rahman > Raymond Dehn
    75 × Tom Hoch > Nekima Levy-Pounds > Al Flowers
    73 × Betsy Hodges > Jacob Frey > Al Flowers
    73 × Betsy Hodges > Tom Hoch > Aswar Rahman
    72 × Jacob Frey > Aswar Rahman > Tom Hoch
    72 × Jacob Frey > Nekima Levy-Pounds > Al Flowers
    72 × Nekima Levy-Pounds > Al Flowers > Jacob Frey
    71 × David Rosenfeld
    71 × Nekima Levy-Pounds > Jacob Frey > Gregg A. Iverson
    70 × Jacob Frey > Nekima Levy-Pounds > Captain Jack Sparrow
    70 × Tom Hoch > Betsy Hodges > Al Flowers
    69 × Jacob Frey > Gregg A. Iverson > Betsy Hodges
    69 × Tom Hoch > Betsy Hodges > Captain Jack Sparrow
    68 × Nekima Levy-Pounds > Jacob Frey > Captain Jack Sparrow
    67 × Nekima Levy-Pounds > Tom Hoch > Aswar Rahman
    67 × Tom Hoch > Raymond Dehn > Captain Jack Sparrow
    66 × Betsy Hodges > Aswar Rahman > Nekima Levy-Pounds
    66 × Betsy Hodges > Jacob Frey > Captain Jack Sparrow
    65 × Charlie Gers > L.A. Nik
    64 × David John Wilson
    64 × Nekima Levy-Pounds > Betsy Hodges > Captain Jack Sparrow
    63 × Raymond Dehn > Al Flowers > Betsy Hodges
    63 × Tom Hoch > Al Flowers > Raymond Dehn
    62 × Tom Hoch > Nekima Levy-Pounds > Captain Jack Sparrow
    61 × Tom Hoch > Betsy Hodges > Aswar Rahman
    61 × Tom Hoch > Captain Jack Sparrow
    61 × Tom Hoch > Raymond Dehn > Gregg A. Iverson
    60 × Betsy Hodges > Tom Hoch > Captain Jack Sparrow
    60 × Jacob Frey > Aswar Rahman
    60 × Jacob Frey > Raymond Dehn > Captain Jack Sparrow
    60 × Raymond Dehn > Betsy Hodges > Aswar Rahman
    60 × Tom Hoch > Al Flowers > Jacob Frey
    60 × Tom Hoch > Aswar Rahman
    59 × Betsy Hodges > Nekima Levy-Pounds > Gregg A. Iverson
    59 × Betsy Hodges > Raymond Dehn > Aswar Rahman
    59 × Nekima Levy-Pounds > Aswar Rahman
    59 × Nekima Levy-Pounds > Betsy Hodges > David Rosenfeld
    58 × Betsy Hodges > Al Flowers > Nekima Levy-Pounds
    58 × Betsy Hodges > Al Flowers > Tom Hoch
    58 × Betsy Hodges > Nekima Levy-Pounds > Captain Jack Sparrow
    58 × Betsy Hodges > Raymond Dehn > Al Flowers
    58 × Jacob Frey > Betsy Hodges > Al Flowers
    57 × Jacob Frey > Al Flowers > Tom Hoch
    56 × Jacob Frey > Aswar Rahman > Nekima Levy-Pounds
    55 × Nekima Levy-Pounds > Aswar Rahman > Al Flowers
    55 × Tom Hoch > Al Flowers > Nekima Levy-Pounds
    55 × Tom Hoch > Charlie Gers > Jacob Frey
    54 × Raymond Dehn > Aswar Rahman > Nekima Levy-Pounds
    54 × Raymond Dehn > Betsy Hodges > David Rosenfeld
    53 × Jacob Frey > Gregg A. Iverson > Tom Hoch
    53 × Jacob Frey > Raymond Dehn > Al Flowers
    53 × Tom Hoch > Aswar Rahman > Nekima Levy-Pounds
    52 × Raymond Dehn > Tom Hoch > Al Flowers
    51 × Charlie Gers > Tom Hoch > Jacob Frey
    50 × Betsy Hodges > Tom Hoch > Gregg A. Iverson
    50 × Raymond Dehn > David Rosenfeld > Nekima Levy-Pounds
    50 × Raymond Dehn > Jacob Frey > Captain Jack Sparrow
    50 × Raymond Dehn > Nekima Levy-Pounds > David John Wilson
    49 × Jacob Frey > Raymond Dehn > Aswar Rahman
    49 × Nekima Levy-Pounds > Tom Hoch > Captain Jack Sparrow
    49 × Raymond Dehn > Aswar Rahman > Betsy Hodges
    49 × Tom Hoch > L.A. Nik
    48 × Betsy Hodges > Al Flowers
    48 × Jacob Frey > Aswar Rahman > Betsy Hodges
    48 × Jacob Frey > Nekima Levy-Pounds > Gregg A. Iverson
    48 × Raymond Dehn > Al Flowers > Nekima Levy-Pounds
    48 × Raymond Dehn > Tom Hoch > Captain Jack Sparrow
    47 × Betsy Hodges > Aswar Rahman > Tom Hoch
    47 × Nekima Levy-Pounds > Aswar Rahman > Jacob Frey
    47 × Nekima Levy-Pounds > Aswar Rahman > Tom Hoch
    47 × Raymond Dehn > Tom Hoch > Aswar Rahman
    47 × Tom Hoch > Jacob Frey > Ronald Lischeid
    46 × Tom Hoch > Al Flowers
    46 × Tom Hoch > Jacob Frey > David Rosenfeld
    44 × Tom Hoch > Captain Jack Sparrow > David John Wilson
    43 × Jacob Frey > Captain Jack Sparrow
    43 × Tom Hoch > Aswar Rahman > Betsy Hodges
    43 × Tom Hoch > Charlie Gers > L.A. Nik
    42 × Jacob Frey > Charlie Gers
    42 × Jacob Frey > Tom Hoch > David Rosenfeld
    42 × Nekima Levy-Pounds > Raymond Dehn > David John Wilson
    42 × Tom Hoch > Betsy Hodges > Gregg A. Iverson
    42 × Tom Hoch > Jacob Frey > Undeclared Write-ins
    42 × Troy Benjegerdes
    41 × Betsy Hodges > Aswar Rahman > Al Flowers
    40 × Betsy Hodges > Al Flowers > Jacob Frey
    40 × Tom Hoch > L.A. Nik > Jacob Frey
    39 × Betsy Hodges > Aswar Rahman > Jacob Frey
    39 × Nekima Levy-Pounds > Betsy Hodges > Gregg A. Iverson
    37 × Raymond Dehn > Jacob Frey > Aswar Rahman
    37 × Tom Hoch > Aswar Rahman > Raymond Dehn
    36 × Charlie Gers > L.A. Nik > Ronald Lischeid
    36 × Charlie Gers > Tom Hoch
    36 × Nekima Levy-Pounds > Jacob Frey > David Rosenfeld
    36 × Raymond Dehn > David Rosenfeld > Captain Jack Sparrow
    35 × Jacob Frey > Al Flowers > Betsy Hodges
    35 × Jacob Frey > Betsy Hodges > David Rosenfeld
    35 × Tom Hoch > Gregg A. Iverson > Jacob Frey
    34 × Betsy Hodges > Captain Jack Sparrow
    34 × Betsy Hodges > Raymond Dehn > Captain Jack Sparrow
    34 × Jacob Frey > Gregg A. Iverson
    34 × Jacob Frey > Gregg A. Iverson > Nekima Levy-Pounds
    34 × L.A. Nik > Charlie Gers
    34 × Raymond Dehn > Jacob Frey > Al Flowers
    34 × Tom Hoch > Al Flowers > Betsy Hodges
    33 × Betsy Hodges > Gregg A. Iverson
    33 × Betsy Hodges > Gregg A. Iverson > Tom Hoch
    33 × Charlie Gers > Jacob Frey > Tom Hoch
    33 × Jacob Frey > Aswar Rahman > Raymond Dehn
    33 × Jacob Frey > Tom Hoch > Undeclared Write-ins
    33 × Raymond Dehn > Al Flowers
    33 × Raymond Dehn > Nekima Levy-Pounds > Undeclared Write-ins
    33 × Tom Hoch > Raymond Dehn > Charlie Gers
    32 × Betsy Hodges > Al Flowers > Raymond Dehn
    32 × Raymond Dehn > David Rosenfeld
    32 × Raymond Dehn > David Rosenfeld > Betsy Hodges
    31 × Aswar Rahman > Tom Hoch > Jacob Frey
    31 × Betsy Hodges > Gregg A. Iverson > Nekima Levy-Pounds
    31 × Betsy Hodges > Jacob Frey > David Rosenfeld
    31 × Nekima Levy-Pounds > David Rosenfeld > Raymond Dehn
    31 × Raymond Dehn > Aswar Rahman > Jacob Frey
    31 × Raymond Dehn > Jacob Frey > David Rosenfeld
    30 × Al Flowers > Nekima Levy-Pounds > Betsy Hodges
    30 × David Rosenfeld > Raymond Dehn > Nekima Levy-Pounds
    30 × Jacob Frey > Al Flowers
    30 × Jacob Frey > Betsy Hodges > Charlie Gers
    30 × Tom Hoch > Aswar Rahman > Al Flowers
    30 × Tom Hoch > Betsy Hodges > Charlie Gers
    30 × Tom Hoch > Charlie Gers > Captain Jack Sparrow
    30 × Tom Hoch > L.A. Nik > Charlie Gers
    29 × Betsy Hodges > Aswar Rahman > Raymond Dehn
    29 × Jacob Frey > Al Flowers > Nekima Levy-Pounds
    29 × Jacob Frey > Tom Hoch > Ian Simpson
    29 × Nekima Levy-Pounds > Tom Hoch > David Rosenfeld
    29 × Tom Hoch > Undeclared Write-ins
    28 × Jacob Frey > Charlie Gers > Tom Hoch
    28 × Nekima Levy-Pounds > David Rosenfeld > Betsy Hodges
    28 × Raymond Dehn > Aswar Rahman > Tom Hoch
    28 × Tom Hoch > Gregg A. Iverson > Raymond Dehn
    28 × Tom Hoch > Jacob Frey > Troy Benjegerdes
    27 × Aswar Rahman > Jacob Frey > Tom Hoch
    27 × Betsy Hodges > David Rosenfeld
    27 × Betsy Hodges > Tom Hoch > David John Wilson
    27 × Charlie Gers > Ronald Lischeid > L.A. Nik
    27 × Jacob Frey > Captain Jack Sparrow > David John Wilson
    27 × Jacob Frey > Raymond Dehn > Gregg A. Iverson
    27 × Nekima Levy-Pounds > Captain Jack Sparrow
    27 × Tom Hoch > Captain Jack Sparrow > Jacob Frey
    27 × Tom Hoch > Gregg A. Iverson
    27 × Tom Hoch > Gregg A. Iverson > Betsy Hodges
    27 × Tom Hoch > Nekima Levy-Pounds > Gregg A. Iverson
    27 × Tom Hoch > Raymond Dehn > David John Wilson
    27 × Tom Hoch > Raymond Dehn > L.A. Nik
    26 × Al Flowers > Betsy Hodges
    26 × Charlie Gers > Undeclared Write-ins
    26 × Jacob Frey > Gregg A. Iverson > Raymond Dehn
    26 × Nekima Levy-Pounds > Betsy Hodges > David John Wilson
    26 × Raymond Dehn > Al Flowers > Tom Hoch
    25 × David Rosenfeld > Nekima Levy-Pounds > Raymond Dehn
    25 × Ian Simpson
    25 × Raymond Dehn > Betsy Hodges > Gregg A. Iverson
    24 × Al Flowers > Nekima Levy-Pounds
    24 × Betsy Hodges > Tom Hoch > David Rosenfeld
    24 × Jacob Frey > Captain Jack Sparrow > Tom Hoch
    24 × Jacob Frey > Tom Hoch > Troy Benjegerdes
    24 × Raymond Dehn > Nekima Levy-Pounds > L.A. Nik
    24 × Tom Hoch > Captain Jack Sparrow > L.A. Nik
    23 × Al Flowers > Raymond Dehn > Tom Hoch
    23 × Betsy Hodges > Al Flowers > Aswar Rahman
    23 × Betsy Hodges > Captain Jack Sparrow > David John Wilson
    23 × Jacob Frey > Charlie Gers > Captain Jack Sparrow
    23 × Jacob Frey > L.A. Nik > Tom Hoch
    23 × Jacob Frey > Undeclared Write-ins
    23 × Nekima Levy-Pounds > Al Flowers > Captain Jack Sparrow
    23 × Raymond Dehn > Jacob Frey > Gregg A. Iverson
    23 × Tom Hoch > Jacob Frey > Ian Simpson
    23 × Tom Hoch > L.A. Nik > Captain Jack Sparrow
    23 × Tom Hoch > Raymond Dehn > David Rosenfeld
    22 × Al Flowers > Betsy Hodges > Nekima Levy-Pounds
    22 × Aswar Rahman > Jacob Frey > Betsy Hodges
    22 × Aswar Rahman > Nekima Levy-Pounds > Jacob Frey
    22 × Jacob Frey > Al Flowers > Raymond Dehn
    22 × Jacob Frey > Nekima Levy-Pounds > David John Wilson
    22 × Jacob Frey > Nekima Levy-Pounds > David Rosenfeld
    22 × Jacob Frey > Tom Hoch > Ronald Lischeid
    22 × Nekima Levy-Pounds > David Rosenfeld
    22 × Raymond Dehn > Captain Jack Sparrow
    22 × Raymond Dehn > Tom Hoch > David Rosenfeld
    21 × Aswar Rahman > Raymond Dehn > Jacob Frey
    21 × Charlie Gers > L.A. Nik > Ian Simpson
    21 × Charlie Gers > Tom Hoch > L.A. Nik
    21 × Jacob Frey > Betsy Hodges > David John Wilson
    21 × Jacob Frey > L.A. Nik
    21 × Nekima Levy-Pounds > Raymond Dehn > Ian Simpson
    21 × Nekima Levy-Pounds > Raymond Dehn > Undeclared Write-ins
    21 × Raymond Dehn > Al Flowers > Jacob Frey
    21 × Tom Hoch > Betsy Hodges > David John Wilson
    21 × Tom Hoch > Nekima Levy-Pounds > David John Wilson
    20 × Aswar Rahman > Nekima Levy-Pounds > Betsy Hodges
    20 × Betsy Hodges > Undeclared Write-ins
    20 × Charlie Gers > L.A. Nik > David John Wilson
    20 × Jacob Frey > Betsy Hodges > L.A. Nik
    20 × L.A. Nik > Jacob Frey > Tom Hoch
    20 × Nekima Levy-Pounds > Aswar Rahman > Captain Jack Sparrow
    20 × Nekima Levy-Pounds > Jacob Frey > David John Wilson
    20 × Raymond Dehn > Al Flowers > Aswar Rahman
    20 × Tom Hoch > Aswar Rahman > Captain Jack Sparrow
    20 × Tom Hoch > Captain Jack Sparrow > Charlie Gers
    20 × Tom Hoch > Ronald Lischeid
    19 × Al Flowers > Tom Hoch > Betsy Hodges
    19 × Betsy Hodges > Nekima Levy-Pounds > David John Wilson
    19 × Raymond Dehn > Captain Jack Sparrow > Nekima Levy-Pounds
    19 × Raymond Dehn > Nekima Levy-Pounds > Ian Simpson
    19 × Raymond Dehn > Tom Hoch > L.A. Nik
    19 × Tom Hoch > Al Flowers > Captain Jack Sparrow
    19 × Tom Hoch > Captain Jack Sparrow > Betsy Hodges
    18 × Al Flowers > Betsy Hodges > Jacob Frey
    18 × Al Flowers > Nekima Levy-Pounds > Raymond Dehn
    18 × Betsy Hodges > Al Flowers > Captain Jack Sparrow
    18 × Betsy Hodges > Jacob Frey > David John Wilson
    18 × Betsy Hodges > Nekima Levy-Pounds > David Rosenfeld
    18 × Jacob Frey > Aswar Rahman > Captain Jack Sparrow
    18 × Jacob Frey > Charlie Gers > L.A. Nik
    18 × Jacob Frey > Gregg A. Iverson > Captain Jack Sparrow
    18 × L.A. Nik > Tom Hoch > Jacob Frey
    18 × Nekima Levy-Pounds > David Rosenfeld > Aswar Rahman
    18 × Raymond Dehn > Jacob Frey > David John Wilson
    18 × Tom Hoch > Betsy Hodges > L.A. Nik
    18 × Tom Hoch > Betsy Hodges > Ronald Lischeid
    17 × Aswar Rahman > Raymond Dehn > Tom Hoch
    17 × Betsy Hodges > Raymond Dehn > David Rosenfeld
    17 × Charlie Gers > Betsy Hodges
    17 × Charlie Gers > L.A. Nik > Captain Jack Sparrow
    17 × Jacob Frey > Captain Jack Sparrow > L.A. Nik
    17 × Jacob Frey > Raymond Dehn > David Rosenfeld
    17 × Nekima Levy-Pounds > David Rosenfeld > Captain Jack Sparrow
    17 × Raymond Dehn > Aswar Rahman
    17 × Raymond Dehn > David Rosenfeld > Tom Hoch
    17 × Tom Hoch > Al Flowers > Aswar Rahman
    17 × Tom Hoch > David John Wilson > Captain Jack Sparrow
    17 × Tom Hoch > Nekima Levy-Pounds > David Rosenfeld
    17 × Tom Hoch > Nekima Levy-Pounds > L.A. Nik
    16 × Al Flowers > Nekima Levy-Pounds > Jacob Frey
    16 × Al Flowers > Nekima Levy-Pounds > Tom Hoch
    16 × Al Flowers > Tom Hoch > Nekima Levy-Pounds
    16 × Aswar Rahman > Al Flowers > Raymond Dehn
    16 × Aswar Rahman > Betsy Hodges > Nekima Levy-Pounds
    16 × Aswar Rahman > Jacob Frey > Nekima Levy-Pounds
    16 × Betsy Hodges > Al Flowers > Gregg A. Iverson
    16 × Betsy Hodges > Gregg A. Iverson > Aswar Rahman
    16 × Betsy Hodges > Jacob Frey > Charlie Gers
    16 × Betsy Hodges > Raymond Dehn > David John Wilson
    16 × Betsy Hodges > Raymond Dehn > Gregg A. Iverson
    16 × Betsy Hodges > Tom Hoch > L.A. Nik
    16 × Charlie Gers > Captain Jack Sparrow > L.A. Nik
    16 × Jacob Frey > David John Wilson
    16 × Jacob Frey > David John Wilson > Captain Jack Sparrow
    16 × Nekima Levy-Pounds > Captain Jack Sparrow > Betsy Hodges
    16 × Nekima Levy-Pounds > Gregg A. Iverson
    16 × Nekima Levy-Pounds > Raymond Dehn > Troy Benjegerdes
    16 × Raymond Dehn > Aswar Rahman > Al Flowers
    16 × Raymond Dehn > Captain Jack Sparrow > David Rosenfeld
    16 × Tom Hoch > David John Wilson
    15 × Al Flowers > Raymond Dehn > Nekima Levy-Pounds
    15 × Aswar Rahman > Jacob Frey > Raymond Dehn
    15 × Aswar Rahman > Tom Hoch
    15 × Betsy Hodges > Gregg A. Iverson > Al Flowers
    15 × Charlie Gers > Jacob Frey
    15 × Charlie Gers > Jacob Frey > Betsy Hodges
    15 × David Rosenfeld > Raymond Dehn > Betsy Hodges
    15 × Jacob Frey > Raymond Dehn > Charlie Gers
    15 × Jacob Frey > Raymond Dehn > David John Wilson
    15 × L.A. Nik > Charlie Gers > Ian Simpson
    15 × L.A. Nik > Tom Hoch
    15 × Nekima Levy-Pounds > Aswar Rahman > David Rosenfeld
    15 × Nekima Levy-Pounds > Gregg A. Iverson > Betsy Hodges
    15 × Nekima Levy-Pounds > Jacob Frey > Charlie Gers
    15 × Raymond Dehn > Aswar Rahman > Captain Jack Sparrow
    15 × Raymond Dehn > Betsy Hodges > Charlie Gers
    15 × Raymond Dehn > Captain Jack Sparrow > Betsy Hodges
    15 × Raymond Dehn > Tom Hoch > David John Wilson
    15 × Raymond Dehn > Tom Hoch > Gregg A. Iverson
    15 × Tom Hoch > David Rosenfeld > Betsy Hodges
    14 × Al Flowers > Tom Hoch
    14 × Al Flowers > Tom Hoch > Jacob Frey
    14 × Betsy Hodges > Charlie Gers
    14 × Betsy Hodges > David Rosenfeld > Captain Jack Sparrow
    14 × Captain Jack Sparrow > Tom Hoch > Jacob Frey
    14 × David Rosenfeld > Nekima Levy-Pounds > Betsy Hodges
    14 × David Rosenfeld > Raymond Dehn > Jacob Frey
    14 × Gregg A. Iverson > Betsy Hodges > Jacob Frey
    14 × Jacob Frey > Captain Jack Sparrow > Betsy Hodges
    14 × Jacob Frey > Nekima Levy-Pounds > L.A. Nik
    14 × Jacob Frey > Raymond Dehn > L.A. Nik
    14 × L.A. Nik > Ronald Lischeid > Charlie Gers
    14 × Nekima Levy-Pounds > Captain Jack Sparrow > David John Wilson
    14 × Nekima Levy-Pounds > Gregg A. Iverson > Jacob Frey
    14 × Nekima Levy-Pounds > Raymond Dehn > L.A. Nik
    14 × Nekima Levy-Pounds > Tom Hoch > Ronald Lischeid
    14 × Nekima Levy-Pounds > Undeclared Write-ins
    14 × Raymond Dehn > Betsy Hodges > David John Wilson
    14 × Tom Hoch > Captain Jack Sparrow > Al Flowers
    14 × Tom Hoch > Captain Jack Sparrow > David Rosenfeld
    14 × Tom Hoch > Charlie Gers > Betsy Hodges
    14 × Tom Hoch > Charlie Gers > Ian Simpson
    14 × Tom Hoch > David John Wilson > Jacob Frey
    14 × Tom Hoch > L.A. Nik > Al Flowers
    13 × Aswar Rahman > Raymond Dehn
    13 × Betsy Hodges > David Rosenfeld > Jacob Frey
    13 × Betsy Hodges > David Rosenfeld > Tom Hoch
    13 × Betsy Hodges > Gregg A. Iverson > Raymond Dehn
    13 × Betsy Hodges > Tom Hoch > Troy Benjegerdes
    13 × Charlie Gers > L.A. Nik > Undeclared Write-ins
    13 × Jacob Frey > Al Flowers > Captain Jack Sparrow
    13 × Jacob Frey > Aswar Rahman > Al Flowers
    13 × Jacob Frey > David Rosenfeld
    13 × Jacob Frey > David Rosenfeld > Captain Jack Sparrow
    13 × L.A. Nik > Charlie Gers > Ronald Lischeid
    13 × Nekima Levy-Pounds > Al Flowers > David Rosenfeld
    13 × Nekima Levy-Pounds > David John Wilson > Captain Jack Sparrow
    13 × Nekima Levy-Pounds > Tom Hoch > David John Wilson
    13 × Nekima Levy-Pounds > Tom Hoch > Gregg A. Iverson
    13 × Ronald Lischeid > Tom Hoch > Jacob Frey
    13 × Tom Hoch > Betsy Hodges > David Rosenfeld
    13 × Tom Hoch > Captain Jack Sparrow > Ian Simpson
    13 × Tom Hoch > Captain Jack Sparrow > Raymond Dehn
    13 × Tom Hoch > David John Wilson > L.A. Nik
    13 × Tom Hoch > Gregg A. Iverson > Captain Jack Sparrow
    13 × Tom Hoch > Nekima Levy-Pounds > Charlie Gers
    13 × Tom Hoch > Raymond Dehn > Troy Benjegerdes
    12 × Al Flowers > Tom Hoch > Raymond Dehn
    12 × Aswar Rahman > Betsy Hodges
    12 × Aswar Rahman > Betsy Hodges > Raymond Dehn
    12 × Aswar Rahman > Jacob Frey
    12 × Aswar Rahman > Raymond Dehn > Nekima Levy-Pounds
    12 × Aswar Rahman > Tom Hoch > Betsy Hodges
    12 × Aswar Rahman > Tom Hoch > Nekima Levy-Pounds
    12 × Betsy Hodges > Aswar Rahman > Captain Jack Sparrow
    12 × Betsy Hodges > Captain Jack Sparrow > Nekima Levy-Pounds
    12 × Betsy Hodges > Jacob Frey > Ronald Lischeid
    12 × Charlie Gers > Betsy Hodges > Jacob Frey
    12 × Charlie Gers > Ronald Lischeid
    12 × Charlie Gers > Tom Hoch > Betsy Hodges
    12 × David Rosenfeld > Betsy Hodges > Nekima Levy-Pounds
    12 × Jacob Frey > Betsy Hodges > Troy Benjegerdes
    12 × Jacob Frey > Betsy Hodges > Undeclared Write-ins
    12 × Jacob Frey > David Rosenfeld > Betsy Hodges
    12 × Jacob Frey > David Rosenfeld > Tom Hoch
    12 × Jacob Frey > Gregg A. Iverson > Al Flowers
    12 × Jacob Frey > L.A. Nik > Captain Jack Sparrow
    12 × Jacob Frey > L.A. Nik > Charlie Gers
    12 × Nekima Levy-Pounds > Al Flowers > Gregg A. Iverson
    12 × Nekima Levy-Pounds > Betsy Hodges > Charlie Gers
    12 × Raymond Dehn > Jacob Frey > Ian Simpson
    12 × Tom Hoch > Al Flowers > Charlie Gers
    12 × Tom Hoch > Charlie Gers > Raymond Dehn
    12 × Tom Hoch > David Rosenfeld
    12 × Tom Hoch > David Rosenfeld > Captain Jack Sparrow
    12 × Tom Hoch > L.A. Nik > Ronald Lischeid
    11 × Al Flowers > Betsy Hodges > Tom Hoch
    11 × Aswar Rahman > Al Flowers > Tom Hoch
    11 × Aswar Rahman > Nekima Levy-Pounds > Raymond Dehn
    11 × Betsy Hodges > Captain Jack Sparrow > Tom Hoch
    11 × Betsy Hodges > Gregg A. Iverson > Captain Jack Sparrow
    11 × Betsy Hodges > Raymond Dehn > L.A. Nik
    11 × Betsy Hodges > Tom Hoch > Charlie Gers
    11 × Betsy Hodges > Tom Hoch > Ronald Lischeid
    11 × Charlie Gers > L.A. Nik > Tom Hoch
    11 × Gregg A. Iverson > Jacob Frey > Betsy Hodges
    11 × Jacob Frey > Al Flowers > Aswar Rahman
    11 × Jacob Frey > Captain Jack Sparrow > Raymond Dehn
    11 × Jacob Frey > Gregg A. Iverson > Charlie Gers
    11 × L.A. Nik > Charlie Gers > Tom Hoch
    11 × L.A. Nik > Undeclared Write-ins
    11 × Nekima Levy-Pounds > Betsy Hodges > L.A. Nik
    11 × Nekima Levy-Pounds > Betsy Hodges > Undeclared Write-ins
    11 × Nekima Levy-Pounds > Captain Jack Sparrow > David Rosenfeld
    11 × Nekima Levy-Pounds > Captain Jack Sparrow > Jacob Frey
    11 × Nekima Levy-Pounds > David Rosenfeld > Al Flowers
    11 × Nekima Levy-Pounds > David Rosenfeld > Jacob Frey
    11 × Nekima Levy-Pounds > David Rosenfeld > Tom Hoch
    11 × Raymond Dehn > Al Flowers > Captain Jack Sparrow
    11 × Raymond Dehn > Betsy Hodges > Undeclared Write-ins
    11 × Raymond Dehn > Captain Jack Sparrow > Jacob Frey
    11 × Raymond Dehn > David Rosenfeld > David John Wilson
    11 × Raymond Dehn > Nekima Levy-Pounds > Ronald Lischeid
    11 × Raymond Dehn > Undeclared Write-ins
    11 × Tom Hoch > Al Flowers > L.A. Nik
    11 × Tom Hoch > Aswar Rahman > Gregg A. Iverson
    11 × Tom Hoch > Gregg A. Iverson > Al Flowers
    11 × Tom Hoch > L.A. Nik > Betsy Hodges
    11 × Tom Hoch > Raymond Dehn > Ronald Lischeid
    11 × Tom Hoch > Troy Benjegerdes
    10 × Al Flowers > Betsy Hodges > Aswar Rahman
    10 × Al Flowers > Jacob Frey
    10 × Aswar Rahman > Betsy Hodges > Jacob Frey
    10 × Betsy Hodges > David John Wilson
    10 × Betsy Hodges > David Rosenfeld > Nekima Levy-Pounds
    10 × Betsy Hodges > Nekima Levy-Pounds > Ian Simpson
    10 × Betsy Hodges > Nekima Levy-Pounds > L.A. Nik
    10 × Charlie Gers > Captain Jack Sparrow
    10 × Charlie Gers > David John Wilson > L.A. Nik
    10 × Charlie Gers > Raymond Dehn > Tom Hoch
    10 × David Rosenfeld > Nekima Levy-Pounds
    10 × David Rosenfeld > Nekima Levy-Pounds > Jacob Frey
    10 × Gregg A. Iverson > Betsy Hodges
    10 × Gregg A. Iverson > Betsy Hodges > Tom Hoch
    10 × Gregg A. Iverson > Jacob Frey > Tom Hoch
    10 × Jacob Frey > Al Flowers > Gregg A. Iverson
    10 × Jacob Frey > Aswar Rahman > Charlie Gers
    10 × Jacob Frey > Charlie Gers > Nekima Levy-Pounds
    10 × Jacob Frey > Charlie Gers > Raymond Dehn
    10 × Jacob Frey > Nekima Levy-Pounds > Charlie Gers
    10 × Jacob Frey > Nekima Levy-Pounds > Ian Simpson
    10 × L.A. Nik > Tom Hoch > Captain Jack Sparrow
    10 × Nekima Levy-Pounds > Raymond Dehn > Gregg A. Iverson
    10 × Nekima Levy-Pounds > Tom Hoch > L.A. Nik
    10 × Raymond Dehn > Al Flowers > David Rosenfeld
    10 × Raymond Dehn > Aswar Rahman > David Rosenfeld
    10 × Raymond Dehn > David Rosenfeld > Jacob Frey
    10 × Raymond Dehn > Jacob Frey > L.A. Nik
    10 × Raymond Dehn > Nekima Levy-Pounds > Charlie Gers
    10 × Raymond Dehn > Nekima Levy-Pounds > Troy Benjegerdes
    10 × Tom Hoch > Aswar Rahman > L.A. Nik
    10 × Tom Hoch > Captain Jack Sparrow > Aswar Rahman
    10 × Tom Hoch > Charlie Gers > Aswar Rahman
    10 × Tom Hoch > Charlie Gers > Nekima Levy-Pounds
    10 × Tom Hoch > Charlie Gers > Ronald Lischeid
    10 × Tom Hoch > Ian Simpson > Captain Jack Sparrow
    10 × Tom Hoch > L.A. Nik > David John Wilson
    10 × Tom Hoch > L.A. Nik > Nekima Levy-Pounds
    10 × Tom Hoch > Ronald Lischeid > Jacob Frey
    10 × Tom Hoch > Troy Benjegerdes > Raymond Dehn
     9 × Aswar Rahman > Nekima Levy-Pounds
     9 × Aswar Rahman > Nekima Levy-Pounds > Al Flowers
     9 × Betsy Hodges > Aswar Rahman > David Rosenfeld
     9 × Betsy Hodges > Aswar Rahman > Gregg A. Iverson
     9 × Betsy Hodges > Jacob Frey > L.A. Nik
     9 × Betsy Hodges > Nekima Levy-Pounds > Ronald Lischeid
     9 × Betsy Hodges > Nekima Levy-Pounds > Undeclared Write-ins
     9 × Captain Jack Sparrow > Jacob Frey > Betsy Hodges
     9 × Captain Jack Sparrow > Jacob Frey > Tom Hoch
     9 × Charlie Gers > Jacob Frey > Captain Jack Sparrow
     9 × Charlie Gers > Ronald Lischeid > Ian Simpson
     9 × Charlie Gers > Tom Hoch > Ronald Lischeid
     9 × David Rosenfeld > Betsy Hodges > Captain Jack Sparrow
     9 × David Rosenfeld > Captain Jack Sparrow
     9 × David Rosenfeld > Jacob Frey > Nekima Levy-Pounds
     9 × Jacob Frey > Charlie Gers > Betsy Hodges
     9 × L.A. Nik > Tom Hoch > Charlie Gers
     9 × Nekima Levy-Pounds > Al Flowers > L.A. Nik
     9 × Nekima Levy-Pounds > Captain Jack Sparrow > Al Flowers
     9 × Nekima Levy-Pounds > Gregg A. Iverson > Tom Hoch
     9 × Nekima Levy-Pounds > Raymond Dehn > Ronald Lischeid
     9 × Raymond Dehn > Captain Jack Sparrow > David John Wilson
     9 × Raymond Dehn > Captain Jack Sparrow > Tom Hoch
     9 × Raymond Dehn > David John Wilson > Captain Jack Sparrow
     9 × Raymond Dehn > Gregg A. Iverson > Tom Hoch
     9 × Raymond Dehn > Nekima Levy-Pounds > Gregg A. Iverson
     9 × Tom Hoch > Al Flowers > David John Wilson
     9 × Tom Hoch > Al Flowers > Gregg A. Iverson
     9 × Tom Hoch > Aswar Rahman > Charlie Gers
     9 × Tom Hoch > Aswar Rahman > David John Wilson
     9 × Tom Hoch > Captain Jack Sparrow > Nekima Levy-Pounds
     9 × Tom Hoch > Charlie Gers > David John Wilson
     9 × Tom Hoch > David John Wilson > Nekima Levy-Pounds
     9 × Tom Hoch > David Rosenfeld > Jacob Frey
     9 × Tom Hoch > David Rosenfeld > Nekima Levy-Pounds
     9 × Tom Hoch > Gregg A. Iverson > Aswar Rahman
     9 × Tom Hoch > Gregg A. Iverson > Troy Benjegerdes
     9 × Tom Hoch > L.A. Nik > Ian Simpson
     9 × Tom Hoch > Raymond Dehn > Undeclared Write-ins
     9 × Tom Hoch > Ronald Lischeid > Charlie Gers
     9 × Tom Hoch > Ronald Lischeid > L.A. Nik
     8 × Al Flowers > Aswar Rahman > Raymond Dehn
     8 × Al Flowers > Betsy Hodges > Raymond Dehn
     8 × Al Flowers > Jacob Frey > Tom Hoch
     8 × Al Flowers > Raymond Dehn
     8 × Al Flowers > Raymond Dehn > Betsy Hodges
     8 × Aswar Rahman > Betsy Hodges > Tom Hoch
     8 × Betsy Hodges > Captain Jack Sparrow > Charlie Gers
     8 × Betsy Hodges > Captain Jack Sparrow > Jacob Frey
     8 × Betsy Hodges > Charlie Gers > Captain Jack Sparrow
     8 × Betsy Hodges > Charlie Gers > David Rosenfeld
     8 × Betsy Hodges > Jacob Frey > Undeclared Write-ins
     8 × Betsy Hodges > Raymond Dehn > Troy Benjegerdes
     8 × Betsy Hodges > Tom Hoch > Ian Simpson
     8 × Captain Jack Sparrow > Charlie Gers > L.A. Nik
     8 × Captain Jack Sparrow > Nekima Levy-Pounds > Raymond Dehn
     8 × Charlie Gers > Aswar Rahman > Tom Hoch
     8 × Charlie Gers > L.A. Nik > Jacob Frey
     8 × Charlie Gers > Raymond Dehn
     8 × Charlie Gers > Tom Hoch > Captain Jack Sparrow
     8 × David John Wilson > Tom Hoch > Jacob Frey
     8 × Gregg A. Iverson > Jacob Frey > Nekima Levy-Pounds
     8 × Jacob Frey > Aswar Rahman > David John Wilson
     8 × Jacob Frey > Betsy Hodges > Ian Simpson
     8 × Jacob Frey > Captain Jack Sparrow > David Rosenfeld
     8 × Jacob Frey > Captain Jack Sparrow > Nekima Levy-Pounds
     8 × Jacob Frey > Charlie Gers > David John Wilson
     8 × Jacob Frey > David Rosenfeld > Raymond Dehn
     8 × Jacob Frey > Gregg A. Iverson > Aswar Rahman
     8 × L.A. Nik > Charlie Gers > David John Wilson
     8 × Nekima Levy-Pounds > Al Flowers > Troy Benjegerdes
     8 × Nekima Levy-Pounds > Captain Jack Sparrow > Raymond Dehn
     8 × Nekima Levy-Pounds > David Rosenfeld > David John Wilson
     8 × Nekima Levy-Pounds > David Rosenfeld > Ronald Lischeid
     8 × Nekima Levy-Pounds > L.A. Nik > Betsy Hodges
     8 × Nekima Levy-Pounds > Tom Hoch > Undeclared Write-ins
     8 × Raymond Dehn > Charlie Gers
     8 × Raymond Dehn > David Rosenfeld > Ronald Lischeid
     8 × Raymond Dehn > Jacob Frey > Charlie Gers
     8 × Raymond Dehn > Jacob Frey > Undeclared Write-ins
     8 × Raymond Dehn > Tom Hoch > Charlie Gers
     8 × Raymond Dehn > Tom Hoch > Ian Simpson
     8 × Raymond Dehn > Tom Hoch > Ronald Lischeid
     8 × Ronald Lischeid > L.A. Nik > Charlie Gers
     8 × Tom Hoch > Betsy Hodges > Ian Simpson
     8 × Tom Hoch > Gregg A. Iverson > Nekima Levy-Pounds
     8 × Tom Hoch > Gregg A. Iverson > Ronald Lischeid
     8 × Tom Hoch > L.A. Nik > Raymond Dehn
     8 × Tom Hoch > Raymond Dehn > Ian Simpson
     7 × Al Flowers > Aswar Rahman
     7 × Al Flowers > Aswar Rahman > Tom Hoch
     7 × Al Flowers > Jacob Frey > Betsy Hodges
     7 × Aswar Rahman > Al Flowers
     7 × Aswar Rahman > Tom Hoch > Raymond Dehn
     7 × Betsy Hodges > Charlie Gers > Gregg A. Iverson
     7 × Betsy Hodges > Charlie Gers > Ian Simpson
     7 × Betsy Hodges > Charlie Gers > L.A. Nik
     7 × Betsy Hodges > David Rosenfeld > Aswar Rahman
     7 × Betsy Hodges > L.A. Nik
     7 × Betsy Hodges > Nekima Levy-Pounds > Charlie Gers
     7 × Betsy Hodges > Ronald Lischeid
     7 × Captain Jack Sparrow > Raymond Dehn > Tom Hoch
     7 × Charlie Gers > Captain Jack Sparrow > David John Wilson
     7 × Charlie Gers > Captain Jack Sparrow > Ian Simpson
     7 × Charlie Gers > David John Wilson > Captain Jack Sparrow
     7 × Charlie Gers > Ian Simpson > L.A. Nik
     7 × Charlie Gers > Tom Hoch > David John Wilson
     7 × David Rosenfeld > Nekima Levy-Pounds > Aswar Rahman
     7 × David Rosenfeld > Tom Hoch > Betsy Hodges
     7 × Gregg A. Iverson > Betsy Hodges > Aswar Rahman
     7 × Gregg A. Iverson > Jacob Frey
     7 × Gregg A. Iverson > Tom Hoch > Betsy Hodges
     7 × Jacob Frey > Aswar Rahman > Gregg A. Iverson
     7 × Jacob Frey > Aswar Rahman > L.A. Nik
     7 × Jacob Frey > Captain Jack Sparrow > Gregg A. Iverson
     7 × Jacob Frey > Charlie Gers > Aswar Rahman
     7 × Jacob Frey > Charlie Gers > Gregg A. Iverson
     7 × Jacob Frey > David John Wilson > Tom Hoch
     7 × Jacob Frey > Nekima Levy-Pounds > Ronald Lischeid
     7 × Jacob Frey > Raymond Dehn > Troy Benjegerdes
     7 × Jacob Frey > Ronald Lischeid > Tom Hoch
     7 × Jacob Frey > Troy Benjegerdes
     7 × L.A. Nik > Charlie Gers > Captain Jack Sparrow
     7 × L.A. Nik > Ronald Lischeid > Ian Simpson
     7 × Nekima Levy-Pounds > Al Flowers > Charlie Gers
     7 × Nekima Levy-Pounds > Al Flowers > Undeclared Write-ins
     7 × Nekima Levy-Pounds > Jacob Frey > Ian Simpson
     7 × Nekima Levy-Pounds > Jacob Frey > Ronald Lischeid
     7 × Nekima Levy-Pounds > L.A. Nik > Captain Jack Sparrow
     7 × Raymond Dehn > Betsy Hodges > Ronald Lischeid
     7 × Raymond Dehn > David Rosenfeld > Al Flowers
     7 × Raymond Dehn > Jacob Frey > Troy Benjegerdes
     7 × Raymond Dehn > L.A. Nik
     7 × Ronald Lischeid > Charlie Gers > L.A. Nik
     7 × Tom Hoch > Aswar Rahman > Ronald Lischeid
     7 × Tom Hoch > Captain Jack Sparrow > Gregg A. Iverson
     7 × Tom Hoch > Charlie Gers > Al Flowers
     7 × Tom Hoch > David John Wilson > Betsy Hodges
     7 × Tom Hoch > David Rosenfeld > Al Flowers
     7 × Tom Hoch > L.A. Nik > Gregg A. Iverson
     7 × Tom Hoch > Nekima Levy-Pounds > Ronald Lischeid
     7 × Tom Hoch > Ronald Lischeid > Captain Jack Sparrow
     7 × Tom Hoch > Ronald Lischeid > David John Wilson
     7 × Troy Benjegerdes > Jacob Frey > Tom Hoch
     6 × Al Flowers > Captain Jack Sparrow
     6 × Al Flowers > Jacob Frey > Nekima Levy-Pounds
     6 × Al Flowers > Jacob Frey > Raymond Dehn
     6 × Al Flowers > Nekima Levy-Pounds > Aswar Rahman
     6 × Al Flowers > Nekima Levy-Pounds > Gregg A. Iverson
     6 × Al Flowers > Tom Hoch > Aswar Rahman
     6 × Aswar Rahman > Al Flowers > Betsy Hodges
     6 × Aswar Rahman > Tom Hoch > Al Flowers
     6 × Aswar Rahman > Tom Hoch > Gregg A. Iverson
     6 × Betsy Hodges > Al Flowers > David John Wilson
     6 × Betsy Hodges > Al Flowers > David Rosenfeld
     6 × Betsy Hodges > Captain Jack Sparrow > L.A. Nik
     6 × Betsy Hodges > Charlie Gers > Jacob Frey
     6 × Betsy Hodges > Charlie Gers > Raymond Dehn
     6 × Betsy Hodges > David John Wilson > Captain Jack Sparrow
     6 × Betsy Hodges > Gregg A. Iverson > David Rosenfeld
     6 × Betsy Hodges > Ian Simpson > Captain Jack Sparrow
     6 × Betsy Hodges > Jacob Frey > Ian Simpson
     6 × Betsy Hodges > Jacob Frey > Troy Benjegerdes
     6 × Betsy Hodges > L.A. Nik > Tom Hoch
     6 × Betsy Hodges > Raymond Dehn > Ian Simpson
     6 × Captain Jack Sparrow > Betsy Hodges > Al Flowers
     6 × Captain Jack Sparrow > Betsy Hodges > Raymond Dehn
     6 × Captain Jack Sparrow > Raymond Dehn > Betsy Hodges
     6 × Charlie Gers > Ian Simpson
     6 × Charlie Gers > Ian Simpson > Jacob Frey
     6 × Charlie Gers > Ian Simpson > Ronald Lischeid
     6 × Charlie Gers > Jacob Frey > Nekima Levy-Pounds
     6 × Charlie Gers > L.A. Nik > Betsy Hodges
     6 × Charlie Gers > Ronald Lischeid > David John Wilson
     6 × Charlie Gers > Ronald Lischeid > Tom Hoch
     6 × Charlie Gers > Tom Hoch > Aswar Rahman
     6 × David Rosenfeld > Betsy Hodges > Tom Hoch
     6 × David Rosenfeld > Nekima Levy-Pounds > Tom Hoch
     6 × David Rosenfeld > Raymond Dehn > Captain Jack Sparrow
     6 × David Rosenfeld > Raymond Dehn > Tom Hoch
     6 × Gregg A. Iverson > Tom Hoch > Jacob Frey
     6 × Jacob Frey > Betsy Hodges > Ronald Lischeid
     6 × Jacob Frey > Captain Jack Sparrow > Al Flowers
     6 × Jacob Frey > David John Wilson > Raymond Dehn
     6 × Jacob Frey > David Rosenfeld > Gregg A. Iverson
     6 × Jacob Frey > David Rosenfeld > Nekima Levy-Pounds
     6 × Jacob Frey > L.A. Nik > Ronald Lischeid
     6 × Jacob Frey > Raymond Dehn > Ian Simpson
     6 × Jacob Frey > Ronald Lischeid
     6 × L.A. Nik > Captain Jack Sparrow > Ian Simpson
     6 × Nekima Levy-Pounds > Al Flowers > Ronald Lischeid
     6 × Nekima Levy-Pounds > Aswar Rahman > Gregg A. Iverson
     6 × Nekima Levy-Pounds > Betsy Hodges > Ronald Lischeid
     6 × Nekima Levy-Pounds > Betsy Hodges > Troy Benjegerdes
     6 × Nekima Levy-Pounds > Captain Jack Sparrow > L.A. Nik
     6 × Nekima Levy-Pounds > Captain Jack Sparrow > Undeclared Write-ins
     6 × Nekima Levy-Pounds > Charlie Gers > Captain Jack Sparrow
     6 × Nekima Levy-Pounds > Charlie Gers > Raymond Dehn
     6 × Nekima Levy-Pounds > Raymond Dehn > Charlie Gers
     6 × Nekima Levy-Pounds > Ronald Lischeid
     6 × Nekima Levy-Pounds > Ronald Lischeid > Betsy Hodges
     6 × Nekima Levy-Pounds > Tom Hoch > Charlie Gers
     6 × Raymond Dehn > Aswar Rahman > L.A. Nik
     6 × Raymond Dehn > Captain Jack Sparrow > Al Flowers
     6 × Raymond Dehn > Captain Jack Sparrow > Undeclared Write-ins
     6 × Raymond Dehn > David John Wilson > Tom Hoch
     6 × Raymond Dehn > Gregg A. Iverson
     6 × Raymond Dehn > Gregg A. Iverson > Jacob Frey
     6 × Raymond Dehn > Gregg A. Iverson > Nekima Levy-Pounds
     6 × Raymond Dehn > L.A. Nik > Tom Hoch
     6 × Raymond Dehn > Tom Hoch > Troy Benjegerdes
     6 × Ronald Lischeid > Charlie Gers
     6 × Ronald Lischeid > L.A. Nik
     6 × Ronald Lischeid > Raymond Dehn > Jacob Frey
     6 × Ronald Lischeid > Tom Hoch > Betsy Hodges
     6 × Tom Hoch > Captain Jack Sparrow > Ronald Lischeid
     6 × Tom Hoch > Captain Jack Sparrow > Troy Benjegerdes
     6 × Tom Hoch > Captain Jack Sparrow > Undeclared Write-ins
     6 × Tom Hoch > Charlie Gers > Troy Benjegerdes
     6 × Tom Hoch > David John Wilson > Aswar Rahman
     6 × Tom Hoch > David John Wilson > Ronald Lischeid
     6 × Tom Hoch > David Rosenfeld > David John Wilson
     6 × Tom Hoch > David Rosenfeld > Raymond Dehn
     6 × Tom Hoch > Gregg A. Iverson > Charlie Gers
     6 × Tom Hoch > Ian Simpson
     6 × Tom Hoch > Troy Benjegerdes > Captain Jack Sparrow
     6 × Troy Benjegerdes > Jacob Frey > Betsy Hodges
     5 × Al Flowers > Betsy Hodges > Gregg A. Iverson
     5 × Al Flowers > Nekima Levy-Pounds > Captain Jack Sparrow
     5 × Al Flowers > Tom Hoch > Captain Jack Sparrow
     5 × Aswar Rahman > Nekima Levy-Pounds > Captain Jack Sparrow
     5 × Aswar Rahman > Nekima Levy-Pounds > David Rosenfeld
     5 × Aswar Rahman > Tom Hoch > Charlie Gers
     5 × Betsy Hodges > Al Flowers > L.A. Nik
     5 × Betsy Hodges > Aswar Rahman > Charlie Gers
     5 × Betsy Hodges > Aswar Rahman > L.A. Nik
     5 × Betsy Hodges > Aswar Rahman > Ronald Lischeid
     5 × Betsy Hodges > Captain Jack Sparrow > Aswar Rahman
     5 × Betsy Hodges > Captain Jack Sparrow > Ian Simpson
     5 × Betsy Hodges > Charlie Gers > Tom Hoch
     5 × Betsy Hodges > David John Wilson > Al Flowers
     5 × Betsy Hodges > David Rosenfeld > David John Wilson
     5 × Betsy Hodges > David Rosenfeld > Raymond Dehn
     5 × Betsy Hodges > Gregg A. Iverson > Charlie Gers
     5 × Betsy Hodges > Ian Simpson
     5 × Betsy Hodges > L.A. Nik > Charlie Gers
     5 × Betsy Hodges > L.A. Nik > Nekima Levy-Pounds
     5 × Betsy Hodges > Raymond Dehn > Charlie Gers
     5 × Betsy Hodges > Raymond Dehn > Ronald Lischeid
     5 × Betsy Hodges > Raymond Dehn > Undeclared Write-ins
     5 × Betsy Hodges > Ronald Lischeid > David John Wilson
     5 × Betsy Hodges > Troy Benjegerdes > Tom Hoch
     5 × Captain Jack Sparrow > Betsy Hodges
     5 × Captain Jack Sparrow > David John Wilson > Charlie Gers
     5 × Captain Jack Sparrow > L.A. Nik > David John Wilson
     5 × Captain Jack Sparrow > L.A. Nik > Jacob Frey
     5 × Captain Jack Sparrow > Raymond Dehn > Jacob Frey
     5 × Captain Jack Sparrow > Ronald Lischeid > L.A. Nik
     5 × Captain Jack Sparrow > Tom Hoch
     5 × Charlie Gers > Aswar Rahman > Jacob Frey
     5 × Charlie Gers > Betsy Hodges > Gregg A. Iverson
     5 × Charlie Gers > L.A. Nik > Troy Benjegerdes
     5 × David John Wilson > Jacob Frey
     5 × David John Wilson > Jacob Frey > Betsy Hodges
     5 × David Rosenfeld > Aswar Rahman > Nekima Levy-Pounds
     5 × David Rosenfeld > Betsy Hodges
     5 × David Rosenfeld > Jacob Frey
     5 × David Rosenfeld > Jacob Frey > Betsy Hodges
     5 × David Rosenfeld > Nekima Levy-Pounds > Captain Jack Sparrow
     5 × Gregg A. Iverson > Betsy Hodges > Captain Jack Sparrow
     5 × Gregg A. Iverson > Tom Hoch > Raymond Dehn
     5 × Ian Simpson > Jacob Frey > Tom Hoch
     5 × Jacob Frey > Al Flowers > David Rosenfeld
     5 × Jacob Frey > Aswar Rahman > David Rosenfeld
     5 × Jacob Frey > Aswar Rahman > Ronald Lischeid
     5 × Jacob Frey > Captain Jack Sparrow > Charlie Gers
     5 × Jacob Frey > Captain Jack Sparrow > Ian Simpson
     5 × Jacob Frey > Captain Jack Sparrow > Ronald Lischeid
     5 × Jacob Frey > Charlie Gers > Ronald Lischeid
     5 × Jacob Frey > David John Wilson > Al Flowers
     5 × Jacob Frey > David Rosenfeld > Troy Benjegerdes
     5 × Jacob Frey > Gregg A. Iverson > David Rosenfeld
     5 × Jacob Frey > Gregg A. Iverson > L.A. Nik
     5 × Jacob Frey > Gregg A. Iverson > Ronald Lischeid
     5 × Jacob Frey > L.A. Nik > Raymond Dehn
     5 × Jacob Frey > Raymond Dehn > Ronald Lischeid
     5 × Jacob Frey > Raymond Dehn > Undeclared Write-ins
     5 × Jacob Frey > Ronald Lischeid > Betsy Hodges
     5 × Jacob Frey > Troy Benjegerdes > Betsy Hodges
     5 × Jacob Frey > Troy Benjegerdes > Captain Jack Sparrow
     5 × Jacob Frey > Troy Benjegerdes > Tom Hoch
     5 × L.A. Nik > Al Flowers
     5 × L.A. Nik > Captain Jack Sparrow
     5 × L.A. Nik > Captain Jack Sparrow > Tom Hoch
     5 × L.A. Nik > Ian Simpson > Charlie Gers
     5 × L.A. Nik > Ian Simpson > Ronald Lischeid
     5 × L.A. Nik > Jacob Frey > Captain Jack Sparrow
     5 × L.A. Nik > Jacob Frey > Nekima Levy-Pounds
     5 × L.A. Nik > Jacob Frey > Raymond Dehn
     5 × L.A. Nik > Tom Hoch > Ronald Lischeid
     5 × Nekima Levy-Pounds > Al Flowers > David John Wilson
     5 × Nekima Levy-Pounds > Aswar Rahman > L.A. Nik
     5 × Nekima Levy-Pounds > Betsy Hodges > Ian Simpson
     5 × Nekima Levy-Pounds > Captain Jack Sparrow > Aswar Rahman
     5 × Nekima Levy-Pounds > Captain Jack Sparrow > Tom Hoch
     5 × Nekima Levy-Pounds > Charlie Gers > Jacob Frey
     5 × Nekima Levy-Pounds > David John Wilson > Tom Hoch
     5 × Nekima Levy-Pounds > Gregg A. Iverson > Charlie Gers
     5 × Nekima Levy-Pounds > Jacob Frey > L.A. Nik
     5 × Raymond Dehn > Aswar Rahman > David John Wilson
     5 × Raymond Dehn > Aswar Rahman > Gregg A. Iverson
     5 × Raymond Dehn > Betsy Hodges > Ian Simpson
     5 × Raymond Dehn > Betsy Hodges > L.A. Nik
     5 × Raymond Dehn > Betsy Hodges > Troy Benjegerdes
     5 × Raymond Dehn > Captain Jack Sparrow > L.A. Nik
     5 × Raymond Dehn > Charlie Gers > Betsy Hodges
     5 × Raymond Dehn > David John Wilson
     5 × Raymond Dehn > David Rosenfeld > Aswar Rahman
     5 × Raymond Dehn > L.A. Nik > Captain Jack Sparrow
     5 × Raymond Dehn > L.A. Nik > Ian Simpson
     5 × Raymond Dehn > Tom Hoch > Undeclared Write-ins
     5 × Ronald Lischeid > David John Wilson > Captain Jack Sparrow
     5 × Ronald Lischeid > Jacob Frey > Tom Hoch
     5 × Tom Hoch > Al Flowers > Ronald Lischeid
     5 × Tom Hoch > Betsy Hodges > Troy Benjegerdes
     5 × Tom Hoch > Charlie Gers > David Rosenfeld
     5 × Tom Hoch > Charlie Gers > Undeclared Write-ins
     5 × Tom Hoch > Ian Simpson > Jacob Frey
     5 × Tom Hoch > Nekima Levy-Pounds > Ian Simpson
     5 × Tom Hoch > Ronald Lischeid > Betsy Hodges
     5 × Tom Hoch > Ronald Lischeid > Gregg A. Iverson
     5 × Troy Benjegerdes > Jacob Frey > Nekima Levy-Pounds
     5 × Undeclared Write-ins > Jacob Frey > Tom Hoch
     4 × Al Flowers > Aswar Rahman > Betsy Hodges
     4 × Al Flowers > Aswar Rahman > Jacob Frey
     4 × Al Flowers > Gregg A. Iverson
     4 × Al Flowers > Jacob Frey > Captain Jack Sparrow
     4 × Al Flowers > Jacob Frey > Gregg A. Iverson
     4 × Aswar Rahman > Betsy Hodges > Al Flowers
     4 × Aswar Rahman > Charlie Gers
     4 × Aswar Rahman > David John Wilson
     4 × Aswar Rahman > Nekima Levy-Pounds > Tom Hoch
     4 × Aswar Rahman > Raymond Dehn > Al Flowers
     4 × Aswar Rahman > Raymond Dehn > Betsy Hodges
     4 × Aswar Rahman > Raymond Dehn > David Rosenfeld
     4 × Betsy Hodges > Al Flowers > Troy Benjegerdes
     4 × Betsy Hodges > Aswar Rahman > David John Wilson
     4 × Betsy Hodges > Aswar Rahman > Troy Benjegerdes
     4 × Betsy Hodges > Captain Jack Sparrow > Al Flowers
     4 × Betsy Hodges > Captain Jack Sparrow > David Rosenfeld
     4 × Betsy Hodges > Captain Jack Sparrow > Raymond Dehn
     4 × Betsy Hodges > David John Wilson > Nekima Levy-Pounds
     4 × Betsy Hodges > David John Wilson > Ronald Lischeid
     4 × Betsy Hodges > David Rosenfeld > Al Flowers
     4 × Betsy Hodges > David Rosenfeld > Charlie Gers
     4 × Betsy Hodges > Gregg A. Iverson > David John Wilson
     4 × Betsy Hodges > Gregg A. Iverson > Troy Benjegerdes
     4 × Betsy Hodges > L.A. Nik > Al Flowers
     4 × Betsy Hodges > L.A. Nik > Captain Jack Sparrow
     4 × Betsy Hodges > L.A. Nik > Jacob Frey
     4 × Betsy Hodges > Nekima Levy-Pounds > Troy Benjegerdes
     4 × Betsy Hodges > Ronald Lischeid > Captain Jack Sparrow
     4 × Betsy Hodges > Ronald Lischeid > Charlie Gers
     4 × Betsy Hodges > Ronald Lischeid > Ian Simpson
     4 × Betsy Hodges > Ronald Lischeid > Tom Hoch
     4 × Betsy Hodges > Tom Hoch > Undeclared Write-ins
     4 × Betsy Hodges > Troy Benjegerdes
     4 × Captain Jack Sparrow > Al Flowers
     4 × Captain Jack Sparrow > Betsy Hodges > Tom Hoch
     4 × Captain Jack Sparrow > David Rosenfeld > L.A. Nik
     4 × Captain Jack Sparrow > David Rosenfeld > Tom Hoch
     4 × Captain Jack Sparrow > Jacob Frey > Nekima Levy-Pounds
     4 × Captain Jack Sparrow > L.A. Nik > Ronald Lischeid
     4 × Captain Jack Sparrow > Nekima Levy-Pounds > Betsy Hodges
     4 × Captain Jack Sparrow > Nekima Levy-Pounds > Tom Hoch
     4 × Captain Jack Sparrow > Raymond Dehn > Nekima Levy-Pounds
     4 × Charlie Gers > Betsy Hodges > Tom Hoch
     4 × Charlie Gers > Captain Jack Sparrow > Jacob Frey
     4 × Charlie Gers > Captain Jack Sparrow > Tom Hoch
     4 × Charlie Gers > David John Wilson > Jacob Frey
     4 × Charlie Gers > Ian Simpson > Captain Jack Sparrow
     4 × Charlie Gers > Jacob Frey > Gregg A. Iverson
     4 × Charlie Gers > Jacob Frey > L.A. Nik
     4 × Charlie Gers > Jacob Frey > Raymond Dehn
     4 × Charlie Gers > Raymond Dehn > Betsy Hodges
     4 × Charlie Gers > Tom Hoch > Ian Simpson
     4 × Charlie Gers > Tom Hoch > Nekima Levy-Pounds
     4 × Charlie Gers > Troy Benjegerdes
     4 × David John Wilson > Captain Jack Sparrow > Ian Simpson
     4 × David John Wilson > Jacob Frey > Tom Hoch
     4 × David John Wilson > Tom Hoch > Betsy Hodges
     4 × David Rosenfeld > Aswar Rahman > Betsy Hodges
     4 × David Rosenfeld > Betsy Hodges > David John Wilson
     4 × David Rosenfeld > Betsy Hodges > Jacob Frey
     4 × David Rosenfeld > Captain Jack Sparrow > David John Wilson
     4 × David Rosenfeld > Captain Jack Sparrow > Raymond Dehn
     4 × David Rosenfeld > David John Wilson > Captain Jack Sparrow
     4 × David Rosenfeld > Raymond Dehn
     4 × David Rosenfeld > Tom Hoch > Nekima Levy-Pounds
     4 × David Rosenfeld > Troy Benjegerdes > Raymond Dehn
     4 × Gregg A. Iverson > Betsy Hodges > Al Flowers
     4 × Gregg A. Iverson > Betsy Hodges > Nekima Levy-Pounds
     4 × Gregg A. Iverson > Nekima Levy-Pounds
     4 × Gregg A. Iverson > Tom Hoch > Al Flowers
     4 × Gregg A. Iverson > Tom Hoch > Nekima Levy-Pounds
     4 × Ian Simpson > Troy Benjegerdes > Captain Jack Sparrow
     4 × Jacob Frey > Al Flowers > David John Wilson
     4 × Jacob Frey > Al Flowers > L.A. Nik
     4 × Jacob Frey > Al Flowers > Ronald Lischeid
     4 × Jacob Frey > Al Flowers > Troy Benjegerdes
     4 × Jacob Frey > Aswar Rahman > Undeclared Write-ins
     4 × Jacob Frey > Captain Jack Sparrow > Aswar Rahman
     4 × Jacob Frey > Charlie Gers > David Rosenfeld
     4 × Jacob Frey > David Rosenfeld > David John Wilson
     4 × Jacob Frey > Ian Simpson
     4 × Jacob Frey > Ian Simpson > Captain Jack Sparrow
     4 × Jacob Frey > L.A. Nik > Nekima Levy-Pounds
     4 × Jacob Frey > Nekima Levy-Pounds > Troy Benjegerdes
     4 × Jacob Frey > Nekima Levy-Pounds > Undeclared Write-ins
     4 × Jacob Frey > Ronald Lischeid > Charlie Gers
     4 × Jacob Frey > Ronald Lischeid > Ian Simpson
     4 × Jacob Frey > Ronald Lischeid > Nekima Levy-Pounds
     4 × Jacob Frey > Troy Benjegerdes > Nekima Levy-Pounds
     4 × Jacob Frey > Troy Benjegerdes > Raymond Dehn
     4 × L.A. Nik > Captain Jack Sparrow > David John Wilson
     4 × L.A. Nik > Charlie Gers > Jacob Frey
     4 × L.A. Nik > Gregg A. Iverson
     4 × L.A. Nik > Jacob Frey
     4 × L.A. Nik > Jacob Frey > Ian Simpson
     4 × L.A. Nik > Ronald Lischeid > Tom Hoch
     4 × Nekima Levy-Pounds > Al Flowers > Ian Simpson
     4 × Nekima Levy-Pounds > Aswar Rahman > Charlie Gers
     4 × Nekima Levy-Pounds > Aswar Rahman > David John Wilson
     4 × Nekima Levy-Pounds > Aswar Rahman > Ian Simpson
     4 × Nekima Levy-Pounds > Aswar Rahman > Ronald Lischeid
     4 × Nekima Levy-Pounds > Captain Jack Sparrow > Charlie Gers
     4 × Nekima Levy-Pounds > Captain Jack Sparrow > Ian Simpson
     4 × Nekima Levy-Pounds > Charlie Gers
     4 × Nekima Levy-Pounds > Charlie Gers > Betsy Hodges
     4 × Nekima Levy-Pounds > David John Wilson > Betsy Hodges
     4 × Nekima Levy-Pounds > David John Wilson > Jacob Frey
     4 × Nekima Levy-Pounds > David Rosenfeld > Undeclared Write-ins
     4 × Nekima Levy-Pounds > Gregg A. Iverson > Raymond Dehn
     4 × Nekima Levy-Pounds > L.A. Nik
     4 × Nekima Levy-Pounds > L.A. Nik > Charlie Gers
     4 × Nekima Levy-Pounds > L.A. Nik > Jacob Frey
     4 × Raymond Dehn > Al Flowers > David John Wilson
     4 × Raymond Dehn > Aswar Rahman > Ronald Lischeid
     4 × Raymond Dehn > Captain Jack Sparrow > Ian Simpson
     4 × Raymond Dehn > Charlie Gers > Captain Jack Sparrow
     4 × Raymond Dehn > Charlie Gers > L.A. Nik
     4 × Raymond Dehn > Charlie Gers > Nekima Levy-Pounds
     4 × Raymond Dehn > David John Wilson > Betsy Hodges
     4 × Raymond Dehn > David John Wilson > Nekima Levy-Pounds
     4 × Raymond Dehn > David Rosenfeld > Troy Benjegerdes
     4 × Raymond Dehn > Gregg A. Iverson > Betsy Hodges
     4 × Raymond Dehn > L.A. Nik > Betsy Hodges
     4 × Raymond Dehn > Ronald Lischeid
     4 × Ronald Lischeid > Betsy Hodges
     4 × Ronald Lischeid > Jacob Frey
     4 × Ronald Lischeid > L.A. Nik > David Rosenfeld
     4 × Ronald Lischeid > L.A. Nik > Ian Simpson
     4 × Ronald Lischeid > Tom Hoch
     4 × Ronald Lischeid > Tom Hoch > Raymond Dehn
     4 × Tom Hoch > Al Flowers > Troy Benjegerdes
     4 × Tom Hoch > Aswar Rahman > Troy Benjegerdes
     4 × Tom Hoch > Betsy Hodges > Undeclared Write-ins
     4 × Tom Hoch > Charlie Gers > Gregg A. Iverson
     4 × Tom Hoch > Gregg A. Iverson > L.A. Nik
     4 × Tom Hoch > Ian Simpson > Betsy Hodges
     4 × Tom Hoch > L.A. Nik > Aswar Rahman
     4 × Tom Hoch > Nekima Levy-Pounds > Troy Benjegerdes
     4 × Tom Hoch > Ronald Lischeid > Al Flowers
     4 × Tom Hoch > Ronald Lischeid > Aswar Rahman
     4 × Tom Hoch > Ronald Lischeid > Ian Simpson
     4 × Tom Hoch > Ronald Lischeid > Raymond Dehn
     4 × Tom Hoch > Troy Benjegerdes > Aswar Rahman
     4 × Tom Hoch > Undeclared Write-ins > Jacob Frey
     4 × Troy Benjegerdes > Nekima Levy-Pounds > Al Flowers
     4 × Troy Benjegerdes > Raymond Dehn > Nekima Levy-Pounds
     4 × Undeclared Write-ins > L.A. Nik
     3 × Al Flowers > Betsy Hodges > Captain Jack Sparrow
     3 × Al Flowers > Betsy Hodges > Troy Benjegerdes
     3 × Al Flowers > Captain Jack Sparrow > Raymond Dehn
     3 × Al Flowers > Charlie Gers > L.A. Nik
     3 × Al Flowers > David John Wilson > Nekima Levy-Pounds
     3 × Al Flowers > David Rosenfeld > Tom Hoch
     3 × Al Flowers > Jacob Frey > Aswar Rahman
     3 × Al Flowers > L.A. Nik
     3 × Al Flowers > Raymond Dehn > Aswar Rahman
     3 × Al Flowers > Raymond Dehn > Ronald Lischeid
     3 × Al Flowers > Tom Hoch > Troy Benjegerdes
     3 × Aswar Rahman > Al Flowers > Captain Jack Sparrow
     3 × Aswar Rahman > Al Flowers > Jacob Frey
     3 × Aswar Rahman > Al Flowers > Nekima Levy-Pounds
     3 × Aswar Rahman > Al Flowers > Ronald Lischeid
     3 × Aswar Rahman > Betsy Hodges > Captain Jack Sparrow
     3 × Aswar Rahman > Betsy Hodges > David John Wilson
     3 × Aswar Rahman > Betsy Hodges > Troy Benjegerdes
     3 × Aswar Rahman > Captain Jack Sparrow
     3 × Aswar Rahman > Captain Jack Sparrow > Tom Hoch
     3 × Aswar Rahman > Jacob Frey > Al Flowers
     3 × Aswar Rahman > Jacob Frey > Charlie Gers
     3 × Aswar Rahman > Jacob Frey > Gregg A. Iverson
     3 × Aswar Rahman > Nekima Levy-Pounds > Gregg A. Iverson
     3 × Aswar Rahman > Nekima Levy-Pounds > L.A. Nik
     3 × Aswar Rahman > Raymond Dehn > Captain Jack Sparrow
     3 × Aswar Rahman > Ronald Lischeid > Tom Hoch
     3 × Aswar Rahman > Tom Hoch > L.A. Nik
     3 × Aswar Rahman > Tom Hoch > Ronald Lischeid
     3 × Aswar Rahman > Troy Benjegerdes
     3 × Betsy Hodges > Charlie Gers > Al Flowers
     3 × Betsy Hodges > Charlie Gers > David John Wilson
     3 × Betsy Hodges > David John Wilson > Ian Simpson
     3 × Betsy Hodges > David John Wilson > Jacob Frey
     3 × Betsy Hodges > David John Wilson > Tom Hoch
     3 × Betsy Hodges > David Rosenfeld > Troy Benjegerdes
     3 × Betsy Hodges > Gregg A. Iverson > Ronald Lischeid
     3 × Betsy Hodges > Ian Simpson > David John Wilson
     3 × Betsy Hodges > Ian Simpson > Nekima Levy-Pounds
     3 × Betsy Hodges > L.A. Nik > David John Wilson
     3 × Betsy Hodges > L.A. Nik > Ronald Lischeid
     3 × Betsy Hodges > Ronald Lischeid > L.A. Nik
     3 × Betsy Hodges > Troy Benjegerdes > Captain Jack Sparrow
     3 × Captain Jack Sparrow > Al Flowers > Betsy Hodges
     3 × Captain Jack Sparrow > Al Flowers > Tom Hoch
     3 × Captain Jack Sparrow > Aswar Rahman > Tom Hoch
     3 × Captain Jack Sparrow > Betsy Hodges > Nekima Levy-Pounds
     3 × Captain Jack Sparrow > Charlie Gers > Jacob Frey
     3 × Captain Jack Sparrow > David John Wilson
     3 × Captain Jack Sparrow > David John Wilson > Betsy Hodges
     3 × Captain Jack Sparrow > David John Wilson > David Rosenfeld
     3 × Captain Jack Sparrow > David John Wilson > Ian Simpson
     3 × Captain Jack Sparrow > David John Wilson > Jacob Frey
     3 × Captain Jack Sparrow > David John Wilson > L.A. Nik
     3 × Captain Jack Sparrow > David Rosenfeld > Betsy Hodges
     3 × Captain Jack Sparrow > David Rosenfeld > Ian Simpson
     3 × Captain Jack Sparrow > David Rosenfeld > Jacob Frey
     3 × Captain Jack Sparrow > Ian Simpson > Charlie Gers
     3 × Captain Jack Sparrow > Ian Simpson > David John Wilson
     3 × Captain Jack Sparrow > Ian Simpson > David Rosenfeld
     3 × Captain Jack Sparrow > Ian Simpson > L.A. Nik
     3 × Captain Jack Sparrow > Jacob Frey
     3 × Captain Jack Sparrow > Jacob Frey > Aswar Rahman
     3 × Captain Jack Sparrow > Jacob Frey > L.A. Nik
     3 × Captain Jack Sparrow > L.A. Nik
     3 × Captain Jack Sparrow > L.A. Nik > Ian Simpson
     3 × Captain Jack Sparrow > Nekima Levy-Pounds > Aswar Rahman
     3 × Captain Jack Sparrow > Tom Hoch > Al Flowers
     3 × Captain Jack Sparrow > Tom Hoch > Betsy Hodges
     3 × Captain Jack Sparrow > Tom Hoch > Raymond Dehn
     3 × Charlie Gers > Betsy Hodges > Nekima Levy-Pounds
     3 × Charlie Gers > Captain Jack Sparrow > Ronald Lischeid
     3 × Charlie Gers > Captain Jack Sparrow > Undeclared Write-ins
     3 × Charlie Gers > David John Wilson > Ian Simpson
     3 × Charlie Gers > David John Wilson > Ronald Lischeid
     3 × Charlie Gers > David Rosenfeld > Ronald Lischeid
     3 × Charlie Gers > Gregg A. Iverson
     3 × Charlie Gers > Gregg A. Iverson > Ronald Lischeid
     3 × Charlie Gers > Ian Simpson > Tom Hoch
     3 × Charlie Gers > Ian Simpson > Undeclared Write-ins
     3 × Charlie Gers > L.A. Nik > Aswar Rahman
     3 × Charlie Gers > L.A. Nik > Nekima Levy-Pounds
     3 × Charlie Gers > Nekima Levy-Pounds > Jacob Frey
     3 × Charlie Gers > Raymond Dehn > Jacob Frey
     3 × Charlie Gers > Ronald Lischeid > Captain Jack Sparrow
     3 × Charlie Gers > Ronald Lischeid > Troy Benjegerdes
     3 × Charlie Gers > Tom Hoch > Al Flowers
     3 × Charlie Gers > Tom Hoch > Raymond Dehn
     3 × Charlie Gers > Tom Hoch > Troy Benjegerdes
     3 × Charlie Gers > Tom Hoch > Undeclared Write-ins
     3 × Charlie Gers > Troy Benjegerdes > Ronald Lischeid
     3 × David John Wilson > Charlie Gers
     3 × David John Wilson > Ian Simpson > Captain Jack Sparrow
     3 × David John Wilson > Jacob Frey > Captain Jack Sparrow
     3 × David John Wilson > Nekima Levy-Pounds > Jacob Frey
     3 × David John Wilson > Raymond Dehn > Jacob Frey
     3 × David Rosenfeld > Al Flowers > Raymond Dehn
     3 × David Rosenfeld > Aswar Rahman
     3 × David Rosenfeld > Aswar Rahman > L.A. Nik
     3 × David Rosenfeld > Betsy Hodges > Al Flowers
     3 × David Rosenfeld > Betsy Hodges > Aswar Rahman
     3 × David Rosenfeld > Betsy Hodges > L.A. Nik
     3 × David Rosenfeld > Captain Jack Sparrow > Jacob Frey
     3 × David Rosenfeld > David John Wilson
     3 × David Rosenfeld > Ian Simpson > Charlie Gers
     3 × David Rosenfeld > Jacob Frey > Raymond Dehn
     3 × David Rosenfeld > Raymond Dehn > Ian Simpson
     3 × David Rosenfeld > Raymond Dehn > Troy Benjegerdes
     3 × David Rosenfeld > Ronald Lischeid > Captain Jack Sparrow
     3 × David Rosenfeld > Tom Hoch
     3 × David Rosenfeld > Tom Hoch > Jacob Frey
     3 × David Rosenfeld > Tom Hoch > Ronald Lischeid
     3 × David Rosenfeld > Troy Benjegerdes > Betsy Hodges
     3 × Gregg A. Iverson > Al Flowers
     3 × Gregg A. Iverson > Betsy Hodges > Charlie Gers
     3 × Gregg A. Iverson > Betsy Hodges > David Rosenfeld
     3 × Gregg A. Iverson > Betsy Hodges > Raymond Dehn
     3 × Gregg A. Iverson > Captain Jack Sparrow > Troy Benjegerdes
     3 × Gregg A. Iverson > Nekima Levy-Pounds > Betsy Hodges
     3 × Gregg A. Iverson > Nekima Levy-Pounds > Jacob Frey
     3 × Gregg A. Iverson > Raymond Dehn > Betsy Hodges
     3 × Gregg A. Iverson > Raymond Dehn > Tom Hoch
     3 × Gregg A. Iverson > Troy Benjegerdes > Al Flowers
     3 × Ian Simpson > Charlie Gers > L.A. Nik
     3 × Ian Simpson > Ronald Lischeid
     3 × Jacob Frey > Captain Jack Sparrow > Troy Benjegerdes
     3 × Jacob Frey > Captain Jack Sparrow > Undeclared Write-ins
     3 × Jacob Frey > David John Wilson > Betsy Hodges
     3 × Jacob Frey > David John Wilson > Nekima Levy-Pounds
     3 × Jacob Frey > David John Wilson > Ronald Lischeid
     3 × Jacob Frey > David Rosenfeld > Aswar Rahman
     3 × Jacob Frey > David Rosenfeld > Charlie Gers
     3 × Jacob Frey > Gregg A. Iverson > David John Wilson
     3 × Jacob Frey > Gregg A. Iverson > Ian Simpson
     3 × Jacob Frey > Ian Simpson > Tom Hoch
     3 × Jacob Frey > L.A. Nik > Al Flowers
     3 × Jacob Frey > L.A. Nik > Betsy Hodges
     3 × Jacob Frey > Ronald Lischeid > Gregg A. Iverson
     3 × Jacob Frey > Troy Benjegerdes > Al Flowers
     3 × Jacob Frey > Troy Benjegerdes > Charlie Gers
     3 × Jacob Frey > Troy Benjegerdes > David John Wilson
     3 × Jacob Frey > Troy Benjegerdes > David Rosenfeld
     3 × Jacob Frey > Troy Benjegerdes > Gregg A. Iverson
     3 × L.A. Nik > Al Flowers > Jacob Frey
     3 × L.A. Nik > Aswar Rahman > Nekima Levy-Pounds
     3 × L.A. Nik > Betsy Hodges
     3 × L.A. Nik > Captain Jack Sparrow > Betsy Hodges
     3 × L.A. Nik > Charlie Gers > David Rosenfeld
     3 × L.A. Nik > Charlie Gers > Troy Benjegerdes
     3 × L.A. Nik > Charlie Gers > Undeclared Write-ins
     3 × L.A. Nik > David John Wilson > Captain Jack Sparrow
     3 × L.A. Nik > David Rosenfeld > Ronald Lischeid
     3 × L.A. Nik > Gregg A. Iverson > Jacob Frey
     3 × L.A. Nik > Jacob Frey > Charlie Gers
     3 × L.A. Nik > Jacob Frey > David John Wilson
     3 × L.A. Nik > Jacob Frey > Ronald Lischeid
     3 × L.A. Nik > Raymond Dehn > Al Flowers
     3 × L.A. Nik > Ronald Lischeid
     3 × L.A. Nik > Ronald Lischeid > Troy Benjegerdes
     3 × L.A. Nik > Tom Hoch > Betsy Hodges
     3 × L.A. Nik > Tom Hoch > Nekima Levy-Pounds
     3 × L.A. Nik > Troy Benjegerdes > Charlie Gers
     3 × L.A. Nik > Troy Benjegerdes > Ronald Lischeid
     3 × Nekima Levy-Pounds > Aswar Rahman > Troy Benjegerdes
     3 × Nekima Levy-Pounds > David John Wilson
     3 × Nekima Levy-Pounds > David John Wilson > Raymond Dehn
     3 × Nekima Levy-Pounds > David Rosenfeld > Charlie Gers
     3 × Nekima Levy-Pounds > David Rosenfeld > Gregg A. Iverson
     3 × Nekima Levy-Pounds > Gregg A. Iverson > Al Flowers
     3 × Nekima Levy-Pounds > Gregg A. Iverson > Aswar Rahman
     3 × Nekima Levy-Pounds > Gregg A. Iverson > David Rosenfeld
     3 × Nekima Levy-Pounds > Ian Simpson > Captain Jack Sparrow
     3 × Nekima Levy-Pounds > L.A. Nik > Aswar Rahman
     3 × Nekima Levy-Pounds > Ronald Lischeid > Captain Jack Sparrow
     3 × Nekima Levy-Pounds > Ronald Lischeid > Tom Hoch
     3 × Nekima Levy-Pounds > Troy Benjegerdes > Captain Jack Sparrow
     3 × Raymond Dehn > Al Flowers > Charlie Gers
     3 × Raymond Dehn > Al Flowers > Gregg A. Iverson
     3 × Raymond Dehn > Al Flowers > Ian Simpson
     3 × Raymond Dehn > Aswar Rahman > Charlie Gers
     3 × Raymond Dehn > Charlie Gers > Jacob Frey
     3 × Raymond Dehn > David Rosenfeld > Charlie Gers
     3 × Raymond Dehn > David Rosenfeld > L.A. Nik
     3 × Raymond Dehn > David Rosenfeld > Undeclared Write-ins
     3 × Raymond Dehn > Gregg A. Iverson > Al Flowers
     3 × Raymond Dehn > L.A. Nik > Aswar Rahman
     3 × Raymond Dehn > Ronald Lischeid > Captain Jack Sparrow
     3 × Raymond Dehn > Ronald Lischeid > Ian Simpson
     3 × Raymond Dehn > Troy Benjegerdes > Nekima Levy-Pounds
     3 × Raymond Dehn > Undeclared Write-ins > Betsy Hodges
     3 × Ronald Lischeid > Betsy Hodges > Al Flowers
     3 × Ronald Lischeid > Captain Jack Sparrow > Ian Simpson
     3 × Ronald Lischeid > Charlie Gers > Captain Jack Sparrow
     3 × Ronald Lischeid > Charlie Gers > Jacob Frey
     3 × Ronald Lischeid > Charlie Gers > Tom Hoch
     3 × Ronald Lischeid > Charlie Gers > Undeclared Write-ins
     3 × Ronald Lischeid > Ian Simpson
     3 × Ronald Lischeid > Jacob Frey > Gregg A. Iverson
     3 × Ronald Lischeid > Jacob Frey > Ian Simpson
     3 × Ronald Lischeid > Jacob Frey > Nekima Levy-Pounds
     3 × Ronald Lischeid > L.A. Nik > David John Wilson
     3 × Ronald Lischeid > L.A. Nik > Nekima Levy-Pounds
     3 × Ronald Lischeid > Nekima Levy-Pounds > Jacob Frey
     3 × Ronald Lischeid > Tom Hoch > Gregg A. Iverson
     3 × Ronald Lischeid > Tom Hoch > Nekima Levy-Pounds
     3 × Tom Hoch > Aswar Rahman > David Rosenfeld
     3 × Tom Hoch > Aswar Rahman > Ian Simpson
     3 × Tom Hoch > David John Wilson > Charlie Gers
     3 × Tom Hoch > David Rosenfeld > Charlie Gers
     3 × Tom Hoch > David Rosenfeld > Ronald Lischeid
     3 × Tom Hoch > Ian Simpson > David John Wilson
     3 × Tom Hoch > Ian Simpson > L.A. Nik
     3 × Tom Hoch > L.A. Nik > David Rosenfeld
     3 × Tom Hoch > Ronald Lischeid > Nekima Levy-Pounds
     3 × Tom Hoch > Ronald Lischeid > Troy Benjegerdes
     3 × Tom Hoch > Troy Benjegerdes > Charlie Gers
     3 × Tom Hoch > Troy Benjegerdes > Gregg A. Iverson
     3 × Tom Hoch > Troy Benjegerdes > Jacob Frey
     3 × Tom Hoch > Troy Benjegerdes > L.A. Nik
     3 × Troy Benjegerdes > Captain Jack Sparrow
     3 × Troy Benjegerdes > Charlie Gers > L.A. Nik
     3 × Troy Benjegerdes > L.A. Nik > Charlie Gers
     3 × Troy Benjegerdes > Nekima Levy-Pounds > Raymond Dehn
     3 × Troy Benjegerdes > Raymond Dehn
     3 × Troy Benjegerdes > Tom Hoch
     3 × Troy Benjegerdes > Tom Hoch > Jacob Frey
     3 × Undeclared Write-ins > David John Wilson
     3 × Undeclared Write-ins > Tom Hoch > Jacob Frey
     2 × Al Flowers > Aswar Rahman > Nekima Levy-Pounds
     2 × Al Flowers > Betsy Hodges > David Rosenfeld
     2 × Al Flowers > Betsy Hodges > Ian Simpson
     2 × Al Flowers > Betsy Hodges > L.A. Nik
     2 × Al Flowers > Captain Jack Sparrow > Betsy Hodges
     2 × Al Flowers > Captain Jack Sparrow > David John Wilson
     2 × Al Flowers > Captain Jack Sparrow > L.A. Nik
     2 × Al Flowers > Charlie Gers
     2 × Al Flowers > David Rosenfeld
     2 × Al Flowers > David Rosenfeld > Charlie Gers
     2 × Al Flowers > Gregg A. Iverson > Betsy Hodges
     2 × Al Flowers > Jacob Frey > David John Wilson
     2 × Al Flowers > Jacob Frey > L.A. Nik
     2 × Al Flowers > Nekima Levy-Pounds > Charlie Gers
     2 × Al Flowers > Nekima Levy-Pounds > David John Wilson
     2 × Al Flowers > Nekima Levy-Pounds > Ronald Lischeid
     2 × Al Flowers > Raymond Dehn > Charlie Gers
     2 × Al Flowers > Raymond Dehn > Jacob Frey
     2 × Al Flowers > Tom Hoch > Gregg A. Iverson
     2 × Al Flowers > Tom Hoch > Ian Simpson
     2 × Aswar Rahman > Captain Jack Sparrow > Al Flowers
     2 × Aswar Rahman > Captain Jack Sparrow > Betsy Hodges
     2 × Aswar Rahman > Captain Jack Sparrow > David John Wilson
     2 × Aswar Rahman > Captain Jack Sparrow > Nekima Levy-Pounds
     2 × Aswar Rahman > Charlie Gers > David John Wilson
     2 × Aswar Rahman > Charlie Gers > Ronald Lischeid
     2 × Aswar Rahman > Charlie Gers > Tom Hoch
     2 × Aswar Rahman > David Rosenfeld > Betsy Hodges
     2 × Aswar Rahman > Gregg A. Iverson > Betsy Hodges
     2 × Aswar Rahman > Gregg A. Iverson > Raymond Dehn
     2 × Aswar Rahman > Jacob Frey > David Rosenfeld
     2 × Aswar Rahman > Raymond Dehn > Ronald Lischeid
     2 × Aswar Rahman > Ronald Lischeid
     2 × Aswar Rahman > Tom Hoch > Captain Jack Sparrow
     2 × Aswar Rahman > Tom Hoch > David John Wilson
     2 × Aswar Rahman > Tom Hoch > David Rosenfeld
     2 × Betsy Hodges > Al Flowers > Charlie Gers
     2 × Betsy Hodges > Al Flowers > Ian Simpson
     2 × Betsy Hodges > Al Flowers > Undeclared Write-ins
     2 × Betsy Hodges > Captain Jack Sparrow > Ronald Lischeid
     2 × Betsy Hodges > David John Wilson > David Rosenfeld
     2 × Betsy Hodges > David John Wilson > Troy Benjegerdes
     2 × Betsy Hodges > David Rosenfeld > Gregg A. Iverson
     2 × Betsy Hodges > David Rosenfeld > Ian Simpson
     2 × Betsy Hodges > David Rosenfeld > Ronald Lischeid
     2 × Betsy Hodges > David Rosenfeld > Undeclared Write-ins
     2 × Betsy Hodges > Gregg A. Iverson > L.A. Nik
     2 × Betsy Hodges > Ian Simpson > Aswar Rahman
     2 × Betsy Hodges > Ian Simpson > Charlie Gers
     2 × Betsy Hodges > Ian Simpson > David Rosenfeld
     2 × Betsy Hodges > L.A. Nik > Aswar Rahman
     2 × Betsy Hodges > L.A. Nik > David Rosenfeld
     2 × Betsy Hodges > L.A. Nik > Ian Simpson
     2 × Betsy Hodges > Ronald Lischeid > Aswar Rahman
     2 × Betsy Hodges > Ronald Lischeid > David Rosenfeld
     2 × Betsy Hodges > Troy Benjegerdes > Al Flowers
     2 × Betsy Hodges > Troy Benjegerdes > Aswar Rahman
     2 × Betsy Hodges > Troy Benjegerdes > David Rosenfeld
     2 × Betsy Hodges > Troy Benjegerdes > Gregg A. Iverson
     2 × Betsy Hodges > Troy Benjegerdes > Jacob Frey
     2 × Betsy Hodges > Troy Benjegerdes > Raymond Dehn
     2 × Captain Jack Sparrow > Al Flowers > David John Wilson
     2 × Captain Jack Sparrow > Al Flowers > Jacob Frey
     2 × Captain Jack Sparrow > Al Flowers > Nekima Levy-Pounds
     2 × Captain Jack Sparrow > Al Flowers > Raymond Dehn
     2 × Captain Jack Sparrow > Aswar Rahman > Nekima Levy-Pounds
     2 × Captain Jack Sparrow > Betsy Hodges > Jacob Frey
     2 × Captain Jack Sparrow > Charlie Gers > David Rosenfeld
     2 × Captain Jack Sparrow > Charlie Gers > Ian Simpson
     2 × Captain Jack Sparrow > Charlie Gers > Tom Hoch
     2 × Captain Jack Sparrow > David John Wilson > Aswar Rahman
     2 × Captain Jack Sparrow > David John Wilson > Raymond Dehn
     2 × Captain Jack Sparrow > David John Wilson > Ronald Lischeid
     2 × Captain Jack Sparrow > David Rosenfeld > Aswar Rahman
     2 × Captain Jack Sparrow > David Rosenfeld > Charlie Gers
     2 × Captain Jack Sparrow > Ian Simpson
     2 × Captain Jack Sparrow > Ian Simpson > Ronald Lischeid
     2 × Captain Jack Sparrow > Jacob Frey > David John Wilson
     2 × Captain Jack Sparrow > Jacob Frey > David Rosenfeld
     2 × Captain Jack Sparrow > Jacob Frey > Ian Simpson
     2 × Captain Jack Sparrow > L.A. Nik > Betsy Hodges
     2 × Captain Jack Sparrow > L.A. Nik > Tom Hoch
     2 × Captain Jack Sparrow > Nekima Levy-Pounds > Jacob Frey
     2 × Captain Jack Sparrow > Raymond Dehn > David John Wilson
     2 × Captain Jack Sparrow > Raymond Dehn > L.A. Nik
     2 × Captain Jack Sparrow > Ronald Lischeid > Ian Simpson
     2 × Captain Jack Sparrow > Tom Hoch > Aswar Rahman
     2 × Captain Jack Sparrow > Tom Hoch > Charlie Gers
     2 × Captain Jack Sparrow > Tom Hoch > David Rosenfeld
     2 × Captain Jack Sparrow > Tom Hoch > Ian Simpson
     2 × Captain Jack Sparrow > Tom Hoch > Nekima Levy-Pounds
     2 × Captain Jack Sparrow > Troy Benjegerdes > Ronald Lischeid
     2 × Charlie Gers > Al Flowers > Aswar Rahman
     2 × Charlie Gers > Al Flowers > Jacob Frey
     2 × Charlie Gers > Al Flowers > Tom Hoch
     2 × Charlie Gers > Aswar Rahman
     2 × Charlie Gers > Aswar Rahman > Al Flowers
     2 × Charlie Gers > Aswar Rahman > Captain Jack Sparrow
     2 × Charlie Gers > Aswar Rahman > L.A. Nik
     2 × Charlie Gers > Aswar Rahman > Ronald Lischeid
     2 × Charlie Gers > Betsy Hodges > Captain Jack Sparrow
     2 × Charlie Gers > Betsy Hodges > Ian Simpson
     2 × Charlie Gers > Betsy Hodges > Raymond Dehn
     2 × Charlie Gers > Betsy Hodges > Undeclared Write-ins
     2 × Charlie Gers > Captain Jack Sparrow > Raymond Dehn
     2 × Charlie Gers > David John Wilson
     2 × Charlie Gers > David John Wilson > Nekima Levy-Pounds
     2 × Charlie Gers > David Rosenfeld > Captain Jack Sparrow
     2 × Charlie Gers > David Rosenfeld > Ian Simpson
     2 × Charlie Gers > Gregg A. Iverson > Betsy Hodges
     2 × Charlie Gers > Gregg A. Iverson > Tom Hoch
     2 × Charlie Gers > Ian Simpson > Troy Benjegerdes
     2 × Charlie Gers > Jacob Frey > Al Flowers
     2 × Charlie Gers > Jacob Frey > Aswar Rahman
     2 × Charlie Gers > Jacob Frey > David John Wilson
     2 × Charlie Gers > Jacob Frey > David Rosenfeld
     2 × Charlie Gers > Jacob Frey > Ian Simpson
     2 × Charlie Gers > L.A. Nik > Raymond Dehn
     2 × Charlie Gers > Nekima Levy-Pounds > Captain Jack Sparrow
     2 × Charlie Gers > Nekima Levy-Pounds > Raymond Dehn
     2 × Charlie Gers > Nekima Levy-Pounds > Tom Hoch
     2 × Charlie Gers > Raymond Dehn > David John Wilson
     2 × Charlie Gers > Raymond Dehn > L.A. Nik
     2 × Charlie Gers > Raymond Dehn > Nekima Levy-Pounds
     2 × Charlie Gers > Raymond Dehn > Troy Benjegerdes
     2 × Charlie Gers > Ronald Lischeid > Betsy Hodges
     2 × Charlie Gers > Ronald Lischeid > Jacob Frey
     2 × Charlie Gers > Ronald Lischeid > Undeclared Write-ins
     2 × Charlie Gers > Tom Hoch > Gregg A. Iverson
     2 × Charlie Gers > Troy Benjegerdes > David Rosenfeld
     2 × Charlie Gers > Undeclared Write-ins > L.A. Nik
     2 × David John Wilson > Al Flowers > Raymond Dehn
     2 × David John Wilson > Aswar Rahman > Al Flowers
     2 × David John Wilson > Aswar Rahman > Tom Hoch
     2 × David John Wilson > Betsy Hodges > Al Flowers
     2 × David John Wilson > Betsy Hodges > Jacob Frey
     2 × David John Wilson > Betsy Hodges > Raymond Dehn
     2 × David John Wilson > Betsy Hodges > Tom Hoch
     2 × David John Wilson > Captain Jack Sparrow
     2 × David John Wilson > Captain Jack Sparrow > Charlie Gers
     2 × David John Wilson > Captain Jack Sparrow > David Rosenfeld
     2 × David John Wilson > Captain Jack Sparrow > Jacob Frey
     2 × David John Wilson > Captain Jack Sparrow > Nekima Levy-Pounds
     2 × David John Wilson > Captain Jack Sparrow > Ronald Lischeid
     2 × David John Wilson > Charlie Gers > L.A. Nik
     2 × David John Wilson > David Rosenfeld > Ronald Lischeid
     2 × David John Wilson > Gregg A. Iverson
     2 × David John Wilson > Ian Simpson > Tom Hoch
     2 × David John Wilson > Jacob Frey > Aswar Rahman
     2 × David John Wilson > Jacob Frey > Nekima Levy-Pounds
     2 × David John Wilson > Jacob Frey > Raymond Dehn
     2 × David John Wilson > L.A. Nik > Captain Jack Sparrow
     2 × David John Wilson > Nekima Levy-Pounds
     2 × David John Wilson > Nekima Levy-Pounds > Tom Hoch
     2 × David John Wilson > Raymond Dehn > Betsy Hodges
     2 × David John Wilson > Raymond Dehn > Nekima Levy-Pounds
     2 × David John Wilson > Ronald Lischeid > L.A. Nik
     2 × David John Wilson > Tom Hoch > Captain Jack Sparrow
     2 × David John Wilson > Tom Hoch > Nekima Levy-Pounds
     2 × David John Wilson > Troy Benjegerdes
     2 × David Rosenfeld > Al Flowers > Nekima Levy-Pounds
     2 × David Rosenfeld > Al Flowers > Ronald Lischeid
     2 × David Rosenfeld > Aswar Rahman > Al Flowers
     2 × David Rosenfeld > Betsy Hodges > Gregg A. Iverson
     2 × David Rosenfeld > Captain Jack Sparrow > Ian Simpson
     2 × David Rosenfeld > Captain Jack Sparrow > Nekima Levy-Pounds
     2 × David Rosenfeld > Captain Jack Sparrow > Troy Benjegerdes
     2 × David Rosenfeld > Charlie Gers > Captain Jack Sparrow
     2 × David Rosenfeld > Charlie Gers > Ronald Lischeid
     2 × David Rosenfeld > David John Wilson > Nekima Levy-Pounds
     2 × David Rosenfeld > Ian Simpson > Captain Jack Sparrow
     2 × David Rosenfeld > Jacob Frey > Gregg A. Iverson
     2 × David Rosenfeld > Jacob Frey > Tom Hoch
     2 × David Rosenfeld > L.A. Nik > Raymond Dehn
     2 × David Rosenfeld > Nekima Levy-Pounds > David John Wilson
     2 × David Rosenfeld > Ronald Lischeid
     2 × David Rosenfeld > Ronald Lischeid > David John Wilson
     2 × David Rosenfeld > Tom Hoch > Captain Jack Sparrow
     2 × David Rosenfeld > Tom Hoch > Raymond Dehn
     2 × David Rosenfeld > Troy Benjegerdes > David John Wilson
     2 × Gregg A. Iverson > Al Flowers > Captain Jack Sparrow
     2 × Gregg A. Iverson > Al Flowers > Jacob Frey
     2 × Gregg A. Iverson > Aswar Rahman
     2 × Gregg A. Iverson > Aswar Rahman > Betsy Hodges
     2 × Gregg A. Iverson > Aswar Rahman > Raymond Dehn
     2 × Gregg A. Iverson > Betsy Hodges > David John Wilson
     2 × Gregg A. Iverson > Captain Jack Sparrow > Al Flowers
     2 × Gregg A. Iverson > Captain Jack Sparrow > Jacob Frey
     2 × Gregg A. Iverson > Captain Jack Sparrow > Nekima Levy-Pounds
     2 × Gregg A. Iverson > Charlie Gers
     2 × Gregg A. Iverson > Charlie Gers > Ronald Lischeid
     2 × Gregg A. Iverson > David Rosenfeld > Betsy Hodges
     2 × Gregg A. Iverson > David Rosenfeld > Captain Jack Sparrow
     2 × Gregg A. Iverson > David Rosenfeld > Tom Hoch
     2 × Gregg A. Iverson > David Rosenfeld > Troy Benjegerdes
     2 × Gregg A. Iverson > Jacob Frey > Al Flowers
     2 × Gregg A. Iverson > Jacob Frey > Captain Jack Sparrow
     2 × Gregg A. Iverson > Jacob Frey > David John Wilson
     2 × Gregg A. Iverson > Jacob Frey > David Rosenfeld
     2 × Gregg A. Iverson > Raymond Dehn > Al Flowers
     2 × Gregg A. Iverson > Raymond Dehn > Captain Jack Sparrow
     2 × Gregg A. Iverson > Raymond Dehn > Jacob Frey
     2 × Gregg A. Iverson > Raymond Dehn > Nekima Levy-Pounds
     2 × Gregg A. Iverson > Ronald Lischeid
     2 × Gregg A. Iverson > Ronald Lischeid > Charlie Gers
     2 × Gregg A. Iverson > Troy Benjegerdes
     2 × Ian Simpson > Betsy Hodges > Raymond Dehn
     2 × Ian Simpson > Captain Jack Sparrow > David John Wilson
     2 × Ian Simpson > Captain Jack Sparrow > Tom Hoch
     2 × Ian Simpson > Charlie Gers > Betsy Hodges
     2 × Ian Simpson > David John Wilson > Captain Jack Sparrow
     2 × Ian Simpson > Nekima Levy-Pounds > Raymond Dehn
     2 × Ian Simpson > Raymond Dehn > Jacob Frey
     2 × Ian Simpson > Raymond Dehn > Tom Hoch
     2 × Ian Simpson > Tom Hoch
     2 × Ian Simpson > Tom Hoch > Captain Jack Sparrow
     2 × Ian Simpson > Tom Hoch > Jacob Frey
     2 × Jacob Frey > Al Flowers > Charlie Gers
     2 × Jacob Frey > Al Flowers > Ian Simpson
     2 × Jacob Frey > Charlie Gers > Ian Simpson
     2 × Jacob Frey > Charlie Gers > Undeclared Write-ins
     2 × Jacob Frey > David John Wilson > Charlie Gers
     2 × Jacob Frey > David John Wilson > David Rosenfeld
     2 × Jacob Frey > David John Wilson > Ian Simpson
     2 × Jacob Frey > David Rosenfeld > L.A. Nik
     2 × Jacob Frey > David Rosenfeld > Ronald Lischeid
     2 × Jacob Frey > Gregg A. Iverson > Troy Benjegerdes
     2 × Jacob Frey > Ian Simpson > Betsy Hodges
     2 × Jacob Frey > Ian Simpson > L.A. Nik
     2 × Jacob Frey > L.A. Nik > David John Wilson
     2 × Jacob Frey > L.A. Nik > David Rosenfeld
     2 × Jacob Frey > L.A. Nik > Gregg A. Iverson
     2 × Jacob Frey > Ronald Lischeid > Captain Jack Sparrow
     2 × Jacob Frey > Ronald Lischeid > David Rosenfeld
     2 × Jacob Frey > Ronald Lischeid > L.A. Nik
     2 × Jacob Frey > Troy Benjegerdes > L.A. Nik
     2 × Jacob Frey > Undeclared Write-ins > Betsy Hodges
     2 × Jacob Frey > Undeclared Write-ins > Raymond Dehn
     2 × L.A. Nik > Betsy Hodges > Al Flowers
     2 × L.A. Nik > Betsy Hodges > Captain Jack Sparrow
     2 × L.A. Nik > Betsy Hodges > Charlie Gers
     2 × L.A. Nik > Captain Jack Sparrow > Charlie Gers
     2 × L.A. Nik > Captain Jack Sparrow > Ronald Lischeid
     2 × L.A. Nik > Charlie Gers > Gregg A. Iverson
     2 × L.A. Nik > David John Wilson
     2 × L.A. Nik > David John Wilson > Charlie Gers
     2 × L.A. Nik > David John Wilson > Ronald Lischeid
     2 × L.A. Nik > Gregg A. Iverson > Charlie Gers
     2 × L.A. Nik > Gregg A. Iverson > Raymond Dehn
     2 × L.A. Nik > Ian Simpson > Captain Jack Sparrow
     2 × L.A. Nik > Nekima Levy-Pounds
     2 × L.A. Nik > Nekima Levy-Pounds > Betsy Hodges
     2 × L.A. Nik > Nekima Levy-Pounds > Jacob Frey
     2 × L.A. Nik > Raymond Dehn > Aswar Rahman
     2 × L.A. Nik > Raymond Dehn > Tom Hoch
     2 × L.A. Nik > Ronald Lischeid > David Rosenfeld
     2 × L.A. Nik > Ronald Lischeid > Jacob Frey
     2 × L.A. Nik > Tom Hoch > Al Flowers
     2 × L.A. Nik > Tom Hoch > Raymond Dehn
     2 × L.A. Nik > Troy Benjegerdes
     2 × L.A. Nik > Troy Benjegerdes > David John Wilson
     2 × Nekima Levy-Pounds > Charlie Gers > David John Wilson
     2 × Nekima Levy-Pounds > Charlie Gers > Ronald Lischeid
     2 × Nekima Levy-Pounds > David John Wilson > Charlie Gers
     2 × Nekima Levy-Pounds > David Rosenfeld > Troy Benjegerdes
     2 × Nekima Levy-Pounds > Ian Simpson > Raymond Dehn
     2 × Nekima Levy-Pounds > Ian Simpson > Ronald Lischeid
     2 × Nekima Levy-Pounds > Jacob Frey > Troy Benjegerdes
     2 × Nekima Levy-Pounds > L.A. Nik > Al Flowers
     2 × Nekima Levy-Pounds > Ronald Lischeid > Aswar Rahman
     2 × Nekima Levy-Pounds > Ronald Lischeid > David John Wilson
     2 × Nekima Levy-Pounds > Ronald Lischeid > David Rosenfeld
     2 × Nekima Levy-Pounds > Ronald Lischeid > Jacob Frey
     2 × Nekima Levy-Pounds > Tom Hoch > Ian Simpson
     2 × Nekima Levy-Pounds > Tom Hoch > Troy Benjegerdes
     2 × Nekima Levy-Pounds > Troy Benjegerdes > Aswar Rahman
     2 × Nekima Levy-Pounds > Troy Benjegerdes > Betsy Hodges
     2 × Nekima Levy-Pounds > Troy Benjegerdes > Jacob Frey
     2 × Nekima Levy-Pounds > Undeclared Write-ins > Betsy Hodges
     2 × Nekima Levy-Pounds > Undeclared Write-ins > Raymond Dehn
     2 × Raymond Dehn > Al Flowers > Ronald Lischeid
     2 × Raymond Dehn > Al Flowers > Troy Benjegerdes
     2 × Raymond Dehn > Aswar Rahman > Undeclared Write-ins
     2 × Raymond Dehn > Captain Jack Sparrow > Aswar Rahman
     2 × Raymond Dehn > Captain Jack Sparrow > Gregg A. Iverson
     2 × Raymond Dehn > Charlie Gers > Aswar Rahman
     2 × Raymond Dehn > Charlie Gers > David John Wilson
     2 × Raymond Dehn > Charlie Gers > David Rosenfeld
     2 × Raymond Dehn > David John Wilson > Aswar Rahman
     2 × Raymond Dehn > David John Wilson > David Rosenfeld
     2 × Raymond Dehn > David John Wilson > Jacob Frey
     2 × Raymond Dehn > David John Wilson > L.A. Nik
     2 × Raymond Dehn > David John Wilson > Ronald Lischeid
     2 × Raymond Dehn > David Rosenfeld > Ian Simpson
     2 × Raymond Dehn > Gregg A. Iverson > David Rosenfeld
     2 × Raymond Dehn > Ian Simpson > Captain Jack Sparrow
     2 × Raymond Dehn > Ian Simpson > Ronald Lischeid
     2 × Raymond Dehn > Jacob Frey > Ronald Lischeid
     2 × Raymond Dehn > L.A. Nik > David John Wilson
     2 × Raymond Dehn > L.A. Nik > David Rosenfeld
     2 × Raymond Dehn > L.A. Nik > Gregg A. Iverson
     2 × Raymond Dehn > L.A. Nik > Jacob Frey
     2 × Raymond Dehn > L.A. Nik > Ronald Lischeid
     2 × Raymond Dehn > L.A. Nik > Undeclared Write-ins
     2 × Raymond Dehn > Ronald Lischeid > Al Flowers
     2 × Raymond Dehn > Ronald Lischeid > Aswar Rahman
     2 × Raymond Dehn > Ronald Lischeid > Betsy Hodges
     2 × Raymond Dehn > Ronald Lischeid > Gregg A. Iverson
     2 × Raymond Dehn > Ronald Lischeid > L.A. Nik
     2 × Raymond Dehn > Ronald Lischeid > Nekima Levy-Pounds
     2 × Raymond Dehn > Troy Benjegerdes
     2 × Raymond Dehn > Troy Benjegerdes > Jacob Frey
     2 × Ronald Lischeid > Aswar Rahman > Captain Jack Sparrow
     2 × Ronald Lischeid > Betsy Hodges > Troy Benjegerdes
     2 × Ronald Lischeid > Captain Jack Sparrow > Betsy Hodges
     2 × Ronald Lischeid > Captain Jack Sparrow > David John Wilson
     2 × Ronald Lischeid > Captain Jack Sparrow > L.A. Nik
     2 × Ronald Lischeid > Charlie Gers > Betsy Hodges
     2 × Ronald Lischeid > Charlie Gers > Raymond Dehn
     2 × Ronald Lischeid > David John Wilson > Charlie Gers
     2 × Ronald Lischeid > David Rosenfeld > Betsy Hodges
     2 × Ronald Lischeid > Gregg A. Iverson
     2 × Ronald Lischeid > Ian Simpson > L.A. Nik
     2 × Ronald Lischeid > L.A. Nik > Tom Hoch
     2 × Ronald Lischeid > Nekima Levy-Pounds > Betsy Hodges
     2 × Ronald Lischeid > Nekima Levy-Pounds > Raymond Dehn
     2 × Ronald Lischeid > Raymond Dehn
     2 × Ronald Lischeid > Raymond Dehn > Tom Hoch
     2 × Ronald Lischeid > Tom Hoch > Captain Jack Sparrow
     2 × Ronald Lischeid > Tom Hoch > Charlie Gers
     2 × Ronald Lischeid > Troy Benjegerdes > Al Flowers
     2 × Tom Hoch > Al Flowers > David Rosenfeld
     2 × Tom Hoch > Aswar Rahman > Undeclared Write-ins
     2 × Tom Hoch > David John Wilson > David Rosenfeld
     2 × Tom Hoch > David John Wilson > Gregg A. Iverson
     2 × Tom Hoch > David John Wilson > Troy Benjegerdes
     2 × Tom Hoch > David Rosenfeld > Aswar Rahman
     2 × Tom Hoch > David Rosenfeld > Gregg A. Iverson
     2 × Tom Hoch > David Rosenfeld > Ian Simpson
     2 × Tom Hoch > David Rosenfeld > L.A. Nik
     2 × Tom Hoch > Gregg A. Iverson > David Rosenfeld
     2 × Tom Hoch > Gregg A. Iverson > Ian Simpson
     2 × Tom Hoch > Ian Simpson > Gregg A. Iverson
     2 × Tom Hoch > Ian Simpson > Ronald Lischeid
     2 × Tom Hoch > L.A. Nik > Troy Benjegerdes
     2 × Tom Hoch > L.A. Nik > Undeclared Write-ins
     2 × Tom Hoch > Nekima Levy-Pounds > Christopher Zimmerman
     2 × Tom Hoch > Nekima Levy-Pounds > Undeclared Write-ins
     2 × Tom Hoch > Ronald Lischeid > David Rosenfeld
     2 × Tom Hoch > Troy Benjegerdes > Betsy Hodges
     2 × Tom Hoch > Troy Benjegerdes > David Rosenfeld
     2 × Tom Hoch > Undeclared Write-ins > Captain Jack Sparrow
     2 × Tom Hoch > Undeclared Write-ins > Charlie Gers
     2 × Tom Hoch > Undeclared Write-ins > L.A. Nik
     2 × Troy Benjegerdes > Aswar Rahman > Al Flowers
     2 × Troy Benjegerdes > Betsy Hodges > Captain Jack Sparrow
     2 × Troy Benjegerdes > Betsy Hodges > Nekima Levy-Pounds
     2 × Troy Benjegerdes > Captain Jack Sparrow > Betsy Hodges
     2 × Troy Benjegerdes > Captain Jack Sparrow > Ronald Lischeid
     2 × Troy Benjegerdes > Ian Simpson
     2 × Troy Benjegerdes > Ian Simpson > Charlie Gers
     2 × Troy Benjegerdes > Jacob Frey > Aswar Rahman
     2 × Troy Benjegerdes > Jacob Frey > Charlie Gers
     2 × Troy Benjegerdes > L.A. Nik > Captain Jack Sparrow
     2 × Troy Benjegerdes > L.A. Nik > Ian Simpson
     2 × Troy Benjegerdes > Nekima Levy-Pounds > Betsy Hodges
     2 × Troy Benjegerdes > Nekima Levy-Pounds > David Rosenfeld
     2 × Troy Benjegerdes > Raymond Dehn > David Rosenfeld
     2 × Troy Benjegerdes > Raymond Dehn > Jacob Frey
     2 × Troy Benjegerdes > Ronald Lischeid
     2 × Troy Benjegerdes > Ronald Lischeid > Jacob Frey
     2 × Troy Benjegerdes > Ronald Lischeid > L.A. Nik
     2 × Troy Benjegerdes > Tom Hoch > Raymond Dehn
     2 × Undeclared Write-ins > Al Flowers
     2 × Undeclared Write-ins > Captain Jack Sparrow
     2 × Undeclared Write-ins > Charlie Gers
     2 × Undeclared Write-ins > Raymond Dehn
     1 × Al Flowers > Aswar Rahman > Captain Jack Sparrow
     1 × Al Flowers > Aswar Rahman > Charlie Gers
     1 × Al Flowers > Aswar Rahman > David John Wilson
     1 × Al Flowers > Aswar Rahman > Gregg A. Iverson
     1 × Al Flowers > Aswar Rahman > L.A. Nik
     1 × Al Flowers > Aswar Rahman > Troy Benjegerdes
     1 × Al Flowers > Captain Jack Sparrow > David Rosenfeld
     1 × Al Flowers > Captain Jack Sparrow > Gregg A. Iverson
     1 × Al Flowers > Captain Jack Sparrow > Nekima Levy-Pounds
     1 × Al Flowers > Captain Jack Sparrow > Tom Hoch
     1 × Al Flowers > Charlie Gers > Raymond Dehn
     1 × Al Flowers > Charlie Gers > Tom Hoch
     1 × Al Flowers > David John Wilson > Captain Jack Sparrow
     1 × Al Flowers > David John Wilson > Ian Simpson
     1 × Al Flowers > David John Wilson > Jacob Frey
     1 × Al Flowers > David Rosenfeld > Jacob Frey
     1 × Al Flowers > David Rosenfeld > L.A. Nik
     1 × Al Flowers > David Rosenfeld > Raymond Dehn
     1 × Al Flowers > Gregg A. Iverson > Charlie Gers
     1 × Al Flowers > Gregg A. Iverson > David Rosenfeld
     1 × Al Flowers > Gregg A. Iverson > Ian Simpson
     1 × Al Flowers > Gregg A. Iverson > Raymond Dehn
     1 × Al Flowers > Gregg A. Iverson > Ronald Lischeid
     1 × Al Flowers > Gregg A. Iverson > Tom Hoch
     1 × Al Flowers > Ian Simpson
     1 × Al Flowers > Ian Simpson > Betsy Hodges
     1 × Al Flowers > Ian Simpson > Captain Jack Sparrow
     1 × Al Flowers > Ian Simpson > David John Wilson
     1 × Al Flowers > Ian Simpson > Ronald Lischeid
     1 × Al Flowers > Jacob Frey > Charlie Gers
     1 × Al Flowers > L.A. Nik > Jacob Frey
     1 × Al Flowers > L.A. Nik > Raymond Dehn
     1 × Al Flowers > L.A. Nik > Undeclared Write-ins
     1 × Al Flowers > Nekima Levy-Pounds > David Rosenfeld
     1 × Al Flowers > Nekima Levy-Pounds > Ian Simpson
     1 × Al Flowers > Nekima Levy-Pounds > Undeclared Write-ins
     1 × Al Flowers > Raymond Dehn > David John Wilson
     1 × Al Flowers > Raymond Dehn > Gregg A. Iverson
     1 × Al Flowers > Raymond Dehn > Ian Simpson
     1 × Al Flowers > Ronald Lischeid
     1 × Al Flowers > Ronald Lischeid > Gregg A. Iverson
     1 × Al Flowers > Ronald Lischeid > L.A. Nik
     1 × Al Flowers > Tom Hoch > Ronald Lischeid
     1 × Al Flowers > Troy Benjegerdes > Captain Jack Sparrow
     1 × Al Flowers > Troy Benjegerdes > Gregg A. Iverson
     1 × Al Flowers > Troy Benjegerdes > L.A. Nik
     1 × Al Flowers > Troy Benjegerdes > Undeclared Write-ins
     1 × Al Flowers > Undeclared Write-ins
     1 × Al Flowers > Undeclared Write-ins > Betsy Hodges
     1 × Aswar Rahman > Al Flowers > David John Wilson
     1 × Aswar Rahman > Al Flowers > Gregg A. Iverson
     1 × Aswar Rahman > Betsy Hodges > David Rosenfeld
     1 × Aswar Rahman > Betsy Hodges > Gregg A. Iverson
     1 × Aswar Rahman > Betsy Hodges > Ian Simpson
     1 × Aswar Rahman > Betsy Hodges > Undeclared Write-ins
     1 × Aswar Rahman > Captain Jack Sparrow > Charlie Gers
     1 × Aswar Rahman > Captain Jack Sparrow > Jacob Frey
     1 × Aswar Rahman > Captain Jack Sparrow > Troy Benjegerdes
     1 × Aswar Rahman > Charlie Gers > Betsy Hodges
     1 × Aswar Rahman > Charlie Gers > Ian Simpson
     1 × Aswar Rahman > Charlie Gers > Jacob Frey
     1 × Aswar Rahman > Charlie Gers > Troy Benjegerdes
     1 × Aswar Rahman > Charlie Gers > Undeclared Write-ins
     1 × Aswar Rahman > David John Wilson > Betsy Hodges
     1 × Aswar Rahman > David John Wilson > L.A. Nik
     1 × Aswar Rahman > David John Wilson > Raymond Dehn
     1 × Aswar Rahman > David John Wilson > Tom Hoch
     1 × Aswar Rahman > David Rosenfeld > Al Flowers
     1 × Aswar Rahman > David Rosenfeld > Captain Jack Sparrow
     1 × Aswar Rahman > David Rosenfeld > David John Wilson
     1 × Aswar Rahman > David Rosenfeld > L.A. Nik
     1 × Aswar Rahman > David Rosenfeld > Nekima Levy-Pounds
     1 × Aswar Rahman > David Rosenfeld > Raymond Dehn
     1 × Aswar Rahman > David Rosenfeld > Ronald Lischeid
     1 × Aswar Rahman > David Rosenfeld > Tom Hoch
     1 × Aswar Rahman > David Rosenfeld > Troy Benjegerdes
     1 × Aswar Rahman > Gregg A. Iverson
     1 × Aswar Rahman > Gregg A. Iverson > Captain Jack Sparrow
     1 × Aswar Rahman > Gregg A. Iverson > Charlie Gers
     1 × Aswar Rahman > Gregg A. Iverson > David John Wilson
     1 × Aswar Rahman > Gregg A. Iverson > Ian Simpson
     1 × Aswar Rahman > Gregg A. Iverson > Jacob Frey
     1 × Aswar Rahman > Gregg A. Iverson > Nekima Levy-Pounds
     1 × Aswar Rahman > Ian Simpson > Al Flowers
     1 × Aswar Rahman > Ian Simpson > Betsy Hodges
     1 × Aswar Rahman > Ian Simpson > Tom Hoch
     1 × Aswar Rahman > Jacob Frey > Captain Jack Sparrow
     1 × Aswar Rahman > Jacob Frey > L.A. Nik
     1 × Aswar Rahman > L.A. Nik
     1 × Aswar Rahman > L.A. Nik > Captain Jack Sparrow
     1 × Aswar Rahman > L.A. Nik > Charlie Gers
     1 × Aswar Rahman > L.A. Nik > Ian Simpson
     1 × Aswar Rahman > L.A. Nik > Raymond Dehn
     1 × Aswar Rahman > L.A. Nik > Troy Benjegerdes
     1 × Aswar Rahman > L.A. Nik > Undeclared Write-ins
     1 × Aswar Rahman > Nekima Levy-Pounds > Charlie Gers
     1 × Aswar Rahman > Nekima Levy-Pounds > David John Wilson
     1 × Aswar Rahman > Nekima Levy-Pounds > Ian Simpson
     1 × Aswar Rahman > Raymond Dehn > David John Wilson
     1 × Aswar Rahman > Raymond Dehn > L.A. Nik
     1 × Aswar Rahman > Raymond Dehn > Troy Benjegerdes
     1 × Aswar Rahman > Ronald Lischeid > Betsy Hodges
     1 × Aswar Rahman > Ronald Lischeid > Jacob Frey
     1 × Aswar Rahman > Ronald Lischeid > L.A. Nik
     1 × Aswar Rahman > Troy Benjegerdes > Betsy Hodges
     1 × Aswar Rahman > Troy Benjegerdes > L.A. Nik
     1 × Aswar Rahman > Troy Benjegerdes > Raymond Dehn
     1 × Aswar Rahman > Troy Benjegerdes > Tom Hoch
     1 × Aswar Rahman > Undeclared Write-ins
     1 × Betsy Hodges > Al Flowers > Ronald Lischeid
     1 × Betsy Hodges > Aswar Rahman > Ian Simpson
     1 × Betsy Hodges > Captain Jack Sparrow > Gregg A. Iverson
     1 × Betsy Hodges > Captain Jack Sparrow > Troy Benjegerdes
     1 × Betsy Hodges > Charlie Gers > Aswar Rahman
     1 × Betsy Hodges > Charlie Gers > Ronald Lischeid
     1 × Betsy Hodges > David John Wilson > Aswar Rahman
     1 × Betsy Hodges > David John Wilson > Charlie Gers
     1 × Betsy Hodges > David John Wilson > Gregg A. Iverson
     1 × Betsy Hodges > Gregg A. Iverson > Ian Simpson
     1 × Betsy Hodges > Gregg A. Iverson > Undeclared Write-ins
     1 × Betsy Hodges > Ian Simpson > Jacob Frey
     1 × Betsy Hodges > Ian Simpson > L.A. Nik
     1 × Betsy Hodges > Ian Simpson > Raymond Dehn
     1 × Betsy Hodges > Ian Simpson > Ronald Lischeid
     1 × Betsy Hodges > Ian Simpson > Tom Hoch
     1 × Betsy Hodges > L.A. Nik > Raymond Dehn
     1 × Betsy Hodges > Ronald Lischeid > Al Flowers
     1 × Betsy Hodges > Ronald Lischeid > Gregg A. Iverson
     1 × Betsy Hodges > Troy Benjegerdes > Ronald Lischeid
     1 × Betsy Hodges > Undeclared Write-ins > David Rosenfeld
     1 × Betsy Hodges > Undeclared Write-ins > Nekima Levy-Pounds
     1 × Captain Jack Sparrow > Al Flowers > Aswar Rahman
     1 × Captain Jack Sparrow > Al Flowers > David Rosenfeld
     1 × Captain Jack Sparrow > Al Flowers > Ian Simpson
     1 × Captain Jack Sparrow > Al Flowers > L.A. Nik
     1 × Captain Jack Sparrow > Aswar Rahman
     1 × Captain Jack Sparrow > Aswar Rahman > Al Flowers
     1 × Captain Jack Sparrow > Aswar Rahman > Betsy Hodges
     1 × Captain Jack Sparrow > Aswar Rahman > Jacob Frey
     1 × Captain Jack Sparrow > Aswar Rahman > Raymond Dehn
     1 × Captain Jack Sparrow > Aswar Rahman > Undeclared Write-ins
     1 × Captain Jack Sparrow > Betsy Hodges > Aswar Rahman
     1 × Captain Jack Sparrow > Betsy Hodges > David John Wilson
     1 × Captain Jack Sparrow > Betsy Hodges > Gregg A. Iverson
     1 × Captain Jack Sparrow > Charlie Gers > David John Wilson
     1 × Captain Jack Sparrow > Charlie Gers > Ronald Lischeid
     1 × Captain Jack Sparrow > David John Wilson > Al Flowers
     1 × Captain Jack Sparrow > David John Wilson > Tom Hoch
     1 × Captain Jack Sparrow > David Rosenfeld > David John Wilson
     1 × Captain Jack Sparrow > David Rosenfeld > Gregg A. Iverson
     1 × Captain Jack Sparrow > David Rosenfeld > Nekima Levy-Pounds
     1 × Captain Jack Sparrow > David Rosenfeld > Raymond Dehn
     1 × Captain Jack Sparrow > David Rosenfeld > Ronald Lischeid
     1 × Captain Jack Sparrow > Gregg A. Iverson > Betsy Hodges
     1 × Captain Jack Sparrow > Gregg A. Iverson > David John Wilson
     1 × Captain Jack Sparrow > Gregg A. Iverson > Raymond Dehn
     1 × Captain Jack Sparrow > Gregg A. Iverson > Troy Benjegerdes
     1 × Captain Jack Sparrow > Ian Simpson > Gregg A. Iverson
     1 × Captain Jack Sparrow > Ian Simpson > Jacob Frey
     1 × Captain Jack Sparrow > Ian Simpson > Troy Benjegerdes
     1 × Captain Jack Sparrow > Jacob Frey > Charlie Gers
     1 × Captain Jack Sparrow > Jacob Frey > Gregg A. Iverson
     1 × Captain Jack Sparrow > Jacob Frey > Raymond Dehn
     1 × Captain Jack Sparrow > L.A. Nik > Al Flowers
     1 × Captain Jack Sparrow > L.A. Nik > Aswar Rahman
     1 × Captain Jack Sparrow > L.A. Nik > Charlie Gers
     1 × Captain Jack Sparrow > L.A. Nik > David Rosenfeld
     1 × Captain Jack Sparrow > L.A. Nik > Gregg A. Iverson
     1 × Captain Jack Sparrow > L.A. Nik > Nekima Levy-Pounds
     1 × Captain Jack Sparrow > L.A. Nik > Raymond Dehn
     1 × Captain Jack Sparrow > Nekima Levy-Pounds
     1 × Captain Jack Sparrow > Nekima Levy-Pounds > Charlie Gers
     1 × Captain Jack Sparrow > Nekima Levy-Pounds > David John Wilson
     1 × Captain Jack Sparrow > Nekima Levy-Pounds > David Rosenfeld
     1 × Captain Jack Sparrow > Nekima Levy-Pounds > Gregg A. Iverson
     1 × Captain Jack Sparrow > Nekima Levy-Pounds > Troy Benjegerdes
     1 × Captain Jack Sparrow > Nekima Levy-Pounds > Undeclared Write-ins
     1 × Captain Jack Sparrow > Raymond Dehn
     1 × Captain Jack Sparrow > Raymond Dehn > Al Flowers
     1 × Captain Jack Sparrow > Ronald Lischeid
     1 × Captain Jack Sparrow > Ronald Lischeid > Charlie Gers
     1 × Captain Jack Sparrow > Ronald Lischeid > David John Wilson
     1 × Captain Jack Sparrow > Ronald Lischeid > David Rosenfeld
     1 × Captain Jack Sparrow > Ronald Lischeid > Jacob Frey
     1 × Captain Jack Sparrow > Ronald Lischeid > Nekima Levy-Pounds
     1 × Captain Jack Sparrow > Ronald Lischeid > Troy Benjegerdes
     1 × Captain Jack Sparrow > Tom Hoch > David John Wilson
     1 × Captain Jack Sparrow > Tom Hoch > Gregg A. Iverson
     1 × Captain Jack Sparrow > Tom Hoch > L.A. Nik
     1 × Captain Jack Sparrow > Tom Hoch > Troy Benjegerdes
     1 × Captain Jack Sparrow > Troy Benjegerdes > Betsy Hodges
     1 × Captain Jack Sparrow > Troy Benjegerdes > Ian Simpson
     1 × Captain Jack Sparrow > Troy Benjegerdes > L.A. Nik
     1 × Captain Jack Sparrow > Undeclared Write-ins > Ian Simpson
     1 × Charlie Gers > Al Flowers
     1 × Charlie Gers > Al Flowers > Captain Jack Sparrow
     1 × Charlie Gers > Al Flowers > L.A. Nik
     1 × Charlie Gers > Al Flowers > Nekima Levy-Pounds
     1 × Charlie Gers > Aswar Rahman > David John Wilson
     1 × Charlie Gers > Aswar Rahman > Ian Simpson
     1 × Charlie Gers > Aswar Rahman > Raymond Dehn
     1 × Charlie Gers > Betsy Hodges > David John Wilson
     1 × Charlie Gers > Betsy Hodges > David Rosenfeld
     1 × Charlie Gers > Betsy Hodges > L.A. Nik
     1 × Charlie Gers > Captain Jack Sparrow > Al Flowers
     1 × Charlie Gers > Captain Jack Sparrow > Aswar Rahman
     1 × Charlie Gers > Captain Jack Sparrow > Betsy Hodges
     1 × Charlie Gers > David John Wilson > Aswar Rahman
     1 × Charlie Gers > David John Wilson > Betsy Hodges
     1 × Charlie Gers > David John Wilson > David Rosenfeld
     1 × Charlie Gers > David John Wilson > Gregg A. Iverson
     1 × Charlie Gers > David John Wilson > Tom Hoch
     1 × Charlie Gers > David John Wilson > Troy Benjegerdes
     1 × Charlie Gers > David Rosenfeld
     1 × Charlie Gers > David Rosenfeld > Al Flowers
     1 × Charlie Gers > David Rosenfeld > Aswar Rahman
     1 × Charlie Gers > David Rosenfeld > Gregg A. Iverson
     1 × Charlie Gers > David Rosenfeld > Jacob Frey
     1 × Charlie Gers > David Rosenfeld > L.A. Nik
     1 × Charlie Gers > David Rosenfeld > Raymond Dehn
     1 × Charlie Gers > Gregg A. Iverson > David Rosenfeld
     1 × Charlie Gers > Ian Simpson > David John Wilson
     1 × Charlie Gers > Ian Simpson > David Rosenfeld
     1 × Charlie Gers > Ian Simpson > Nekima Levy-Pounds
     1 × Charlie Gers > Jacob Frey > Troy Benjegerdes
     1 × Charlie Gers > Jacob Frey > Undeclared Write-ins
     1 × Charlie Gers > L.A. Nik > Al Flowers
     1 × Charlie Gers > Nekima Levy-Pounds
     1 × Charlie Gers > Nekima Levy-Pounds > Betsy Hodges
     1 × Charlie Gers > Nekima Levy-Pounds > Gregg A. Iverson
     1 × Charlie Gers > Nekima Levy-Pounds > L.A. Nik
     1 × Charlie Gers > Nekima Levy-Pounds > Ronald Lischeid
     1 × Charlie Gers > Raymond Dehn > Al Flowers
     1 × Charlie Gers > Raymond Dehn > Captain Jack Sparrow
     1 × Charlie Gers > Raymond Dehn > Ian Simpson
     1 × Charlie Gers > Raymond Dehn > Ronald Lischeid
     1 × Charlie Gers > Ronald Lischeid > David Rosenfeld
     1 × Charlie Gers > Ronald Lischeid > Nekima Levy-Pounds
     1 × Charlie Gers > Ronald Lischeid > Raymond Dehn
     1 × Charlie Gers > Troy Benjegerdes > Captain Jack Sparrow
     1 × Charlie Gers > Troy Benjegerdes > David John Wilson
     1 × Charlie Gers > Troy Benjegerdes > Ian Simpson
     1 × Charlie Gers > Troy Benjegerdes > Jacob Frey
     1 × Charlie Gers > Troy Benjegerdes > L.A. Nik
     1 × Charlie Gers > Troy Benjegerdes > Raymond Dehn
     1 × Charlie Gers > Troy Benjegerdes > Tom Hoch
     1 × Charlie Gers > Undeclared Write-ins > Jacob Frey
     1 × Christopher Zimmerman > Nekima Levy-Pounds > Raymond Dehn
     1 × David John Wilson > Al Flowers > Captain Jack Sparrow
     1 × David John Wilson > Al Flowers > David Rosenfeld
     1 × David John Wilson > Al Flowers > Ian Simpson
     1 × David John Wilson > Al Flowers > Troy Benjegerdes
     1 × David John Wilson > Aswar Rahman
     1 × David John Wilson > Aswar Rahman > Betsy Hodges
     1 × David John Wilson > Aswar Rahman > David Rosenfeld
     1 × David John Wilson > Betsy Hodges > David Rosenfeld
     1 × David John Wilson > Captain Jack Sparrow > Al Flowers
     1 × David John Wilson > Captain Jack Sparrow > Aswar Rahman
     1 × David John Wilson > Captain Jack Sparrow > Betsy Hodges
     1 × David John Wilson > Captain Jack Sparrow > Gregg A. Iverson
     1 × David John Wilson > Captain Jack Sparrow > L.A. Nik
     1 × David John Wilson > Captain Jack Sparrow > Tom Hoch
     1 × David John Wilson > Charlie Gers > Al Flowers
     1 × David John Wilson > Charlie Gers > Nekima Levy-Pounds
     1 × David John Wilson > Charlie Gers > Ronald Lischeid
     1 × David John Wilson > David Rosenfeld > Al Flowers
     1 × David John Wilson > David Rosenfeld > Aswar Rahman
     1 × David John Wilson > David Rosenfeld > Captain Jack Sparrow
     1 × David John Wilson > David Rosenfeld > Charlie Gers
     1 × David John Wilson > David Rosenfeld > Troy Benjegerdes
     1 × David John Wilson > Gregg A. Iverson > Al Flowers
     1 × David John Wilson > Gregg A. Iverson > Betsy Hodges
     1 × David John Wilson > Gregg A. Iverson > Ian Simpson
     1 × David John Wilson > Ian Simpson > Betsy Hodges
     1 × David John Wilson > Ian Simpson > L.A. Nik
     1 × David John Wilson > Ian Simpson > Ronald Lischeid
     1 × David John Wilson > Jacob Frey > Charlie Gers
     1 × David John Wilson > Jacob Frey > David Rosenfeld
     1 × David John Wilson > L.A. Nik > Aswar Rahman
     1 × David John Wilson > L.A. Nik > Ian Simpson
     1 × David John Wilson > L.A. Nik > Troy Benjegerdes
     1 × David John Wilson > Nekima Levy-Pounds > Aswar Rahman
     1 × David John Wilson > Nekima Levy-Pounds > David Rosenfeld
     1 × David John Wilson > Nekima Levy-Pounds > Raymond Dehn
     1 × David John Wilson > Raymond Dehn
     1 × David John Wilson > Raymond Dehn > Aswar Rahman
     1 × David John Wilson > Raymond Dehn > Charlie Gers
     1 × David John Wilson > Raymond Dehn > Troy Benjegerdes
     1 × David John Wilson > Ronald Lischeid
     1 × David John Wilson > Ronald Lischeid > Jacob Frey
     1 × David John Wilson > Ronald Lischeid > Raymond Dehn
     1 × David John Wilson > Tom Hoch
     1 × David John Wilson > Tom Hoch > Al Flowers
     1 × David John Wilson > Tom Hoch > Aswar Rahman
     1 × David John Wilson > Tom Hoch > Charlie Gers
     1 × David John Wilson > Tom Hoch > Undeclared Write-ins
     1 × David John Wilson > Troy Benjegerdes > Betsy Hodges
     1 × David John Wilson > Troy Benjegerdes > Ian Simpson
     1 × David John Wilson > Troy Benjegerdes > Jacob Frey
     1 × David John Wilson > Troy Benjegerdes > Nekima Levy-Pounds
     1 × David John Wilson > Undeclared Write-ins
     1 × David Rosenfeld > Al Flowers
     1 × David Rosenfeld > Al Flowers > Jacob Frey
     1 × David Rosenfeld > Aswar Rahman > Gregg A. Iverson
     1 × David Rosenfeld > Aswar Rahman > Raymond Dehn
     1 × David Rosenfeld > Aswar Rahman > Ronald Lischeid
     1 × David Rosenfeld > Betsy Hodges > Charlie Gers
     1 × David Rosenfeld > Betsy Hodges > Raymond Dehn
     1 × David Rosenfeld > Betsy Hodges > Ronald Lischeid
     1 × David Rosenfeld > Captain Jack Sparrow > Aswar Rahman
     1 × David Rosenfeld > Captain Jack Sparrow > Ronald Lischeid
     1 × David Rosenfeld > Captain Jack Sparrow > Tom Hoch
     1 × David Rosenfeld > Captain Jack Sparrow > Undeclared Write-ins
     1 × David Rosenfeld > Charlie Gers
     1 × David Rosenfeld > Charlie Gers > L.A. Nik
     1 × David Rosenfeld > Charlie Gers > Raymond Dehn
     1 × David Rosenfeld > Charlie Gers > Tom Hoch
     1 × David Rosenfeld > David John Wilson > Betsy Hodges
     1 × David Rosenfeld > David John Wilson > L.A. Nik
     1 × David Rosenfeld > Gregg A. Iverson > Al Flowers
     1 × David Rosenfeld > Gregg A. Iverson > Captain Jack Sparrow
     1 × David Rosenfeld > Gregg A. Iverson > Jacob Frey
     1 × David Rosenfeld > Gregg A. Iverson > Raymond Dehn
     1 × David Rosenfeld > Ian Simpson
     1 × David Rosenfeld > Ian Simpson > Betsy Hodges
     1 × David Rosenfeld > Ian Simpson > David John Wilson
     1 × David Rosenfeld > Ian Simpson > Raymond Dehn
     1 × David Rosenfeld > Ian Simpson > Troy Benjegerdes
     1 × David Rosenfeld > Jacob Frey > Aswar Rahman
     1 × David Rosenfeld > Jacob Frey > Captain Jack Sparrow
     1 × David Rosenfeld > Jacob Frey > David John Wilson
     1 × David Rosenfeld > Jacob Frey > Undeclared Write-ins
     1 × David Rosenfeld > L.A. Nik
     1 × David Rosenfeld > L.A. Nik > Al Flowers
     1 × David Rosenfeld > L.A. Nik > Aswar Rahman
     1 × David Rosenfeld > L.A. Nik > Betsy Hodges
     1 × David Rosenfeld > L.A. Nik > Charlie Gers
     1 × David Rosenfeld > L.A. Nik > Tom Hoch
     1 × David Rosenfeld > L.A. Nik > Undeclared Write-ins
     1 × David Rosenfeld > Nekima Levy-Pounds > Al Flowers
     1 × David Rosenfeld > Nekima Levy-Pounds > L.A. Nik
     1 × David Rosenfeld > Nekima Levy-Pounds > Ronald Lischeid
     1 × David Rosenfeld > Nekima Levy-Pounds > Undeclared Write-ins
     1 × David Rosenfeld > Raymond Dehn > Al Flowers
     1 × David Rosenfeld > Raymond Dehn > Aswar Rahman
     1 × David Rosenfeld > Raymond Dehn > Charlie Gers
     1 × David Rosenfeld > Raymond Dehn > Gregg A. Iverson
     1 × David Rosenfeld > Ronald Lischeid > Betsy Hodges
     1 × David Rosenfeld > Ronald Lischeid > Charlie Gers
     1 × David Rosenfeld > Ronald Lischeid > Gregg A. Iverson
     1 × David Rosenfeld > Ronald Lischeid > Ian Simpson
     1 × David Rosenfeld > Ronald Lischeid > Jacob Frey
     1 × David Rosenfeld > Ronald Lischeid > Tom Hoch
     1 × David Rosenfeld > Tom Hoch > Aswar Rahman
     1 × David Rosenfeld > Tom Hoch > Charlie Gers
     1 × David Rosenfeld > Tom Hoch > Gregg A. Iverson
     1 × David Rosenfeld > Troy Benjegerdes > Gregg A. Iverson
     1 × David Rosenfeld > Troy Benjegerdes > Ian Simpson
     1 × David Rosenfeld > Undeclared Write-ins > Tom Hoch
     1 × Gregg A. Iverson > Al Flowers > Aswar Rahman
     1 × Gregg A. Iverson > Al Flowers > Betsy Hodges
     1 × Gregg A. Iverson > Al Flowers > David John Wilson
     1 × Gregg A. Iverson > Al Flowers > Ian Simpson
     1 × Gregg A. Iverson > Al Flowers > Raymond Dehn
     1 × Gregg A. Iverson > Al Flowers > Tom Hoch
     1 × Gregg A. Iverson > Aswar Rahman > Al Flowers
     1 × Gregg A. Iverson > Aswar Rahman > Tom Hoch
     1 × Gregg A. Iverson > Betsy Hodges > Ian Simpson
     1 × Gregg A. Iverson > Betsy Hodges > L.A. Nik
     1 × Gregg A. Iverson > Captain Jack Sparrow
     1 × Gregg A. Iverson > Captain Jack Sparrow > Aswar Rahman
     1 × Gregg A. Iverson > Captain Jack Sparrow > David Rosenfeld
     1 × Gregg A. Iverson > Captain Jack Sparrow > Raymond Dehn
     1 × Gregg A. Iverson > Captain Jack Sparrow > Tom Hoch
     1 × Gregg A. Iverson > Charlie Gers > Aswar Rahman
     1 × Gregg A. Iverson > Charlie Gers > Tom Hoch
     1 × Gregg A. Iverson > Charlie Gers > Troy Benjegerdes
     1 × Gregg A. Iverson > David John Wilson > Al Flowers
     1 × Gregg A. Iverson > David John Wilson > Aswar Rahman
     1 × Gregg A. Iverson > David Rosenfeld > Aswar Rahman
     1 × Gregg A. Iverson > David Rosenfeld > Jacob Frey
     1 × Gregg A. Iverson > Ian Simpson > Betsy Hodges
     1 × Gregg A. Iverson > Ian Simpson > Ronald Lischeid
     1 × Gregg A. Iverson > Ian Simpson > Tom Hoch
     1 × Gregg A. Iverson > Ian Simpson > Troy Benjegerdes
     1 × Gregg A. Iverson > Jacob Frey > Ian Simpson
     1 × Gregg A. Iverson > Jacob Frey > Raymond Dehn
     1 × Gregg A. Iverson > L.A. Nik
     1 × Gregg A. Iverson > L.A. Nik > Betsy Hodges
     1 × Gregg A. Iverson > L.A. Nik > Captain Jack Sparrow
     1 × Gregg A. Iverson > Nekima Levy-Pounds > Al Flowers
     1 × Gregg A. Iverson > Nekima Levy-Pounds > David Rosenfeld
     1 × Gregg A. Iverson > Nekima Levy-Pounds > L.A. Nik
     1 × Gregg A. Iverson > Nekima Levy-Pounds > Tom Hoch
     1 × Gregg A. Iverson > Raymond Dehn
     1 × Gregg A. Iverson > Raymond Dehn > David Rosenfeld
     1 × Gregg A. Iverson > Raymond Dehn > L.A. Nik
     1 × Gregg A. Iverson > Raymond Dehn > Ronald Lischeid
     1 × Gregg A. Iverson > Ronald Lischeid > Al Flowers
     1 × Gregg A. Iverson > Ronald Lischeid > Betsy Hodges
     1 × Gregg A. Iverson > Ronald Lischeid > L.A. Nik
     1 × Gregg A. Iverson > Tom Hoch
     1 × Gregg A. Iverson > Tom Hoch > Aswar Rahman
     1 × Gregg A. Iverson > Tom Hoch > Charlie Gers
     1 × Gregg A. Iverson > Tom Hoch > David Rosenfeld
     1 × Gregg A. Iverson > Tom Hoch > Ronald Lischeid
     1 × Gregg A. Iverson > Tom Hoch > Troy Benjegerdes
     1 × Gregg A. Iverson > Troy Benjegerdes > Aswar Rahman
     1 × Gregg A. Iverson > Troy Benjegerdes > Jacob Frey
     1 × Gregg A. Iverson > Troy Benjegerdes > Nekima Levy-Pounds
     1 × Gregg A. Iverson > Troy Benjegerdes > Tom Hoch
     1 × Gregg A. Iverson > Undeclared Write-ins > Captain Jack Sparrow
     1 × Ian Simpson > Al Flowers
     1 × Ian Simpson > Al Flowers > Captain Jack Sparrow
     1 × Ian Simpson > Aswar Rahman > Al Flowers
     1 × Ian Simpson > Aswar Rahman > Jacob Frey
     1 × Ian Simpson > Aswar Rahman > L.A. Nik
     1 × Ian Simpson > Aswar Rahman > Nekima Levy-Pounds
     1 × Ian Simpson > Aswar Rahman > Raymond Dehn
     1 × Ian Simpson > Aswar Rahman > Troy Benjegerdes
     1 × Ian Simpson > Betsy Hodges > Captain Jack Sparrow
     1 × Ian Simpson > Betsy Hodges > Gregg A. Iverson
     1 × Ian Simpson > Betsy Hodges > Nekima Levy-Pounds
     1 × Ian Simpson > Betsy Hodges > Tom Hoch
     1 × Ian Simpson > Captain Jack Sparrow
     1 × Ian Simpson > Captain Jack Sparrow > Charlie Gers
     1 × Ian Simpson > Captain Jack Sparrow > David Rosenfeld
     1 × Ian Simpson > Captain Jack Sparrow > L.A. Nik
     1 × Ian Simpson > Captain Jack Sparrow > Raymond Dehn
     1 × Ian Simpson > Captain Jack Sparrow > Troy Benjegerdes
     1 × Ian Simpson > Charlie Gers
     1 × Ian Simpson > Charlie Gers > Al Flowers
     1 × Ian Simpson > Charlie Gers > Captain Jack Sparrow
     1 × Ian Simpson > Charlie Gers > David Rosenfeld
     1 × Ian Simpson > Charlie Gers > Jacob Frey
     1 × Ian Simpson > Charlie Gers > Tom Hoch
     1 × Ian Simpson > David John Wilson > Charlie Gers
     1 × Ian Simpson > Gregg A. Iverson > Captain Jack Sparrow
     1 × Ian Simpson > Jacob Frey > Betsy Hodges
     1 × Ian Simpson > Jacob Frey > Captain Jack Sparrow
     1 × Ian Simpson > Jacob Frey > Charlie Gers
     1 × Ian Simpson > Jacob Frey > Raymond Dehn
     1 × Ian Simpson > L.A. Nik
     1 × Ian Simpson > L.A. Nik > Charlie Gers
     1 × Ian Simpson > L.A. Nik > David Rosenfeld
     1 × Ian Simpson > L.A. Nik > Jacob Frey
     1 × Ian Simpson > L.A. Nik > Raymond Dehn
     1 × Ian Simpson > Nekima Levy-Pounds > Betsy Hodges
     1 × Ian Simpson > Nekima Levy-Pounds > Charlie Gers
     1 × Ian Simpson > Nekima Levy-Pounds > Tom Hoch
     1 × Ian Simpson > Nekima Levy-Pounds > Troy Benjegerdes
     1 × Ian Simpson > Raymond Dehn > Gregg A. Iverson
     1 × Ian Simpson > Raymond Dehn > Nekima Levy-Pounds
     1 × Ian Simpson > Ronald Lischeid > Betsy Hodges
     1 × Ian Simpson > Ronald Lischeid > Captain Jack Sparrow
     1 × Ian Simpson > Ronald Lischeid > Charlie Gers
     1 × Ian Simpson > Ronald Lischeid > David John Wilson
     1 × Ian Simpson > Ronald Lischeid > David Rosenfeld
     1 × Ian Simpson > Ronald Lischeid > Jacob Frey
     1 × Ian Simpson > Ronald Lischeid > L.A. Nik
     1 × Ian Simpson > Tom Hoch > Al Flowers
     1 × Ian Simpson > Tom Hoch > Aswar Rahman
     1 × Ian Simpson > Tom Hoch > Betsy Hodges
     1 × Ian Simpson > Tom Hoch > David John Wilson
     1 × Ian Simpson > Tom Hoch > David Rosenfeld
     1 × Ian Simpson > Troy Benjegerdes
     1 × Ian Simpson > Troy Benjegerdes > Aswar Rahman
     1 × Ian Simpson > Troy Benjegerdes > L.A. Nik
     1 × Ian Simpson > Troy Benjegerdes > Tom Hoch
     1 × Jacob Frey > Al Flowers > Undeclared Write-ins
     1 × Jacob Frey > Aswar Rahman > Ian Simpson
     1 × Jacob Frey > Charlie Gers > Al Flowers
     1 × Jacob Frey > Charlie Gers > Troy Benjegerdes
     1 × Jacob Frey > David John Wilson > Aswar Rahman
     1 × Jacob Frey > David John Wilson > Gregg A. Iverson
     1 × Jacob Frey > David John Wilson > L.A. Nik
     1 × Jacob Frey > David Rosenfeld > Al Flowers
     1 × Jacob Frey > Gregg A. Iverson > Undeclared Write-ins
     1 × Jacob Frey > Ian Simpson > Al Flowers
     1 × Jacob Frey > Ian Simpson > Aswar Rahman
     1 × Jacob Frey > Ian Simpson > Charlie Gers
     1 × Jacob Frey > Ian Simpson > Gregg A. Iverson
     1 × Jacob Frey > Ian Simpson > Nekima Levy-Pounds
     1 × Jacob Frey > Ian Simpson > Raymond Dehn
     1 × Jacob Frey > Ian Simpson > Ronald Lischeid
     1 × Jacob Frey > Ian Simpson > Undeclared Write-ins
     1 × Jacob Frey > L.A. Nik > Aswar Rahman
     1 × Jacob Frey > L.A. Nik > Ian Simpson
     1 × Jacob Frey > L.A. Nik > Troy Benjegerdes
     1 × Jacob Frey > Ronald Lischeid > Aswar Rahman
     1 × Jacob Frey > Ronald Lischeid > Raymond Dehn
     1 × Jacob Frey > Ronald Lischeid > Undeclared Write-ins
     1 × Jacob Frey > Troy Benjegerdes > Aswar Rahman
     1 × Jacob Frey > Troy Benjegerdes > Ronald Lischeid
     1 × Jacob Frey > Undeclared Write-ins > Charlie Gers
     1 × Jacob Frey > Undeclared Write-ins > Nekima Levy-Pounds
     1 × Jacob Frey > Undeclared Write-ins > Tom Hoch
     1 × L.A. Nik > Al Flowers > Betsy Hodges
     1 × L.A. Nik > Al Flowers > Charlie Gers
     1 × L.A. Nik > Al Flowers > Ronald Lischeid
     1 × L.A. Nik > Aswar Rahman > Al Flowers
     1 × L.A. Nik > Aswar Rahman > Captain Jack Sparrow
     1 × L.A. Nik > Aswar Rahman > Charlie Gers
     1 × L.A. Nik > Aswar Rahman > David John Wilson
     1 × L.A. Nik > Aswar Rahman > Jacob Frey
     1 × L.A. Nik > Aswar Rahman > Tom Hoch
     1 × L.A. Nik > Betsy Hodges > Aswar Rahman
     1 × L.A. Nik > Betsy Hodges > David John Wilson
     1 × L.A. Nik > Betsy Hodges > Gregg A. Iverson
     1 × L.A. Nik > Betsy Hodges > Ian Simpson
     1 × L.A. Nik > Betsy Hodges > Nekima Levy-Pounds
     1 × L.A. Nik > Betsy Hodges > Raymond Dehn
     1 × L.A. Nik > Betsy Hodges > Tom Hoch
     1 × L.A. Nik > Captain Jack Sparrow > Al Flowers
     1 × L.A. Nik > Captain Jack Sparrow > David Rosenfeld
     1 × L.A. Nik > Captain Jack Sparrow > Jacob Frey
     1 × L.A. Nik > Captain Jack Sparrow > Nekima Levy-Pounds
     1 × L.A. Nik > Charlie Gers > Al Flowers
     1 × L.A. Nik > Charlie Gers > Betsy Hodges
     1 × L.A. Nik > Charlie Gers > Raymond Dehn
     1 × L.A. Nik > David John Wilson > Betsy Hodges
     1 × L.A. Nik > David John Wilson > David Rosenfeld
     1 × L.A. Nik > David John Wilson > Ian Simpson
     1 × L.A. Nik > David John Wilson > Jacob Frey
     1 × L.A. Nik > David John Wilson > Troy Benjegerdes
     1 × L.A. Nik > David Rosenfeld
     1 × L.A. Nik > David Rosenfeld > Betsy Hodges
     1 × L.A. Nik > David Rosenfeld > David John Wilson
     1 × L.A. Nik > David Rosenfeld > Raymond Dehn
     1 × L.A. Nik > Gregg A. Iverson > Tom Hoch
     1 × L.A. Nik > Ian Simpson
     1 × L.A. Nik > Ian Simpson > Gregg A. Iverson
     1 × L.A. Nik > Jacob Frey > Betsy Hodges
     1 × L.A. Nik > Nekima Levy-Pounds > Captain Jack Sparrow
     1 × L.A. Nik > Nekima Levy-Pounds > Ronald Lischeid
     1 × L.A. Nik > Nekima Levy-Pounds > Tom Hoch
     1 × L.A. Nik > Raymond Dehn > Jacob Frey
     1 × L.A. Nik > Ronald Lischeid > Al Flowers
     1 × L.A. Nik > Ronald Lischeid > David John Wilson
     1 × L.A. Nik > Tom Hoch > Aswar Rahman
     1 × L.A. Nik > Tom Hoch > David John Wilson
     1 × L.A. Nik > Tom Hoch > David Rosenfeld
     1 × L.A. Nik > Tom Hoch > Gregg A. Iverson
     1 × L.A. Nik > Tom Hoch > Ian Simpson
     1 × L.A. Nik > Tom Hoch > Troy Benjegerdes
     1 × L.A. Nik > Troy Benjegerdes > Captain Jack Sparrow
     1 × L.A. Nik > Troy Benjegerdes > Jacob Frey
     1 × L.A. Nik > Troy Benjegerdes > Tom Hoch
     1 × Nekima Levy-Pounds > Al Flowers > Theron Preston Washington
     1 × Nekima Levy-Pounds > Captain Jack Sparrow > Ronald Lischeid
     1 × Nekima Levy-Pounds > Captain Jack Sparrow > Troy Benjegerdes
     1 × Nekima Levy-Pounds > Charlie Gers > Al Flowers
     1 × Nekima Levy-Pounds > Charlie Gers > Aswar Rahman
     1 × Nekima Levy-Pounds > Charlie Gers > David Rosenfeld
     1 × Nekima Levy-Pounds > Charlie Gers > Gregg A. Iverson
     1 × Nekima Levy-Pounds > Charlie Gers > L.A. Nik
     1 × Nekima Levy-Pounds > Charlie Gers > Tom Hoch
     1 × Nekima Levy-Pounds > Charlie Gers > Undeclared Write-ins
     1 × Nekima Levy-Pounds > David John Wilson > Al Flowers
     1 × Nekima Levy-Pounds > David John Wilson > Aswar Rahman
     1 × Nekima Levy-Pounds > David John Wilson > David Rosenfeld
     1 × Nekima Levy-Pounds > David John Wilson > Ian Simpson
     1 × Nekima Levy-Pounds > David John Wilson > L.A. Nik
     1 × Nekima Levy-Pounds > David John Wilson > Ronald Lischeid
     1 × Nekima Levy-Pounds > David John Wilson > Troy Benjegerdes
     1 × Nekima Levy-Pounds > David Rosenfeld > L.A. Nik
     1 × Nekima Levy-Pounds > Gregg A. Iverson > Captain Jack Sparrow
     1 × Nekima Levy-Pounds > Gregg A. Iverson > David John Wilson
     1 × Nekima Levy-Pounds > Gregg A. Iverson > Ian Simpson
     1 × Nekima Levy-Pounds > Gregg A. Iverson > L.A. Nik
     1 × Nekima Levy-Pounds > Gregg A. Iverson > Ronald Lischeid
     1 × Nekima Levy-Pounds > Ian Simpson
     1 × Nekima Levy-Pounds > Ian Simpson > Al Flowers
     1 × Nekima Levy-Pounds > Ian Simpson > Aswar Rahman
     1 × Nekima Levy-Pounds > Ian Simpson > Betsy Hodges
     1 × Nekima Levy-Pounds > Ian Simpson > Jacob Frey
     1 × Nekima Levy-Pounds > Ian Simpson > L.A. Nik
     1 × Nekima Levy-Pounds > Ian Simpson > Tom Hoch
     1 × Nekima Levy-Pounds > Ian Simpson > Undeclared Write-ins
     1 × Nekima Levy-Pounds > L.A. Nik > David Rosenfeld
     1 × Nekima Levy-Pounds > L.A. Nik > Gregg A. Iverson
     1 × Nekima Levy-Pounds > L.A. Nik > Ian Simpson
     1 × Nekima Levy-Pounds > L.A. Nik > Raymond Dehn
     1 × Nekima Levy-Pounds > L.A. Nik > Ronald Lischeid
     1 × Nekima Levy-Pounds > L.A. Nik > Tom Hoch
     1 × Nekima Levy-Pounds > Ronald Lischeid > Al Flowers
     1 × Nekima Levy-Pounds > Ronald Lischeid > Gregg A. Iverson
     1 × Nekima Levy-Pounds > Ronald Lischeid > Ian Simpson
     1 × Nekima Levy-Pounds > Ronald Lischeid > Raymond Dehn
     1 × Nekima Levy-Pounds > Ronald Lischeid > Troy Benjegerdes
     1 × Nekima Levy-Pounds > Ronald Lischeid > Undeclared Write-ins
     1 × Nekima Levy-Pounds > Troy Benjegerdes
     1 × Nekima Levy-Pounds > Troy Benjegerdes > Al Flowers
     1 × Nekima Levy-Pounds > Troy Benjegerdes > Charlie Gers
     1 × Nekima Levy-Pounds > Troy Benjegerdes > David John Wilson
     1 × Nekima Levy-Pounds > Troy Benjegerdes > Raymond Dehn
     1 × Nekima Levy-Pounds > Troy Benjegerdes > Tom Hoch
     1 × Nekima Levy-Pounds > Undeclared Write-ins > Jacob Frey
     1 × Raymond Dehn > Al Flowers > L.A. Nik
     1 × Raymond Dehn > Aswar Rahman > Ian Simpson
     1 × Raymond Dehn > Aswar Rahman > Troy Benjegerdes
     1 × Raymond Dehn > Captain Jack Sparrow > Charlie Gers
     1 × Raymond Dehn > Captain Jack Sparrow > Ronald Lischeid
     1 × Raymond Dehn > Captain Jack Sparrow > Troy Benjegerdes
     1 × Raymond Dehn > Charlie Gers > Gregg A. Iverson
     1 × Raymond Dehn > Charlie Gers > Ian Simpson
     1 × Raymond Dehn > Charlie Gers > Ronald Lischeid
     1 × Raymond Dehn > Charlie Gers > Tom Hoch
     1 × Raymond Dehn > Charlie Gers > Undeclared Write-ins
     1 × Raymond Dehn > David Rosenfeld > Gregg A. Iverson
     1 × Raymond Dehn > Gregg A. Iverson > Aswar Rahman
     1 × Raymond Dehn > Gregg A. Iverson > Captain Jack Sparrow
     1 × Raymond Dehn > Gregg A. Iverson > L.A. Nik
     1 × Raymond Dehn > Gregg A. Iverson > Troy Benjegerdes
     1 × Raymond Dehn > Ian Simpson
     1 × Raymond Dehn > Ian Simpson > Al Flowers
     1 × Raymond Dehn > Ian Simpson > Betsy Hodges
     1 × Raymond Dehn > Ian Simpson > Charlie Gers
     1 × Raymond Dehn > Ian Simpson > David John Wilson
     1 × Raymond Dehn > Ian Simpson > Gregg A. Iverson
     1 × Raymond Dehn > Ian Simpson > Nekima Levy-Pounds
     1 × Raymond Dehn > L.A. Nik > Al Flowers
     1 × Raymond Dehn > L.A. Nik > Charlie Gers
     1 × Raymond Dehn > L.A. Nik > Nekima Levy-Pounds
     1 × Raymond Dehn > Ronald Lischeid > Charlie Gers
     1 × Raymond Dehn > Ronald Lischeid > David John Wilson
     1 × Raymond Dehn > Ronald Lischeid > David Rosenfeld
     1 × Raymond Dehn > Ronald Lischeid > Tom Hoch
     1 × Raymond Dehn > Ronald Lischeid > Troy Benjegerdes
     1 × Raymond Dehn > Troy Benjegerdes > Aswar Rahman
     1 × Raymond Dehn > Troy Benjegerdes > Captain Jack Sparrow
     1 × Raymond Dehn > Troy Benjegerdes > Charlie Gers
     1 × Raymond Dehn > Troy Benjegerdes > David Rosenfeld
     1 × Raymond Dehn > Troy Benjegerdes > Gregg A. Iverson
     1 × Raymond Dehn > Troy Benjegerdes > L.A. Nik
     1 × Raymond Dehn > Troy Benjegerdes > Ronald Lischeid
     1 × Raymond Dehn > Troy Benjegerdes > Tom Hoch
     1 × Raymond Dehn > Undeclared Write-ins > Captain Jack Sparrow
     1 × Raymond Dehn > Undeclared Write-ins > Nekima Levy-Pounds
     1 × Ronald Lischeid > Al Flowers > L.A. Nik
     1 × Ronald Lischeid > Aswar Rahman
     1 × Ronald Lischeid > Aswar Rahman > Betsy Hodges
     1 × Ronald Lischeid > Aswar Rahman > Charlie Gers
     1 × Ronald Lischeid > Aswar Rahman > Ian Simpson
     1 × Ronald Lischeid > Aswar Rahman > Jacob Frey
     1 × Ronald Lischeid > Aswar Rahman > Nekima Levy-Pounds
     1 × Ronald Lischeid > Aswar Rahman > Raymond Dehn
     1 × Ronald Lischeid > Aswar Rahman > Tom Hoch
     1 × Ronald Lischeid > Betsy Hodges > Charlie Gers
     1 × Ronald Lischeid > Betsy Hodges > David Rosenfeld
     1 × Ronald Lischeid > Betsy Hodges > Jacob Frey
     1 × Ronald Lischeid > Betsy Hodges > L.A. Nik
     1 × Ronald Lischeid > Betsy Hodges > Nekima Levy-Pounds
     1 × Ronald Lischeid > Betsy Hodges > Raymond Dehn
     1 × Ronald Lischeid > Captain Jack Sparrow > Aswar Rahman
     1 × Ronald Lischeid > Captain Jack Sparrow > Jacob Frey
     1 × Ronald Lischeid > Captain Jack Sparrow > Raymond Dehn
     1 × Ronald Lischeid > Captain Jack Sparrow > Troy Benjegerdes
     1 × Ronald Lischeid > Charlie Gers > David John Wilson
     1 × Ronald Lischeid > Charlie Gers > David Rosenfeld
     1 × Ronald Lischeid > Charlie Gers > Gregg A. Iverson
     1 × Ronald Lischeid > Charlie Gers > Ian Simpson
     1 × Ronald Lischeid > Charlie Gers > Nekima Levy-Pounds
     1 × Ronald Lischeid > David John Wilson
     1 × Ronald Lischeid > David John Wilson > David Rosenfeld
     1 × Ronald Lischeid > David John Wilson > L.A. Nik
     1 × Ronald Lischeid > David Rosenfeld > Al Flowers
     1 × Ronald Lischeid > David Rosenfeld > Aswar Rahman
     1 × Ronald Lischeid > David Rosenfeld > Captain Jack Sparrow
     1 × Ronald Lischeid > David Rosenfeld > Charlie Gers
     1 × Ronald Lischeid > David Rosenfeld > David John Wilson
     1 × Ronald Lischeid > David Rosenfeld > Tom Hoch
     1 × Ronald Lischeid > Gregg A. Iverson > Charlie Gers
     1 × Ronald Lischeid > Gregg A. Iverson > David John Wilson
     1 × Ronald Lischeid > Gregg A. Iverson > L.A. Nik
     1 × Ronald Lischeid > Gregg A. Iverson > Nekima Levy-Pounds
     1 × Ronald Lischeid > Gregg A. Iverson > Raymond Dehn
     1 × Ronald Lischeid > Ian Simpson > Betsy Hodges
     1 × Ronald Lischeid > Ian Simpson > David John Wilson
     1 × Ronald Lischeid > Ian Simpson > Jacob Frey
     1 × Ronald Lischeid > Ian Simpson > Tom Hoch
     1 × Ronald Lischeid > Jacob Frey > Al Flowers
     1 × Ronald Lischeid > Jacob Frey > Betsy Hodges
     1 × Ronald Lischeid > Jacob Frey > Captain Jack Sparrow
     1 × Ronald Lischeid > Jacob Frey > Charlie Gers
     1 × Ronald Lischeid > Jacob Frey > L.A. Nik
     1 × Ronald Lischeid > L.A. Nik > Captain Jack Sparrow
     1 × Ronald Lischeid > L.A. Nik > Troy Benjegerdes
     1 × Ronald Lischeid > L.A. Nik > Undeclared Write-ins
     1 × Ronald Lischeid > Nekima Levy-Pounds
     1 × Ronald Lischeid > Nekima Levy-Pounds > Captain Jack Sparrow
     1 × Ronald Lischeid > Nekima Levy-Pounds > Tom Hoch
     1 × Ronald Lischeid > Raymond Dehn > Al Flowers
     1 × Ronald Lischeid > Raymond Dehn > Betsy Hodges
     1 × Ronald Lischeid > Raymond Dehn > Captain Jack Sparrow
     1 × Ronald Lischeid > Raymond Dehn > Charlie Gers
     1 × Ronald Lischeid > Raymond Dehn > David John Wilson
     1 × Ronald Lischeid > Raymond Dehn > Gregg A. Iverson
     1 × Ronald Lischeid > Raymond Dehn > Nekima Levy-Pounds
     1 × Ronald Lischeid > Tom Hoch > Al Flowers
     1 × Ronald Lischeid > Tom Hoch > Aswar Rahman
     1 × Ronald Lischeid > Tom Hoch > David John Wilson
     1 × Ronald Lischeid > Tom Hoch > David Rosenfeld
     1 × Ronald Lischeid > Tom Hoch > L.A. Nik
     1 × Ronald Lischeid > Tom Hoch > Troy Benjegerdes
     1 × Ronald Lischeid > Troy Benjegerdes > Betsy Hodges
     1 × Ronald Lischeid > Troy Benjegerdes > Captain Jack Sparrow
     1 × Ronald Lischeid > Troy Benjegerdes > Gregg A. Iverson
     1 × Ronald Lischeid > Troy Benjegerdes > Ian Simpson
     1 × Ronald Lischeid > Troy Benjegerdes > Jacob Frey
     1 × Ronald Lischeid > Troy Benjegerdes > Raymond Dehn
     1 × Tom Hoch > Al Flowers > Ian Simpson
     1 × Tom Hoch > Al Flowers > Undeclared Write-ins
     1 × Tom Hoch > David John Wilson > Ian Simpson
     1 × Tom Hoch > David John Wilson > Undeclared Write-ins
     1 × Tom Hoch > David Rosenfeld > Troy Benjegerdes
     1 × Tom Hoch > Gregg A. Iverson > David John Wilson
     1 × Tom Hoch > Ian Simpson > Al Flowers
     1 × Tom Hoch > Ian Simpson > Charlie Gers
     1 × Tom Hoch > Ian Simpson > David Rosenfeld
     1 × Tom Hoch > Ian Simpson > Nekima Levy-Pounds
     1 × Tom Hoch > Ian Simpson > Raymond Dehn
     1 × Tom Hoch > Ian Simpson > Troy Benjegerdes
     1 × Tom Hoch > Ian Simpson > Undeclared Write-ins
     1 × Tom Hoch > Troy Benjegerdes > Al Flowers
     1 × Tom Hoch > Troy Benjegerdes > David John Wilson
     1 × Tom Hoch > Troy Benjegerdes > Ian Simpson
     1 × Tom Hoch > Troy Benjegerdes > Nekima Levy-Pounds
     1 × Tom Hoch > Troy Benjegerdes > Ronald Lischeid
     1 × Tom Hoch > Undeclared Write-ins > Al Flowers
     1 × Tom Hoch > Undeclared Write-ins > Raymond Dehn
     1 × Troy Benjegerdes > Al Flowers
     1 × Troy Benjegerdes > Al Flowers > Aswar Rahman
     1 × Troy Benjegerdes > Al Flowers > Betsy Hodges
     1 × Troy Benjegerdes > Al Flowers > Nekima Levy-Pounds
     1 × Troy Benjegerdes > Al Flowers > Raymond Dehn
     1 × Troy Benjegerdes > Al Flowers > Ronald Lischeid
     1 × Troy Benjegerdes > Aswar Rahman > David John Wilson
     1 × Troy Benjegerdes > Aswar Rahman > Raymond Dehn
     1 × Troy Benjegerdes > Aswar Rahman > Tom Hoch
     1 × Troy Benjegerdes > Betsy Hodges > Aswar Rahman
     1 × Troy Benjegerdes > Betsy Hodges > Gregg A. Iverson
     1 × Troy Benjegerdes > Betsy Hodges > Ian Simpson
     1 × Troy Benjegerdes > Betsy Hodges > Raymond Dehn
     1 × Troy Benjegerdes > Captain Jack Sparrow > David John Wilson
     1 × Troy Benjegerdes > Captain Jack Sparrow > L.A. Nik
     1 × Troy Benjegerdes > Captain Jack Sparrow > Nekima Levy-Pounds
     1 × Troy Benjegerdes > Captain Jack Sparrow > Raymond Dehn
     1 × Troy Benjegerdes > Captain Jack Sparrow > Tom Hoch
     1 × Troy Benjegerdes > Charlie Gers > Betsy Hodges
     1 × Troy Benjegerdes > Charlie Gers > Captain Jack Sparrow
     1 × Troy Benjegerdes > David John Wilson
     1 × Troy Benjegerdes > David John Wilson > Betsy Hodges
     1 × Troy Benjegerdes > David John Wilson > Captain Jack Sparrow
     1 × Troy Benjegerdes > David John Wilson > Charlie Gers
     1 × Troy Benjegerdes > David John Wilson > L.A. Nik
     1 × Troy Benjegerdes > David Rosenfeld
     1 × Troy Benjegerdes > David Rosenfeld > Charlie Gers
     1 × Troy Benjegerdes > David Rosenfeld > Jacob Frey
     1 × Troy Benjegerdes > Gregg A. Iverson > Aswar Rahman
     1 × Troy Benjegerdes > Gregg A. Iverson > Tom Hoch
     1 × Troy Benjegerdes > Ian Simpson > Captain Jack Sparrow
     1 × Troy Benjegerdes > Ian Simpson > Ronald Lischeid
     1 × Troy Benjegerdes > Jacob Frey > Al Flowers
     1 × Troy Benjegerdes > Jacob Frey > Captain Jack Sparrow
     1 × Troy Benjegerdes > Jacob Frey > Raymond Dehn
     1 × Troy Benjegerdes > Jacob Frey > Ronald Lischeid
     1 × Troy Benjegerdes > L.A. Nik > Betsy Hodges
     1 × Troy Benjegerdes > L.A. Nik > David Rosenfeld
     1 × Troy Benjegerdes > L.A. Nik > Ronald Lischeid
     1 × Troy Benjegerdes > Nekima Levy-Pounds > Aswar Rahman
     1 × Troy Benjegerdes > Nekima Levy-Pounds > Jacob Frey
     1 × Troy Benjegerdes > Raymond Dehn > Al Flowers
     1 × Troy Benjegerdes > Raymond Dehn > David John Wilson
     1 × Troy Benjegerdes > Raymond Dehn > Gregg A. Iverson
     1 × Troy Benjegerdes > Raymond Dehn > Ian Simpson
     1 × Troy Benjegerdes > Raymond Dehn > L.A. Nik
     1 × Troy Benjegerdes > Raymond Dehn > Tom Hoch
     1 × Troy Benjegerdes > Ronald Lischeid > Al Flowers
     1 × Troy Benjegerdes > Ronald Lischeid > Captain Jack Sparrow
     1 × Troy Benjegerdes > Ronald Lischeid > Ian Simpson
     1 × Troy Benjegerdes > Ronald Lischeid > Tom Hoch
     1 × Troy Benjegerdes > Tom Hoch > Aswar Rahman
     1 × Troy Benjegerdes > Tom Hoch > Betsy Hodges
     1 × Troy Benjegerdes > Tom Hoch > David John Wilson
     1 × Troy Benjegerdes > Tom Hoch > Gregg A. Iverson
     1 × Troy Benjegerdes > Tom Hoch > Nekima Levy-Pounds
     1 × Troy Benjegerdes > Undeclared Write-ins > Ronald Lischeid
     1 × Undeclared Write-ins > Betsy Hodges
     1 × Undeclared Write-ins > Betsy Hodges > Captain Jack Sparrow
     1 × Undeclared Write-ins > Betsy Hodges > Ian Simpson
     1 × Undeclared Write-ins > Betsy Hodges > Nekima Levy-Pounds
     1 × Undeclared Write-ins > Betsy Hodges > Raymond Dehn
     1 × Undeclared Write-ins > Betsy Hodges > Tom Hoch
     1 × Undeclared Write-ins > Captain Jack Sparrow > Betsy Hodges
     1 × Undeclared Write-ins > Captain Jack Sparrow > David John Wilson
     1 × Undeclared Write-ins > Captain Jack Sparrow > David Rosenfeld
     1 × Undeclared Write-ins > Charlie Gers > Jacob Frey
     1 × Undeclared Write-ins > Charlie Gers > L.A. Nik
     1 × Undeclared Write-ins > Charlie Gers > Ronald Lischeid
     1 × Undeclared Write-ins > David John Wilson > Captain Jack Sparrow
     1 × Undeclared Write-ins > David Rosenfeld
     1 × Undeclared Write-ins > David Rosenfeld > Ian Simpson
     1 × Undeclared Write-ins > David Rosenfeld > Troy Benjegerdes
     1 × Undeclared Write-ins > Gregg A. Iverson > Tom Hoch
     1 × Undeclared Write-ins > Gregg A. Iverson > Troy Benjegerdes
     1 × Undeclared Write-ins > Jacob Frey
     1 × Undeclared Write-ins > Jacob Frey > Al Flowers
     1 × Undeclared Write-ins > Jacob Frey > Aswar Rahman
     1 × Undeclared Write-ins > Nekima Levy-Pounds > Al Flowers
     1 × Undeclared Write-ins > Nekima Levy-Pounds > David John Wilson
     1 × Undeclared Write-ins > Raymond Dehn > Jacob Frey
     1 × Undeclared Write-ins > Tom Hoch > Al Flowers
     1 × Undeclared Write-ins > Tom Hoch > Aswar Rahman
     1 × Undeclared Write-ins > Tom Hoch > Betsy Hodges
     1 × Undeclared Write-ins > Troy Benjegerdes > Ronald Lischeid

Round-Robin — every pair, head-to-head (For – Against):
   Jacob Frey                 beats Raymond Dehn                46704 – 34970
   Jacob Frey                 beats Nekima Levy-Pounds          47368 – 35519
   Jacob Frey                 beats Betsy Hodges                45825 – 37703
   Jacob Frey                 beats Tom Hoch                    41663 – 31223
   Jacob Frey                 beats Charlie Gers                54470 –  2395
   Jacob Frey                 beats Aswar Rahman                54347 –  3903
   Jacob Frey                 beats Captain Jack Sparrow        54604 –  2931
   Jacob Frey                 beats Gregg A. Iverson            54545 –  1534
   Jacob Frey                 beats Al Flowers                  54441 –  4321
   Jacob Frey                 beats David Rosenfeld             54640 –  2106
   Jacob Frey                 beats L.A. Nik                    54602 –  1879
   Jacob Frey                 beats David John Wilson           54680 –  1236
   Jacob Frey                 beats Undeclared Write-ins        54738 –   507
   Jacob Frey                 beats Ronald Lischeid             54681 –  1109
   Jacob Frey                 beats Troy Benjegerdes            54708 –   625
   Jacob Frey                 beats Ian Simpson                 54725 –   697
   Jacob Frey                 beats Christopher Zimmerman       54757 –     3
   Jacob Frey                 beats Theron Preston Washington   54757 –     1
   Raymond Dehn               beats Nekima Levy-Pounds          34120 – 29962
   Betsy Hodges               beats Raymond Dehn                37513 – 35133
   Tom Hoch                   beats Raymond Dehn                40644 – 36737
   Raymond Dehn               beats Charlie Gers                43999 –  2883
   Raymond Dehn               beats Aswar Rahman                43754 –  4298
   Raymond Dehn               beats Captain Jack Sparrow        43991 –  3275
   Raymond Dehn               beats Gregg A. Iverson            43984 –  2510
   Raymond Dehn               beats Al Flowers                  43719 –  4229
   Raymond Dehn               beats David Rosenfeld             43906 –  1662
   Raymond Dehn               beats L.A. Nik                    44051 –  2146
   Raymond Dehn               beats David John Wilson           44063 –  1386
   Raymond Dehn               beats Undeclared Write-ins        44085 –   537
   Raymond Dehn               beats Ronald Lischeid             44056 –  1185
   Raymond Dehn               beats Troy Benjegerdes            44043 –   677
   Raymond Dehn               beats Ian Simpson                 44074 –   732
   Raymond Dehn               beats Christopher Zimmerman       44093 –     3
   Raymond Dehn               beats Theron Preston Washington   44094 –     1
   Betsy Hodges               beats Nekima Levy-Pounds          38080 – 33529
   Tom Hoch                   beats Nekima Levy-Pounds          41620 – 37656
   Nekima Levy-Pounds         beats Charlie Gers                43888 –  2891
   Nekima Levy-Pounds         beats Aswar Rahman                43551 –  3719
   Nekima Levy-Pounds         beats Captain Jack Sparrow        43844 –  3228
   Nekima Levy-Pounds         beats Gregg A. Iverson            43835 –  2371
   Nekima Levy-Pounds         beats Al Flowers                  43557 –  3444
   Nekima Levy-Pounds         beats David Rosenfeld             43725 –  1686
   Nekima Levy-Pounds         beats L.A. Nik                    43902 –  2173
   Nekima Levy-Pounds         beats David John Wilson           43904 –  1366
   Nekima Levy-Pounds         beats Undeclared Write-ins        43945 –   534
   Nekima Levy-Pounds         beats Ronald Lischeid             43916 –  1167
   Nekima Levy-Pounds         beats Troy Benjegerdes            43914 –   700
   Nekima Levy-Pounds         beats Ian Simpson                 43935 –   741
   Nekima Levy-Pounds         beats Christopher Zimmerman       43950 –     1
   Nekima Levy-Pounds         beats Theron Preston Washington   43951 –     0
   Betsy Hodges               beats Tom Hoch                    40900 – 39704
   Betsy Hodges               beats Charlie Gers                49756 –  2796
   Betsy Hodges               beats Aswar Rahman                49491 –  4180
   Betsy Hodges               beats Captain Jack Sparrow        49748 –  3446
   Betsy Hodges               beats Gregg A. Iverson            49669 –  1977
   Betsy Hodges               beats Al Flowers                  49417 –  4158
   Betsy Hodges               beats David Rosenfeld             49688 –  2084
   Betsy Hodges               beats L.A. Nik                    49825 –  2162
   Betsy Hodges               beats David John Wilson           49840 –  1389
   Betsy Hodges               beats Undeclared Write-ins        49875 –   570
   Betsy Hodges               beats Ronald Lischeid             49833 –  1165
   Betsy Hodges               beats Troy Benjegerdes            49852 –   671
   Betsy Hodges               beats Ian Simpson                 49865 –   733
   Betsy Hodges               beats Christopher Zimmerman       49891 –     3
   Betsy Hodges               beats Theron Preston Washington   49891 –     1
   Tom Hoch                   beats Charlie Gers                46688 –  2182
   Tom Hoch                   beats Aswar Rahman                46601 –  3879
   Tom Hoch                   beats Captain Jack Sparrow        46855 –  2828
   Tom Hoch                   beats Gregg A. Iverson            46830 –  1831
   Tom Hoch                   beats Al Flowers                  46588 –  4050
   Tom Hoch                   beats David Rosenfeld             46888 –  2150
   Tom Hoch                   beats L.A. Nik                    46832 –  1629
   Tom Hoch                   beats David John Wilson           46946 –  1153
   Tom Hoch                   beats Undeclared Write-ins        46989 –   494
   Tom Hoch                   beats Ronald Lischeid             46915 –   984
   Tom Hoch                   beats Troy Benjegerdes            46962 –   586
   Tom Hoch                   beats Ian Simpson                 46967 –   661
   Tom Hoch                   beats Christopher Zimmerman       47004 –     1
   Tom Hoch                   beats Theron Preston Washington   47004 –     1
   Aswar Rahman               beats Charlie Gers                 5256 –  2980
   Captain Jack Sparrow       beats Charlie Gers                 3995 –  2962
   Charlie Gers               beats Gregg A. Iverson             2996 –  2711
   Al Flowers                 beats Charlie Gers                 5342 –  2998
   Charlie Gers               beats David Rosenfeld              3002 –  2451
   Charlie Gers               beats L.A. Nik                     2824 –  1939
   Charlie Gers               beats David John Wilson            3008 –  1543
   Charlie Gers               beats Undeclared Write-ins         3033 –   592
   Charlie Gers               beats Ronald Lischeid              2952 –  1114
   Charlie Gers               beats Troy Benjegerdes             3016 –   736
   Charlie Gers               beats Ian Simpson                  3006 –   717
   Charlie Gers               beats Christopher Zimmerman        3041 –     3
   Charlie Gers               beats Theron Preston Washington    3041 –     1
   Aswar Rahman               beats Captain Jack Sparrow         5263 –  4070
   Aswar Rahman               beats Gregg A. Iverson             5260 –  2694
   Al Flowers                 beats Aswar Rahman                 5127 –  5099
   Aswar Rahman               beats David Rosenfeld              5244 –  2433
   Aswar Rahman               beats L.A. Nik                     5288 –  2288
   Aswar Rahman               beats David John Wilson            5290 –  1608
   Aswar Rahman               beats Undeclared Write-ins         5318 –   651
   Aswar Rahman               beats Ronald Lischeid              5296 –  1253
   Aswar Rahman               beats Troy Benjegerdes             5296 –   752
   Aswar Rahman               beats Ian Simpson                  5308 –   833
   Aswar Rahman               beats Christopher Zimmerman        5320 –     3
   Aswar Rahman               beats Theron Preston Washington    5320 –     1
   Captain Jack Sparrow       beats Gregg A. Iverson             4122 –  2729
   Al Flowers                 beats Captain Jack Sparrow         5297 –  4066
   Captain Jack Sparrow       beats David Rosenfeld              4034 –  2399
   Captain Jack Sparrow       beats L.A. Nik                     4060 –  2204
   Captain Jack Sparrow       beats David John Wilson            4079 –  1470
   Captain Jack Sparrow       beats Undeclared Write-ins         4187 –   636
   Captain Jack Sparrow       beats Ronald Lischeid              4140 –  1249
   Captain Jack Sparrow       beats Troy Benjegerdes             4151 –   751
   Captain Jack Sparrow       beats Ian Simpson                  4136 –   761
   Captain Jack Sparrow       beats Christopher Zimmerman        4198 –     3
   Captain Jack Sparrow       beats Theron Preston Washington    4198 –     1
   Al Flowers                 beats Gregg A. Iverson             5298 –  2674
   Gregg A. Iverson           beats David Rosenfeld              2730 –  2462
   Gregg A. Iverson           beats L.A. Nik                     2729 –  2326
   Gregg A. Iverson           beats David John Wilson            2748 –  1645
   Gregg A. Iverson           beats Undeclared Write-ins         2757 –   661
   Gregg A. Iverson           beats Ronald Lischeid              2729 –  1267
   Gregg A. Iverson           beats Troy Benjegerdes             2742 –   746
   Gregg A. Iverson           beats Ian Simpson                  2750 –   836
   Gregg A. Iverson           beats Christopher Zimmerman        2759 –     3
   Gregg A. Iverson           beats Theron Preston Washington    2759 –     1
   Al Flowers                 beats David Rosenfeld              5326 –  2448
   Al Flowers                 beats L.A. Nik                     5329 –  2295
   Al Flowers                 beats David John Wilson            5350 –  1617
   Al Flowers                 beats Undeclared Write-ins         5372 –   648
   Al Flowers                 beats Ronald Lischeid              5357 –  1264
   Al Flowers                 beats Troy Benjegerdes             5351 –   747
   Al Flowers                 beats Ian Simpson                  5368 –   825
   Al Flowers                 beats Christopher Zimmerman        5378 –     3
   Al Flowers                 beats Theron Preston Washington    5378 –     0
   David Rosenfeld            beats L.A. Nik                     2469 –  2314
   David Rosenfeld            beats David John Wilson            2472 –  1599
   David Rosenfeld            beats Undeclared Write-ins         2496 –   650
   David Rosenfeld            beats Ronald Lischeid              2471 –  1243
   David Rosenfeld            beats Troy Benjegerdes             2483 –   744
   David Rosenfeld            beats Ian Simpson                  2489 –   824
   David Rosenfeld            beats Christopher Zimmerman        2501 –     3
   David Rosenfeld            beats Theron Preston Washington    2501 –     1
   L.A. Nik                   beats David John Wilson            2302 –  1583
   L.A. Nik                   beats Undeclared Write-ins         2338 –   629
   L.A. Nik                   beats Ronald Lischeid              2241 –  1160
   L.A. Nik                   beats Troy Benjegerdes             2318 –   749
   L.A. Nik                   beats Ian Simpson                  2315 –   754
   L.A. Nik                   beats Christopher Zimmerman        2347 –     3
   L.A. Nik                   beats Theron Preston Washington    2347 –     1
   David John Wilson          beats Undeclared Write-ins         1658 –   661
   David John Wilson          beats Ronald Lischeid              1617 –  1266
   David John Wilson          beats Troy Benjegerdes             1645 –   764
   David John Wilson          beats Ian Simpson                  1643 –   822
   David John Wilson          beats Christopher Zimmerman        1664 –     3
   David John Wilson          beats Theron Preston Washington    1664 –     1
   Ronald Lischeid            beats Undeclared Write-ins         1297 –   656
   Troy Benjegerdes           beats Undeclared Write-ins          778 –   662
   Ian Simpson                beats Undeclared Write-ins          850 –   658
   Undeclared Write-ins       beats Christopher Zimmerman         664 –     3
   Undeclared Write-ins       beats Theron Preston Washington     664 –     1
   Ronald Lischeid            beats Troy Benjegerdes             1270 –   756
   Ronald Lischeid            beats Ian Simpson                  1265 –   795
   Ronald Lischeid            beats Christopher Zimmerman        1300 –     3
   Ronald Lischeid            beats Theron Preston Washington    1300 –     1
   Ian Simpson                beats Troy Benjegerdes              836 –   764
   Troy Benjegerdes           beats Christopher Zimmerman         781 –     3
   Troy Benjegerdes           beats Theron Preston Washington     781 –     1
   Ian Simpson                beats Christopher Zimmerman         853 –     3
   Ian Simpson                beats Theron Preston Washington     853 –     1
   Christopher Zimmerman      beats Theron Preston Washington       3 –     1

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
                              |         Jacob Frey          |       Raymond Dehn         |    Nekima Levy-Pounds      |       Betsy Hodges         |         Tom Hoch           |       Charlie Gers         |       Aswar Rahman         |   Captain Jack Sparrow     |     Gregg A. Iverson       |        Al Flowers          |      David Rosenfeld       |         L.A. Nik           |     David John Wilson      |   Undeclared Write-ins     |      Ronald Lischeid       |     Troy Benjegerdes       |        Ian Simpson         |   Christopher Zimmerman    | Theron Preston Washington  |
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                 Jacob Frey > |             ---             |  46704 -  22810 -  34970   |  47368 -  21597 -  35519   |  45825 -  20956 -  37703   |  41663 -  31598 -  31223   |  54470 -  47619 -   2395   |  54347 -  46234 -   3903   |  54604 -  46949 -   2931   |  54545 -  48405 -   1534   |  54441 -  45722 -   4321   |  54640 -  47738 -   2106   |  54602 -  48003 -   1879   |  54680 -  48568 -   1236   |  54738 -  49239 -    507   |  54681 -  48694 -   1109   |  54708 -  49151 -    625   |  54725 -  49062 -    697   |  54757 -  49724 -      3   |  54757 -  49726 -      1   |
               Raymond Dehn > |   34970 -  22810 -  46704   |            ---             |  34120 -  40402 -  29962   |  35133 -  31838 -  37513   |  36737 -  27103 -  40644   |  43999 -  57602 -   2883   |  43754 -  56432 -   4298   |  43991 -  57218 -   3275   |  43984 -  57990 -   2510   |  43719 -  56536 -   4229   |  43906 -  58916 -   1662   |  44051 -  58287 -   2146   |  44063 -  59035 -   1386   |  44085 -  59862 -    537   |  44056 -  59243 -   1185   |  44043 -  59764 -    677   |  44074 -  59678 -    732   |  44093 -  60388 -      3   |  44094 -  60389 -      1   |
         Nekima Levy-Pounds > |   35519 -  21597 -  47368   |  29962 -  40402 -  34120   |            ---             |  33529 -  32875 -  38080   |  37656 -  25208 -  41620   |  43888 -  57705 -   2891   |  43551 -  57214 -   3719   |  43844 -  57412 -   3228   |  43835 -  58278 -   2371   |  43557 -  57483 -   3444   |  43725 -  59073 -   1686   |  43902 -  58409 -   2173   |  43904 -  59214 -   1366   |  43945 -  60005 -    534   |  43916 -  59401 -   1167   |  43914 -  59870 -    700   |  43935 -  59808 -    741   |  43950 -  60533 -      1   |  43951 -  60533 -      0   |
               Betsy Hodges > |   37703 -  20956 -  45825   |  37513 -  31838 -  35133   |  38080 -  32875 -  33529   |            ---             |  40900 -  23880 -  39704   |  49756 -  51932 -   2796   |  49491 -  50813 -   4180   |  49748 -  51290 -   3446   |  49669 -  52838 -   1977   |  49417 -  50909 -   4158   |  49688 -  52712 -   2084   |  49825 -  52497 -   2162   |  49840 -  53255 -   1389   |  49875 -  54039 -    570   |  49833 -  53486 -   1165   |  49852 -  53961 -    671   |  49865 -  53886 -    733   |  49891 -  54590 -      3   |  49891 -  54592 -      1   |
                   Tom Hoch > |   31223 -  31598 -  41663   |  40644 -  27103 -  36737   |  41620 -  25208 -  37656   |  39704 -  23880 -  40900   |            ---             |  46688 -  55614 -   2182   |  46601 -  54004 -   3879   |  46855 -  54801 -   2828   |  46830 -  55823 -   1831   |  46588 -  53846 -   4050   |  46888 -  55446 -   2150   |  46832 -  56023 -   1629   |  46946 -  56385 -   1153   |  46989 -  57001 -    494   |  46915 -  56585 -    984   |  46962 -  56936 -    586   |  46967 -  56856 -    661   |  47004 -  57479 -      1   |  47004 -  57479 -      1   |
               Charlie Gers > |    2395 -  47619 -  54470   |   2883 -  57602 -  43999   |   2891 -  57705 -  43888   |   2796 -  51932 -  49756   |   2182 -  55614 -  46688   |            ---             |   2980 -  96248 -   5256   |   2962 -  97527 -   3995   |   2996 -  98777 -   2711   |   2998 -  96144 -   5342   |   3002 -  99031 -   2451   |   2824 -  99721 -   1939   |   3008 -  99933 -   1543   |   3033 - 100859 -    592   |   2952 - 100418 -   1114   |   3016 - 100732 -    736   |   3006 - 100761 -    717   |   3041 - 101440 -      3   |   3041 - 101442 -      1   |
               Aswar Rahman > |    3903 -  46234 -  54347   |   4298 -  56432 -  43754   |   3719 -  57214 -  43551   |   4180 -  50813 -  49491   |   3879 -  54004 -  46601   |   5256 -  96248 -   2980   |            ---             |   5263 -  95151 -   4070   |   5260 -  96530 -   2694   |   5099 -  94258 -   5127   |   5244 -  96807 -   2433   |   5288 -  96908 -   2288   |   5290 -  97586 -   1608   |   5318 -  98515 -    651   |   5296 -  97935 -   1253   |   5296 -  98436 -    752   |   5308 -  98343 -    833   |   5320 -  99161 -      3   |   5320 -  99163 -      1   |
       Captain Jack Sparrow > |    2931 -  46949 -  54604   |   3275 -  57218 -  43991   |   3228 -  57412 -  43844   |   3446 -  51290 -  49748   |   2828 -  54801 -  46855   |   3995 -  97527 -   2962   |   4070 -  95151 -   5263   |            ---             |   4122 -  97633 -   2729   |   4066 -  95121 -   5297   |   4034 -  98051 -   2399   |   4060 -  98220 -   2204   |   4079 -  98935 -   1470   |   4187 -  99661 -    636   |   4140 -  99095 -   1249   |   4151 -  99582 -    751   |   4136 -  99587 -    761   |   4198 - 100283 -      3   |   4198 - 100285 -      1   |
           Gregg A. Iverson > |    1534 -  48405 -  54545   |   2510 -  57990 -  43984   |   2371 -  58278 -  43835   |   1977 -  52838 -  49669   |   1831 -  55823 -  46830   |   2711 -  98777 -   2996   |   2694 -  96530 -   5260   |   2729 -  97633 -   4122   |            ---             |   2674 -  96512 -   5298   |   2730 -  99292 -   2462   |   2729 -  99429 -   2326   |   2748 - 100091 -   1645   |   2757 - 101066 -    661   |   2729 - 100488 -   1267   |   2742 - 100996 -    746   |   2750 - 100898 -    836   |   2759 - 101722 -      3   |   2759 - 101724 -      1   |
                 Al Flowers > |    4321 -  45722 -  54441   |   4229 -  56536 -  43719   |   3444 -  57483 -  43557   |   4158 -  50909 -  49417   |   4050 -  53846 -  46588   |   5342 -  96144 -   2998   |   5127 -  94258 -   5099   |   5297 -  95121 -   4066   |   5298 -  96512 -   2674   |            ---             |   5326 -  96710 -   2448   |   5329 -  96860 -   2295   |   5350 -  97517 -   1617   |   5372 -  98464 -    648   |   5357 -  97863 -   1264   |   5351 -  98386 -    747   |   5368 -  98291 -    825   |   5378 -  99103 -      3   |   5378 -  99106 -      0   |
            David Rosenfeld > |    2106 -  47738 -  54640   |   1662 -  58916 -  43906   |   1686 -  59073 -  43725   |   2084 -  52712 -  49688   |   2150 -  55446 -  46888   |   2451 -  99031 -   3002   |   2433 -  96807 -   5244   |   2399 -  98051 -   4034   |   2462 -  99292 -   2730   |   2448 -  96710 -   5326   |            ---             |   2469 -  99701 -   2314   |   2472 - 100413 -   1599   |   2496 - 101338 -    650   |   2471 - 100770 -   1243   |   2483 - 101257 -    744   |   2489 - 101171 -    824   |   2501 - 101980 -      3   |   2501 - 101982 -      1   |
                   L.A. Nik > |    1879 -  48003 -  54602   |   2146 -  58287 -  44051   |   2173 -  58409 -  43902   |   2162 -  52497 -  49825   |   1629 -  56023 -  46832   |   1939 -  99721 -   2824   |   2288 -  96908 -   5288   |   2204 -  98220 -   4060   |   2326 -  99429 -   2729   |   2295 -  96860 -   5329   |   2314 -  99701 -   2469   |            ---             |   2302 - 100599 -   1583   |   2338 - 101517 -    629   |   2241 - 101083 -   1160   |   2318 - 101417 -    749   |   2315 - 101415 -    754   |   2347 - 102134 -      3   |   2347 - 102136 -      1   |
          David John Wilson > |    1236 -  48568 -  54680   |   1386 -  59035 -  44063   |   1366 -  59214 -  43904   |   1389 -  53255 -  49840   |   1153 -  56385 -  46946   |   1543 -  99933 -   3008   |   1608 -  97586 -   5290   |   1470 -  98935 -   4079   |   1645 - 100091 -   2748   |   1617 -  97517 -   5350   |   1599 - 100413 -   2472   |   1583 - 100599 -   2302   |            ---             |   1658 - 102165 -    661   |   1617 - 101601 -   1266   |   1645 - 102075 -    764   |   1643 - 102019 -    822   |   1664 - 102817 -      3   |   1664 - 102819 -      1   |
       Undeclared Write-ins > |     507 -  49239 -  54738   |    537 -  59862 -  44085   |    534 -  60005 -  43945   |    570 -  54039 -  49875   |    494 -  57001 -  46989   |    592 - 100859 -   3033   |    651 -  98515 -   5318   |    636 -  99661 -   4187   |    661 - 101066 -   2757   |    648 -  98464 -   5372   |    650 - 101338 -   2496   |    629 - 101517 -   2338   |    661 - 102165 -   1658   |            ---             |    656 - 102531 -   1297   |    662 - 103044 -    778   |    658 - 102976 -    850   |    664 - 103817 -      3   |    664 - 103819 -      1   |
            Ronald Lischeid > |    1109 -  48694 -  54681   |   1185 -  59243 -  44056   |   1167 -  59401 -  43916   |   1165 -  53486 -  49833   |    984 -  56585 -  46915   |   1114 - 100418 -   2952   |   1253 -  97935 -   5296   |   1249 -  99095 -   4140   |   1267 - 100488 -   2729   |   1264 -  97863 -   5357   |   1243 - 100770 -   2471   |   1160 - 101083 -   2241   |   1266 - 101601 -   1617   |   1297 - 102531 -    656   |            ---             |   1270 - 102458 -    756   |   1265 - 102424 -    795   |   1300 - 103181 -      3   |   1300 - 103183 -      1   |
           Troy Benjegerdes > |     625 -  49151 -  54708   |    677 -  59764 -  44043   |    700 -  59870 -  43914   |    671 -  53961 -  49852   |    586 -  56936 -  46962   |    736 - 100732 -   3016   |    752 -  98436 -   5296   |    751 -  99582 -   4151   |    746 - 100996 -   2742   |    747 -  98386 -   5351   |    744 - 101257 -   2483   |    749 - 101417 -   2318   |    764 - 102075 -   1645   |    778 - 103044 -    662   |    756 - 102458 -   1270   |            ---             |    764 - 102884 -    836   |    781 - 103700 -      3   |    781 - 103702 -      1   |
                Ian Simpson > |     697 -  49062 -  54725   |    732 -  59678 -  44074   |    741 -  59808 -  43935   |    733 -  53886 -  49865   |    661 -  56856 -  46967   |    717 - 100761 -   3006   |    833 -  98343 -   5308   |    761 -  99587 -   4136   |    836 - 100898 -   2750   |    825 -  98291 -   5368   |    824 - 101171 -   2489   |    754 - 101415 -   2315   |    822 - 102019 -   1643   |    850 - 102976 -    658   |    795 - 102424 -   1265   |    836 - 102884 -    764   |            ---             |    853 - 103628 -      3   |    853 - 103630 -      1   |
      Christopher Zimmerman > |       3 -  49724 -  54757   |      3 -  60388 -  44093   |      1 -  60533 -  43950   |      3 -  54590 -  49891   |      1 -  57479 -  47004   |      3 - 101440 -   3041   |      3 -  99161 -   5320   |      3 - 100283 -   4198   |      3 - 101722 -   2759   |      3 -  99103 -   5378   |      3 - 101980 -   2501   |      3 - 102134 -   2347   |      3 - 102817 -   1664   |      3 - 103817 -    664   |      3 - 103181 -   1300   |      3 - 103700 -    781   |      3 - 103628 -    853   |            ---             |      3 - 104480 -      1   |
  Theron Preston Washington > |       1 -  49726 -  54757   |      1 -  60389 -  44094   |      0 -  60533 -  43951   |      1 -  54592 -  49891   |      1 -  57479 -  47004   |      1 - 101442 -   3041   |      1 -  99163 -   5320   |      1 - 100285 -   4198   |      1 - 101724 -   2759   |      0 -  99106 -   5378   |      1 - 101982 -   2501   |      1 - 102136 -   2347   |      1 - 102819 -   1664   |      1 - 103819 -    664   |      1 - 103183 -   1300   |      1 - 103702 -    781   |      1 - 103630 -    853   |      1 - 104480 -      3   |            ---             |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate                  W–L–T   Copeland   Margin  Beats
    1  Jacob Frey                 18–0–0        18  +783593  Betsy Hodges, Tom Hoch, Raymond Dehn, Nekima Levy-Pounds, Al Flowers, Aswar Rahman, Captain Jack Sparrow, Charlie Gers, Gregg A. Iverson, David Rosenfeld, L.A. Nik, David John Wilson, Ronald Lischeid, Ian Simpson, Troy Benjegerdes, Undeclared Write-ins, Christopher Zimmerman, Theron Preston Washington
    2  Betsy Hodges               17–1–0        17  +671311  Tom Hoch, Raymond Dehn, Nekima Levy-Pounds, Al Flowers, Aswar Rahman, Captain Jack Sparrow, Charlie Gers, Gregg A. Iverson, David Rosenfeld, L.A. Nik, David John Wilson, Ronald Lischeid, Ian Simpson, Troy Benjegerdes, Undeclared Write-ins, Christopher Zimmerman, Theron Preston Washington
    3  Tom Hoch                   16–2–0        16  +629875  Raymond Dehn, Nekima Levy-Pounds, Al Flowers, Aswar Rahman, Captain Jack Sparrow, Charlie Gers, Gregg A. Iverson, David Rosenfeld, L.A. Nik, David John Wilson, Ronald Lischeid, Ian Simpson, Troy Benjegerdes, Undeclared Write-ins, Christopher Zimmerman, Theron Preston Washington
    4  Raymond Dehn               15–3–0        15  +576525  Nekima Levy-Pounds, Al Flowers, Aswar Rahman, Captain Jack Sparrow, Charlie Gers, Gregg A. Iverson, David Rosenfeld, L.A. Nik, David John Wilson, Ronald Lischeid, Ian Simpson, Troy Benjegerdes, Undeclared Write-ins, Christopher Zimmerman, Theron Preston Washington
    5  Nekima Levy-Pounds         14–4–0        14  +565274  Al Flowers, Aswar Rahman, Captain Jack Sparrow, Charlie Gers, Gregg A. Iverson, David Rosenfeld, L.A. Nik, David John Wilson, Ronald Lischeid, Ian Simpson, Troy Benjegerdes, Undeclared Write-ins, Christopher Zimmerman, Theron Preston Washington
    6  Al Flowers                 13–5–0        13  -172931  Aswar Rahman, Captain Jack Sparrow, Charlie Gers, Gregg A. Iverson, David Rosenfeld, L.A. Nik, David John Wilson, Ronald Lischeid, Ian Simpson, Troy Benjegerdes, Undeclared Write-ins, Christopher Zimmerman, Theron Preston Washington
    7  Aswar Rahman               12–6–0        12  -173900  Captain Jack Sparrow, Charlie Gers, Gregg A. Iverson, David Rosenfeld, L.A. Nik, David John Wilson, Ronald Lischeid, Ian Simpson, Troy Benjegerdes, Undeclared Write-ins, Christopher Zimmerman, Theron Preston Washington
    8  Captain Jack Sparrow       11–7–0        11  -195623  Charlie Gers, Gregg A. Iverson, David Rosenfeld, L.A. Nik, David John Wilson, Ronald Lischeid, Ian Simpson, Troy Benjegerdes, Undeclared Write-ins, Christopher Zimmerman, Theron Preston Washington
    9  Charlie Gers               10–8–0        10  -213195  Gregg A. Iverson, David Rosenfeld, L.A. Nik, David John Wilson, Ronald Lischeid, Ian Simpson, Troy Benjegerdes, Undeclared Write-ins, Christopher Zimmerman, Theron Preston Washington
   10  Gregg A. Iverson           9–9–0          9  -220752  David Rosenfeld, L.A. Nik, David John Wilson, Ronald Lischeid, Ian Simpson, Troy Benjegerdes, Undeclared Write-ins, Christopher Zimmerman, Theron Preston Washington
   11  David Rosenfeld            8–10–0         8  -224798  L.A. Nik, David John Wilson, Ronald Lischeid, Ian Simpson, Troy Benjegerdes, Undeclared Write-ins, Christopher Zimmerman, Theron Preston Washington
   12  L.A. Nik                   7–11–0         7  -227227  David John Wilson, Ronald Lischeid, Ian Simpson, Troy Benjegerdes, Undeclared Write-ins, Christopher Zimmerman, Theron Preston Washington
   13  David John Wilson          6–12–0         6  -240713  Ronald Lischeid, Ian Simpson, Troy Benjegerdes, Undeclared Write-ins, Christopher Zimmerman, Theron Preston Washington
   14  Ronald Lischeid            5–13–0         5  -246557  Ian Simpson, Troy Benjegerdes, Undeclared Write-ins, Christopher Zimmerman, Theron Preston Washington
   15  Ian Simpson                4–14–0         4  -255149  Troy Benjegerdes, Undeclared Write-ins, Christopher Zimmerman, Theron Preston Washington
   16  Troy Benjegerdes           3–15–0         3  -256145  Undeclared Write-ins, Christopher Zimmerman, Theron Preston Washington
   17  Undeclared Write-ins       2–16–0         2  -258646  Christopher Zimmerman, Theron Preston Washington
   18  Christopher Zimmerman      1–17–0         1  -270452  Theron Preston Washington
   19  Theron Preston Washington  0–18–0         0  -270490  —

Winner — Ranked Robin (RCV-RR): Jacob Frey
   beats every opponent head-to-head — the Condorcet winner.
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 19): Jacob Frey
   Outside (18):       Raymond Dehn, Nekima Levy-Pounds, Betsy Hodges, Tom Hoch, Charlie Gers, Aswar Rahman, Captain Jack Sparrow, Gregg A. Iverson, Al Flowers, David Rosenfeld, L.A. Nik, David John Wilson, Undeclared Write-ins, Ronald Lischeid, Troy Benjegerdes, Ian Simpson, Christopher Zimmerman, Theron Preston Washington
   One member ⇒ Jacob Frey is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner Jacob Frey is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/minneapolis_2017_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/minneapolis_2017/cases/minneapolis_2017_ranked_robin.yaml
```

## See also

- [Center squeeze (topic hub)](../../../../07_Concepts/topics/center_squeeze/README.md)
- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Ballot & terminology basics](../../../../07_Concepts/topics/ballot_and_terminology_basics.md)
- [Exhausted ballots (untangled)](../../../../06_Other/RCV_IRV/concepts/exhausted_ballots_301.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [minneapolis_2017_irv](minneapolis_2017_irv.md)
