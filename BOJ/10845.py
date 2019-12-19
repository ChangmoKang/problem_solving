import sys
sys.stdin = open('input/10845.txt')
input = sys.stdin.readline


N = int(input())
q = []
result = []
for _ in range(N):
    method = input().split()
    if len(method) == 2:
        q.append(int(method[1]))
    else:
        if method[0] == 'pop':
            target = -1
            if q:
                target = q.pop(0)
        elif method[0] == 'size':
            target = len(q)
        elif method[0] == 'empty':
            if q:
                target = 0
            else:
                target = 1
        elif method[0] == 'front':
            if q:
                target = q[0]
            else:
                target = -1
        elif method[0] == 'back':
            if q:
                target = q[-1]
            else:
                target = -1
        result.append(str(target))
print("\n".join(result))
