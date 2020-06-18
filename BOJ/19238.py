import sys
sys.stdin = open('input/19238.txt')


def is_visitable(r, c):
    return True if 0 <= r < N and 0 <= c < N and not visited[r][c] and board[r][c] == EMPTY else False


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
EMPTY, WALL = range(2)
R, C, POWER = range(3)

N, M, P = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
car = list(map(int, input().split()))
car[R] -= 1
car[C] -= 1
car.append(P)
person = {}
for _ in range(M):
    fr, fc, tr, tc = map(int, input().split())
    person[fr - 1, fc - 1] = (tr - 1, tc - 1)

while person and car[POWER] > 0:
    start = (car[R], car[C])
    if start in person:
        destination = person[start]
        
        visited = [[False]*N for _ in range(N)]
        visited[start[R]][start[C]] = True

        cnt = 0
        q = [start]
        flag = False
        while q:
            cnt += 1
            car[POWER] -= 1

            qs, q = q, []
            for r, c in qs:
                for x in range(4):
                    rr, cc = r + dr[x], c + dc[x]
                    if is_visitable(rr, cc):
                        visited[rr][cc] = True
                        if (rr, cc) == destination:
                            flag = True
                            car[R] = rr
                            car[C] = cc
                            car[POWER] += 2*cnt
                            person.pop(start)
                            break
                        q.append((rr, cc))
                
                if flag:
                    break

            if flag:
                break

            if car[POWER] == 0:
                break
        else:
            car[POWER] = 0
            break

    else:
        visited = [[False]*N for _ in range(N)]
        visited[start[R]][start[C]] = True

        q = [start]
        flag = False
        candi = []
        while q:
            car[POWER] -= 1

            qs, q = q, []
            for r, c in qs:
                for x in range(4):
                    rr, cc = r + dr[x], c + dc[x]
                    if is_visitable(rr, cc):
                        visited[rr][cc] = True
                        if (rr, cc) in person:
                            flag = True
                            candi.append((rr, cc))
                        q.append((rr, cc))

            if candi:
                candi.sort(key=lambda x: (x[0], x[1]))
                start = candi[0]
                car[R] = start[R]
                car[C] = start[C]
                break

            if car[POWER] == 0:
                break
        else:
            car[POWER] = 0
            break


        if car[POWER] == 0:
            break

        destination = person[start]
        
        visited = [[False]*N for _ in range(N)]
        visited[start[R]][start[C]] = True

        cnt = 0
        q = [start]
        flag = False
        while q:
            cnt += 1
            car[POWER] -= 1

            qs, q = q, []
            for r, c in qs:
                for x in range(4):
                    rr, cc = r + dr[x], c + dc[x]
                    if is_visitable(rr, cc):
                        visited[rr][cc] = True
                        if (rr, cc) == destination:
                            flag = True
                            car[R] = rr
                            car[C] = cc
                            car[POWER] += 2*cnt
                            person.pop(start)
                            break
                        q.append((rr, cc))
                
                if flag:
                    break

            if flag:
                break

            if car[POWER] == 0:
                break
        else:
            car[POWER] = 0
            break

print(-1) if car[POWER] == 0 else print(car[POWER])