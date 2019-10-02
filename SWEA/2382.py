import sys
sys.stdin = open('input/2382.txt')


ways = {
    1: [-1, 0],
    2: [1, 0],
    3: [0, -1],
    4: [0, 1]
}

for tc in range(1, int(input()) + 1):
    N, T, K = map(int, input().split())
    microbe = [list(map(int, input().split())) for _ in range(K)]

    for _ in range(T):
        trash = []
        board = [[0]*N for _ in range(N)]
        for k in range(len(microbe)):
            microbe[k][0] += ways[microbe[k][-1]][0]
            microbe[k][1] += ways[microbe[k][-1]][1]
            if microbe[k][0] == 0 or microbe[k][0] == N - 1 or microbe[k][1] == 0 or microbe[k][1] == N - 1:
                microbe[k][2] = int(microbe[k][2]/2)
                if microbe[k][2] == 0:
                    trash.append(microbe[k])
                    continue

                if microbe[k][-1] % 2:
                    microbe[k][-1] += 1
                else:
                    microbe[k][-1] -= 1
            
            else:
                board[microbe[k][0]][microbe[k][1]] += 1

        for i in range(1, N - 1):
            for j in range(1, N - 1):
                if board[i][j] > 1:
                    collision_microbe = [microbe[w] for w in range(len(microbe)) if microbe[w][0] == i and microbe[w][1] == j]
                    new_microbe_count = sum([collision_microbe[w][2] for w in range(len(collision_microbe))])
                    new_microbe_direction = max(collision_microbe, key=lambda x: x[2])[3]
                    microbe.append([i, j, new_microbe_count, new_microbe_direction])
                    trash.extend(collision_microbe)

        for target in trash:
            microbe.remove(target)
    
    result = 0
    for i in range(len(microbe)):
        result += microbe[i][2]
    print(f"#{tc} {result}")
