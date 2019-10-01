import sys
sys.stdin = open('input/2105.txt')


def check(route, location, direction, move):
    global result
    if direction == 4:
        if len(route) > result:
            result = len(route)

    elif direction < 2:
        while True:
            location[0] += dr[direction]
            location[1] += dc[direction]
            if 0 <= location[0] < N and 0 <= location[1] < N:
                spot = board[location[0]][location[1]]
                if spot not in route:
                    move[direction] += 1

                    route.append(spot)

                    check(route[:], location[:], direction + 1, move[:])
                else:
                    break
            else:
                break
    elif direction < 4:
        flag = 0
        for _ in range(move[direction - 2]):
            location[0] += dr[direction]
            location[1] += dc[direction]
            if 0 <= location[0] < N and 0 <= location[1] < N:
                spot = board[location[0]][location[1]]
                if spot not in route:
                    route.append(spot)
                else:
                    flag = 1
                    break
            else:
                flag = 1
                break
        if not flag:
            check(route[:], location[:], direction + 1, move)


dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]
for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    result = -1

    for i in range(N - 2):
        for j in range(1, N - 1):
            check([], [i, j], 0, [0, 0])

    print(f"#{tc} {result}")
