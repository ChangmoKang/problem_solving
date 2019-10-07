import sys
sys.stdin = open('input/1018.txt')


line = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
correct = [
    [line[w % 2] for w in range(8)],
    [line[(w + 1) % 2] for w in range(8)]
]
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]

    result = float('inf')

    for i in range(N - 7):
        for j in range(M - 7):
            for k in range(2):
                sub_result = 0
                flag = 0
                for r in range(8):
                    for c in range(8):
                        if sub_result >= result:
                            flag = 1
                            break
                        if board[i + r][j + c] != correct[k][r][c]:
                            sub_result += 1
                    if flag:
                        break
                if not flag:
                    result = sub_result

    print(result)
