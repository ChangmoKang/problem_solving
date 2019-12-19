import sys
from math import log
sys.stdin = open('input/2164.txt')

N = int(input())
if N <= 2:
    print(N)
else:
    N -= 2
    x = int(log(N + 2, 2) - 1)
    N -= 2 ** (x + 1) - 2
    print(2 * N) if N else print(2 ** (x + 1))
