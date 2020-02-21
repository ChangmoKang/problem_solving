def solution(arrangement):
    arrangement = arrangement.replace("()", "*").strip("*")
    
    stack, answer = [], 0
    
    for el in arrangement:
        if el == '(':
            stack.append(1)
        elif el == ')':
            answer += stack.pop()
        else:
            answer += len(stack)

    return answer
