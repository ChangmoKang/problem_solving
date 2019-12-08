import sys
sys.stdin = open('input/2839.txt')


N = int(input())

five = N // 5
three = 0
N -= 5 * five

flag = 1
while True:
    if N % 3 == 0:
        three = N // 3
        break

    if five == 0:
        flag = 0
        break

    N += 5
    five -= 1

print(five + three) if flag else print(-1)
