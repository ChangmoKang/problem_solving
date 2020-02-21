import sys
sys.stdin = open('input/15683.txt')

WATCHED = 7

def check(index, blind_spot):
    global result
    if index == len(cctv):
        if result > blind_spot:
            result = blind_spot
    else:
        r, c, k = cctv[index]
        for dirs in monitor[k]:
            visited = []
            for dir in dirs:
                rr, cc = r, c
                while True:
                    rr += dr[dir]
                    cc += dc[dir]

                    if not (0 <= rr < R and 0 <= cc < C and board[rr][cc] != 6):
                        break

                    if board[rr][cc] == 0:
                        board[rr][cc] = WATCHED
                        visited.append([rr, cc])
                        blind_spot -= 1
                    
            check(index + 1, blind_spot)

            for rr, cc in visited:
                board[rr][cc] = 0
                blind_spot += 1


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

monitor = {
    1: [[0], [1], [2], [3]],
    2: [[0, 1], [2, 3]],
    3: [[0, 3], [1, 2], [2, 0], [3, 1]],
    4: [[0, 3, 1], [1, 2, 0], [2, 0, 3], [3, 1, 2]],
    5: [[0, 1, 2, 3]]
}

R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

max_blind_spot = 0
cctv = []
for i in range(R):
    for j in range(C):
        if board[i][j] == 0:
            max_blind_spot += 1
        elif 1 <= board[i][j] <= 5:
            cctv.append([i, j, board[i][j]])

result = max_blind_spot
check(0, max_blind_spot)
print(result)
