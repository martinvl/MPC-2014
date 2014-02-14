# @EXPECTED_RESULTS@: CORRECT

from sys import stdin

T = int(stdin.readline())
N = int(1e4)

choice = {'Rock':'Paper', 'Paper':'Scissors', 'Scissors':'Rock'}

for i in xrange(T):
    for j in xrange(N):
        you, friend = stdin.readline().split()
        second = choice[friend]

        if second == you:
            second = friend

        print second
