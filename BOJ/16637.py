import sys
sys.stdin = open('input/16637.txt')


def calc():
    global result
    sub_result = nums[0]

    v = [0]*M
    for i in range(M):
        if not v[i]:
            if visited[i + 1]:
                v[i + 1] = 1
                if ops[i + 1] == "+":
                    tmp = nums[i + 1] + nums[i + 2]
                elif ops[i + 1] == "-":
                    tmp = nums[i + 1] - nums[i + 2]
                elif ops[i + 1] == '*':
                    tmp = nums[i + 1] * nums[i + 2]

                if ops[i] == "+":
                    sub_result += tmp
                elif ops[i] == "-":
                    sub_result -= tmp
                else:
                    sub_result *= tmp
            else:
                if ops[i] == "+":
                    sub_result += nums[i + 1]
                elif ops[i] == "-":
                    sub_result -= nums[i + 1]
                else:
                    sub_result *= nums[i + 1]
    
    if sub_result > result:
        result = sub_result


def check(start):
    if start < M:
        for i in range(start, M):
            visited[i] = 1
            calc()
            check(i + 2)
            visited[i] = 0
                

for tc in range(1, int(input()) + 1):
    N = int(input())
    data = list(input())

    nums = [int(data[i]) for i in range(0, N, 2)]

    ops = [data[i] for i in range(1, N, 2)]
    N = len(nums)
    M = len(ops)

    result = -float('inf')
    visited = [0]*M + [0]

    calc()
    check(0)
    print(result)
