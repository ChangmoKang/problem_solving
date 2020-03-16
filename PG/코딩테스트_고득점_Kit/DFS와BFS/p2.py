from collections import deque

def solution(n, computers):
    computers = [[t_i for t_i, is_connected in enumerate(f_c) if is_connected and f_i != t_i] for f_i, f_c in enumerate(computers)]

    answer = 0
    visited = [False]*n
    for s_i in range(n):
        if not visited[s_i]:
            visited[s_i] = True
            answer += 1
            
            q = deque([s_i])
            while q:
                f_i = q.popleft()
                for t_i in computers[f_i]:
                    if not visited[t_i]:
                        visited[t_i] = True
                        q.append(t_i)

    return answer
