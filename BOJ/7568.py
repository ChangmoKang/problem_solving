import sys
sys.stdin = open('input/7568.txt')

N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]

rank = [0]*N

for i in range(N):
    upper_rank = 1
    for j in range(N):
        if i != j:
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                upper_rank += 1
    rank[i] = upper_rank

print(*rank)
