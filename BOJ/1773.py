import sys
sys.stdin = open('input/1773.txt')

N, C = map(int, input().split())
students = [int(input()) for _ in range(N)]

if 1 in students:
    print(C)
else:
    firecracker = [0]*(C + 1)
    for cycle in students:
        for i in range(cycle, C + 1, cycle):
            firecracker[i] = 1
    print(sum(firecracker))
