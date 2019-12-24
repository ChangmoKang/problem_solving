import sys
sys.stdin = open('input/11866.txt')


N, K = map(int, input().split())
q = list(range(1, N + 1))
visited = [1] + [0] * N
result = []
index = -1
while len(result) != N:
    index = (index + K) % len(q)
    result.append(str(q.pop(index)))
    index -= 1
print(f'<{", ".join(result)}>')
