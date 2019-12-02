def solution(prices):
    answer = []
    for index1 in range(len(prices) - 1):
        price1 = prices[index1]
        flag = 0
        for index2 in range(index1 + 1, len(prices)):
            price2 = prices[index2]
            if price1 > price2:
                answer.append(index2 - index1)
                flag = 1
                break
        if not flag:
            answer.append(index2 - index1)
    answer.append(0)
    return answer


if __name__ == "__main__":
    INPUT1 = [
        [1, 2, 3, 2, 3]
    ]
    ANSWER = [
        [4, 3, 1, 1, 0]
    ]

    for index in range(1):
        print(True) if ANSWER[index] == solution(INPUT1[index]) else print(False)