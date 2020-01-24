import sys
sys.stdin = open('input/17135.txt')


def check(count, start):
    global result
    if count == 3:
        targets = [TARGETS[w][:] for w in range(N)]

        sub_result = 0
        for _ in range(R):
            kills = list()
            for archer in archers:
                min_d = D
                min_l = None
                for target in targets:
                    target_r, target_c = target
                    d = abs(R - target_r) + abs(archer - target_c)
                    if min_d > d:
                        min_d = d
                        min_l = target
                    elif min_d == d:
                        if min_l == None or min_l[1] > target_c:
                            min_l = target

                if min_l != None and min_l not in kills:
                    kills.append(min_l)

            sub_result += len(kills)

            for kill in kills:
                targets.remove(kill)

            trash = list()
            for index in range(len(targets)):
                target_r, target_c = targets[index]
                targets[index] = [target_r + 1, target_c]
                if targets[index][0] == R:
                    trash.append(targets[index])
            
            for t in trash:
                targets.remove(t)

        result = max(sub_result, result)

    else:
        for i in range(start, C):
            archers[count] = i
            check(count + 1, i + 1)
            archers[count] = -1


R, C, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
TARGETS = [[r, c] for r in range(R - 1, -1, -1) for c in range(C) if board[r][c]]
N = len(TARGETS)

result = -1
archers = [-1]*3
check(0, 0)

print(result)
