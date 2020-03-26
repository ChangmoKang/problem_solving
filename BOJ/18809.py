import sys
from itertools import combinations
sys.stdin = open('input/18809.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M, G, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
available = [(i, j) for i in range(N) for j in range(M) if board[i][j] == 2]

result = 0
for tmp_a in combinations(range(len(available)), R):
    tmp = set(range(len(available))) - set(tmp_a)
    for tmp_b in combinations(tmp, G):
        sub_result = 0
        visited = [[0]*M for _ in range(N)]

        a = {available[t] for t in tmp_a}
        b = {available[t] for t in tmp_b}

        for r, c in a:
            visited[r][c] = 1
        
        for r, c in b:
            visited[r][c] = 1

        time = 1
        while a and b:
            time += 1

            aa, a = a, set()
            for r, c in aa:
                for x in range(4):
                    rr, cc = r + dr[x], c + dc[x]
                    if 0 <= rr < N and 0 <= cc < M and not visited[rr][cc] and board[rr][cc] != 0:
                        visited[rr][cc] = time
                        a.add((rr, cc))

            bb, b = b, set()
            for r, c in bb:
                for x in range(4):
                    rr, cc = r + dr[x], c + dc[x]
                    if 0 <= rr < N and 0 <= cc < M and (not visited[rr][cc] or visited[rr][cc] == time) and board[rr][cc] != 0:
                        if visited[rr][cc] == time and (rr, cc) not in b:
                            visited[rr][cc] = float('inf')
                            a.remove((rr, cc))
                            sub_result += 1
                            continue

                        visited[rr][cc] = time
                        b.add((rr, cc))

        if sub_result > result:
            result = sub_result

print(result)
