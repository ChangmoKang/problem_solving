import sys
sys.stdin = open('input/3055.txt')


def bfs():
    global water, status, result
    time = 0
    while water or status:
        time += 1
        contents, water = water, []
        for r, c in contents:
            for x in range(4):
                rr = r + dr[x]
                cc = c + dc[x]
                if 0 <= rr < N and 0 <= cc < M and not water_visited[rr][cc] and board[rr][cc] != 'X' and board[rr][cc] != 'D':
                    water_visited[rr][cc] = 1
                    water.append([rr, cc])
        
        contents, status = status, []
        for r, c in contents:
            for x in range(4):
                rr = r + dr[x]
                cc = c + dc[x]
                if 0 <= rr < N and 0 <= cc < M and not water_visited[rr][cc] and not status_visited[rr][cc] and board[rr][cc] != 'X':
                    if board[rr][cc] == 'D':
                        result = time
                        return True
                    status_visited[rr][cc] = 1
                    status.append([rr, cc])
    return False


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

result = 0
water = []
water_visited = [[0]*M for _ in range(N)]
status_visited = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == 'S':
            board[i][j] == '.'
            status = [[i, j]]
            status_visited[i][j] = 1
        elif board[i][j] == '*':
            water.append([i, j])
            water_visited[i][j] = 1

if bfs():
    print(result)
else:
    print('KAKTUS')
