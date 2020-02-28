def solution(s):
    opposite = {
        '(': ')',
        ')': '(',
        '{': '}',
        '}': '{',
        '[': ']',
        ']': '['
    }
    
    stack = []
    for bracket in s:
        if bracket in '({[':
            stack.append(bracket)
        else:
            if stack and bracket == opposite[stack[-1]]:
                stack.pop()
            else:
                return False
    
    return not stack
