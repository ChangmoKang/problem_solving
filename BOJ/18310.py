import sys
sys.stdin = open("input/18310.txt")


N = int(input())
house = sorted(list(map(int, input().split())))

print(house[(N - 1)//2])
