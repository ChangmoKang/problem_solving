import sys
sys.stdin = open('input/14725.txt')


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

    
    def dfs(self, curr, depth):
        for key in sorted(curr.keys()):
            if key == '*':
                continue

            print("--"*depth + key)
            self.dfs(curr[key], depth + 1)




N = int(input())

trie = Trie()
for _ in range(N):
    word = list(input().split())[1:]
    trie.add(word)

trie.dfs(trie.head, 0)
