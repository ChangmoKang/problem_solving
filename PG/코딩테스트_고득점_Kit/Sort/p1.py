def solution(array, commands):
    return [sorted(array[f - 1: t])[k - 1] for f, t, k in commands]
