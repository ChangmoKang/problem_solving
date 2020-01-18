import sys
sys.stdin = open('input/1157.txt')


save = [0]*26
word = input().upper()
for w in word:
    save[ord(w) - 65] += 1

max_value = max(save)
max_index = save.index(max_value)
count = save.count(max_value)

if count == 1:
    print(chr(max_index + 65))
else:
    print('?')
