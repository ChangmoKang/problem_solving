import sys
sys.stdin = open('input/17838.txt')


def check(word):
    if len(word) == 7:
        if word[0] != word[2]:
            if word[0] == word[1] and word[0] == word[4]:
                if word[2] == word[3] and word[2] == word[5] and word[2] == word[6]:
                    return "1"
    return "0"


N = int(input())
words = [list(input()) for _ in range(N)]

result = []
for word in words:
    result.append(check(word))
result = "\n".join(result)
print(result)
