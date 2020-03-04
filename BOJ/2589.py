import sys
sys.stdin = open('input/2589.txt')


def bfs(start):
    global result

    q = [start]
    route = -1
    while q:
        route += 1

        contents, q = q, []
        for r, c in contents:
            for x in range(4):
                rr = r + dr[x]
                cc = c + dc[x]
                if 0 <= rr < N and 0 <= cc < M and not visited[rr][cc] and board[rr][cc] == 'L':
                    visited[rr][cc] = True
                    q.append([rr, cc])

    if route > result:
        result = route


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

result = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'L':
            visited = [[False]*M for _ in range(N)]
            visited[i][j] = True
            bfs([i, j])
print(result)


"""
>>> visited에 depth를 저장하는 방식

import sys
sys.stdin = open('input/2589.txt')


def bfs(start):
    global result

    q = [start]
    max_value = 0
    while q:
        contents, q = q, []
        for r, c in contents:
            for x in range(4):
                rr = r + dr[x]
                cc = c + dc[x]
                if 0 <= rr < N and 0 <= cc < M and visited[rr][cc] == -1 and board[rr][cc] == 'L':
                    visited[rr][cc] = visited[r][c] + 1
                    max_value = max(max_value, visited[rr][cc])
                    q.append([rr, cc])

    if max_value > result:
        result = max_value
    

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

result = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'L':
            visited = [[-1]*M for _ in range(N)]
            visited[i][j] = 0
            bfs([i, j])
print(result)
"""