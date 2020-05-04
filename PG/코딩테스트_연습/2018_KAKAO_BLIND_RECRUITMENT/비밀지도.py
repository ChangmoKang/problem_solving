def solution(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        b1 = bin(a1)[2:]
        if len(b1) < n:
            b1 = '0'*(n - len(b1)) + b1

        b2 = bin(a2)[2:]
        if len(b2) < n:
            b2 = '0'*(n - len(b2)) + b2
            
        result = ""
        for elem1, elem2 in zip(b1, b2):
            if elem1 == '1' or elem2 == '1':
                result += '#'
            else:
                result += ' '

        answer.append(result)

    return answer