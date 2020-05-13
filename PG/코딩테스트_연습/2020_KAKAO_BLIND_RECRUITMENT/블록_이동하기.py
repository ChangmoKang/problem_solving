from collections import deque

R, C = 0, 1
EMPTY, WALL = 0, 1
STAY, UL, UR, DL, DR = (0, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)

DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]
SHAPE = {'UD': (0, 1), 'LR': (2, 3)}
CONVERT_SHAPE = {'UD':'LR', 'LR':'UD'}
ROTATE = {
    0: ((UR, STAY), (STAY, UL)),
    1: ((DR, STAY), (STAY, DL)),
    2: ((DL, STAY), (STAY, UL)),
    3: ((DR, STAY), (STAY, UR))
}

def solution(board):
    
    def is_arrived(w_a, w_b):
        return True if w_a == destination or w_b == destination else False
    
    
    def is_visitable(w_a, w_b):
        if 0 <= w_a[R] < N and 0 <= w_a[C] < N and board[w_a[R]][w_a[C]] == EMPTY:
            if 0 <= w_b[R] < N and 0 <= w_b[C] < N and board[w_b[R]][w_b[C]] == EMPTY:
                return True
        return False
    
    
    N = len(board)
    destination = (N - 1, N - 1)
    q = deque([
        (((0, 0), (0, 1)), 'UD', 0)
    ])
    visited = set()
    visited.add(
        ((0, 0), (0, 1))
    )
    
    while q:
        wings, dir, time = q.popleft()

        wing_a, wing_b = wings
        for x, direct in enumerate(DELTA):
            new_direct_wing_a = (wing_a[R] + direct[R], wing_a[C] + direct[C])
            new_direct_wing_b = (wing_b[R] + direct[R], wing_b[C] + direct[C])
            
            new_direct_wings = tuple(sorted([new_direct_wing_a, new_direct_wing_b]))
            
            if is_visitable(*new_direct_wings) and new_direct_wings not in visited:
                if is_arrived(*new_direct_wings):
                    return time + 1

                visited.add(new_direct_wings)
                q.append((new_direct_wings, dir, time + 1))
                
                if x in SHAPE[dir]:
                    for rotate_a, rotate_b in ROTATE[x]:
                        new_rotate_wing_a = (wing_a[R] + rotate_a[R], wing_a[C] + rotate_a[C])
                        new_rotate_wing_b = (wing_b[R] + rotate_b[R], wing_b[C] + rotate_b[C])
                        
                        new_rotate_wings = tuple(sorted([new_rotate_wing_a, new_rotate_wing_b]))
                        
                        if new_rotate_wings not in visited:
                            visited.add(new_rotate_wings)
                            q.append((new_rotate_wings, CONVERT_SHAPE[dir], time + 1))
