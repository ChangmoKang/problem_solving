import sys
sys.stdin = open('input/2583.txt')


def bfs(q):
    room = 1
    while q:
        r, c = q.pop(0)
        for x in range(4):
            rr, cc = r + dr[x], c + dc[x]
            if 0 <= rr < R and 0 <= cc < C and not visited[rr][cc] and board[rr][cc] == 0:
                visited[rr][cc] = 1
                room += 1
                q.append([rr, cc])
    return room


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
R, C, K = map(int, input().split())
board = [[0]*C for _ in range(R)]

for _ in range(K):
    c1, r1, c2, r2 = map(int, input().split())
    for r in range(r1, r2):
        for c in range(c1, c2):
            board[r][c] = 1

result = []
visited = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if board[i][j] == 0 and not visited[i][j]:
            visited[i][j] = 1
            result.append(bfs([[i, j]]))
result.sort()
print(len(result))
print(*result)
