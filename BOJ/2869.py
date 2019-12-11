import sys
from math import ceil
sys.stdin = open('input/2869.txt')

A, B, V = map(int, input().split())
V -= A

if V <= 0:
    print(1)
else:
    days = ceil(V / (A - B))
    print(days + 1)