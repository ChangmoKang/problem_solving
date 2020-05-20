from itertools import combinations

def solution(n):
    def get_primes(k):
        is_prime = [False, False] + [True]*(k - 1)
        for i in range(2, int(k ** 0.5) + 1):
            if is_prime[i]:
                is_prime[2*i::i] = [False] * ((k - i) // i)
        return [x for x in range(k + 1) if is_prime[x]]


    if n < 10:
        return 0

    primes = get_primes(n - 5)
    
    answer = 0
    for three_nums in combinations(primes, 3):
        if sum(three_nums) == n:
            answer += 1

    return answer
