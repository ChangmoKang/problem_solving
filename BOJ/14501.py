import sys
sys.stdin = open('input/14501.txt')


def check(day, sub_result):
    global result
    if day == N:
        if sub_result > result:
            result = sub_result
    elif day < N:
        check(day + consult[day][0], sub_result + consult[day][1])
        check(day + 1, sub_result)


N = int(input())
consult = [list(map(int, input().split())) for _ in range(N)]
result = 0
check(0, 0)
print(result)
