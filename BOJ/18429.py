import sys
sys.stdin = open('input/18429.txt')


def check(count, weight):
    global result
    if count == N:
        result += 1
    else:
        weight -= K
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                if weight + kit[i] >= 500:
                    check(count + 1, weight + kit[i])
                visited[i] = False


N, K = map(int, input().split())
kit = list(map(int, input().split()))

result = 0
visited = [False]*N
check(0, 500)
print(result)
