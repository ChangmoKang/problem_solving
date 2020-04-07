import sys, heapq
sys.stdin = open('input/11286.txt')


N = int(input())

q = []
result = []
for _ in range(N):
    num = int(input())
    if num == 0:
        if not q:
            result.append('0')
        else:
            result.append(str(heapq.heappop(q)[1]))
    else:
        heapq.heappush(q, (abs(num), num))

print("\n".join(result))
