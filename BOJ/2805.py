import sys
from collections import Counter
sys.stdin = open('input/2805.txt')


N, M = map(int, input().split())
trees = Counter(map(int, input().split()))

l, r = 1, max(trees)

while l <= r:
    m = (l + r) // 2

    condition = sum((tree_h - m)*tree_cnt for tree_h, tree_cnt in trees.items() if tree_h > m)

    if condition < M:
        r = m - 1
    else:
        l = m + 1

print(l - 1)
