import sys
sys.stdin = open('input/17952.txt')
input = sys.stdin.readline

time = int(input())
stack = []
current = []
result = 0
for _ in range(time):
    target = list(map(int, input().split()))
    if target[0] == 1:
        if current:
            stack.append(current)
        current = [target[1], target[2] - 1]
        if current[-1] == 0:
            result += current[0]
            if stack:
                current = stack.pop()
            else:
                current = []
    else:
        if current:
            current[-1] -= 1
            if current[-1] == 0:
                result += current[0]
                if stack:
                    current = stack.pop()
                else:
                    current = []
print(result)
