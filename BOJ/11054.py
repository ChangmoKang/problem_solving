import sys
sys.stdin = open('input/11054.txt')


N = int(input())
a = [0] + list(map(int, input().split()))
dp_1 = [0]*(N + 1)
dp_1[1] = 1
dp_2 = [0]*(N + 1)
dp_2[N] = 1

for i in range(2, N + 1):
    dp_1[i] = 1
    for j in range(1, i + 1):
        if a[i] > a[j] and dp_1[i] <= dp_1[j]:
            dp_1[i] = dp_1[j] + 1
        elif a[i] == a[j]:
            dp_1[i] = dp_1[j]

for i in range(N, 0, -1):
    dp_2[i] = 1
    for j in range(N, i, -1):
        if a[i] > a[j] and dp_2[i] <= dp_2[j]:
            dp_2[i] = dp_2[j] + 1
        elif a[i] == a[j]:
            dp_2[i] = dp_2[j]

dp = [dp_1[i] + dp_2[i] for i in range(N + 1)]
print(max(dp) - 1)
