# Railway management
A segment is reachable unless itself is blocked, or if any segments between it and each of the terminal stations. This can be checked quickly if you keep track of the lowest and highest blocked segment, the hard part is to update this as segments are unblocked. Must be able to block, unblock and check segments in at least O(log n) to pass.

One way to do this is to use a maxheap and a minheap, into which blocked segments are added and unblocked segments are removed. Then block/unblock take O(log n) and checks can be done in O(1). Unfortunately `heapq` in the Python standard library doesn't implement _remove_, so this can be a little cumbersome.

A similar way is to use sets with efficient methods of finding max and min. I don't think this exists in the Python standard library, however.

A third way is to use a [Fenwick tree](http://en.wikipedia.org/wiki/Fenwick_tree), with a bucket for each segment. Increment the bucket by 1 if the segment it represents becomes blocked, decrement by 1 if it is unblocked. Then the status of segment _i_ can be checked by looking at the sum of the buckets from 0 to _i_, and from _i_ to _n_-1. If either of these are 0, then there is `good service`. All of these operations take O(log n).

Overall complexity is O(_k_ log _n_).

__Difficulty__: 5  
__Problem text__: Finished  
__Input/output__: Finished  
__Solutions__: martinvl, olalia, vidar
