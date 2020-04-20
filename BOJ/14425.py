import sys
sys.stdin = open('input/14425.txt')
input = sys.stdin.readline


class Trie:
    head = {}

    def add(self, word):
        curr = self.head

        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        
        curr['*'] = True


    def search(self, word):
        curr = self.head

        for ch in word:
            if ch not in curr:
                return False
            curr = curr[ch]

        if '*' in curr:
            return True
        else:
            return False


N, M = map(int, input().split())
trie = Trie()
result = 0
for _ in range(N):
    trie.add(input())

for _ in range(M):
    if trie.search(input()):
        result += 1

print(result)