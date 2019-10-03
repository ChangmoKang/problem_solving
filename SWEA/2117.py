import sys
sys.stdin = open('input/2117.txt')


def calc(r, c, index):
    return abs(customer[index][0] - r) + abs(customer[index][1] - c)

cost = [w*w + (w-1)*(w-1) for w in range(1, 40)]
for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    customer = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                customer.append([i, j])

    result = 0

    for i in range(N):
        for j in range(N):
            dist = sorted([calc(i, j, idx) for idx in range(len(customer))])
            for x in range(len(dist)):
                if cost[dist[x]] <= (x + 1) * K:
                    if x + 1 > result:
                        result = x + 1

    print(f"#{tc} {result}")
