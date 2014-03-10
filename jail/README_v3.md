# Hedge

So you find yourself trapped in the (0,0) square of a rectangular _M_ times _N_ hedge maze that is divided into unit squares. You want to get to the exit which is in _(M-1, N-1)_. Being a bit excentric, you will always increase exactly one of your coordinates by 1 at each step, minimizing the total number of steps. (Diagonal moves are not allowed.) This makes things a bit difficult, but luckily, you also have a team of self sacrificing heroes with you, so whenever you encounter a wall, you may leave one hero behind to help all the others climb over.

![](../images/hedge3.png)

Now, what you would like to know is exactly how many of you can reach the exit this way.

## Input:
The first line of input contains 3 integers, _M_, _N_ and _H_, denoting dimensions of the maze, and the number of heroes (including you). The following _M_ lines containins _N-1_ numbers that are all 0 or 1. There is a hedge between square (i,j) and (i,j+1) if and only if the j'th number on the i'th line is 1. Then follows _M-1_ lines with _N_ numbers on each line, telling that there is a hedge between (i,j) and (i+1, j) if and only if the j'th number on the i'th line is 1. Square coordinates and lines are here 0-indexed.

## Output:
For each test case, output one number on a single line, the maximal number of heroes that may reach the goal.

## Constraints
2 &le; _M_,_N_ &le; 300  
2 &le; _H_ &le; 10<sup>9</sup>

## Sample input 1
```
3 4 4  
1 0 0  
1 1 0  
0 1 0  
0 0 0 0  
0 0 0 0  
```

## Sample output 1
```
3  
```

## Sample input 2
```
3 2 2  
1  
1  
1  
1 1  
1 1  
```

## Sample output 2
```
0  
```
