import sys
sys.stdin = open('input/14890.txt')

def check(slope):
    visited = [False]*N

    for i in range(N - 1):
        if slope[i] == slope[i + 1] + 1: # 왼쪽이 큰 경우
            for x in range(1, L + 1):
                if i + x >= N:
                    return 0
                elif slope[i + x] != slope[i + 1]:
                    return 0

            for x in range(1, L + 1):
                visited[i + x] = True

        elif slope[i] + 1 == slope[i + 1]: # 오른쪽이 큰 경우
            for x in range(L):
                if i - x < 0:
                    return 0
                elif visited[i - x]:
                    return 0
                elif slope[i - x] != slope[i]:
                    return 0

            for x in range(L):
                visited[i - x] = True

        elif abs(slope[i] - slope[i + 1]) > 1: # 높이 차이가 1 초과인 경우
            return 0
    
    return 1


N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
trans_board = list(map(list, zip(*board)))

print(sum(check(board[i]) + check(trans_board[i]) for i in range(N)))
