"""
Every time Sverre does a split, he get one more chocolate bar, so it does not
matter how he divides it. The number of splits needed is R * C - 1.
"""
from sys import stdin

R = int(stdin.readline())
C = int(stdin.readline())
print R * C - 1
