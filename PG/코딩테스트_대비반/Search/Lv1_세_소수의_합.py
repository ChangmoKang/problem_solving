def solution(n):
    def get_primes(k):
        is_prime = [False, False] + [True]*(k - 1)
        for i in range(2, int(k ** 0.5) + 1):
            if is_prime[i]:
                is_prime[2*i::i] = [False] * ((k - i) // i)
        return [x for x in range(k + 1) if is_prime[x]]


    def check(count, start, sub_result):
        nonlocal result
        if count == 3:
            if sub_result == n:
                result += 1
        else:
            for i in range(start, len(primes)):
                if sub_result + primes[i] <= n:
                    check(count + 1, i + 1, sub_result + primes[i])


    if n < 10:
        return 0

    primes = get_primes(n - 5)
    
    result = 0
    check(0, 0, 0)
    
    return result
