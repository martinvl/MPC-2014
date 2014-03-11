# Delivery
This can be formulated as a [2SAT](http://en.wikipedia.org/wiki/2-satisfiability)-problem. Create one variable for each package. Each package must be on one of two trucks; let its variable be `True` if it is on the truck going directly to its destination, `False` if it is on the truck going there indirectly.

Then add clauses to fulfill the incompatibilities:

For instance if package _i_ (going to Bergen) is incompatible with package _j_ (also going to Bergen). Then variables _i_ and _j_ cannot be the same, so we add the clauses ( _i_ ^ _j_ ) and ( &not;_i_ ^ &not;_j_ ). Similar clauses exist for each of the other cases.

Algorithms exist for solving this problem in O(_n_<sup>2</sup>) time, which there is plenty of time for.

Greedy solutions also exist, and are accepted.

__Difficulty__: 5  
__Problem text__: Finished  
__Input/output__: Finished  
__Solutions__: martinvl, olalia, matias