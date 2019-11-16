import sys
input = sys.stdin.readline
sys.stdin = open('input/17390.txt')


N, Q = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
questions = [list(map(int, input().split())) for _ in range(Q)]
arr = [0]*(N + 1)

for i in range(1, N + 1):
    arr[i] = arr[i - 1] + nums[i - 1]

for l, r in questions:
    print(arr[r] - arr[l - 1])
