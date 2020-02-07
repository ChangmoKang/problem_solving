def solution(N, works):
    while N:
        works.sort(reverse=True)
        max_value = works[0]
        min_value = works[-1]

        if max_value == min_value:
            if N >= len(works):
                q = N // len(works)
                works = [work - q for work in works]
                N -= q * len(works)

            for i in range(N):
                works[i] -= 1
            N = 0

        else:
            for idx in range(len(works)):
                work = works[idx]
                if work < max_value:
                    diff = max_value - work
                    for _ in range(diff):
                        if not N:
                            break

                        for i in range(idx):
                            if N:
                                works[i] -= 1
                                N -= 1
                            else:
                                break
                    break

    for idx, work in enumerate(works):
        if work < 0:
            works[idx] = 0

    if max(works):
        dic = {}
        for work in works:
            if work not in dic:
                dic[work] = 1
            else:
                dic[work] += 1

        result = 0
        for key, value in dic.items():
            result += value * pow(key, 2)
        return result

    else:
        return 0


if __name__ == "__main__":
    INPUT1 = [
        4,
        2
    ]
    INPUT2 = [
        [4, 3, 3],
        [3, 3, 3]
    ]
    ANSWER = [
        12,
        17
    ]
    
    for index in range(len(ANSWER)):
        print(True) if ANSWER[index] == solution(INPUT1[index], INPUT2[index]) else print(False)
