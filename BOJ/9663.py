import sys
sys.stdin = open('input/9663.txt')


def check(row):
    global cnt
    if row == N:
        cnt += 1
    else:
        for column in range(N):
            flag = 0
            for rr, cc in visited:
                if cc == column or abs(rr - row) == abs(cc - column):
                    flag = 1
                    break
            if not flag:
                visited.append([row, column])
                check(row + 1)
                visited.remove([row, column])
    
N = int(input())

visited = []
cnt = 0
check(0)

print(cnt)
