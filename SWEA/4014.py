import sys
sys.stdin = open('input/4014.txt')


for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    for idx in range(2):
        if idx:
            board = list(map(list, zip(*board)))
        for i in range(N):
            visited = [0]*N
            flag = 0
            for j in range(N - 1):
                if board[i][j] == board[i][j+1]:
                    pass
                # 왼쪽이 더 높은 경우
                elif board[i][j] == board[i][j+1] + 1:
                    if j + K < N:
                        c = j
                        for _ in range(K):
                            c += 1
                            if board[i][c] != board[i][j+1] or visited[c]:
                                flag = 1
                                break

                        if not flag:
                            c = j
                            for _ in range(K):
                                c += 1
                                visited[c] = 1
                    else:
                        flag = 1
                        break
                # 오른쪽이 더 높은 경우
                elif board[i][j] + 1 == board[i][j+1]:
                    if j - (K - 1) >= 0:
                        c = j + 1
                        for _ in range(K):
                            c -= 1
                            if board[i][c] != board[i][j] or visited[c]:
                                flag = 1
                                break

                        if not flag:
                            c = j + 1
                            for _ in range(K):
                                c -= 1
                                visited[c] = 1
                    else:
                        flag = 1
                        break
                else:
                    flag = 1
                    break
            if not flag:
                result += 1

    print(f"#{tc} {result}")
