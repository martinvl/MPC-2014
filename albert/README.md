# Albert
Albert the physicist lives on the number line in his hometown at the origo.
One day he decides to go visit his friend, the mathematician Isaac,
who lives in another town far far away on the positive side of the line. 

Albert loves driving, so he decides to go by car,
but since time is money, he will drive directly to Isaac without turning or backing up.
The fuel tank on Albert's car is quite small, in fact, it can only take _L_ liters of gas,
therefore he may have to buy more gas in the towns he visits on his way.
His car spends exactly one liter of gas per length unit.

![](../images/albert.png)

Albert starts from his hometown at x = 0 with an empty fuel tank.
Each town he visits has exactly one gas station, with a given fixed gas price.
At each town he may buy as much fuel as he wants to, but he must of course not exceed the volume in the fuel tank.

He knows that the distance between some of the neighboring cities are quite big,
so Albert is worried that he may run out of gas at some point, and not be able to get to Isaac's town at all.
And if he is able to get there, how much will the trip cost him?


## Input:
The input start with one integer _L_, the volume of the fuel tank on Albert's car.
Then follows an integer _N_, the number of towns between Albert's town and Isaac's town. (Both Albert's town and Isaac's town are included.)

Finally follows _N_ lines, each representing a town, with two integers _D_ and _P_.
_D_ is the position of the town on the number line, while _P_ is the price per liter of gas in that town.
The _N_ lines will be sorted by increasing _D_, and no two towns lie on the same point.
Isaac always lives in the last town.


## Output:
If Albert is able to reach Isaac's hometown, output the least amount of money he needs to spend on the trip.
Otherwise, output the string "Stay home".

## Constraints
0 &le; _L_ &le; 20  
2 &le; _N_ &le; 1000  
0 &le; _D_ &le; 1000  
0 &le; _P_ &le; 10000

## Sample input 1:
```
2
2
0 100
3 0
```

## Sample output 1:
```
Stay home
```

## Sample input 2:
```
10
6
0 6 
4 3
6 9
8 5
18 2
28 0
```

## Sample output 2:
```
94
```





