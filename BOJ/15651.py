import sys
sys.stdin = open('input/NM1.txt')


def check(count):
    if count == M:
        print(*arr)
    else:
        for i in range(N):
            arr[count] = i + 1
            check(count + 1)
            arr[count] = 0


N, M = map(int, input().split())
arr = [0]*M
check(0)
