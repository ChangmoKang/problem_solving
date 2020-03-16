from itertools import permutations

def solution(numbers):
    def get_primes(n):
        is_primes = [False, False] + [True] * (n - 1)
        for k in range(2, int(n**0.5) + 1):
            if is_primes[k]:
                is_primes[2*k::k] = [False] * ((n - k) // k)
        return {x for x in range(n + 1) if is_primes[x]}


    N = len(numbers)
    primes = get_primes(pow(10, N))

    nums = set()

    for i in range(1, N + 1):
        for num_str in permutations(numbers, i):
            nums.add(int("".join(num_str)))

    return sum(1 for num in nums if num in primes)
