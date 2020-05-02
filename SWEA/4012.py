import sys
from itertools import permutations
sys.stdin = open('input/4012.txt')


def check(count, List):
    global result

    if count == N - 1:
        if List.count(1) == N // 2:
            a = [i for i in range(N) if List[i] == 1]
            b = [i for i in range(N) if List[i] == 0]
            
            r_a = 0
            for r, c in permutations(a, 2):
                r_a += board[r][c]

            r_b = 0
            for r, c in permutations(b, 2):
                r_b += board[r][c]

            if result > abs(r_a - r_b):
                result = abs(r_a - r_b)
        return

    for i in range(2):
        List[count] = i
        check(count + 1, List)
        List[count] = 0
        


for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    result = float('inf')
    check(0, [0]*N)
    print(f"#{tc} {result}")
