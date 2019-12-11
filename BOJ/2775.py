import sys
sys.stdin = open('input/2775.txt')

apt = [[0]*15 for _ in range(15)]

for i in range(1, 15):
    apt[0][i] = i

for height in range(1, 15):
    for i in range(1, 15):
        apt[height][i] = sum(apt[height - 1][:i + 1])

for _ in range(int(input())):
    info = [int(input()) for _ in range(2)]
    print(apt[info[0]][info[1]])
