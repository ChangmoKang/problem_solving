import sys
sys.stdin = open('input/NM2.txt')


def check(count, start):
    if count == M:
        print(*arr)
    else:
        for i in range(start, N):
            arr[count] = nums[i]
            check(count + 1, i)
            arr[count] = 0


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

arr = [0]*M
check(0, 0)
