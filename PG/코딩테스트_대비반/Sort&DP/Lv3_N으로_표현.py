def solution(N, number):
    if N == number:
        return 1

    cases = [0] + [{int(str(N)*i)} for i in range(1, 9)]
    
    for N_count in range(2, 9):
        for i in range(1, N_count//2 + 1):
            for r in cases[i]:
                for c in cases[N_count - i]:
                    cases[N_count].add(r + c)
                    cases[N_count].add(r - c)
                    cases[N_count].add(c - r)
                    cases[N_count].add(r * c)
                    if r != 0 and c != 0:
                        cases[N_count].add(r // c)
                        cases[N_count].add(c // r)
        if number in cases[N_count]:
            return N_count
    return -1
