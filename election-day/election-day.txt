Tomorrow is election day at MAPS and the time has come to choose a new leader for the organization.
There is however, one problem: how to pick a leader when every reasonable person wants to be the new leader?
In such a case, every person at the election would simply vote for herself.

Yang (the mathematician) suggests an easy process to pick the new leader. It goes as follows:
the $N$ candidates will place themselves at positions 1 through $N$ on a line
and then every second person (modulo $N$ and starting at the second position)
will consecutively be eliminated until there is only one candidate left.


For example, if $N=5$ the candidate's positions are 1,2,3,4 and 5.
The first candidates to be eliminated are at positions
2, 4.
Then those at positions
1 and 5
follow, so the person at position 3 becomes the next leader.

The board is extremely happy they now have a way to choose the new leader!
Little do they know of Yang's wicked plans.

Yang knows all MAPPERS to be reasonable, but he is not sure how many persons will be present at the election.

Given a list of $T$ numbers, each a number of possible candidates $N$, 
can you help Yang calculate a table telling him where to position himself for each $N$?


Input:
The first line of the input gives the number $T$ of entries in the table.
$T$ entries follow, one for each line.
Each entry consists of the possible number $N$ of candidates to participate in the election.

1<= T <= 400

Small input:
1<= N <= 10^5

Large input:
1<= N <= 10^15


Output:
For each entry $N$ in the table output the position $i$ where Yang would place himself.

$1<= i<= N$.



Example input:
3
1
3
5

Example output:
1
3
3
 
