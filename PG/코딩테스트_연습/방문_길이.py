X, Y = 0, 1
d = {
    'U': [0, 1],
    'D': [0, -1],
    'R': [1, 0],
    'L': [-1, 0]
}


def solution(dirs):
    new_road = set()
    
    r = c = 0
    for dir in dirs:
        rr, cc = r + d[dir][X], c + d[dir][Y]
        if -5 <= rr <= 5 and -5 <= cc <= 5:
            new_road.add((r, c, rr, cc))
            new_road.add((rr, cc, r, c))
            r, c = rr, cc

    return len(new_road)//2
