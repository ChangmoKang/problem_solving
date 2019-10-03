import sys
sys.stdin = open('input/5653.txt')


N = 350
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for tc in range(1, int(input()) + 1):
    R, C, K = map(int, input().split())
    board = [[0]*N for _ in range(N)]
    live_cell = []
    for r in range(R):
        c = 0
        for el in list(map(int, input().split())):
            if el:
                live_cell.append([150 + r, 150 + c])
                board[150 + r][150 + c] = [el, 2 * el]
            c += 1

    for t in range(K):
        # 죽는 세포와 새로운 세포 저장할 list
        trash = []
        new_cell = []
        for r, c in live_cell:
            # 번식 확인 후 번식
            cell = board[r][c]
            if cell[0] == cell[1]:
                for i in range(4):
                    rr = r + dr[i]
                    cc = c + dc[i]
                    if board[rr][cc] == 0:
                        board[rr][cc] = [cell[0], 2*cell[0]]
                        new_cell.append([rr, cc])
                    elif 2 * board[rr][cc][0] == board[rr][cc][1] and cell[0] > board[rr][cc][0] and [rr, cc] not in live_cell:
                        board[rr][cc] = [cell[0], 2*cell[0]]

            # 생명력 감소
            board[r][c][1] -= 1

            if board[r][c][1] == 0:
                trash.append([r, c])

        if trash:
            for dead_cell in trash:
                live_cell.remove(dead_cell)

        if new_cell:
            live_cell.extend(new_cell)

    result = len(live_cell)
    print(f"#{tc} {result}")
