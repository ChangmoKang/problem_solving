import sys
sys.stdin = open('input/10448.txt')


def check(count, sub_result):
    global result
    if count == 3:
        if sub_result == target:
            result = 1
            return

    else:
        for n in range(end, 0, -1):
            if result:
                return
            if sub_result + table[n] <= target:
                check(count + 1, sub_result + table[n])


def find_end():
    for x in range(45):
        if table[x] > target:
            return x
    return 44


table = [int(i * (i + 1) / 2) for i in range(45)]
for _ in range(int(input())):
    target = int(input())
    end = find_end()
    result = 0
    check(0, 0)
    print(result)
