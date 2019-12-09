import sys
sys.stdin = open('input/1193.txt')

N = int(input())
bottom = int((-1 + (1 + 8 * N) ** 0.5)/2)
N -= int(bottom * (bottom + 1) / 2)

if bottom % 2:
    print(f"{N}/{bottom+2-N}") if N else print(f"1/{bottom}")
else:
    print(f"{bottom+2-N}/{N}") if N else print(f"{bottom}/1")
