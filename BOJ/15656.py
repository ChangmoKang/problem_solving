import sys
sys.stdin = open('input/NM2.txt')


def check(count):
    if count == M:
        print(*arr)
    else:
        for i in range(N):
            arr[count] = nums[i]
            check(count + 1)
            arr[count] = 0


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

arr = [0]*M
check(0)
