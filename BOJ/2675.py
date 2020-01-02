import sys
sys.stdin = open('input/2675.txt')


for _ in range(int(input())):
    N, word = input().split()
    N = int(N)
    new_word = [N * word[i] for i in range(len(word))]
    print("".join(new_word))
