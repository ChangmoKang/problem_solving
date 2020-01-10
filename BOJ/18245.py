import sys
sys.stdin = open('input/18245.txt')


skip = 2
while True:
    word = input()
    if word == 'Was it a cat I saw?':
        break

    N = len(word)

    result = [word[i] for i in range(0, N, skip)]
    print("".join(result))
    skip += 1
