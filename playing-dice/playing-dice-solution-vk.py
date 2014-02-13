"""
instead of calculating expected value, just add the side + 1 for each dice.
Keep track of best pile at all time.
"""

from sys import stdin

winner = None
winner_value = None
# Input
n = int(stdin.readline())
for pile in range(n):
    number_of_piles = int(stdin.readline())
    pile_sum = 0
    for dice in range(number_of_piles):
        dice_data = [int(i) for i in stdin.readline().split(" ")]
        pile_sum += (dice_data[0] + 1) * dice_data[1]

    if pile_sum > winner_value or winner_value is None:
        winner = pile+1
        winner_value = pile_sum
    elif pile_sum == winner_value:
        winner = str(winner) + "*"
    else:
        pass

print winner
