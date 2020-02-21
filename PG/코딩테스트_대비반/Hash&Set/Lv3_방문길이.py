from collections import defaultdict

def solution(dirs):
    X, Y, OPPOSITE = 0, 1, 2
    BORDER_S, BORDER_E = -5, 6

    move = {
        'U': [0, 1, 'D'],
        'D': [0, -1, 'U'],
        'R': [1, 0, 'L'],
        'L': [-1, 0, 'R']
    }
    
    answer = 0
    curr = [0, 0]
    # coord = {(x, y): set() for x in range(BORDER_S, BORDER_E) for y in range(BORDER_S, BORDER_E)}  # in 탐색을 O(1)로 하기 위해 set()으로 초기화
    coord = defaultdict(set)

    for cmd in dirs:
        next_x, next_y = curr[X] + move[cmd][X], curr[Y] + move[cmd][Y]
        if BORDER_S <= next_x < BORDER_E and BORDER_S <= next_y < BORDER_E:
            if cmd not in coord[curr[X], curr[Y]]:
                coord[curr[X], curr[Y]].add(cmd)  # 현재 위치에서 다음 위치로 가는 방향 저장
                coord[next_x, next_y].add(move[cmd][OPPOSITE])  # 다음 위치에서 현재 위치로 가는 방향 저장
                answer += 1
            curr = [next_x, next_y]
    
    return answer
