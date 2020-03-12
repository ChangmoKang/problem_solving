from itertools import permutations

def solution(numbers):
    def get_primes(n):
        is_primes = [False, False] + [True] * (n - 1)
        for k in range(2, int(n**0.5) + 1):
            if is_primes[k]:
                is_primes[2*k::k] = [False] * ((n - k) // k)
        return {x for x in range(n + 1) if is_primes[x]}


    answer = 0        
    primes = get_primes(10**len(numbers))

    save = set()

    for i in range(1, len(numbers) + 1):
        for tmp in permutations(numbers, i):
            save.add(int("".join(tmp)))

    for num in save:
        if num in primes:
            answer += 1

    return answer
