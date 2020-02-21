def solution(s):
    s = list(s)
    
    answer = [s.pop()]
    
    while s:
        el = s.pop()

        if answer[-1] <= el:
            answer.append(el)

    return "".join(answer[::-1])
