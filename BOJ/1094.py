import sys
sys.stdin = open('input/1094.txt')


N = int(input())
result = 0
while True:
    if N == 1:
        result += 1
        break
    result += N % 2
    N //= 2
print(result)
