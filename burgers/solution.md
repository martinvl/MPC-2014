# Burgers
Because of the small input size, brute force is sufficient. Notice first that there is no point in using a spatula more than once, because this simply undoes the previous flips. Furthermore a spatula can either be used or not, so in all there are 2<sup>_s_</sup> ways to do the flipping. You can check the result if a given combination of super-spatulas in O(_bs_) time, so total running time is O(_bs_ 2<sup>_s_</sup>).

Checking the result of a combination of super-spatulas can be a little cumbersome. The easiest is probably to represent these as binary numbers (integers), and then use XOR (which is equivalent to flipping) consecutively untill you have one number. If this is `0b1111 ... 1111`, then this is a valid flip.

It is also possible to solve this a lot more efficient using linear optimization, but this is beyond the scope of this problem.

__Difficulty__: 3  
__Problem text__: Finished  
__Input/output__: Finished  
__Solutions__: martinvl, olalia