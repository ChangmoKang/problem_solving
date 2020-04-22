import sys
sys.stdin = open('input/9372.txt')
input = sys.stdin.readline


def get_parent(x):
    if parent[x] == x:
        return x

    parent[x] = get_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def find_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    return True if a == b else False


for _ in range(int(input())):
    N, M = map(int, input().split())
    answer = 0
    parent = list(range(N + 1))

    for _ in range(M):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a

        if not find_parent(a, b):
            answer += 1
            union_parent(a, b)

    print(answer)
