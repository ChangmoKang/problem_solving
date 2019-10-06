import sys
sys.stdin = open('input/NM3.txt')


def check(count):
    if count == M:
        target = tuple(arr)
        if target not in saved:
            print(*arr)
            saved.add(target)
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                arr[count] = nums[i]
                check(count + 1)
                arr[count] = 0
                visited[i] = 0


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
saved = set()

arr = [0]*M
visited = [0]*N

check(0)
