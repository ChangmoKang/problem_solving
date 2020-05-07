"""
import re
from collections import Counter


KEY, VALUE = 0, 1


def solution(s):
    return list(map(int, [k for k, v in sorted(Counter(re.findall('\d+', s)).items(), key=lambda x: -x[VALUE])]))
"""


def solution(s):
    s = s[2:-2].split("},{")
    s.sort(key=len)

    answer = []
    for tuple_ in s:
        tuple_ = list(map(int, tuple_.split(',')))
        for elem in tuple_:
            if elem not in answer:
                answer.append(elem)

    return answer
    