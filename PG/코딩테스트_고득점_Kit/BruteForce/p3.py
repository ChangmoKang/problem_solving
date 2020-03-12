from itertools import permutations

def solution(baseball):
    cases = ["".join(list(map(str, case))) for case in permutations(range(1, 10), 3)]
    
    answer = 0
    for case in cases:
        for number, strike, ball in baseball:
            s = b = 0
            number = str(number)

            for v1, v2 in zip(case, number):
                if v1 == v2:
                    s += 1
                elif v1 in number:
                    b += 1

            if s != strike or b != ball:
                break
        else:
            answer += 1
            
    return answer
