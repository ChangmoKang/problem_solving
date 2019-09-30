import sys
sys.stdin = open('input/4013.txt')


def rotate(index, direction):
    q = [[index, direction]]
    while q:
        each_index, each_direction  = q.pop()

        if each_index - 1 >= 0 and magnets[each_index - 1][2] != magnets[each_index][-2]:
            if not visited[each_index - 1]:
                visited[each_index - 1] = 1
                q.append([each_index - 1, -each_direction])
        if each_index + 1 < N and magnets[each_index + 1][-2] != magnets[each_index][2]:
            if not visited[each_index + 1]:
                visited[each_index + 1] = 1
                q.append([each_index + 1, -each_direction])

        if each_direction == 1:
            tmp = magnets[each_index].pop()
            magnets[each_index].insert(0, tmp)
        else:
            tmp = magnets[each_index].pop(0)
            magnets[each_index].append(tmp)

for tc in range(1, int(input()) + 1):
    N = 4
    K = int(input())
    magnets = [list(map(int, input().split())) for _ in range(N)]
    
    for _ in range(K):
        idx, d = map(int, input().split())
        
        visited = [0]*N
        visited[idx - 1] = 1
        rotate(idx - 1, d)
    
    result = sum([2**i for i in range(N) if magnets[i][0] == 1])
    print(f"#{tc} {result}")
