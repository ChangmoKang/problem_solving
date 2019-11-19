import sys
sys.stdin = open('input/17471.txt')


def bfs(team):
    visited = [0]*N
    q = [team[0]]
    visited[team[0]] = 1
    team.remove(team[0])

    while q:
        target = q.pop(0)
        if team == []:
            return True
        
        for i in range(N):
            if adj[target][i] and i in team and not visited[i]:
                q.append(i)
                visited[i] = 1
                team.remove(i)
    return False


def check(count, one_side_sum):
    global result
    if count == N:
        if sum(divide) == 0 or divide[0] == 1:
            return
        A = [x for x in range(N) if divide[x] == 1]
        B = [x for x in range(N) if divide[x] == 0]

        if bfs(A) and bfs(B):
            other_side_sum = total - one_side_sum
            diff = abs(one_side_sum - other_side_sum)
            if result > diff:
                result = diff
    else:
        for i in range(2):
            divide[count] = i
            if i:
                check(count + 1, one_side_sum + people[count])
            else:
                check(count + 1, one_side_sum)
            divide[count] = 0


N = int(input())
people = list(map(int, input().split()))
total = sum(people)
adj = [[0]*N for _ in range(N)]
for i in range(N):
    for j in list(map(int, input().split()))[1:]:
        adj[i][j - 1] = 1
        adj[j - 1][i] = 1

result = float('inf')

divide = [0]*N
check(0, 0)

print(result) if result != float('inf') else print(-1)
