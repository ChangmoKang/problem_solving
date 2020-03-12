def solution(numbers):
    if sum(numbers) == 0:
        return '0'
    
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    
    return "".join(numbers)
