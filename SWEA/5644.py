import sys
sys.stdin = open('input/5644.txt')


def charging():
    global result
    possible_charger_idx = [[], []]
    for idx in range(len(chargers)):
        for i in range(2):
            dist = abs(people[i][0] - chargers[idx][0]) + abs(people[i][1] - chargers[idx][1])
            if dist <= chargers[idx][2]:
                possible_charger_idx[i].append(idx)

    sub_result = 0

    if possible_charger_idx[0] and not possible_charger_idx[1]:
        for idx in possible_charger_idx[0]:
            if chargers[idx][3] > sub_result:
                sub_result = chargers[idx][3]

    elif possible_charger_idx[1] and not possible_charger_idx[0]:
        for idx in possible_charger_idx[1]:
            if chargers[idx][3] > sub_result:
                sub_result = chargers[idx][3]

    elif possible_charger_idx[0] and possible_charger_idx[1]:
        for i in possible_charger_idx[0]:
            for j in possible_charger_idx[1]:
                if i == j:
                    if chargers[i][3] > sub_result:
                        sub_result = chargers[i][3]
                else:
                    tmp = chargers[i][3] + chargers[j][3]
                    if tmp > sub_result:
                        sub_result = tmp

    result += sub_result


dx = [0, 0, 1, 0, -1]
dy = [0, -1, 0, 1, 0]
for tc in range(1, int(input()) + 1):
    K, A = map(int, input().split())
    people = [[1, 1], [10, 10]]
    moves = [list(map(int, input().split())) for _ in range(2)]
    chargers = [list(map(int, input().split())) for _ in range(A)]

    result = 0

    for k in range(K):
        charging()
        for i in range(2):
            people[i][0] += dx[moves[i][k]]
            people[i][1] += dy[moves[i][k]]
    charging()

    print(f"#{tc} {result}")
