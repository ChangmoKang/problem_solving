import sys
sys.stdin = open('input/1712.txt')


A, B, C = map(int, input().split())
if B >= C:
    print(-1)
else:
    print(A//(C - B) + 1)
