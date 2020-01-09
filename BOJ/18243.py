import sys
sys.stdin = open('input/18243.txt')


# def dfs(start, depth):
#     global result
#     if depth > 6:
#         result = 1
#     else:
#         if not result:
#             for index in range(1, N + 1):
#                 if not visited[index]:
#                     visited[index] = 1
#                     dfs(i, depth + 1)
#                     visited[index] = 0


def bfs(start):
    visited = [0]*(N + 1)
    visited[start] = 1
    
    q = [start]
    cnt = 1
    depth = 0
    while q:
        if depth > 6:
            return False
        qs, q = q, []
        for target in qs:
            for index in range(1, N + 1):
                if board[target][index] and not visited[index]:
                    cnt += 1
                    visited[index] = 1
                    q.append(index)
        depth += 1

    if cnt == N:
        return True
    else:
        return False


answer = ['Small World!', 'Big World!']
N, K = map(int, input().split())
board = [[0]*(N + 1) for _ in range(N + 1)]
for _ in range(K):
    A, B = map(int, input().split())
    board[A][B] = 1
    board[B][A] = 1


result = 0
for i in range(1, N + 1):
    if not bfs(i):
        result = 1
        break

print(answer[result])
