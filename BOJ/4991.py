import sys
sys.stdin = open('input/4991.txt')
input = sys.stdin.readline


def check(count, start, sub_result):
    global result
    if count == dust_N - 1:
        result = sub_result
    else:
        for i in range(1, dust_N):
            if not dust_visited[i]:
                dust_visited[i] = 1
                if saved_route[start][i] == None:
                    value = bfs(start, i)
                    saved_route[start][i] = value
                    saved_route[i][start] = value
                else:
                    value = saved_route[start][i]
                if value != -1 and sub_result + value < result:
                    check(count + 1, i, sub_result + value)
                dust_visited[i] = 0


def bfs(start, order):
    visited = [[0]*C for _ in range(R)]
    visited[dust[start][0]][dust[start][1]] = 1

    q = [dust[start]]
    cnt = 0
    while q:
        cnt += 1
        qs, q = q, []
        for r, c in qs:
            for x in range(4):
                rr, cc = r + dr[x], c + dc[x]
                if 0 <= rr < R and 0 <= cc < C and board[rr][cc] != 'x' and not visited[rr][cc]:
                    visited[rr][cc] = 1
                    if [rr, cc] == dust[order]:
                        return cnt
                    q.append([rr, cc])
    return -1


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
while True:
    C, R = map(int, input().split())
    if R == 0 and C == 0:
        break

    board = [list(input()) for _ in range(R)]
    dust = []
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'o':
                board[i][j] = '.'
                robot = [i, j]
            elif board[i][j] == '*':
                dust.append([i, j])

    result = float('inf')
    dust.insert(0, robot)
    dust_N = len(dust)
    dust_visited = [0]*dust_N
    saved_route = [[None]*dust_N for _ in range(dust_N)]
    check(0, 0, 0)
    print(-1) if result == float('inf') else print(result)
