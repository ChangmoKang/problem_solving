# 올바른 괄호
def solution(s):
    stack = 0
    
    for bracket in s:
        if bracket == '(':
            stack += 1
        else:
            if stack:
                stack -= 1
            else:
                return False
    
    return not stack


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
