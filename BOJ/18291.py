import sys
sys.stdin = open('input/18291.txt')
input = sys.stdin.readline


def pow(base, target_exponent):
    if target_exponent == 0:
        return 1
    
    divide = pow(base, target_exponent // 2) % 1000000007
    value = divide * divide
    
    if target_exponent % 2:
        return base * value
    else:
        return value


for _ in range(int(input())):
    N = int(input())
    if N == 1:
        print(1)
    else:
        print(pow(2, N - 2) % 1000000007)
