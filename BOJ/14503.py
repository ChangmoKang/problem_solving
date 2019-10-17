import sys
sys.stdin = open('input/14503.txt')


def rotate():
    if status[2] == 0:
        status[2] = 3
    else:
        status[2] -= 1


d = [[-1, 0], [0, 1], [1, 0], [0, -1]]
ways = {
    0: [d[3], d[2], d[1], d[0]],
    1: [d[0], d[3], d[2], d[1]],
    2: [d[1], d[0], d[3], d[2]],
    3: [d[2], d[1], d[0], d[3]]
}

R, C = map(int, input().split())
status = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(R)]
visited = [board[w][:] for w in range(R)]

clear = 1
visited[status[0]][status[1]] = 1

while True:
    flag = 0
    for dr, dc in ways[status[2]]:
        rr = status[0] + dr
        cc = status[1] + dc

        rotate()

        if 0 <= rr < R and 0 <= cc < C and not visited[rr][cc]:
            status[0] = rr
            status[1] = cc

            visited[rr][cc] = 1
            clear += 1

            flag = 1
            break

    if not flag:
        for _ in range(2):
            rotate()
        rr = status[0] + d[status[2]][0]
        cc = status[1] + d[status[2]][1]
        if 0 <= rr < R and 0 <= cc < C and board[rr][cc] != 1:
            status[0] = rr
            status[1] = cc
            for _ in range(2):
                rotate()
        else:
            break

print(clear)
