import sys
sys.stdin = open('input/17471.txt')


def check_relation(team, f, t):
    q = [f]
    visited = [0] * N
    visited[f] = 1
    while q:
        tmp = q.pop(0)
        for x in range(1, 1 + relation[tmp][0]):
            if not visited[relation[tmp][x] - 1]:
                if relation[tmp][x] - 1 == t:
                    return 1
                if (relation[tmp][x] - 1) not in team:
                    continue
                visited[relation[tmp][x] - 1] = 1
                q.append(relation[tmp][x] - 1)
    return 0


def check(count):
    global result
    if count == N:
        if 0 < sum(target) < N:
            one_team = [w for w in range(N) if target[w]]
            other_team = [w for w in range(N) if not target[w]]
            sub_result = abs(sum([nums[w] for w in one_team]) - sum([nums[w] for w in other_team]))
            
            if result > sub_result:
                for i in range(len(one_team)):
                    flag1 = 0
                    for j in range(i + 1, len(one_team)):
                        if not check_relation(one_team, one_team[i], one_team[j]):
                            flag1 = 1
                            break
                    if flag1:
                        break
                
                for i in range(len(other_team)):
                    flag2 = 0
                    for j in range(i + 1, len(other_team)):
                        if not check_relation(other_team, other_team[i], other_team[j]):
                            flag2 = 1
                            break
                    if flag2:
                        break

                if not flag1 and not flag2:
                    result = sub_result
    else:
        for i in range(2):
            target[count] = i
            check(count + 1)
            target[count] = -1


for tc in range(1, int(input()) + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    relation = [list(map(int, input().split())) for _ in range(N)]

    result = float('inf')

    target = [0] * N
    check(0)

    print(-1) if result == float('inf') else print(result)
