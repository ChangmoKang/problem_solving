def solution(N, stages):
    user_N = len(stages)
    
    remain_users = [0]*N
    for stage in stages:
        if stage != N + 1:
            remain_users[stage - 1] += 1
            
    result = {}
    for stage, remain_user in enumerate(remain_users, start=1):
        if user_N:
            result[stage] = remain_user / user_N
            user_N -= remain_user
        else:
            result[stage] = 0
            
    return sorted(result, key=lambda x: -result[x])
