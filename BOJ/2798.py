import sys
sys.stdin = open('input/2798.txt')


def check(count, sub_result):
    global result

    if count == 3:
        if sub_result > result:
            result = sub_result
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                if sub_result + nums[i] <= M:
                    check(count + 1, sub_result + nums[i])
                visited[i] = 0

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

result = 0
visited = [0]*N

check(0, 0)

print(result)
