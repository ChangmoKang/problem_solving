import sys
sys.stdin = open('input/18247.txt')


for _ in range(int(input())):
    N, M = map(int, input().split())
    if N >= 12 and M >= 4:
        print(11 * M + 4)
    else:
        print(-1)
