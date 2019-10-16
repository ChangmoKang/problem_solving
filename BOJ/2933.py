import sys
sys.stdin = open('input/2933.txt')


def destroy(row, index):
    if index % 2:
        for c in range(C - 1, -1, -1):
            if board[row][c] == 'x':
                board[row][c] = '.'
                return
    else:
        for c in range(C):
            if board[row][c] == 'x':
                board[row][c] = '.'
                return


def check_bottom(column):
    q = [[R - 1, column]]
    while q:
        r, c = q.pop(0)
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            if 0 <= rr < R and 0 <= cc < C and not visited[rr][cc] and board[rr][cc] == 'x':
                visited[rr][cc] = 1
                q.append([rr, cc])


def check_float_cluster():
    cluster = []
    for r in range(R - 2, -1, -1):
        for c in range(C):
            if not visited[r][c] and board[r][c] == 'x':
                q = [[r, c]]
                cluster.append([r, c])
                visited[r][c] = 2
                while q:
                    row, column = q.pop(0)
                    for i in range(4):
                        rr = row + dr[i]
                        cc = column + dc[i]
                        if 0 <= rr < R and 0 <= cc < C and not visited[rr][cc] and board[rr][cc] == 'x':
                            visited[rr][cc] = 2
                            q.append([rr, cc])
                            cluster.append([rr, cc])
                return cluster
    return None


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
K = int(input())
target_rows = [R - w for w in list(map(int, input().split()))]

for order in range(K):
    destroy(target_rows[order], order)

    visited = [[0]*C for _ in range(R)]

    for c in range(C):
        if board[R - 1][c] == 'x':
            visited[R - 1][c] = 1
            check_bottom(c)

    float_cluster = check_float_cluster()
    
    if float_cluster:
        min_depth = float('inf')
        
        for r, c in float_cluster:
            depth = (R - 1) - r
            for rr in range(r + 1, R):
                if board[rr][c] == 'x' and visited[rr][c] == 1:
                    depth = (rr - 1) - r
                    break
                
            if min_depth > depth:
                min_depth = depth
        
        for r, c in float_cluster:
            board[r][c] = '.'

        for r, c in float_cluster:
            board[r + min_depth][c] = 'x'

for x in range(R):
    print("".join(board[x]))
