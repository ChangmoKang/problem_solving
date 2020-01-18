import sys
sys.stdin = open('input/1232.txt')


def check(v):
    if type(dic[v]) != list:
        return dic[v]
    else:
        if dic[v][0] == '+':
            return check(dic[v][1]) + check(dic[v][2])
        elif dic[v][0] == '-':
            return check(dic[v][1]) - check(dic[v][2])
        elif dic[v][0] == '*':
            return check(dic[v][1]) * check(dic[v][2])
        else:
            return check(dic[v][1]) / check(dic[v][2])


for tc in range(1, 11):
    N = int(input())

    dic = {}
    for _ in range(N):
        INPUT = input().split()
        if len(INPUT) == 4:
            op = INPUT.pop(1)
            v, l, r = list(map(int, INPUT))
            dic[v] = [op, l, r]
            
        else:
            v, num = list(map(int, INPUT))
            dic[v] = num
    
    print(f'#{tc} {int(check(1))}')
