import sys
sys.stdin = open('input/NM1.txt')


def check(count, start):
    if count == M:
        print(*arr)
    else:
        for i in range(start, N):
            arr[count] = i + 1
            check(count + 1, i)
            arr[count] = 0


N, M = map(int, input().split())
arr = [0]*M
check(0, 0)
