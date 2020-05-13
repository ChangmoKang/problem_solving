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
    

    def move_wings(ws, *args):
        if len(args) == 1:
            new_w_a = (wing_a[R] + args[0][R], wing_a[C] + args[0][C])
            new_w_b = (wing_b[R] + args[0][R], wing_b[C] + args[0][C])
        else:
            new_w_a = (wing_a[R] + args[0][R], wing_a[C] + args[0][C])
            new_w_b = (wing_b[R] + args[1][R], wing_b[C] + args[1][C])
        
        return tuple(sorted([new_w_a, new_w_b]))
    

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
            new_direct_wings = move_wings(wings, direct)
            
            if is_visitable(*new_direct_wings) and new_direct_wings not in visited:
                if is_arrived(*new_direct_wings):
                    return time + 1

                visited.add(new_direct_wings)
                q.append((new_direct_wings, dir, time + 1))
                
                if x in SHAPE[dir]:
                    for rotate in ROTATE[x]:
                        new_rotate_wings = move_wings(wings, *rotate)
                        
                        if new_rotate_wings not in visited:
                            visited.add(new_rotate_wings)
                            q.append((new_rotate_wings, CONVERT_SHAPE[dir], time + 1))
