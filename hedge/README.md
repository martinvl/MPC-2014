# Hedge

So you find yourself trapped in the (0,0) square of a rectangular _X_ times _Y_ hedge maze that is divided into unit squares.  You want to get to the exit which is in _(X-1, Y-1)_.  Being a bit excentric, you will always increase exactly one of your coordinates by 1 at each step, minimizing the total number of steps. This makes things a bit difficult, but luckily, you also have a team of self sacrificing heroes with you, so whenever you encounter a wall, you may leave one hero behind to help all the others climb over.

Now, what you would like to know is exactly how many of you can reach the exit this way.

## Input specification:
The first line of input contains a single integer _T_, denoting the number of test cases.  Then for each test case there will be a line containing 3 integers, _X_, _Y_ and _M_, denoting dimensions of the maze, and the number of heroes (including you).   The following _X_ lines containins _Y-1_ numbers that are all 0 or 1.  There is a hedge between square (i,j) and (i,j+1) if and only if the j'th number on the i'th line is 1.  Then follows _X-1_ lines with _Y_ numbers on each line, telling that there is a hedge between (i,j) and (i+1, j) if and only if the j'th number on the i'th line is 1.

## Output specification:
For each test case, output one number on a single line, the maximal number of heroes that may reach the goal.

## Constraints
1 &le; _T_ &le; 100  
2 &le; _X_,_Y_ &le; 300  
2 &le; _M_ &le; 10<sup>9</sup>

## Sample input
2  
3 3 4  
1 0  
1 1  
0 1  
0 0 0  
0 0 0  
3 2 2  
1  
1  
1  
1 1  
1 1  

## Sample output
3  
0  

