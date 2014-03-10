# @EXPECTED_RESULTS@: CORRECT

from sys import stdin

print 'BEER!' if int(stdin.readline()) % 6 == 0 else 'FIGHT!'
