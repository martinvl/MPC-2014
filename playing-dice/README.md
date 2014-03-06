One of your friends have just found a bunch of dice of all kinds of shapes in
his parents house, and now he is challenging you to play with him. The rules
are that firstly he will make $n$ different piles of dice, then you will pick 
one of them, and then he will pick another. After that you'll both roll all
your dice, and the person with the highest result wins the game.

Upon inspection you find that all the dice have sides numbered from 1 to $x$
where $x$ is the number of faces on the die. Of course you also check that
every die has an euqal probability to land on any face.

As always you are very keen on winning, no matter what it takes. So when your
friend has made the piles of dice (and boy, those are huge piles), you look 
outside the window as you are seeing something strange. When your friend turns
to look, you quickly type a program on your computer to aid you in picking the
pile that will maximize the probability for you to win the game.

Input:
First one integer $n$ >= 2 giving the number of piles of dice. Then for every
pile there will be a line with an integer $i$ >= 1 stating how many types of 
dice there are in that pile. (Dice with an equal number of faces are of the 
same type.) Then follows $i$ lines with integers $x$ >= 1 and $y$ >= 1, where 
$x$ the number of faces for that type, and $y$ is the number of dice of that
type.

The piles are to be thought of as numbered from 1 to $n$.

Output:
The number of the pile you should pick to maximize your chance of winning the
game. If two or more piles are tied in beeing best the output should be the
number of the first of those piles in addition to a '*' to warn you that the
odds might be even.


Example 1 input:
2
1
6 2
1
12 1

Example 1 output:
1

Example 2 input:
3
2
6 2
4 2
1
8 3
6
1 1
2 1
3 1
4 1
5 1
6 1

Example 2 output:
2*
