import sys
sys.stdin = open('input/1003.txt')


for _ in range(int(input())):
    target = int(input())
    result = [[1, 0], [0, 1]]
    if target <= 1:
        print(*result[target])
    else:
        index = 1
        while True:
            index += 1
            result.append([result[-2][0] + result[-1][0], result[-2][1] + result[-1][1]])
            if index == target:
                break
        print(*result[target])
