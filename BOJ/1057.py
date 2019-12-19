import sys
sys.stdin = open('input/1057.txt')


N, A, B = map(int, input().split())
result = 1
while True:
    if (A % 2 and A + 1 == B) or (B % 2 and B + 1 == A):
        break
    A = A // 2 + A % 2
    B = B // 2 + B % 2
    result += 1
print(result)
