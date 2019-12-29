import sys
sys.stdin = open('input/1759.txt')


def check(count, start, inspector):
    if count == N:
        if inspector[0] >= 1 and inspector[1] >= 1:
            result.append("".join(tmp))
    else:
        for i in range(start, K):
            tmp[count] = words[i]
            if words[i] in vowel:
                inspector[1] += 1
                check(count + 1, i + 1, inspector)
                inspector[1] -=1
            else:
                inspector[0] += 1
                check(count + 1, i + 1, inspector)
                inspector[0] -= 1
            tmp[count] = 0


vowel = ['a', 'e', 'i', 'o', 'u']

N, K = map(int, input().split())
words = sorted(input().split())
tmp = [0]*N
result = []
check(0, 0, [-1, 0])
print("\n".join(result))
