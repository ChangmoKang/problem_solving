import sys
sys.stdin = open('input/5209.txt')


def check(order, sub_result):
    global result
    if order == N:
        if result > sub_result:
            result = sub_result
    else:
        for j in range(N):
            if sub_result > result:
                break
            if not visited[j]:
                visited[j] = 1
                check(order + 1, sub_result + board[order][j])
                visited[j] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    result = float('inf')
    check(0, 0)
    print(f"#{tc} {result}")
