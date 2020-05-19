def solution(s):
    stack = []
    for elem in s:
        if stack and stack[-1] == elem:
            stack.pop()
        else:
            stack.append(elem)
    
    return 1 if not stack else 0
