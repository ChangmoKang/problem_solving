import sys
sys.stdin = open('input/17142.txt')


def check(count, start):
    global result
    if count == K:
        q = [virus[arr[w]][:] for w in range(K)]
        copied_visited = [visited[w][:] for w in range(N)]
        for r, c in q:
            copied_visited[r][c] = 1
        time = 0
        room_cnt = 0
        while q:
            time += 1
            contents, q = q, []
            for r, c in contents:
                for x in range(4):
                    rr = r + dr[x]
                    cc = c + dc[x]
                    if 0 <= rr < N and 0 <= cc < N and not copied_visited[rr][cc] and board[rr][cc] != 1:
                        copied_visited[rr][cc] = 1
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
visited = [[0]*N for _ in range(N)]

virus = []
room = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus.append([i, j])
        elif board[i][j] == 1:
            visited[i][j] = 1
        else:
            room += 1

if room:
    result = float('inf')
    arr = [0]*K
    v = [0]*len(virus)
    check(0, 0)
    print(result) if result != float('inf') else print(-1)
else:
    print(0)
