import sys
sys.stdin = open('input/1220.txt')

for tc in range(1, 11):
    N = int(input())
    board = [input().split() for _ in range(N)]

    result = 0
    for j in range(N):
        flag = 0
        for i in range(N):
            if flag == 0 and board[i][j] == "1":
                flag = 1
            elif flag == 1 and board[i][j] == "2":
                result += 1
                flag = 0
    
    print(f"#{tc} {result}")
