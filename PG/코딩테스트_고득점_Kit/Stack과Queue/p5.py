def solution(arrangement):
    answer = 0
    arrangement = arrangement.replace("()","*")
    stack = []
    cnt = 0
    for i in range(len(arrangement)):
        each = arrangement[i]
        if each == '(':
            stack.append(1)
        elif each == ')':
            answer += stack.pop()
        elif stack and each == '*':
            cnt += 1
            if arrangement[i + 1] != '*':
                for x in range(len(stack)):
                    stack[x] += cnt
                cnt = 0
    return answer


if __name__ == "__main__":
    INPUT1 = [
        "()(((()())(())()))(())"
    ]
    ANSWER = [
        17
    ]

    for index in range(1):
        print(True) if ANSWER[index] == solution(INPUT1[index]) else print(False)