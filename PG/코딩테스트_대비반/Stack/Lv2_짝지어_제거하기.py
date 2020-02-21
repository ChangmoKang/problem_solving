def solution(s):
    stack = []
    for el in s:
        if stack:
            if el == stack[-1]:
                stack.pop()
            else:
                stack.append(el)
        else:
            stack.append(el)

    return 0 if stack else 1
