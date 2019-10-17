import sys
sys.stdin = open('input/9012.txt')


def check():
    for target in targets:
        if stack:
            if target == '(':
                stack.append(0)
            else:
                if stack[-1] == 0:
                    stack.pop()
                else:
                    stack.append(1)
        else:
            if target == '(':
                stack.append(0)
            else:
                print('NO')
                return False
    return True


N = int(input())
for _ in range(N):
    targets = list(input())
    stack = []

    if check():
        if stack:
            print('NO')
        else:
            print('YES')
