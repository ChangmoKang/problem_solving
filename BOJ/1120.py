import sys
sys.stdin = open('input/1120.txt')


A, B = map(list, input().split())
N = len(B) - len(A)
result = float('inf')
for start in range(N + 1):
    cnt = 0
    for index in range(len(A)):
        if A[index] != B[start + index]:
            cnt += 1
    if result > cnt:
        result = cnt

print(result)
