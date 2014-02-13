#!/usr/bin/env python

# Usage: check_rps.py input_file second_move second_move_friend.
# input_file is the input file for the problem where the first move is given
# for both you and your friend.
# second_move is the output of your solution, containing your second move.
# second_move_computer contains your friend's second move.

ROCK = 0x1
PAPER = 0x10
SCISSORS = 0x100
MASK = 0x111

R = 'Rock'
P = 'Paper'
S = 'Scissors'

move_value_map = {R:ROCK, P:PAPER, S:SCISSORS}
value_move_map = {ROCK:R, PAPER:P, SCISSORS:S}
win_map = {R:{P:False, S:True}, P:{R:True, S:False}, S:{R:False, P:True}}

class IllegalMovesError(Exception):
    def __str__(self):
        return 'Illegal moves'

def get_third(first, second):
    if first == second:
        raise IllegalMovesError()

    third = ~(move_value_map[first] + move_value_map[second]) & MASK
    return value_move_map[third]

def get_score(you, friend):
    if you == friend:
        return .5
    elif win_map[you][friend]:
        return 1
    else:
        return 0


if __name__ == '__main__':
    from sys import argv, exit

    test_in = open(argv[1], 'r')
    solution_out = open(argv[2], 'r')
    jury_out = open(argv[3], 'r')

    T = int(test_in.readline())
    N = int(1e4)
    min_score = 4750

    for i in xrange(T):
        score = 0

        for j in xrange(N):
            you_first, friend_first = test_in.readline().split()
            you_second = solution_out.readline().strip()
            friend_second = jury_out.readline().strip()

            try:
                you_third = get_third(you_first, you_second)
                friend_third = get_third(friend_first, friend_second)

                score += get_score(you_third, friend_third)
            except IllegalMovesError:
                pass

        if score < min_score:
            print score, 'points. Not enough points.'

    test_in.close()
    solution_out.close()
    jury_out.close()
