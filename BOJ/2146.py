import sys
sys.stdin = open('input/2146.txt')


def init():
    for index in range(island_N):
        for r, c in each_wide[index]:
            if not board[r][c]:
                if not visited[r][c]:
                    visited[r][c] = 1
                board[r][c] = index + 1
            else:
                return 1
    return 0


def check():
    global each_wide, result
    cnt = 1
    while True:
        sub_result = float('inf')
        cnt += 1
        target, each_wide = each_wide, []
        for index in range(island_N):
            island_id = index + 1
            wide = set()
            for r, c in target[index]:
                board[r][c] = island_id
                for x in range(4):
                    rr, cc = r + dr[x], c + dc[x]
                    if 0 <= rr < N and 0 <= cc < N:
                        if board[rr][cc] and board[rr][cc] != island_id:
                            if board[rr][cc] > island_id:
                                return 2 * (cnt - 1)
                            else:
                                sub_result = 2 * (cnt - 1) + 1
                        if not visited[rr][cc]:
                            visited[rr][cc] = 1
                            board[rr][cc] = island_id
                            wide.add((rr, cc))
            each_wide.append(wide)
        if sub_result != float('inf'):
            return sub_result


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]


island_id = 1
visited = [[0]*N for _ in range(N)]
each_wide = []
for i in range(N):
    for j in range(N):
        wide = set()
        if board[i][j] and not visited[i][j]:
            visited[i][j] = 1
            board[i][j] = island_id
            q = [[i, j]]
            while q:
                qs, q = q, []
                for r, c in qs:
                    for x in range(4):
                        rr, cc = r + dr[x], c + dc[x]
                        if 0 <= rr < N and 0 <= cc < N:
                            if board[rr][cc]:
                                if not visited[rr][cc]:
                                    visited[rr][cc] = 1
                                    board[rr][cc] = island_id
                                    q.append([rr, cc])
                            else:
                                wide.add((rr, cc))
            island_id += 1
            each_wide.append(wide)

island_N = len(each_wide)

result = init()
if not result:
    result = check()

print(result)
