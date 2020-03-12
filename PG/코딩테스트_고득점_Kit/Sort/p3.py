def solution(citations):
    N = len(citations)
    citations.sort()
    for i, c in enumerate(citations):
        h = N - i
        if c >= h:
            return h
