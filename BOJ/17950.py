import sys
sys.stdin = open('input/17950.txt')
input = sys.stdin.readline

H, K = map(int, input().split())
result = 0
factor = K
for _ in range(H):
    result += factor * int(input())
    factor *= K
    factor %= 1000000007 

result %= 1000000007
print(result)
