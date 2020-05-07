def solution(s):
    s = s[2:-2].split("},{")
    s.sort(key=len)

    answer = []
    for tuple_ in s:
        tuple_ = list(map(int, tuple_.split(',')))
        for elem in tuple_:
            if elem not in answer:
                answer.append(elem)

    return answer
    