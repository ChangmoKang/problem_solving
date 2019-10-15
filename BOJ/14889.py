import sys
sys.stdin = open('input/14889.txt')


def check(count, start):
    global result
    if count == N//2:
        tuple_arr = tuple(arr)
        if tuple_arr not in saved:
            saved.add(tuple_arr)
            arr2 = list(set(range(N)) - set(arr))
            saved.add(tuple(arr2))
            sub_result1 = 0
            for i in range(N//2 - 1):
                for j in range(i + 1, N//2):
                    sub_result1 += dic[arr[i], arr[j]]

            sub_result2 = 0
            for i in range(N//2 - 1):
                for j in range(i + 1, N//2):
                    sub_result2 += dic[arr2[i], arr2[j]]

            sub_result = abs(sub_result1 - sub_result2)
            if result > sub_result:
                result = sub_result

    else:
        for i in range(start, N):
            if not visited[i]:
                visited[i] = 1
                arr[count] = i
                check(count + 1, i + 1)
                arr[count] = 0
                visited[i] = 0


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

result = float('inf')
saved = set()
arr = [0]*(N//2)

dic = {}
for i in range(N - 1):
    for j in range(i + 1, N):
        dic[i, j] = board[i][j] + board[j][i]

visited = [0]*N
check(0, 0)
print(result)
