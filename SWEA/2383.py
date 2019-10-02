import sys
sys.stdin = open('input/2383.txt')


def calc(index, stair_index):
    return abs(people[index][0] - stair[stair_index][0])\
        +\
            abs(people[index][1] - stair[stair_index][1])


def check(count):
    global result

    if count == N:
        wait = [[] for _ in range(2)]

        # 각각의 계단에 도달하는 시간을 계산한다.
        for idx in range(N):
            wait[choice[idx]].append(calc(idx, choice[idx]))

        # 빨리 도착하는 순서로 정렬한다.
        for idx in range(2):
            wait[idx].sort()

        # 가장 빨리 계단에 도착하는 시간부터 시작한다.
        if wait[0] and wait[1]:
            t = min(wait[0][0], wait[1][0])
        elif wait[0] and not wait[1]:
            t = wait[0][0]
        elif wait[1] and not wait[0]:
            t = wait[1][0]

        # 계단의 상태
        status = [[0]*3 for _ in range(2)]
        while True:
            # 계단에 내려갈 수 있으면 내려간다.
            for idx in range(2):
                for i in range(3):
                    if wait[idx]:
                        if status[idx][i] == 0 and wait[idx][0] <= t:
                            wait[idx].pop(0)
                            status[idx][i] = stair[idx][2]

            # 계단에 있는 사람을 한 칸씩 내린다.
            for idx in range(2):
                for i in range(3):
                    if status[idx][i] > 0:
                        status[idx][i] -= 1

            t += 1

            if not wait[0] and not wait[1] and not sum(status[0]) and not sum(status[1]):
                break
        if result > t + 1:
            result = t + 1
    else:
        for i in range(2):
            choice[count] = i
            check(count + 1)
            choice[count] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    people = []
    stair = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                people.append([i, j])
            elif board[i][j] > 1:
                stair.append([i, j, board[i][j]])
    
    result = float('inf')

    # board를 더 이상 쓰지 않으므로 N을 재정의한다.
    N = len(people)
    choice = [-1]*N
    check(0)
    
    print(f"#{tc} {result}")
