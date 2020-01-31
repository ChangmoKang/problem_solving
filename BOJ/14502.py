import sys
sys.stdin = open('input/14502.txt')


def init():
    global empty
    for r in range(R):
        for c in range(C):
            if board[r][c] == 0:
                empty += 1
            elif board[r][c] == 2:
                virus.append([r, c])

    for r in range(R):
        for c in range(C):
            if board[r][c] == 0:
                return check(0, r, c)


def check(count, i, j):
    global result
    if count == 3:
        visited = [[0]*C for _ in range(R)]
        for r, c in virus:
            visited[r][c] = 1

        room = empty
        q = [v for v in virus]
        while q:
            qs, q = q, []
            for r, c in qs:
                for x in range(4):
                    rr, cc = r + dr[x], c + dc[x]
                    if 0 <= rr < R and 0 <= cc < C and board[rr][cc] != 1 and not visited[rr][cc]:
                        visited[rr][cc] = 1
                        room -= 1
                        q.append([rr, cc])

        if room > result:
            result = room
    else:
        while True:
            if i == R:
                break

            if board[i][j] == 0:
                board[i][j] = 1

                if j == C - 1:
                    check(count + 1, i + 1, 0)
                else:
                    check(count + 1, i, j + 1)
                
                board[i][j] = 0

            if j == C - 1:
                i += 1
                j = 0
            else:
                j += 1


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

empty = -3
virus = []
result = 0
init()

print(result)
