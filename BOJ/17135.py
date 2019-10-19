import sys
sys.stdin = open('input/17135.txt')


def calc(archer, enemy):
    return abs(archer[1] - enemy[1]) + abs(archer[0] - enemy[0])


def check(count, start):
    global result
    if count == 3:
        arrows = [arr[w] for w in range(3)]
        targets = [TARGETS[w][:] for w in range(N)]
        kill = 0
        targets_idx = set(range(N))
        for _ in range(R):
            trash = set()
            for arrow in arrows:
                current_idx = None
                current_dist = D + 1
                for idx in list(targets_idx):
                    dist = calc(arrow, targets[idx])
                    if dist < current_dist:
                        current_idx = idx
                        current_dist = dist
                    elif dist == current_dist and current_idx != None:
                        if targets[idx][1] <= targets[current_idx][1]:
                            current_idx = idx
                if current_idx != None:
                    trash.add(current_idx)

            if trash:
                kill += len(trash)
                targets_idx = targets_idx - trash

            trash = set()

            for idx in list(targets_idx):
                targets[idx][0] += 1
                if targets[idx][0] == R:
                    trash.add(idx)

            if trash:
                targets_idx = targets_idx - trash
        if kill > result:
            result = kill
    else:
        for i in range(start, C):
            arr[count][1] = i
            check(count + 1, i + 1)
            arr[count][1] = 0


R, C, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

TARGETS = []
for i in range(R - 1, -1, -1):
    for j in range(C):
        if board[i][j] == 1:
            TARGETS.append([i, j])

N = len(TARGETS)
result = 0
arr = [[R,0] for _ in range(3)]
check(0, 0)
print(result)
