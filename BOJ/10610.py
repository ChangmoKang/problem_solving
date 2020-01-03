import sys
sys.stdin = open('input/10610.txt')


nums = sorted(list(map(int, list(input().rstrip()))), reverse=True)
if not nums.count(0) or sum(nums) % 3:
    print(-1)
else:
    print(*nums, sep="")
