def solution(n):
    def check(r):
        nonlocal answer
        if r == n:
            answer += 1
        else:
            for c in range(n):
                if c in cols_set:
                    for rr in range(r):
                        if r - rr == abs(cols[rr] - c):
                            break
                    else:
                        cols[r] = c
                        cols_set.remove(c)
                        check(r + 1)
                        cols_set.add(c)
                        cols[r] = None


    answer = 0
    cols = [None]*n
    cols_set = set(range(n))
    check(0)
    return answer
