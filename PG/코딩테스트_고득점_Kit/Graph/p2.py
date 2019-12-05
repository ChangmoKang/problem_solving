def solution(N, results):
    graph = [[0]*(N + 1) for _ in range(N + 1)]

    for win, lose in results:
        graph[win][lose] = 1
        graph[lose][win] = 2

    for target in range(1, N + 1):
        visited = [0] * (N + 1)
        q = [target]
        visited[target] = 1
        while q:
            qs, q = q, []
            for player in qs:
                for opponent in range(1, N + 1):
                    if not visited[opponent] and graph[player][opponent] == 2:
                        visited[opponent] = 1
                        graph[target][opponent] = 2
                        graph[opponent][target] = 1
                        q.append(opponent)

    answer = 0
    for i in range(1, N + 1):
        flag = 1
        for j in range(1, N + 1):
            if i != j:
                if graph[i][j] == 0:
                    flag = 0
                    break
        if flag:
            answer += 1
    
    return answer


if __name__ == "__main__":
    INPUT1 = [
        5
    ]
    INPUT2 = [
        [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    ]
    ANSWER = [
        2
    ]
    
    for index in range(1):
        print(True) if ANSWER[index] == solution(INPUT1[index], INPUT2[index]) else print(False)
