# Nuts
The number of combinations for each scheme is given by _n_<sup> &sum; c<sub>i</sub></sup>. Calculating this number for each scheme is to slow, since this requires arbitrary size integers (bigint). The trick is to take the logarithm of each such value, because then the multiplications become additions, and the result is possible to handle.

Then simply find the index for the highest such value.

The logarithm is strictly increasing, so it maintains the sorting order.

__Difficulty__: 3  
__Problem text__: Finished  
__Input/output__: Finished  
__Solutions__: martinvl, olalia, vidar