# Beer shopper
![](../images/beer.jpg)

Greg is a good guy, who likes to look after his friends. Being a good guy means Greg has to buy beers for his friends all the time. 
As we all know beer comes in sixpacks, so Greg has to buy beers in multiples of six. Greg wants share exactly one beer with each of his friends, because if someone gets more than onethere will be lots of fighting. Needless to say, leaving one or more beers undrunken is out of the question.

Help Greg out writing a program that determines whether it is possible to buy beer in such a way that each of his _f_ friends get exactly one.

## Input
Input consists of a single line with a single integer _f_, the number of friends Greg wants to buy beer to.

## Output
If it is possible to buy a number of sixpacks such that the beer can be shared evenly among Greg's friends, simply output `BEER!`. Otherwise output `FIGHT!`.

## Constraints
0 < _f_ &le; 10<sup>9</sup>

## Sample input 1
```
6
```

## Sample output 1
```
BEER!
```

## Sample input 2
```
12
```

## Sample output 2
```
BEER!
```

## Sample input 3
```
15
```

## Sample output 3
```
FIGHT!
```