import sys
sys.stdin = open('input/17472.txt')


def numbering(r, c):
    q = [[r, c]]
    while q:
        contents, q = q, []
        for content in contents:
            for x in range(4):
                rr = content[0] + dr[x]
                cc = content[1] + dc[x]
                if 0 <= rr < R and 0 <= cc < C and board[rr][cc]:
                    if not visited[rr][cc]:
                        visited[rr][cc] = 1
                        board[rr][cc] = N
                        q.append([rr, cc])


def dfs(r, c, d, count):
    rr = r + dr[d]
    cc = c + dc[d]
    if 0 <= rr < R and 0 <= cc < C:
        if board[rr][cc] == 0:
            dfs(rr, cc, d, count + 1)
        elif board[rr][cc] != 0 and board[rr][cc] != board[i][j]:
            to_num = board[rr][cc]
            if count > 1 and dist[from_num][to_num] > count:
                dist[from_num][to_num] = count


def check(sub_result, count):
    global result
    if sum([1 for v in visited if v]) == N:
        if result > sub_result and count == N - 2:
            result = sub_result
    else:
        for r in range(1, N):
            for c in range(1, N):
                if dist[r][c] != float('inf'):
                    if not visited[r]:
                        visited[r] = 1
                        if not visited[c]:
                            visited[c] = 1
                            check(sub_result + dist[r][c], count + 1)
                            visited[c] = 0
                        visited[r] = 0
                    else:
                        if not visited[c]:
                            visited[c] = 1
                            check(sub_result + dist[r][c], count + 1)
                            visited[c] = 0


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

N = 1
visited = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if board[i][j] and not visited[i][j]:
            board[i][j] = N
            visited[i][j] = 1
            numbering(i, j)
            N += 1

dist = [[float('inf')]*N for _ in range(N)]

for i in range(R):
    for j in range(C):
        if board[i][j]:
            from_num = board[i][j]
            for x in range(4):
                dfs(i, j, x, 0)


visited = [1] + [0]*(N-1)
result = float('inf')

check(0, 0)
print(result) if result != float('inf') else print(-1)
