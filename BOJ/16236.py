import sys
sys.stdin = open('input/16236.txt')


def find_shark():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                board[i][j] = 0
                return [i, j, 2, 0]


def bfs():
    global time
    visited = [[0]*N for _ in range(N)]
    visited[status[0]][status[1]] = 1
    q = [status[:]]
    eat = []
    time_cnt = 0
    while q:
        if eat:
            eat.sort()
            board[eat[0][0]][eat[0][1]] = 0
            status[0], status[1] = eat[0][0], eat[0][1]
            if status[3] + 1 == status[2]:
                status[2] += 1
                status[3] = 0
            else:
                status[3] += 1
            time += time_cnt
            return True
        contents, q = q, []
        for r, c, *_ in contents:
            for x in range(4):
                rr = r + dr[x]
                cc = c + dc[x]
                if 0 <= rr < N and 0 <= cc < N and not visited[rr][cc] and board[rr][cc] <= status[2]:
                    visited[rr][cc] = 1
                    if 0 < board[rr][cc] < status[2]:
                        eat.append([rr, cc])
                    q.append([rr, cc])
        time_cnt += 1
    return False


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
status = find_shark()

time = 0
flag = 0
while True:
    if not bfs():
        break
print(time)
