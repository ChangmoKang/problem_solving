from itertools import product, chain


EMPTY, BLOCK = 0, 1


def solution(key, lock):
    def rotate_key():
        rotated_key = [[0]*M for _ in range(M)]
        for rr in range(M):
            for cc in range(M):
                rotated_key[cc][(M - 1) - rr] = key[rr][cc]
        return rotated_key
    
    
    def key_to_shapes():
        shape = [(rr, cc) for rr, cc in product(range(M), range(M)) if key[rr][cc]]
        shapes = [[(rr - shape[i][0], cc - shape[i][1]) for rr, cc in shape] for i in range(len(shape))]
        return shapes

    
    def visitable(i, j):
        return True if 0 <= i < N and 0 <= j < N else False
    
    
    N, M = len(lock), len(key)
    
    empty_cnt = N**2 - sum(chain(*lock))
    
    if not empty_cnt:
        return True
    
    for _ in range(4):
        shapes = key_to_shapes()
        for r, c in product(range(N), range(N)):
            if lock[r][c] == EMPTY:
                for shape in shapes:
                    cnt = 0
                    for key_r, key_c in shape:
                        if visitable(r + key_r, c + key_c):
                            if lock[r + key_r][c + key_c] == BLOCK:
                                break
                            cnt += 1
                    else:
                        if cnt == empty_cnt:
                            return True
        key = rotate_key()

    return False
    