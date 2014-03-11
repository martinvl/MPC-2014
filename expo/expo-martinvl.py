# @EXPECTED_RESULTS@: CORRECT

from sys import stdin

print pow(*map(int, stdin.readline().split()))
