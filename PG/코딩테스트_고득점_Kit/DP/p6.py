def solution(money):
    N = len(money)

    rob_0 = [0]*N
    rob_0[0:2] = [money[0]]*2
    for i in range(2, N - 1):
        rob_0[i] = max(rob_0[i - 1], money[i] + rob_0[i - 2])

    skip_0 = [0]*N
    skip_0[1] = money[1]
    for i in range(2, N):
        skip_0[i] = max(skip_0[i - 1], money[i] + skip_0[i - 2])

    return max(rob_0[-2], skip_0[-1])
