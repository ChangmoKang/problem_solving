import sys
sys.stdin = open('input/5014.txt')


def check():
    if S == G:
        return 0
    visited = [0]*F
    visited[S] = 1
    q = [S]
    cnt = 0
    while q:
        cnt += 1
        qs, q = q, []
        for curr_floor in qs:
            up = curr_floor + U
            if up == G:
                return cnt
            if up < F and not visited[up]:
                visited[up] = 1
                q.append(up)

            down = curr_floor - D
            if down == G:
                return cnt
            if down >= 0 and not visited[down]:
                visited[down] = 1
                q.append(down)
    return -1


F, S, G, U, D = map(int, input().split())
S -= 1
G -= 1
result = check()
print('use the stairs') if result == -1 else print(result)
