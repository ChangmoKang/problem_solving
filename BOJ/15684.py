import sys
sys.stdin = open('input/15684.txt')


def test():
    for c in range(C):
        curr_loc = c

        for r in range(R):
            if board[r][curr_loc]:
                curr_loc += 1
            elif curr_loc > 0 and board[r][curr_loc - 1]:
                curr_loc -= 1
                
        if c != curr_loc:
            return False
    return True


def check(r, c, count):
    global result
    if count == k:
        if test():
            result = count
    else:
        while True:
            if c == C - 1:
                r += 1
                c = 0
            else:
                c += 1

            if r == R:
                break

            if c != C - 1 and not board[r][c]:
                board[r][c] = 1
                check(r, c, count + 1)
                board[r][c] = 0            


C, M, R = map(int, input().split())
board = [[0]*C for _ in range(R)]
for _ in range(M):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 1

if test():
    print(0)
else:
    result = -1
    for k in range(1, 4):
        if result != - 1:
            break
        check(0, -1, 0)
    print(result)
