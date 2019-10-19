import sys
sys.stdin = open('input/17135.txt')


def check(count, start):
    global result
    if count == K:
        time = 0
        room_cnt = 0
        q = [virus[arr[w]][:] for w in range(K)]
        visited = [[0]*N for _  in range(N)]
        for r, c in q:
            visited[r][c] = 1
        while q:
            time += 1
            if result < time:
                return
            contents, q = q, []
            for r, c in contents:
                for x in range(4):
                    rr = r + dr[x]
                    cc = c + dc[x]
                    if 0 <= rr < N and 0 <= cc < N and not visited[rr][cc] and board[rr][cc] != 1:
                        visited[rr][cc] = 1
                        if board[rr][cc] == 0:
                            room_cnt += 1
                        if room_cnt == room:
                            if result > time:
                                result = time
                                return
                        q.append([rr, cc])
    else:
        for i in range(start, len(virus)):
            arr[count] = i
            check(count + 1, i + 1)
            arr[count] = 0


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

room = -K
virus = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 0:
            room += 1
        elif board[i][j] == 2:
            virus.append([i, j])
            board[i][j] = 0
            room += 1

if room:
    result = float('inf')
    arr = [0]*K
    check(0, 0)
    print(result) if result != float('inf') else print(-1)
else:
    print(0)
