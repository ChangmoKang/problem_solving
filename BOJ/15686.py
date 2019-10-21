import sys
sys.stdin = open('input/15686.txt')


def calc(fr, to):
    return abs(fr[1] - to[1]) + abs(fr[0] - to[0])


def check(count, start):
    global result
    if count == K:
        store = [STORE[arr[w]] for w in range(K)]
        total_dist = 0
        for h in home:
            each_dist = float('inf')
            for s in store:
                tmp_dist = calc(h, s)
                if tmp_dist < each_dist:
                    each_dist = tmp_dist
            total_dist += each_dist
            if total_dist > result:
                return
        
        if result > total_dist:
            result = total_dist
    else:
        for i in range(start, len(STORE)):
            arr[count] = i
            check(count + 1, i + 1)
            arr[count] = 0


N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

home = []
STORE = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            home.append([i, j])
        elif board[i][j] == 2:
            board[i][j] = 0
            STORE.append([i, j])


result = float('inf')
arr = [0]*K
check(0, 0)
print(result)
