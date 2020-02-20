from collections import deque

NORMAL = -1
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def solution(m, n, infests, vaccinateds):
    remain_employee = m * n - (len(infests) + len(vaccinateds))
    
    # 처음부터 모든 직원이 병에 걸리거나 백신을 맞은 경우 0을 리턴
    if remain_employee == 0:
        return 0

    infests = deque(infests)
    employee = [[NORMAL]*(n + 1) for _ in range(m + 1)]
    
    # 초기 감염자를 0으로 설정
    for i, j in infests:
        employee[i][j] = 0
    
    # 백신을 맞은 직원은 감염되지 않으므로 inf로 설정
    for i, j in vaccinateds:
        employee[i][j] = float('inf')

    # 백신을 맞지 않은 직원을 감염시킴
    while infests:
        r, c = infests.popleft()
        
        for x in range(4):
            next_r, next_c = r + dr[x], c + dc[x]
            if 1 <= next_r < m + 1 and 1 <= next_c < n + 1 and employee[next_r][next_c] == NORMAL:
                employee[next_r][next_c] = employee[r][c] + 1  # (r, c)에 있는 감염된 직원이 하루 뒤에 (next_r, next_c)로 병을 옮기는 것
                remain_employee -= 1
                if remain_employee == 0:
                    return employee[next_r][next_c]
                infests.append([next_r, next_c])
    
    # 병을 퍼트린 후에도 NORMAL 직원이 남아있기 때문에 -1을 리턴
    return -1