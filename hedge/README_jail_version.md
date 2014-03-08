# Hedge

So you find yourself trapped in a prison.
However, together with _M_ inmates, you have deviced a plan to escape the prison guards and win your freedom!

In order to safely escape to the pickup car waiting, which will bring you and your comrades to freedom, you must cross the prison yard.
The prison yard is rectangular grid of dimensions _X_ times _Y_ divided into unit squares.
You and your inmates are at the _(0,0)_ square, and you want to get to the pickup car which will be at _(X-1, Y-1)_.
However, the prison guards will be chasing you.
In the rush of the moment, you will not necessarily take optimal decisions.
In fact, you know you will always increase exactly one your coordinates by _1_ at each step, minimizing the total number of steps.
This makes things a bit difficult, but luckily, your inmates will sacrifice themselves for your freedom.
Whenever you encounter a wall, on of your inmates will leave behind the help all others climb over.

![](../images/hedge2.png)

Now, given a map of the prison yard you wish to calculate if you can make it, and how many of you comrades can make the escape.

## Input:
The first line of input contains 3 integers, _X_, _Y_ and _M_, denoting dimensions of the prison yard, and the number of inmates escaping with you.
The following _Y_ lines containins _X-1_ numbers that are all 0 or 1.
There is a prison wall between square (i,j) and (i+1,j) if and only if the i'th number on the j'th line is 1.
Then follows _Y-1_ lines with _X_ numbers on each line, telling that there is a hedge between (i,j) and (i, j+1) if and only if the i'th number on the j'th line is 1.
Square coordinates and lines are here 0-indexed.

## Output:
If you are able to escape, output one number on a single line, the maximal number of inmates that may reach the pickup point together with you.
If the pickup point can not be reached, print 'Impossible'.

## Constraints
2 &le; _X_,_Y_ &le; 300  
2 &le; _M_ &le; 10<sup>9</sup>

## Sample input 1
```
4 3 4  
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

