# 올바른 괄호
def solution(s):
    value = 0
    for bracket in s:
        if bracket == '(':
            value += 1
        else:
            if value:
                value -= 1
            else:
                return False
    return value == 0


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
