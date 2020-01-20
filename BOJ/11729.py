import sys
sys.stdin = open('input/11729.txt')


def check(num, f, b, t):
    if num == 1:
        result.append([f, t])
    else:
        check(num - 1, f, t, b)
        result.append([f, t])
        check(num - 1, b, f, t)

result = []
check(int(input()), 1, 2, 3)

print(len(result))
for el in result:
    print(*el)
