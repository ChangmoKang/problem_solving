import sys
from itertools import permutations
sys.stdin = open('input/17281.txt')
input = sys.stdin.readline


N = int(input())
inning = [list(map(int, input().split())) for _ in range(N)]

answer = 0

for order in permutations(range(1, 9)):
    order = list(order[:3]) + [0] + list(order[3:])

    index = 0
    score = 0
    for each in inning:
        a, b, c = 0, 0, 0
        out = 0
        while out < 3:
            result = each[order[index]]

            if result == 0:
                out += 1
            elif result == 1:
                score += c
                a, b, c = 1, a, b
            elif result == 2:
                score += (b + c)
                a, b, c = 0, 1, a
            elif result == 3:
                score += (a + b + c)
                a, b, c = 0, 0, 1
            elif result == 4:
                score += (a + b + c + 1)
                a, b, c = 0, 0, 0

            index = (index + 1) % 9

    if score > answer:
        answer = score

print(answer)
