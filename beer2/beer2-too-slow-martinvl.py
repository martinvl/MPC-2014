# @EXPECTED_RESULTS@: TIMELIMIT

from sys import stdin

print 'BEER!' if int(stdin.readline()) % 198 else 'FIGHT!'
