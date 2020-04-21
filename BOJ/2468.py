import sys
from itertools import product
from collections import deque
sys.stdin = open('input/2468.txt')
input = sys.stdin.readline


def find_min_max():
    minv, maxv = 100, 0
    for r, c in product(range(N), range(N)):
        if board[r][c] < minv:
            minv = board[r][c]
        if board[r][c] > maxv:
            maxv = board[r][c]

    return minv, maxv


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

answer = 0
L, R = find_min_max()
for h in range(L, R):
    visited = [[False]*N for _ in range(N)]
    cnt = 0
    for i, j in product(range(N), range(N)):
        if not visited[i][j] and board[i][j] > h:
            cnt += 1
            visited[i][j] = True
            q = deque([[i, j]])

            while q:
                r, c = q.popleft()
                for x in range(4):
                    rr, cc = r + dr[x], c + dc[x]
                    if 0 <= rr < N and 0 <= cc < N and board[rr][cc] > h and not visited[rr][cc]:
                        visited[rr][cc] = True
                        q.append([rr, cc])
            
    if cnt > answer:
        answer = cnt

print(answer) if answer else print(1)
