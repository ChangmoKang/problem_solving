from itertools import permutations

def solution(n, weak, dist):
    dist.sort(reverse=True)

    W, D = len(weak), len(dist)
    
    for cnt in range(1, D + 1):
        for order in permutations(dist, cnt):
            for i in range(W):
                target = weak[i:] + [n + w for w in weak[:i]]

                if target[-1] - target[0] <= sum(order):
                    return cnt

                start = 0
                for ord in order:
                    inc = 0
                    while True:
                        if target[start + inc] - target[start] <= ord:
                            inc += 1
                            if start + inc == W:
                                return cnt
                        else:
                            start += inc
                            break

    return -1
