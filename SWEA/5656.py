import sys
from itertools import product
from collections import deque
sys.stdin = open('input/5656.txt')

def bfs():
    def destroy(r, c):
        nonlocal new_bricks
        
        L = new_board[r][c]

        new_bricks -= 1
        new_board[r][c] = EMPTY

        if L > 1:
            for rr in range(r - (L - 1), r + L):
                if 0 <= rr < R and new_board[rr][c] != EMPTY:
                    destroy(rr, c)

            for cc in range(c - (L - 1), c + L):
                if 0 <= cc < C and new_board[r][cc] != EMPTY:
                    destroy(r, cc)


    result = o_bricks

    q = deque([[K, o_bricks, o_board]])
    while q:
        shots, bricks, board = q.popleft()

        if not shots:
            if result > bricks:
                result = bricks
            continue
            
        for i in range(R):
            for j in range(C):
                if board[i][j] != EMPTY:
                    new_bricks = bricks
                    new_board = [b[:] for b in board]

                    destroy(i, j)

                    if not new_bricks:
                        return 0

                    for r in range(R):
                        temp = [elem for elem in new_board[r] if elem != EMPTY]
                        new_board[r] = [0]*(C - len(temp)) + temp

                    q.append([shots - 1, new_bricks, new_board])
                    break

    return result


EMPTY = 0
for tc in range(1, int(input()) + 1):
    K, R, C = map(int, input().split())
    o_board = list(map(list, zip(*[list(map(int, input().split())) for _ in range(C)])))

    o_bricks = 0
    for i, j in product(range(R), range(C)):
        if o_board[i][j] != EMPTY:
            o_bricks += 1
    
    print(f"#{tc} {bfs()}")
