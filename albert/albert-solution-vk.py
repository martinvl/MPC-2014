# @EXPECTED_RESULTS@: CORRECT

"""
Description: Greedy algorithm using the fact that the positions are integers
and not doubles. Divides the number road/line into unit length segments. Then
iterates through the towns from cheapest to most expensive, and use that price
for the L next road segments if they are not covered yet.

Complexity:
Check if it is possible to go: O(N)
Sort towns by price: O(NlogN)
Do the covering: O(NL)

Possible improvements: Instead of keeping track of each single unit road
segment, somehow just keep track of the start point and end point for each
price.
"""
from sys import stdin


def will_not_make_it(L, towns):
    # Tells if the trip is not possible
    for i in range(len(towns)-1):
        if towns[i+1][0] - towns[i][0] > L:
            return True
    return False


def calculate_output(L, N, towns):
    if will_not_make_it(L, towns):
        return "Stay home"

    # Make one road segment for each length unit, set them to -1 (not covered)
    road_segments = [-1]*(towns[len(towns)-1][0])
    towns_sorted_by_price = sorted(towns, key=lambda tup: tup[1])

    # For each town (starting with the cheapest), use that price for all the L
    # following road segments (if the road segment is not covered yet).
    for town in towns_sorted_by_price:
        pos = town[0]
        for i in range(L):
            if pos+i < len(road_segments):
                if road_segments[pos+i] == -1:
                    road_segments[pos+i] = town[1]
    return sum(road_segments)


# Input
L = int(stdin.readline())
N = int(stdin.readline())
towns = []
for i in range(N):
    towns.append([int(i) for i in stdin.readline().split(" ")])

# Output
print calculate_output(L, N, towns)
