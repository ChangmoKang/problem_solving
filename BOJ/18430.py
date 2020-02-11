import sys
sys.stdin = open('input/18430.txt')


def check(r, c, sub_result):
    global result
    if r == R:
        if sub_result > result:
            result = sub_result
    else:
        if c + 1 == C:
            check(r + 1, 0, sub_result)
        else:
            check(r, c + 1, sub_result)

        if not visited[r][c]:
            for k, s in new_board[r][c].items():
                flag = 0
                for direction in shape[k]:
                    rr, cc = r + dr[direction], c + dc[direction]
                    if visited[rr][cc]:
                        flag = 1
                        break

                if not flag:
                    visited[r][c] = 1
                    for direction in shape[k]:
                        rr, cc = r + dr[direction], c + dc[direction]
                        visited[rr][cc] = 1

                    if c + 1 == C:
                        check(r + 1, 0, sub_result + s)
                    else:
                        check(r, c + 1, sub_result + s)
                    
                    visited[r][c] = 0
                    for direction in shape[k]:
                        rr, cc = r + dr[direction], c + dc[direction]
                        visited[rr][cc] = 0


def make_boomerang(r, c, k):
    s = 2 * board[r][c] 
    for direction in shape[k]:
        rr, cc = r + dr[direction], c + dc[direction]
        if 0 <= rr < R and 0 <= cc < C:
            s += board[rr][cc]
        else:
            return -1
    return s


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
shape = {
    0: [0, 2],
    1: [0, 3],
    2: [1, 2],
    3: [1, 3]
}
R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

if R == 1 or C == 1:
    print(0)
else:
    result = 0
    new_board = [[None]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            dic = {}
            for kind in range(4):
                strength = make_boomerang(i, j, kind)
                if strength != -1:
                    dic[kind] = strength
            new_board[i][j] = dic

    visited = [[0]*C for _ in range(R)]
    check(0, 0, 0)
    print(result)
