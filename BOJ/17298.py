import sys
sys.stdin = open('input/17298.txt')


N = int(input())
stack = list(map(int, input().split()))
result = [None] * (N - 1) + [-1]
max_value = stack[-1]
for index in range(N - 2, -1, -1):
    target = stack[index]
    if target >= max_value:
        result[index] = -1
        max_value = target
    else:
        for i in range(index + 1, N):
            if stack[i] > target:
                result[index] = stack[i]
                break
print(*result)
