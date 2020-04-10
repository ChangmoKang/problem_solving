import sys
sys.stdin = open('input/1922.txt')
input = sys.stdin.readline


def get_parent(x):
    if parent[x] == x:
        return x

    parent[x] = get_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    return True if a == b else False


N, K = [int(input()) for _ in range(2)]
edge = [list(map(int, input().split())) for _ in range(K)]
edge.sort(key=lambda x: x[-1])

parent = list(range(N + 1))
cnt = 0
result = 0
for a, b, v in edge:
    if cnt == N - 1:
        break

    if not find_parent(a, b):
        result += v
        union_parent(a, b)
        cnt += 1

print(result)
