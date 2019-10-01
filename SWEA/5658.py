import sys
sys.stdin = open('input/5658.txt')

for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    num_list = list(input())
    
    nums = set()

    rotate_count = N//4
    for _ in range(rotate_count):
        for i in range(4):
            each_hex_num = "".join(num_list[i * rotate_count: (i + 1) * rotate_count])
            each_int_num = int(each_hex_num, 16)
            nums.add(each_int_num)
        tmp = num_list.pop()
        num_list.insert(0, tmp)

    nums = list(nums)
    nums.sort(reverse=True)
    print(f"#{tc} {nums[K - 1]}")
