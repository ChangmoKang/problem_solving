import sys
from itertools import combinations
sys.stdin = open('input/18809.txt')
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

KIND = 1
EMPTY, RED, GREEN, FLOWER = 0, 1, 2, 3

N, M, G, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
available = [(i, j) for i in range(N) for j in range(M) if board[i][j] == 2]

result = 0
for R_available in combinations(range(len(available)), R):
    left_available = set(range(len(available))) - set(R_available)
    for G_available in combinations(left_available, G):
        sub_result = 0
        visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

        red = [available[elem] for elem in R_available]
        green = [available[elem] for elem in G_available]

        for r, c in red:
            visited[r][c][KIND] = RED
        
        for r, c in green:
            visited[r][c][KIND] = GREEN

        time = 0
        while red and green:
            time += 1

            reds, red = red, []
            for r, c in reds:
                if visited[r][c][KIND] == FLOWER:
                    continue

                for x in range(4):
                    rr, cc = r + dr[x], c + dc[x]
                    if not (0 <= rr < N and 0 <= cc < M) or board[rr][cc] == 0:
                        continue

                    if visited[rr][cc][KIND] == EMPTY:
                        visited[rr][cc] = [time, RED]
                        red.append([rr, cc])


            greens, green = green, []
            for r, c in greens:
                for x in range(4):
                    rr, cc = r + dr[x], c + dc[x]
                    if not (0 <= rr < N and 0 <= cc < M) or board[rr][cc] == 0:
                        continue

                    if visited[rr][cc][KIND] == EMPTY:
                        visited[rr][cc] = [time, GREEN]
                        green.append([rr, cc])

                    elif visited[rr][cc] == [time, RED]:
                        visited[rr][cc][KIND] = FLOWER
                        sub_result += 1

        if sub_result > result:
            result = sub_result

print(result)
