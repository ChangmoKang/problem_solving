import sys
sys.stdin = open('input/10250.txt')


for _ in range(int(input())):
    H, W, N = map(int, input().split())
    width_cnt = (N - 1) // H
    height_cnt = (N - 1) % H + 1
    print(f"{height_cnt}{width_cnt + 1}") if width_cnt + 1 >= 10 else print(f"{height_cnt}0{width_cnt + 1}")
