import sys
sys.stdin = open('input/1920.txt')
input = sys.stdin.readline

N = int(input())
nums = sorted(list(map(int, input().split())))

save = set()
result = []
M = int(input())
for target in map(int, input().split()):
    target = int(target)
    if target in save:
        result.append('1')
    else:
        flag = False
        l, r = 0, N - 1
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                result.append('1')
                save.add(target)
                flag = True
                break

            if target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        
        if not flag:
            result.append('0')

print("\n".join(result))
