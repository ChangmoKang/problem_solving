import sys
from itertools import product
from collections import deque
sys.stdin = open('input/17472.txt')


def get_parent(x):
    if parent[x] == x:
        return x
    
    parent[x] = get_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    return True if a == b else False


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
visited = [[0]*C for _ in range(R)]

num = 0
for i, j in product(range(R), range(C)):
    if not visited[i][j] and board[i][j]:
        num += 1

        q = deque([[i, j]])
        visited[i][j] = num

        while q:
            r, c = q.popleft()
            for x in range(4):
                rr, cc = r + dr[x], c + dc[x]
                if 0 <= rr < R and 0 <= cc < C and not visited[rr][cc] and board[rr][cc]:
                    visited[rr][cc] = num
                    q.append([rr, cc])

parent = list(range(num + 1))

adj = {}

for r, c in product(range(R), range(C)):
    if board[r][c]:
        for x in range(4):
            rr, cc = r, c
            dist = 0
            while True:
                rr += dr[x]
                cc += dc[x]

                if not (0 <= rr < R and 0 <= cc < C):
                    break

                if not board[rr][cc]:
                    dist += 1
                    continue

                if visited[r][c] == visited[rr][cc]:
                    break

                if board[rr][cc] and visited[r][c] != visited[rr][cc]:
                    if dist < 2:
                        break

                    a, b = visited[r][c], visited[rr][cc]

                    if a < b:
                        if (a, b) not in adj:
                            adj[a, b] = dist
                        else:
                            if adj[a, b] > dist:
                                adj[a, b] = dist
                    else:
                        if (b, a) not in adj:
                            adj[b, a] = dist
                        else:
                            if adj[b, a] > dist:
                                adj[b, a] = dist

                    break

result = []
for node, value in adj.items():
    result.append([node[0], node[1], value])
result.sort(key=lambda x: x[2])

answer = 0
cnt = 0
for a, b, v in result:
    if not find_parent(a, b):
        union_parent(a, b)
        cnt += 1
        answer += v

for i in range(1, num + 1):
    get_parent(i)

print(answer) if sum(parent) == num else print(-1)
