# @EXPECTED_RESULTS@: TIMELIMIT

from sys import stdin

a, b, n = map(int, stdin.readline().split())
print pow(a, b) % n
