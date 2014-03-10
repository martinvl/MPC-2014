# Flaps2
Implement improper integral either by analytical solution (expressed through the gamma function), or by numerical integration. SciPy has methods for this. In order to implement this by hand one must observe that it suffices to integrate up to for instance _t_ = 50 (not infinity) to get an approximation.

Must also apply some root-finding algorithm to find _p_. Bisection (binary search) is fast enough. Newton is tricky due to irregularities in the gamma function. SciPy has several methods that will work.

There is plenty of time, but you need a half-decent numerical integration and root-finding implementation.

__Difficulty__: 4  
__Problem text__: Finished  
__Input/output__: Finished  
__Solutions__: martinvl (multiple), read and approved by staalezh