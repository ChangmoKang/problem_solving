import sys
sys.stdin = open('input/4012.txt')


def calc_flavor(idx):
    sum_flavor = 0
    for i in range(len(idx) - 1):
        for j in range(i + 1, len(idx)):
            sum_flavor += table[idx[i]][idx[j]]
            sum_flavor += table[idx[j]][idx[i]]
    dic[tuple(idx)] = sum_flavor


def check(count):
    global result
    if count == N//2:
        other = list(set(range(N)) - set(pick))

        if tuple(pick) not in dic:
            calc_flavor(pick)

        if tuple(other) not in dic:
            calc_flavor(other)
        
        sub_result = abs(dic[tuple(pick)] - dic[tuple(other)])
        
        if result > sub_result:
            result = sub_result
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                if i >= pick[count - 1]:
                    pick[count] = i
                    check(count + 1)
                    pick[count] = 0
                visited[i] = 0

for tc in range(1, int(input()) + 1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    visited = [0]*N
    pick = [0]*(N//2)

    dic = {}
    result = float('inf')
    check(0)

    print(f"#{tc} {result}")
