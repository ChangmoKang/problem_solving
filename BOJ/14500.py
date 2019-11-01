import sys
sys.stdin = open('input/14500.txt')


def dfs(r, c, count, sub_result):
    global result
    if count == 3:
        if sub_result > result:
            result = sub_result
    else:
        for x in range(4):
            rr = r + dr[x]
            cc = c + dc[x]
            if 0 <= rr < R and 0 <= cc < C and not visited[rr][cc]:
                visited[rr][cc] = 1
                dfs(rr, cc, count + 1, sub_result + board[rr][cc])
                visited[rr][cc] = 0


def edge(r, c, sub_result):
    global result
    for index in range(4):
        flag = 0
        tmp_result = sub_result
        for x in ways[index]:
            rr = r + dr[x]
            cc = c + dc[x]
            if 0 <= rr < R and 0 <= cc < C:
                tmp_result += board[rr][cc]
            else:
                flag = 1
                break
        if not flag:
            if tmp_result > result:
                result = tmp_result


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ways = {
    0: [0, 1, 2],
    1: [1, 2, 3],
    2: [2, 3, 0],
    3: [3, 0, 1]
}

R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
visited = [[0]*C for _ in range(R)]

result = 0

for i in range(R):
    for j in range(C):
        visited[i][j] = 1
        dfs(i, j, 0, board[i][j])
        visited[i][j] = 0
        edge(i, j, board[i][j])

print(result)
