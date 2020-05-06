from itertools import permutations


def solution(n, weak, dist):
    W, D = len(weak), len(dist)
    
    for friend_N in range(1, D + 1):
        for order in permutations(dist, friend_N):
            for i in range(W):
                target = weak[i:] + [n + w for w in weak[:i]]

                if target[-1] - target[0] <= sum(order):
                    return friend_N

                start = 0
                for ord in order:
                    inc = 0
                    while True:
                        if target[start + inc] - target[start] <= ord:
                            inc += 1
                            if start + inc == W:
                                return friend_N
                        else:
                            start += inc
                            break

    return -1
