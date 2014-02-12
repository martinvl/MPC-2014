"""
Just calculating the best option for each of the three cases (win, loose and
draw) on the first match by hand.
"""
from sys import stdin


def beats(command):
    if command == "Scissors":
        return "Rock"
    if command == "Paper":
        return "Scissors"
    if command == "Rock":
        return "Paper"


def answer(commands):
    if beats(commands[0]) == commands[1]:
        return commands[1]
    elif beats(commands[1]) == commands[0]:
        return commands[1]
    else:
        return beats(commands[0])


T = int(stdin.readline())
for test_case in range(T):
    for match in range(10000):
        print answer(stdin.readline().split())
