import sys
sys.stdin = open('input/17779.txt')


def bfs(s, num):
    visited[s[0]][s[1]] = num
    value[num] += board[s[0]][s[1]]

    q = [s]
    while q:
        qs, q = q, []
        for r, c in qs:
            for x in range(4):
                rr, cc = r + dr[x], c + dc[x]
                if 0 <= rr < N and 0 <= cc < N and not visited[rr][cc]:
                    visited[rr][cc] = num
                    q.append([rr, cc])
                    value[num] += board[rr][cc]


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
result = float('inf')

for r in range(N - 1):
    for c in range(1, N - 1):
        for d1 in range(1, c + 1):
            for d2 in range(1, N - c):
                if r + d1 < N and r + d2 < N and r + d1 + d2 < N:
                    visited = [[0]*N for _ in range(N)]
                    value = [0]*6
                    for index in range(d1):
                        visited[r + index][c - index] = 5
                        visited[r + d2 + index][c + d2 - index] = 5
                        value[5] += board[r + index][c - index]
                        value[5] += board[r + d2 + index][c + d2 - index]
                    for index in range(d2):
                        visited[r + index][c + index] = 5
                        visited[r + d1 + index][c - d1 + index] = 5
                        value[5] += board[r + index][c + index]
                        value[5] += board[r + d1 + index][c - d1 + index]
                    value[5] -= board[r][c]
                    visited[r + d1 + d2][c - d1 + d2] = 5
                    value[5] += board[r + d1 + d2][c - d1 + d2]

                    for index in range(r):
                        visited[index][c] = 1
                        value[1] += board[index][c]

                    for index in range(c - d1):
                        visited[r + d1][index] = 3
                        value[3] += board[r + d1][index]

                    for index in range(c + d2 + 1, N):
                        visited[r + d2][index] = 2
                        value[2] += board[r + d2][index]

                    for index in range(r + d1 + d2 + 1, N):
                        visited[index][c - d1 + d2] = 4
                        value[4] += board[index][c - d1 + d2]

                    bfs([0, 0], 1)
                    bfs([0, N - 1], 2)
                    bfs([N - 1, 0], 3)
                    bfs([N - 1, N - 1], 4)

                    for rr in range(N):
                        for cc in range(N):
                            if visited[rr][cc] == 0:
                                value[5] += board[rr][cc]
                    
                    value.pop(0)
                    tmp = max(value) - min(value)
                    if result > tmp:
                        result = tmp

print(result)
