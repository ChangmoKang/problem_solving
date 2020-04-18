import sys
from itertools import product
sys.stdin = open('input/17090.txt')
input = sys.stdin.readline


d = {
    'U': [-1, 0],
    'D': [1, 0],
    'L': [0, -1],
    'R': [0, 1]
}

DR, DC = 0, 1
UNKNOWN, FAIL, PASS = 0, 1, 2

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
save = [[UNKNOWN]*C for _ in range(R)]

answer = 0
for i, j in product(range(R), range(C)):
    if save[i][j] != UNKNOWN:
        if save[i][j] == PASS:
            answer += 1
        continue

    path = set([(i, j)])
    r, c = i, j
    while True:
        new_r, new_c = r + d[board[r][c]][DR], c + d[board[r][c]][DC]
        
        if not (0 <= new_r < R and 0 <= new_c < C) or save[new_r][new_c] == PASS:
            for path_r, path_c in path:
                save[path_r][path_c] = PASS
            answer += 1
            break

        if save[new_r][new_c] == FAIL or (new_r, new_c) in path:
            for path_r, path_c in path:
                save[path_r][path_c] = FAIL
            break

        path.add((new_r, new_c))
        r, c = new_r, new_c

print(answer)
