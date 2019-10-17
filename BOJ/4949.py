import sys
sys.stdin = open('input/4949.txt')


def check():
    for target in targets:
        if stack:
            if target == '(':
                stack.append(1)
            elif target == '[':
                stack.append(2)
            elif target == ')' or target == ']':
                if stack[-1] == 1 and target == ')':
                    stack.pop()
                elif stack[-1] == 2 and target == ']':
                    stack.pop()
                else:
                    print('no')
                    return False
        else:
            if target == '(':
                stack.append(1)
            elif target == '[':
                stack.append(2)
            elif target == ')' or target == ']':
                print('no')
                return False
    return True

while True:
    targets = input()
    if targets == '.':
        break
    else:
        targets = list(targets)
        stack = []
        
        if check():
            if stack:
                print('no')
            else:
                print('yes')
