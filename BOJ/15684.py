import sys
sys.stdin = open('input/15684.txt')


def test():
    for c in range(C):
        location = c
        for r in range(R):
            if location - 1 >= 0 and board[r][location - 1]:
                location -= 1
            elif location < C - 1 and board[r][location]:
                location += 1
        if location != c:
            return 0
    return 1


def check(r, c, count):
    global result
    if count == 3:
        pass
    else:
        if result > count + 1:
            while True:
                if c == (C - 1) - 1:
                    r += 1
                    c = 0
                else:
                    c += 1

                if r == R:
                    break


                if board[r][c] or (c - 1 >= 0 and board[r][c - 1]) or (c + 1 < C - 1 and board[r][c + 1]):
                    continue
                
                board[r][c] = 1
                if test():
                    result = count + 1
                check(r, c, count + 1)
                board[r][c] = 0


C, K, R = map(int, input().split())
board = [[0]*(C - 1) for _ in range(R)]
result = float('inf')

for _ in range(K):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1

if K == 0:
    print(0)
elif K == R * (C - 1):
    if test():
        print(0)
    else:
        print(-1)
else:
    if test():
        print(0)
    else:
        check(0, -1, 0)
        print(result) if result != float('inf') else print(-1)
