import sys
sys.stdin = open('input/2020_kakao_3.txt')

key_info = [list(map(int, input().split())) for _ in range(3)]
lock_info = [list(map(int, input().split())) for _ in range(3)]

M = len(key_info)
N = len(lock_info)

keys = [[r, c] for r in range(M) for c in range(M) if key_info[r][c]]
locks = [[r, c] for r in range(N) for c in range(N) if not lock_info[r][c]]

if not locks:
    answer = True
else:
    answer = False

if not answer:
    for rotate_cnt in range(4):
        for idx1 in range(len(keys)):
            for lock_idx in range(len(locks)):
                r, c = keys[idx1]

                dr = locks[lock_idx][0] - r
                dc = locks[lock_idx][1] - c

                keys[idx1] = [r + dr, c + dc]

                for idx2 in range(len(keys)):
                    if idx2 != idx1:
                        rr, cc = keys[idx2]
                        keys[idx2] = [rr + dr, cc + dc]

                # 맞는지 확인하기
                check_keys = []
                for i in range(len(keys)):
                    rrr, ccc = keys[i]
                    if 0 <= rrr < N and 0 <= ccc < N:
                        check_keys.append([rrr, ccc])

                check_keys.sort()

                if check_keys == locks:
                    answer = True

                # 원래대로 돌려 놓기
                for idx2 in range(len(keys)):
                    if idx2 != idx1:
                        rr, cc = keys[idx2]
                        keys[idx2] = [rr - dr, cc - dc]

                keys[idx1] = [r, c]
        
        # 회전시키기
        if rotate_cnt < 3:
            for key_idx in range(len(keys)):
                r, c = keys[key_idx]
                keys[key_idx] = [c, (M - 1) - r]

print(answer)