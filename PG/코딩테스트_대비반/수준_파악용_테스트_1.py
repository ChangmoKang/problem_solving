def solution(s):
    stack = []
    for v in s:
        if v == '(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                return False
    return stack == []


if __name__ == "__main__":
    INPUT = [
        "()()",
        "(())()",
        ")()(",
        ")()("
    ]
    ANSWER = [
        True,
        True,
        False,
        False
    ]
    
    for index in range(len(ANSWER)):
        print(True) if ANSWER[index] == solution(INPUT[index]) else print(False)
