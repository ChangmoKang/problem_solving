def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    sorted_arr = []

    l = r = 0
    while l < len(left_arr) and r < len(right_arr):
        if int(left_arr[l] + right_arr[r]) > int(right_arr[r] + left_arr[l]):
            sorted_arr.append(left_arr[l])
            l += 1
        else:
            sorted_arr.append(right_arr[r])
            r += 1

    sorted_arr += left_arr[l:]
    sorted_arr += right_arr[r:]

    return sorted_arr


def solution(numbers):    
    if sum(numbers) == 0:
        return '0'

    str_numbers = list(map(str, numbers))
    sorted_str_numbers = merge_sort(str_numbers)

    return "".join(sorted_str_numbers)
