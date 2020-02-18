from math import ceil

def solution(progresses, speeds):
    answer = []
    
    N = len(progresses)
    remains = [ceil((100 - p) / s) for p, s in zip(progresses, speeds)]

    front = 0
    for index in range(len(remains)):
        if remains[index] > remains[front]:
            answer.append(index - front)
            front = index
    else:
        answer.append(N - front)

    return answer
