import sys
sys.stdin = open('input/17779.txt')


def check(r, c, left, right):
    global result
    # 가운데
    for x in range(left):
        visited[r + x][c - x] = 3
    for xx in range(right):
        visited[r + left + xx][c - left + xx] = 3

    for x in range(right):
        visited[r + x][c + x] = 3
    for xx in range(left):
        visited[r + right + xx][c + right - xx] = 3

    visited[r + left + right][c - left + right] = 3


    sum_list = [0,0,0,0]

    # 위로
    for x in range(r):
        visited[x][c] = 1
        sum_list[0] += board[x][c]

    # 왼쪽
    for x in range(c - left):
        visited[r + left][x] = 4
        sum_list[2] += board[r + left][x]

    # 오른쪽
    for x in range(c + right + 1, N):
        visited[r + right][x] = 2
        sum_list[1] += board[r + right][x]

    # 아래
    for x in range(r + left + right + 1, N):
        visited[x][c - left + right] = 5
        sum_list[3] += board[x][c - left + right]

    number = [1, 2, 4, 5]
    number_idx = 0
    for r in [0, N -1]:
        for c in [0, N - 1]:
            visited[r][c] = number[number_idx]
            sum_list[number_idx] += board[r][c]
            q = [[r, c]]
            while q:
                el = q.pop(0)
                for idx in range(4):
                    rr = el[0] + dr[idx]
                    cc = el[1] + dc[idx]
                    if 0 <= rr < N and 0 <= cc < N and not visited[rr][cc]:
                        visited[rr][cc] = number[number_idx]
                        q.append([rr, cc])
                        sum_list[number_idx] += board[rr][cc]
            number_idx += 1

    sum_list.append(total - sum(sum_list))

    sub_result = max(sum_list) - min(sum_list)
    if result > sub_result:
        result = sub_result


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
total = sum([sum(board[i]) for i in range(N)])
result = float('inf')

for i in range(N - 2):
    for j in range(1, N - 1):
        for d1 in range(1, N):
            if i + d1 > N - 1 or j - d1 < 0:
                break
            for d2 in range(1, N):
                if i + d2 > N - 1 or j + d2 > N - 1 or i + d1 + d2 > N - 1:
                    break
                visited = [[0]*N for _ in range(N)]
                check(i, j, d1, d2)

print(result)
