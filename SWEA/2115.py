import sys
sys.stdin = open('input/2115.txt')


def calc(index, count, value, bucket, visited):
    global honey

    if count <= C:
        if value > honey[index]:
            honey[index] = value

    for i in range(M):
        if not visited[i]:
            visited[i] = 1
            calc(index, count + bucket[i], value + bucket[i]**2, bucket, visited)
            visited[i] = 0


for tc in range(1, int(input()) + 1):
    N, M, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    for i in range(N):
        for j in range(N - (M - 1)):
            honey = [0, 0]

            bucket1 = board[i][j:j+M]
            calc(0, 0, 0, bucket1, [0]*M)

            for r in range(i, N):
                if r == i:
                    for c in range(j + M, N - (M - 1)):
                        bucket2 = board[r][c:c+M]
                        calc(1, 0, 0, bucket2, [0]*M)
                else:
                    for c in range(N - (M - 1)):
                        bucket2 = board[r][c:c+M]
                        calc(1, 0, 0, bucket2, [0]*M)

            sub_result = sum(honey)
            if sub_result > result:
                result = sub_result

    print(f"#{tc} {result}")
