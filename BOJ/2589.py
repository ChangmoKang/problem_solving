import sys
sys.stdin = open('input/2589.txt')


def bfs(start):
    global result

    q = [start]
    sub_result = 0
    while q:
        sub_result += 1
        contents, q = q, []
        for r, c in contents:
            for x in range(4):
                rr = r + dr[x]
                cc = c + dc[x]
                if 0 <= rr < N and 0 <= cc < M and not visited[rr][cc] and board[rr][cc] == 'L':
                    visited[rr][cc] = 1
                    q.append([rr, cc])

    if sub_result - 1 > result:
        result = sub_result - 1


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

result = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'L':
            visited = [[0]*M for _ in range(N)]
            visited[i][j] == 1
            bfs([i, j])

print(result)
