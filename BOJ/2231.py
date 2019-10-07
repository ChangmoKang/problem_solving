import sys
sys.stdin = open('input/2231.txt')

target = int(input())

for i in range(target):
    num = str(i)
    each_num = list(map(int, list(num)))

    if int(num) + sum(each_num) == target:
        break

print(0) if i == target - 1 else print(i)
