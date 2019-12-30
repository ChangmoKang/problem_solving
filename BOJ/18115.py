import sys
sys.stdin = open('input/18115.txt')


N = int(input())
copy_N = N
visited = [0]*N
f = -1
s = -1
t = -1
result = [None]*N
for method in map(int, input().split()):
    if method == 1:
        if not visited[f + 1]:
            f += 1
            visited[f] = 1
            result[f] = str(N)
            if f + 1 < copy_N and visited[f + 1]:
                f = s
        else:
            f = s + 1
            visited[f] = 1
            result[f] = str(N)
    elif method == 2:
        if f >= s:
            s = f + 2
        else:
            s += 1
        visited[s] = 1
        result[s] = str(N)
    else:
        result[t] = str(N)
        t -= 1
    N -= 1
print(" ".join(result))
