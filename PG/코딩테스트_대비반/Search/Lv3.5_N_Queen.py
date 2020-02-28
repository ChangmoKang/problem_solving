def solution(n):
    def check(r):
        nonlocal answer
        if r == n:
            answer += 1
            return

        for c in range(n):
            if c not in col_set and r - c not in diag_set1 and r + c not in diag_set2:
                col_set.add(c)
                diag_set1.add(r - c)
                diag_set2.add(r + c)
                check(r + 1)
                col_set.remove(c)
                diag_set1.remove(r - c)
                diag_set2.remove(r + c)


    answer = 0
    col_set, diag_set1, diag_set2 = set(), set(), set()
    check(0)
    return answer
