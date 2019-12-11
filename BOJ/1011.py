import sys
sys.stdin = open('input/1011.txt')


for _ in range(int(input())):
    A, B = map(int, input().split())
    tmp = B - A
    
    target = int(tmp ** 0.5)

    if target ** 2 == tmp:
        print(2 * target - 1)
    else:
        f = target ** 2
        t = (target + 1) ** 2
        print(2 * target + 1) if tmp > (f + t) / 2 else print(2 * target)
