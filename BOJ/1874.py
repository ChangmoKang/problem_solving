import sys
sys.stdin = open('input/1874.txt')

N = int(input())
order = [int(input()) for _ in range(N)]
nums = list(range(N + 1))
stack = []
result = []
idx = 1
order_idx = 0
while True:
    if order_idx == N:
        print("\n".join(result))
        break

    if order[order_idx] > idx:  # 4, 1
        stack.append(nums[idx])
        result.append('+')
        idx += 1
    elif order[order_idx] == idx:
        stack.append(nums[idx])
        stack.pop()
        result.append('+')
        result.append('-')
        order_idx += 1
        idx += 1
    else:
        if stack[-1] == order[order_idx]:
            stack.pop()
            result.append('-')
            order_idx += 1
        else:
            print('NO')
            break
