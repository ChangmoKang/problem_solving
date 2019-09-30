import sys
sys.stdin = open('input/4008.txt')


def calc(idx, count, sub_result):
    if idx == 0:
        return sub_result + nums[count + 1]
    elif idx == 1:
        return sub_result - nums[count + 1]
    elif idx == 2:
        return sub_result * nums[count + 1]
    elif idx == 3:
        return int(sub_result / nums[count + 1])


def check(count, sub_result):
    if count == N - 1:
        if sub_result > result[0]:
            result[0] = sub_result
        if sub_result < result[1]:
            result[1] = sub_result
    else:
        for i in range(4):
            if methods[i]:
                methods[i] -= 1
                check(count + 1, calc(i, count, sub_result))
                methods[i] += 1


for tc in range(1, int(input()) + 1):
    N = int(input())
    methods = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    # Max값, Min값
    result = [-float('inf'), float('inf')]
    check(0, nums[0])
    print(f"#{tc} {abs(result[0] - result[1])}")
