import sys
sys.stdin = open('input/17281.txt')


def check(count):
    global result
    if count == 9:
        total = 0
        current_idx = 0
        for k in range(N):
            out_count = 0
            base = []
            while True:
                if out_count == 3:
                    break

                if board[k][order[current_idx]] == 0:
                    out_count += 1
                elif board[k][order[current_idx]] < 4:
                    end_index = -1
                    if base:
                        for i in range(len(base)):
                            base[i] += board[k][order[current_idx]]
                            if base[i] >= 4:
                                end_index = i

                    if end_index != -1:
                        base = base[end_index + 1:]
                        total += end_index + 1

                    base.append(board[k][order[current_idx]])
                else:
                    total += len(base) + 1
                    base = []
                
                # 순서 바꾸기
                if current_idx + 1 == 9:
                    current_idx = 0
                else:
                    current_idx += 1

        if total > result:
            result = total
    elif count == 3:
        order[count] = 0
        check(count + 1)
    else:
        for i in range(1, 9):
            if not visited[i]:
                visited[i] = 1
                order[count] = i
                check(count + 1)
                order[count] = 0
                visited[i] = 0
            

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

order = [0]*9
visited = [1] + [0]*8
cnt = 0
result = 0
check(0)
print(result)
