import sys
sys.stdin = open('input/1629.txt')


def A_pow_B(base, n):
    if n == 0:
        return 1

    half = n // 2
    
    sub_result = A_pow_B(base, half)
    result = sub_result * sub_result

    if n % 2:
        return (base * result) % C
    else:
        return result % C


A, B, C = map(int, input().split())
print(A_pow_B(A, B))

# print(pow(*map(int, input().split())))