import sys
sys.stdin = open('input/17827.txt')

N, M, K = map(int, input().split())
K -= 1
nums = list(map(int, input().split()))
question = [int(input()) for _ in range(M)]

result = []
for q in question:
    if q < N:
        result.append(str(nums[q]))
    else:
        if N == K:
            result.append(str(nums[-1]))
        else:
            idx = K + (q - K)%((N - 1) - (K - 1))
            result.append(str(nums[idx]))

result = "\n".join(result)
print(result)
