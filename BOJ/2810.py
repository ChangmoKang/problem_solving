import sys
sys.stdin = open('input/2810.txt')

N = int(input())
seats = input()
s = seats.replace("LL", "L")
print(len(s) + 1) if len(s) + 1 <= N else print(len(s))
