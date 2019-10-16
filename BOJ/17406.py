import sys
sys.stdin = open('input/17406.txt')


def calc(r, c, N, mat):
    for n in range(1, N + 1):
        box1 = mat[r - n + 1][c - n]
        box2 = None
        for w in range(-n, n):
            if box1:
                box2 = mat[r - n][c + w]
                mat[r - n][c + w] = box1
                box1 = None
            else:
                box1 = mat[r - n][c + w]
                mat[r - n][c + w] = box2
                box2 = None

        for w in range(-n, n):
            if box1:
                box2 = mat[r + w][c + n]
                mat[r + w][c + n] = box1
                box1 = None
            else:
                box1 = mat[r + w][c + n]
                mat[r + w][c + n] = box2
                box2 = None

        for w in range(n, -n, -1):
            if box1:
                box2 = mat[r + n][c +w]
                mat[r + n][c +w] = box1
                box1 = None
            else:
                box1 = mat[r + n][c +w]
                mat[r + n][c +w] = box2
                box2 = None

        for w in range(n, -n, -1):
            if box1:
                box2 = mat[r + w][c - n]
                mat[r + w][c - n] = box1
                box1 = None
            else:
                box1 = mat[r + w][c - n]
                mat[r + w][c - n] = box2
                box2 = None
    return mat


def check(count, matrix):
    global result
    if count == K:
        for i in range(R):
            sub_result = sum(matrix[i])
            if result > sub_result:
                result = sub_result
    else:
        for idx in range(K):
            if not visited[idx]:
                visited[idx] = 1
                copied_maxtrix = [matrix[w][:] for w in range(R)]
                copied_maxtrix = calc(methods[idx][0] - 1, methods[idx][1] - 1, methods[idx][2], copied_maxtrix)
                check(count + 1, copied_maxtrix)
                visited[idx] = 0


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
R, C, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
methods = [list(map(int, input().split())) for _ in range(K)]

result = float('inf')

visited = [0]*K
check(0, board)

print(result)
