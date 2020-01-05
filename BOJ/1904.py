import sys
sys.stdin = open('input/1904.txt')


N = int(input())
if N <= 2:
    print(N)
else:
    a, b = 1, 2
    index = 3
    while True:
        t = b
        b = (a + b) % 15746
        a = t
        if N == index:
            break
        index += 1
    print(b)
