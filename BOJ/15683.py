import sys
sys.stdin = open('input/15683.txt')


def check(count):
    global result, room
    if count == len(cctvs):
        if result > room:
            result = room
    else:
        for idxs in ways[cctvs[count][2]]:
            visited = []
            for idx in idxs:
                r, c, d = cctvs[count]
                while True:
                    r += dr[idx]
                    c += dc[idx]

                    if not (0 <= r < R and 0 <= c < C) or board[r][c] == 6:
                        break

                    if board[r][c] == 0:
                        board[r][c] = d
                        visited.append([r, c])
                        room -= 1
            check(count + 1)
            for r, c in visited:
                board[r][c] = 0
                room += 1


ways = {
    1: [[0], [1], [2], [3]],
    2: [[0, 1], [2, 3]],
    3: [[0, 3], [1, 3], [1, 2], [0, 2]],
    4: [[0, 2, 3], [0, 1, 3], [1, 2, 3], [0, 1, 2]],
    5: [[0, 1, 2, 3]]
}

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

room = 0
cctvs = []
for i in range(R):
    for j in range(C):
        if board[i][j] == 0:
            room += 1
        elif 1 <= board[i][j] <= 5:
            cctvs.append([i, j, board[i][j]])

result = room
check(0)
print(result)
