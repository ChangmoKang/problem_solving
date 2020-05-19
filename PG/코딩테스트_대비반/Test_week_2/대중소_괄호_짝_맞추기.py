BRACKET = {
    '{': '}',
    '[': ']',
    '(': ')'
}

def solution(s):
    stack = []
    
    for elem in s:
        if elem in '{[(':
            stack.append(elem)
        else:
            if stack and elem == BRACKET[stack[-1]]:
                stack.pop()
            else:
                return False
    
    return not stack
