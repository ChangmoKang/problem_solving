import sys
sys.stdin = open('input/9461.txt')


nums = [None, 1, 1, 1, 2, 2]
index = 5
result = []
for _ in range(int(input())):
    target = int(input())
    if target > index:
        while True:
            nums.append(nums[index] + nums[index - 4])
            index += 1
            if index == target:
                break
    result.append(str(nums[target]))

print("\n".join(result))
