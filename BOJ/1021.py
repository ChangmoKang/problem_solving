import sys
sys.stdin = open('input/1021.txt')


N, K = map(int, input().split())
targets = list(map(int, input().split()))

result = 0
q = list(range(1, N + 1))
for target in targets:
    loc = q.index(target)
    if loc:
        if len(q[:loc]) >= len(q[loc:]):
            result += len(q[loc:])
        else:
            result += len(q[:loc])
    q = q[loc:] + q[:loc]
    q.pop(0)
print(result)
