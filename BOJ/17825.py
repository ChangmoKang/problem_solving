import sys
sys.stdin = open('input/17825.txt')


def check(count, sub_result):
    global result
    if count == 10:
        if sub_result > result:
            result = sub_result
    else:
        for i in range(4):
            r, c = horse[i]
            if r != 9:
                rr, cc = move(r, c, ps[count])
                if [rr, cc] == [9, 0] or [rr, cc] not in horse:
                    horse[i] = [rr, cc]
                    check(count + 1, sub_result + board[rr][cc])
                    horse[i] = [r, c]


def move(rr, cc, value):
    if 0 <= rr <= 2:
        if cc == len(board[rr]) - 1:
            rr += 4
            cc = -1 + value
        else:
            cc += value
    else:
        cc += value

    while True:
        flag = 0
        if 0 <= rr <= 2:
            if cc >= len(board[rr]):
                flag = 1
                cc -= len(board[rr])
                rr += 1

        elif rr == 3 or rr == 7:
            if cc >= len(board[rr]):
                flag = 1
                cc -= len(board[rr])
                rr = 8

        elif 4 <= rr <= 6:
            if cc >= len(board[rr]):
                flag = 1
                cc -= len(board[rr])
                rr = 7

        elif rr == 8:
            if cc >= len(board[rr]):
                flag = 1
                cc = 0
                rr = 9

        if not flag:
            return rr, cc


board = [
    [2, 4, 6, 8, 10],       # 0
    [12, 14, 16, 18, 20],   # 1
    [22, 24, 26, 28, 30],   # 2
    [32, 34, 36, 38],       # 3
    [13, 16, 19],           # 4
    [22, 24],               # 5
    [28, 27, 26],           # 6
    [25, 30, 35],           # 7
    [40],                   # 8
    [0]                     # 9
]

ps = list(map(int, input().split()))
horse = [[0, -1] for _ in range(4)]

result = 0
check(0, 0)
print(result)
