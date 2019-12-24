import sys
sys.stdin = open('input/3197.txt')
input = sys.stdin.readline


def find_L():
    ans = []
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'L':
                ans.append([i, j])
                if len(ans) == 2:
                    return ans


def bfs(k):
    v = [[0]*C for _ in range(R)]
    q = [s]
    v[s[0]][s[1]] = 1
    while q:
        qs, q = q, []
        for r, c in qs:
            for x in range(4):
                rr, cc = r + dr[x], c + dc[x]
                if 0 <= rr < R and 0 <= cc < C and not v[rr][cc] and visited[rr][cc] <= k:
                    v[rr][cc] = 1
                    if [rr, cc] == g:
                        return True
                    q.append([rr, cc])
    return False


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

# Store glaciers adjacent on water
melt = set()
visited = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if board[i][j] in '.L' and not visited[i][j]:
            visited[i][j] = 1
            q = [[i, j]]
            while q:
                qs, q = q, []
                for r, c in qs:
                    for x in range(4):
                        rr, cc = r + dr[x], c + dc[x]
                        if 0 <= rr < R and 0 <= cc < C and not visited[rr][cc]:
                            visited[rr][cc] = 1
                            if board[rr][cc] == 'X':
                                melt.add((rr, cc))
                                visited[rr][cc] = 2
                            else:
                                q.append([rr, cc])

# Save melting point by days
days = 2
while melt:
    days += 1
    target, melt = melt, set()
    for r, c in target:
        for x in range(4):
            rr, cc = r + dr[x], c + dc[x]
            if 0 <= rr < R and 0 <= cc < C and not visited[rr][cc]:
                visited[rr][cc] = days
                if board[rr][cc] == 'X':
                    melt.add((rr, cc))

# Find swan
s, g = find_L()

# Binary search
min_day = 2
max_day = days - 1

while min_day <= max_day:
    mid = int((min_day + max_day)/2)

    if bfs(mid):
        max_day = mid - 1
    else:
        min_day = mid + 1

print(min_day - 1)
