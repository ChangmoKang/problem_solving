def solution(N, edge):
    graph = [[] for _ in range(N + 1)]
    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)

    visited = [0]*(N + 1)
    result = 0

    q = [1]
    visited[1] = 1
    while q:
        qs, q = q, []
        result = len(qs)
        for f in qs:
            for t in graph[f]:
                if not visited[t]:
                    visited[t] = 1
                    q.append(t)
    return result


if __name__ == "__main__":
    INPUT1 = [
        6
    ]
    INPUT2 = [
        [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    ]
    ANSWER = [
        3
    ]
    
    for index in range(1):
        print(True) if ANSWER[index] == solution(INPUT1[index], INPUT2[index]) else print(False)
