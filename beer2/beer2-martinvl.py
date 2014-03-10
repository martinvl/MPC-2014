# @EXPECTED_RESULTS@: CORRECT

from sys import stdin

def div_by_two(num):
    return int(num[-1]) % 2 == 0

def div_by_three(num):
    return sum(map(int, num)) % 3 == 0

num = stdin.readline().replace('\n', '')
print 'BEER!' if div_by_two(num) and div_by_three(num) else 'FIGHT!'
