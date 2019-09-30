import sys
sys.stdin = open('input/1952.txt')


def check(count, sub_result):
    global result
    if count > 11:
        if result > sub_result:
            result = sub_result
    else:
        check(count + 1, sub_result + kinds[0] * months[count])
        check(count + 1, sub_result + kinds[1])
        check(count + 3, sub_result + kinds[2])


for tc in range(1, int(input()) + 1):
    kinds = list(map(int, input().split()))
    months = list(map(int, input().split()))

    result = kinds[-1]
    check(0, 0)
    print(f"#{tc} {result}")
