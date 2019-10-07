import sys
sys.stdin = open('input/11650.txt')


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[0], x[1]))

for i in range(N):
    print(*arr[i])
