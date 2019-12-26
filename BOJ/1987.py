import sys
sys.stdin = open('input/1987.txt')


def dfs(count, v):
    global result
    for x in range(4):
        rr, cc = v[0] + dr[x], v[1] + dc[x]
        if 0 <= rr < R and 0 <= cc < C:
            if board[rr][cc] not in visited:
                visited.add(board[rr][cc])
                dfs(count + 1, [rr, cc])
                visited.remove(board[rr][cc])
            else:
                if count > result:
                    result = count
                

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

visited = set()
visited.add(board[0][0])
result = 1
dfs(1, [0, 0])
print(result)
