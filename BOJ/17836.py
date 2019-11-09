import sys
sys.stdin = open('input/17836.txt')


def bfs():
    global result
    time = 0
    visited = [[0]*M for _ in range(N)]
    visited[0][0] = 1
    q = [[0, 0]]
    while q and time <= K:
        time += 1
        contents, q = q, []
        for r, c in contents:
            for x in range(4):
                rr = r + dr[x]
                cc = c + dc[x]
                if rr == N - 1 and cc == M - 1:
                    if result > time:
                        result = time

                elif 0 <= rr < N and 0 <= cc < M and not visited[rr][cc] and board[rr][cc] != 1 :
                    visited[rr][cc] = 1
                    if board[rr][cc] == 2:
                        if (N - 1) - rr + (M - 1) - cc + time < result:
                            result = (N - 1) - rr + (M - 1) - cc + time
                    q.append([rr, cc])


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

result = float('inf')
bfs()
print(result) if result <= K else print("Fail")
