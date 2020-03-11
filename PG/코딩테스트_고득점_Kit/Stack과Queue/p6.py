def solution(prices):
    N = len(prices)
    answer = [0]*N
    for i in range(N):
        i_moment_price = prices[i]
        for j in range(i + 1, N):
            j_moment_price = prices[j]
            answer[i] += 1
            if i_moment_price > j_moment_price:
                break
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