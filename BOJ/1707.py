import sys
sys.stdin = open('input/1707.txt')
input = sys.stdin.readline


def check(count):
    global result
    if result:
        return

    if count == N - 1:
        if sum(bi):
            if ins():
                result = True
    else:
        for i in range(2):
            bi[count] = i
            check(count + 1)
            bi[count] = -1


def ins():
    for f in range(N - 1):
        for t in range(f + 1, N):
            if bi[f] == bi[t]:
                if t in rel[f]:
                    return False
    return True


for _ in range(int(input())):
    N, K = map(int, input().split())
    
    if N == 1:
        print("YES")
    else:
        rel = [[] for _ in range(N)]
        for _ in range(K):
            f, t = map(int, input().split())
            rel[f - 1].append(t - 1)
            rel[t - 1].append(f - 1)

        result = False
        bi = [0]*N
        check(0)
        print("YES") if result else print("NO")
