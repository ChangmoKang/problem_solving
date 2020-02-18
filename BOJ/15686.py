import sys
sys.stdin = open('input/15686.txt')


def check(count, start):
    global result
    if count == M:
        picked_store = [store[x] for x in store_index]
        sub_result = 0

        for r, c in home:
            home_result = float('inf')
            for rr, cc in picked_store:
                chicken_dist = abs(rr - r) + abs(cc - c)
                if chicken_dist < home_result:
                    home_result = chicken_dist
            sub_result += home_result
        
        if result > sub_result:
            result = sub_result
    else:
        for i in range(start, len(store)):
            store_index[count] = i
            check(count + 1, i + 1)
            store_index[count] = None


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

home = []
store = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            home.append([i, j])
        elif board[i][j] == 2:
            store.append([i, j])

result = float('inf')
store_index = [None]*M
check(0, 0)
print(result)
