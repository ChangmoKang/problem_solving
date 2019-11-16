import sys
sys.stdin = open('input/17826.txt')

for tc in range(1, int(input()) + 1):
    scores = list(map(int, input().split()))
    target = int(input())

    for index in range(len(scores)):
        score = scores[index]
        if target == score:
            break

    if 0 <= index <= 4:
        print("A+")
    elif 5 <= index <= 14:
        print("A0")
    elif 15 <= index <= 29:
        print("B+")
    elif 30 <= index <= 34:
        print("B0")
    elif 35 <= index <= 44:
        print("C+")
    elif 45 <= index <= 47:
        print("C0")
    else:
        print("F")
