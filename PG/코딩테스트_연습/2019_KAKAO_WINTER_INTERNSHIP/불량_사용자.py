from itertools import product


MASK = '*'


def solution(users, bans):
    ban_target_users = [[] for _ in range(len(bans))]
    for i, ban in enumerate(bans):
        N = len(ban)
        
        for user in users:
            M = len(user)
            if N == M:
                for u, b in zip(user, ban):
                    if b == MASK:
                        continue
                    
                    if u != b:
                        break
                else:
                    ban_target_users[i].append(user)
    
    answer = set()
    for banned_user in product(*ban_target_users):
        banned_user = set(banned_user)
        if len(banned_user) == len(bans):
            banned_user = sorted(list(banned_user))
            answer.add(tuple(banned_user))

    return len(answer)
