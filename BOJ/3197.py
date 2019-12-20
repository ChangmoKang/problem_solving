import sys
sys.stdin = open('input/3197.txt')


def find_L():
    mark = []
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'L':
                board[i][j] = '.'
                mark.append(visited[i][j])
                if len(mark) == 2:
                    return mark


def bfs():
    S, G = L
    q = [S]
    V = [0]*N
    V[S] = 1
    while q:
        qs, q = q, []
        for FROM in qs:
            for TO in adj[FROM]:
                if not V[TO]:
                    if TO == G:
                        return True
                    V[TO] = 1
                    q.append(TO)
    return False


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]


melt = []
visited = [[-1]*C for _ in range(R)]
index = 0
for i in range(R):
    for j in range(C):
        if board[i][j] == '.' and visited[i][j] == -1:
            melt.append(set())
            visited[i][j] = index
            q = [[i, j]]
            while q:
                qs, q = q, []
                for r, c in qs:
                    for x in range(4):
                        rr = r + dr[x]
                        cc = c + dc[x]
                        if 0 <= rr < R and 0 <= cc < C and visited[rr][cc] == -1:
                            visited[rr][cc] = index
                            if board[rr][cc] == 'X':
                                melt[index].add((rr, cc))
                            else:
                                q.append([rr, cc])
            index += 1

L = find_L()
# print(L)

result = 0
N = len(melt)
adj = [[] for _ in range(N)]
while True:
    target, melt = melt, [set() for _ in range(N)]
    for i in range(N):
        for r, c in target[i]:
            for x in range(4):
                rr = r + dr[x]
                cc = c + dc[x]
                if 0 <= rr < R and 0 <= cc < C:
                    if visited[rr][cc] == -1:
                        visited[rr][cc] = i
                        if board[rr][cc] == 'X':
                            melt[i].add((rr, cc))
                    else:
                        j = visited[rr][cc]
                        if (i != j) and j not in adj[i]:
                            adj[i].append(j)
    
    # print(adj)
    result += 1
    if bfs():
        break

print(result)
