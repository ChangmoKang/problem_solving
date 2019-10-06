import sys
sys.stdin = open('input/NM1.txt')


def check(count):
    if count == M:
        print(*arr)
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                arr[count] = i + 1
                check(count + 1)
                arr[count] = 0
                visited[i] = 0


N, M = map(int, input().split())

arr = [0]*M
visited = [0]*N
check(0)
