import sys
sys.stdin = open('input/12869.txt')


def check():
    if not sum(SCV):
        return 0

    q = [SCV]
    cnt = 0
    while q:
        cnt += 1
        qs, q = q, []
        for target in qs:
            for attack in d[len(target)]:
                copied_target = target[:]
                for target_index in range(len(target) - 1, -1, -1):
                    copied_target[target_index] -= attack[target_index]
                    if copied_target[target_index] <= 0:
                        copied_target.pop(target_index)
                if not copied_target:
                    return cnt
                else:
                    t = tuple(copied_target)
                    if t not in visited:
                        visited.add(t)
                        q.append(copied_target)


d = [
    None,
    [[9]],
    [[9, 3], [3, 9]],
    [[9, 3, 1], [9, 1, 3], [3, 9, 1], [3, 1, 9], [1, 9, 3], [1, 3, 9]]
]
N = int(input())
SCV = list(map(int, input().split()))
visited = set()
result = check()
print(result)
