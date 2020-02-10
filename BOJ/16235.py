import sys
sys.stdin = open('input/16235.txt')


dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]
N, M, K = map(int, input().split())
land = [[5]*N for _ in range(N)]
add = [list(map(int, input().split())) for _ in range(N)]
live = {(i, j): [] for i in range(N) for j in range(N)}
for _ in range(M):
    i, j, age = map(int, input().split())
    live[i - 1, j - 1].append(age)

for _ in range(K):
    # 봄, 여름
    for loc, trees in live.items():
        r, c = loc

        if land[r][c] >= sum(trees):
            live[r, c] = [trees[i] + 1 for i in range(len(trees))]
            land[r][c] -= sum(trees)
        else:
            for index in range(len(trees)):
                tree = trees[index]
                if land[r][c] >= tree:
                    land[r][c] -= tree
                else:
                    break
            live[r, c] = [trees[i] + 1 for i in range(index)]
            land[r][c] += sum([int(trees[i]/2) for i in range(index, len(trees))])


    # 가을
    for loc, trees in live.items():
        r, c = loc
        for tree in trees:
            if tree % 5 == 0:
                for x in range(8):
                    rr, cc = r + dr[x], c + dc[x]
                    if 0 <= rr < N and 0 <= cc < N:
                        live[rr, cc].insert(0, 1)

    # 겨울
    for i in range(N):
        for j in range(N):
            land[i][j] += add[i][j]

print(sum([len(value) for value in live.values()]))
