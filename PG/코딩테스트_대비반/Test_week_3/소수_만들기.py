from itertools import combinations

def solution(nums):
    def get_primes(n):
        is_prime = [False, False] + [True]*(n - 1)
        for k in range(2, int(n**0.5) + 1):
            if is_prime[k]:
                is_prime[2*k::k] = [False] * ((n - k) // k)
        return {x for x in range(n) if is_prime[x]} # 소수인지 검사하기 위해 set 자료형으로 return


    primes = get_primes(3000)

    return sum(1 for picked_nums in combinations(nums, 3) if sum(picked_nums) in primes)
