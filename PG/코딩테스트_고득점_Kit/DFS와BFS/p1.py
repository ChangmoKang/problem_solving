from itertools import product

def solution(numbers, target):
    cases = [[num, -num] for num in numbers]
    return sum(1 for case in product(*cases) if sum(case) == target)
