import sys
sys.stdin = open('input/5397.txt')


for _ in range(int(input())):
    words = list(input())

    result = []
    arrow = []
    for word in words:
        if word in '<>-':
            if word == '<':
                if result:
                    value = result.pop()
                    arrow.append(value)
            elif word == '>':
                if arrow:
                    value = arrow.pop()
                    result.append(value)
            else:
                if result:
                    result.pop()
        else:
            result.append(word)

    if arrow:
        result.extend(arrow[::-1])

    print("".join(result))
