def solution(n, arr1, arr2):
    def func(target):
        return '#' if target == '1' else ' '

    answer = []
    for a1, a2 in zip(arr1, arr2):
        row = bin(a1|a2)[2:]
        if len(row) < n:
            row = '0'*(n - len(row)) + row
            
        row = "".join(list(map(func, row)))
        answer.append(row)

    return answer
