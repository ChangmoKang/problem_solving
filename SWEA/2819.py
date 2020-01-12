import sys
sys.stdin = open('input/2819.txt')


def dfs(r, c, count, sub_result):
    if count == 6:
        result.add(sub_result)
    else:
        for x in range(4):
            rr, cc = r + dr[x], c + dc[x]
            if 0 <= rr < N and 0 <= cc < N:
                dfs(rr, cc, count + 1, sub_result + board[rr][cc])


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
N = 4
for tc in range(1, int(input()) + 1):
    board = [input().split() for _ in range(N)]
    result = set()
    for i in range(N):
        for j in range(N):
            dfs(i, j, 0, board[i][j])
    print(f"#{tc} {len(result)}")
