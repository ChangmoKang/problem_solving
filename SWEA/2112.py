import sys
sys.stdin = open('input/2112.txt')


def inspector():
    for j in range(C):
        flag = 0
        for i in range(R - (K - 1)):
            tmp = sum([board[i+x][j] for x in range(K)])
            if tmp == 0 or tmp == K:
                flag = 1
                break
        if not flag:
            return 0
    return 1


def check(count, start):
    global result
    if count == k:
        if inspector():
            result = k
            return
    else:
        for i in range(start, R):
            if result > k:
                saved = board[i]
                for w in range(2):
                    board[i] = film[w]
                    check(count + 1, i + 1)
                board[i] = saved


for tc in range(1, int(input()) + 1):
    R, C, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(R)]

    film = [[0]*C, [1]*C]
    result = K

    for k in range(K):
        if result <= k:
            break
        target = [0]*k
        check(0, 0)

    print(f"#{tc} {result}")
