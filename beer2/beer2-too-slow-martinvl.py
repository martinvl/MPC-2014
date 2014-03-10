# @EXPECTED_RESULTS@: TIMELIMIT

from sys import stdin

print 'BEER!' if int(stdin.readline()) % 6 == 0 else 'FIGHT!'
