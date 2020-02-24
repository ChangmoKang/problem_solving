import sys
sys.stdin = open('input/14891.txt')


def check(i, m):
    if not visited[i]:
        visited[i] = True
    
        if i - 1 >= 0 and not visited[i - 1]:
            if magnet[i - 1][2] != magnet[i][-2]:
                check(i - 1, -m)

        if i + 1 < 4 and not visited[i + 1]:
            if magnet[i][2] != magnet[i + 1][-2]:
                check(i + 1, -m)

        rotate(i, m)


def rotate(i, m):
    if m == 1:
        tmp = magnet[i].pop()
        magnet[i].insert(0, tmp)
    else:
        tmp = magnet[i].pop(0)
        magnet[i].append(tmp)


magnet = [list(map(int, list(input()))) for _ in range(4)]
for _ in range(int(input())):
    index, method = map(int, input().split())
    visited = [False]*4
    check(index - 1, method)

print(sum(2**i for i in range(4) if magnet[i][0] == 1))
