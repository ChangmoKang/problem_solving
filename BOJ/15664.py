import sys
sys.stdin = open('input/NM3.txt')


def check(count, start):
    if count == M:
        target = tuple(arr)
        if target not in saved:
            print(*arr)
            saved.add(target)
    else:
        for i in range(start, N):
            arr[count] = nums[i]
            check(count + 1, i + 1)
            arr[count] = 0


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
saved = set()

arr = [0]*M
check(0, 0)
