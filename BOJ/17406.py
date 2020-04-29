import sys
from itertools import permutations
sys.stdin = open('input/17406.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

R, C, M = map(int, input().split())
o_board = [list(map(int, input().split())) for _ in range(R)]
ops = []
for _ in range(M):
    r, c, k = map(int, input().split())
    ops.append((r - 1, c - 1, k))

answer = float('inf')
for order in permutations(ops):
    board = [o_b[:] for o_b in o_board]

    for r, c, k in order:
        for l in range(1, k + 1):
            rr = r - l
            cc = c - l

            t1 = board[rr][cc]
            t2 = None
            for x in range(4):
                for _ in range(2*l):
                    rr += dr[x]
                    cc += dc[x]

                    if t1 is not None:
                        t2 = board[rr][cc]
                        board[rr][cc] = t1
                        t1 = None
                    elif t2 is not None:
                        t1 = board[rr][cc]
                        board[rr][cc] = t2
                        t2 = None
    
    result = min(sum(b) for b in board)

    if answer > result:
        answer = result

print(answer)
