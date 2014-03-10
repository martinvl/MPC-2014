# Bacterial growth
<center><img src="../images/bacterial.png" /></center>  


Lisa is a lab technician working at Rikshospitalet testing blood samples. Testing blood samples can be a labour intensive undertaking. For each sample Lisa must first prepare a petri dish with a growth medium, then add some of the blood from the sample. After a day has passed Lisa counts the number of visible bacteria cells, using a microscope. Then after another couple of days Lisa recounts the number of bacteria. The amount of growth in the given time span gives the doctors an impression of how aggressive the bacteria is.

Lately Lisa has been testing a lot of samples for the _Quatuor_ bacteria, which she has noticed grows in a very predictable way. If the petri dish is divided into a grid where each bacteria cell occupies a grid cell, the growth during one day can be described as follows: Each cell divides into five, such that there is a cell added north, south, east and west of the original cell. The only exceptions from this growth pattern is when any of these grid cells are already occupied of other cells, or are outside of boundary of the petri dish. The petri dishes are all circular.

An example image series of such growth can be seen below.
<pre>
+--------------------------------------------------------+
|      Day 1       |      Day 2       |      Day 3       |
+------------------+------------------+------------------+
|XXXXXXXXXXXXXXXXXX|XXXXXXXXXXXXXXXXXX|XXXXXXXXXXXXXXXXXX|
|XXXXXX......XXXXXX|XXXXXX......XXXXXX|XXXXXX......XXXXXX|
|XXXX..........XXXX|XXXX..........XXXX|XXXX..........XXXX|
|XXX............XXX|XXX............XXX|XXX......#.....XXX|
|XX..............XX|XX.......#......XX|XX......###.....XX|
|XX.......#......XX|XX......###.....XX|XX.....#####....XX|
|X................X|X........#.......X|X.......###.#....X|
|X................X|X...........#....X|X........#.###...X|
|X...........#....X|X..........###...X|X.........#####..X|
|X................X|X...........#....X|X..........###...X|
|X................X|X................X|X...........#....X|
|X................X|X................X|X.....#..........X|
|XX..............XX|XX....#.........XX|XX...###........XX|
|XX....#.........XX|XX...###........XX|XX..#####.......XX|
|XXX............XXX|XXX...#........XXX|XXX..###.......XXX|
|XXXX..........XXXX|XXXX..........XXXX|XXXX..#.......XXXX|
|XXXXXX......XXXXXX|XXXXXX......XXXXXX|XXXXXX......XXXXXX|
|XXXXXXXXXXXXXXXXXX|XXXXXXXXXXXXXXXXXX|XXXXXXXXXXXXXXXXXX|
+--------------------------------------------------------+

</pre>

Instead of wasting time on performing tests she can predict the result for, Lisa has better things to do. Therefore she needs you to make a program that can predict the result of the test, given an image of the petri dish after day 1. To make sure her boss doesn't discover that she's not actually performing the tests, Lisa will vary the size (diameter) of the petri dishes, and the number of days between the initial and the final count.

## Input specification
The first line of input contains two integers _d_ and _t_, the diameter of the petri dish, and the number of days the bacteria should grow before the final count.
Then follows _d_ lines, each containing _d_ characters. These lines make up the image of the petri dish. The character `#`, `.` and `X` represent a bacteria cell, an empty petri dish and the outside of the petri dish, respectively.

## Output specification
Output the number of bacteria cells there are in the petri dish after _t_ days of growth, given the initial state in the input.

## Constraints
1 &le; _d_ &le; 100  
1 &le; _t_ &le; 20

## Sample input
```
16 2
     ......     
   ..........   
  ............  
 .............. 
 .......#...... 
................
................
...........#....
................
................
................
 .............. 
 ....#......... 
  ............  
   ..........   
     ......  
```

## Sample output
```
39
```
