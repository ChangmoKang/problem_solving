import sys
sys.stdin = open('input/17142.txt')


def init():
    global empty
    for r in range(N):
        for c in range(N):
            if board[r][c] == 0:
                empty += 1
            elif board[r][c] == 2:
                virus.append([r, c])


def check(count, start):
    global result
    if count == K:
        active_virus = [virus[index] for index in active_virus_index]

        visited = [[0]*N for _ in range(N)]
        for r, c in active_virus:
            visited[r][c] = 1

        time = 0
        occupied = 0
        while active_virus:
            time += 1

            if time > result:
                return

            qs, active_virus = active_virus, []
            for r, c in qs:
                for x in range(4):
                    rr, cc = r + dr[x], c + dc[x]
                    if 0 <= rr < N and 0 <= cc < N and board[rr][cc] != 1 and not visited[rr][cc]:
                        visited[rr][cc] = 1
                        if board[rr][cc] == 0:
                            occupied += 1
                        active_virus.append([rr, cc])

            if empty == occupied:
                if result > time:
                    result = time
                    return
    else:
        for i in range(start, len(virus)):
            active_virus_index[count] = i
            check(count + 1, i + 1)
            active_virus_index[count] = None


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

empty = 0
virus = []
init()

if empty == 0:
    print(0)
else:
    result = float('inf')
    active_virus_index = [None]*K
    check(0, 0)
    print(result) if result != float('inf') else print(-1)
