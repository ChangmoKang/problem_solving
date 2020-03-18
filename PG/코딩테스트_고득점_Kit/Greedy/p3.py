def solution(number, k):
    number = list(number)

    answer = []
    for i, num in enumerate(number):
        if not answer:
            answer.append(num)
            continue

        while True:
            if num > answer[-1]:
                answer.pop()
                k -= 1
                               
                if k == 0:
                    break

                if not answer:
                    answer.append(num)
                    break
            else:
                answer.append(num)
                break

        if k == 0:
            answer += number[i:]
            return "".join(answer)

    return "".join(answer[:-k])
