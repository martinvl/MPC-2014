# Downhill cross-country skiing
Jon is not your average cross-country skier. He likes to go really really fast, both upwards and downwards. This tends to lead to some problems, especially going downhill when the trails are crowded. The biggest problem is people not as good Jon falling in the trails, leaving Jon with no other option than running into them.

![](../images/skiing.png)

After several broken pairs of skies, Jon has decided to change his behavior in the trails. Now, he will ski down the slopes in such a way that no accidents can possiblty occur. He has come up 
with a formula for the minimal distance he must have to the _i_-th skier (0-indexed, that is) in front of him, in order to be able to safely stop without risking collision. The formula is v&sdot;b(i + 1), where _v_ is the speed Jon is going, and _b_ is a constant depending on the conditions related to how fast he is able to slow down.

However, Jon doesn't have the time to apply this rule to each of the skiers in front of him (the trails are _really_ crowded), so he needs your help. Write a program that, given the distance between each of the skiers in front of Jon, calculates the minimum distance Jon has to keep to skier in front of him, in order to safely avoid accidents.

## Input specification
The first line of input contains three integers, _n_, _v_ and _b_. This is the number of skiers in front of Jon, the speed he is going and the breaking constant, respectively.
Then follows a line containing _n_ integers _s<sub>i</sub>_, the distance between the _i_-th skier and the skier directly behind him. Note that the first number is the distance between Jon and the first skier.

## Output specification
Output the minimal distance Jon can keep to the skier in front of him, while still being safe.

## Constraints
1 &le; _v_, _b_ &le; 30  
1 &le; _n_ &le; 10<sup>4</sup>  
1 &le; _s<sub>i</sub>_ &le; 100

## Sample input
```
10 5 3
15 15 13 13 19 15 15 10 18 17
```

## Sample output
```
20
```