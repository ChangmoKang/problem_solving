import sys
sys.stdin = open('input/2846.txt')


def check():
    global result
    value = top - bottom
    if value > result:
        result = top - bottom


N = int(input())
arr = list(map(int, input().split()))

result = 0
bottom, top = arr[0], arr[0]
for i in range(1, N):
    if arr[i] > top:
        top = arr[i]
    else:
        value = top - bottom
        check()
        bottom, top = arr[i], arr[i]

if bottom != top:
    check()

print(result)
