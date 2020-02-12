import sys
sys.stdin = open('input/18428.txt')


def is_student_safe():
    for r, c in teachers:
        for x in range(4):
            rr, cc = r + dr[x], c + dc[x]
            while True:
                if not (0 <= rr < N and 0 <= cc < N) or board[rr][cc] == 'O':
                    break

                if board[rr][cc] == 'S':
                    return False

                rr += dr[x]
                cc += dc[x]
    return True


def check(r, c, count):
    global result
    if count == 3:
        if is_student_safe():
            result = "YES"
    else:
        while True:
            if result == "YES":
                break

            if c + 1 == N:
                r += 1
                c = 0
            else:
                c += 1

            if r == N:
                break

            if board[r][c] == 'X':
                board[r][c] = 'O'
                check(r, c, count + 1)
                board[r][c] = 'X'


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
N = int(input())
board = [input().split() for _ in range(N)]

result = "NO"
teachers = [[i, j] for i in range(N) for j in range(N) if board[i][j] == 'T']
check(0, -1, 0)

print(result)
