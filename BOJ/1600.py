import sys
sys.stdin = open('input/1600.txt')


def bfs(start):
    global result
    q = [start]
    while q:
        qs, q = q, []
        for r, c, cnt, k in qs:
            # 인접한 곳으로 이동
            for x in range(4):
                rr = r + dr[x]
                cc = c + dc[x]
                if 0 <= rr < R and 0 <= cc < C and board[rr][cc] == 0:
                    if rr == R - 1 and cc == C - 1:
                        if result > cnt + 1:
                            result = cnt + 1
                    elif visited[k][rr][cc] > cnt + 1:
                        visited[k][rr][cc] = cnt + 1
                        q.append([rr, cc, cnt + 1, k])
            # 말처럼 이동
            if k:
                for xx in range(8):
                    rr = r + drr[xx]
                    cc = c + dcc[xx]
                    if 0 <= rr < R and 0 <= cc < C and board[rr][cc] == 0:
                        if rr == R - 1 and cc == C - 1:
                            if result > cnt + 1:
                                result = cnt + 1
                        elif visited[k - 1][rr][cc] > cnt + 1:
                            visited[k - 1][rr][cc] = cnt + 1
                            q.append([rr, cc, cnt + 1, k - 1])


# 인접한 곳으로 이동
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# 말처럼 이동
drr = [-1, -2, -2, -1, 1, 2, 2, 1]
dcc = [-2, -1, 1, 2, 2, 1, -1, -2]

K = int(input())
C, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
# 말처럼 이동 가능한 횟수에 따른 visited 준비
visited = [[[float('inf')]*C for _ in range(R)] for _ in range(K + 1)]

result = float('inf')
bfs([0, 0, 0, K])
print(-1) if result == float('inf') else print(result)
