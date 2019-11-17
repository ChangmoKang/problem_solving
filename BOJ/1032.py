import sys
sys.stdin = open('input/1032.txt')

N = int(input())
file_names = [input() for _ in range(N)]
file_names_N = len(file_names[0])

result = []
for i in range(file_names_N):
    flag = 0
    target = file_names[0][i]
    for index in range(1, N):
        file_name = file_names[index]
        if target != file_name[i]:
            flag = 1
            break

    if flag:
        result.append('?')
    else:
        result.append(target)

result = "".join(result)
print(result)
