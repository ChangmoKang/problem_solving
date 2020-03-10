class MyStrNumber:
    def __init__(self, num):
        self.num = str(num)

    def __lt__(self, other):
        return self.num + other.num < other.num + self.num

    def __repr__(self):
        return self.num


def solution(numbers):
    if sum(numbers) == 0:
        return '0'

    str_numbers = [MyStrNumber(num) for num in numbers]
    str_numbers.sort(reverse=True)

    return "".join(map(str, str_numbers))

"""
>>> lambda를 이용한 방법 (제일 빠름)
def solution(numbers):
    if sum(numbers) == 0:
        return '0'

    numbers.sort(key=lambda x:str(x)*3, reverse=True)

    return "".join(map(str, numbers))
"""