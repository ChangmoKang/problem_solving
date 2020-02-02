import sys
sys.stdin = open('input/17141.txt')


def init():
    global empty
    for r in range(N):
        for c in range(N):
            if board[r][c] == 0:
                empty += 1
            elif board[r][c] == 2:
                possible_virus.append([r, c])
    empty += len(possible_virus) - K


def check(count, start):
    global result
    if count == K:
        visited = [[0]*N for _ in range(N)]
        q = [possible_virus[index] for index in virus_index]
        for r, c in q:
            visited[r][c] = 1

        time = 0
        occupied = 0

        while q:
            time += 1
            if time > result:
                return

            qs, q = q, []
            for r, c in qs:
                for x in range(4):
                    rr, cc = r + dr[x], c + dc[x]
                    if 0 <= rr < N and 0 <= cc < N and board[rr][cc] != 1 and not visited[rr][cc]:
                        visited[rr][cc] = 1
                        occupied += 1
                        if empty == occupied:
                            if result > time:
                                result = time
                                return
                        q.append([rr, cc])
    else:
        for i in range(start, len(possible_virus)):
            virus_index[count] = i
            check(count + 1, i + 1)
            virus_index[count] = None


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

empty = 0
possible_virus = []
init()

if empty == 0:
    print(0)
else:
    result = float('inf')
    virus_index = [None]*K
    check(0, 0)

    print(-1) if result == float('inf') else print(result)
