import sys
sys.stdin = open('input/5650.txt')


ways = {
    0: {
        1: 1,
        2: 3,
        3: 2,
        4: 1,
        5: 1
    },
    1 : {
        1: 3,
        2: 0,
        3: 0,
        4: 2,
        5: 0
    },
    2 : {
        1: 0,
        2: 1,
        3: 3,
        4: 3,
        5: 3
    },
    3: {
        1: 2,
        2: 2,
        3: 1,
        4: 0,
        5: 2
    }
}

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    wormholes = [[] for _ in range(5)]
    for i in range(N):
        for j in range(N):
            if 6 <= board[i][j] <= 10:
                wormholes[board[i][j] - 6].append([i, j])

    holes = {}
    for wormhole in wormholes:
        if wormhole:
            holes[tuple(wormhole[0])] = wormhole[1]
            holes[tuple(wormhole[1])] = wormhole[0]

    result = 0

    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                q = [[i, j, w, 0] for w in range(4)]
                while q:
                    current_ball = q.pop(0)
                    rr = current_ball[0] + dr[current_ball[2]]
                    cc = current_ball[1] + dc[current_ball[2]]
                    if 0 <= rr < N and 0 <= cc < N:
                        if (rr == i and cc == j) or board[rr][cc] == -1:
                            if current_ball[-1] > result:
                                result = current_ball[-1]
                        elif board[rr][cc] == 0:
                            q.append([rr, cc, current_ball[2], current_ball[-1]])
                        elif 1 <= board[rr][cc] <= 5:
                            q.append([rr, cc, ways[current_ball[2]][board[rr][cc]], current_ball[-1] + 1])
                        elif 6 <= board[rr][cc] <= 10:
                            t = holes[rr, cc]
                            q.append([t[0], t[1], current_ball[2], current_ball[-1]])
                    else:
                        q.append([rr, cc, ways[current_ball[2]][5], current_ball[-1] + 1])

    print(f"#{tc} {result}")
