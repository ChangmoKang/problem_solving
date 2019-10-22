import sys
sys.stdin = open('input/17780.txt')


def move(idx):
    r, c, d = chess[idx]
    rr, cc = chess[idx][0] + dr[d], chess[idx][1] + dc[d]

    if 0 <= rr < N and 0 <= cc < N and board[rr][cc] != 2:
        return rr, cc, d
    elif not (0 <= rr < N and 0 <= cc < N) or board[rr][cc] == 2:
        other_d = other_ways[d]
        o_rr, o_cc = chess[idx][0] + dr[other_d], chess[idx][1] + dc[other_d]
        if 0 <= o_rr < N and 0 <= o_cc < N and board[o_rr][o_cc] != 2:
            return o_rr, o_cc, other_d
        elif not (0 <= o_rr < N and 0 <= o_cc < N) or board[o_rr][o_cc] == 2:
            return r, c, other_d


def check():
    for time in range(1, 1001):
        for idx in range(K):
            r, c, _ = chess[idx]
            rr, cc, dd = move(idx)
            
            start = dic[r, c].index(idx)
            if start == 0:
                if not (r == rr and c == cc):
                    if board[rr][cc] == 1:
                        dic[rr, cc].extend(dic[r, c][::-1])
                    else:
                        dic[rr, cc].extend(dic[r, c])

                    if len(dic[rr, cc]) >= 4:
                        return time

                if len(dic[r, c]) > 1:
                    if board[rr][cc] == 1:
                        for x_idx in range(len(dic[r, c]) - 1, start - 1, -1):
                            x = dic[r, c][x_idx]
                            if x == idx:
                                chess[x] = [rr, cc, dd]
                            else:
                                chess[x] = [rr, cc, chess[x][2]]
                    else:
                        for x_idx in range(start, len(dic[r, c])):
                            x = dic[r, c][x_idx]
                            if x == idx:
                                chess[x] = [rr, cc, dd]
                            else:
                                chess[x] = [rr, cc, chess[x][2]]
                else:
                    chess[idx] = [rr, cc, dd]
                if not (r == rr and c == cc):
                    dic[r, c] = []
    return -1


other_ways = {
    0: 1,
    1: 0,
    2: 3,
    3: 2
}

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
chess = []
for _ in range(K):
    r, c, d = map(int, input().split())
    chess.append([r - 1, c - 1, d - 1])

dic = {}
for i in range(N):
    for j in range(N):
        dic[i, j] = []

for i in range(K):
    dic[chess[i][0], chess[i][1]].append(i)

print(check())
