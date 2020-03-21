import sys
sys.stdin = open('input/18795.txt')

N, M = map(int, input().split())
trash = [list(map(int, input().split())) for _ in range(2)]

print(sum(list(map(sum, trash))))
