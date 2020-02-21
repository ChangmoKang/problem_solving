from collections import Counter

def solution(v):
    trans_v = list(map(list, zip(*v)))

    X_AXIS, Y_AXIS, KEY, COUNT = 0, 1, 0, 1
    x = sorted(Counter(trans_v[X_AXIS]).items(), key=lambda x: x[COUNT])[0][KEY]
    y = sorted(Counter(trans_v[Y_AXIS]).items(), key=lambda x: x[COUNT])[0][KEY]
    
    return [x, y]
