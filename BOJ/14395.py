import sys
sys.stdin = open('input/14395.txt')


def calc(idx, num):
    if idx == 0:
        return num * num
    elif idx == 1:
        return num + num
    elif idx == 2:
        return 0
    elif idx == 3:
        return 1


def bfs(v):
    visited = set()
    visited.add(v[0])
    q = [v]
    while q:
        number, saved = q.pop(0)
        for x in range(4):
            new_number = calc(x, number)
            if new_number not in visited:
                visited.add(new_number)
                if x == 0:
                    if new_number > t:
                        continue
                if x == 1:
                    if new_number > t:
                        continue
                if x == 3:
                    if number == 0:
                        break
                copied_saved = saved[:]
                copied_saved.append(ops[x])
                if new_number == t:
                    print("".join(copied_saved))
                    return
                q.append([calc(x, number), copied_saved])
    print(-1)

ops = ['*', '+', '-', '/']
s, t = map(int, input().split())
if s == t:
    print(0)
else:
    bfs([s, []])
