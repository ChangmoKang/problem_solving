import sys
from math import ceil
sys.stdin = open('input/2292.txt')

N = int(input())
print(ceil((-3 + (9 + 12 * (N - 1)) ** 0.5)/6) + 1)