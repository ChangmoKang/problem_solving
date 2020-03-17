def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    Intersection = lost & reserve
    
    lost -= Intersection
    reserve -= Intersection
    
    answer = n - len(lost)
    
    for student in lost:
        if student - 1 > 0 and student - 1 in reserve:
            answer += 1
            reserve.remove(student - 1)
        elif student + 1 <= n and student + 1 in reserve:
            answer += 1
            reserve.remove(student + 1)

    return answer
