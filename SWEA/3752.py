import sys
sys.stdin = open('input/3752.txt')


for tc in range(1, int(input()) + 1):
    N = int(input())
    scores = list(map(int, input().split()))
    board = [1] + [0] * 10000

    max_value = sum(scores)
    for score in scores:
        for index in range(max_value, -1, -1):
            if board[index]:
                board[index + score] = 1

    print(f"#{tc} {sum(board[:max_value]) + 1}")
