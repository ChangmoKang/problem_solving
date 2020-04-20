import sys
sys.setrecursionlimit(10**6)


END = '*'
class Trie:
    def __init__(self):
        self.head = {}
        self.cnt = 0


    def add(self, word):
        curr = self.head

        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]

        curr[END] = True

        
    def dfs(self, curr, depth, solo):
        nexts = list(curr.keys())

        if len(nexts) == 1:
            next = nexts[0]

            if next == END:
                self.cnt += depth - solo
                return

            self.dfs(curr[next], depth + 1, solo + 1)

        else:
            for next in nexts:
                if next == END:
                    self.cnt += depth
                    continue

                self.dfs(curr[next], depth + 1, 0)


def solution(words):
    trie = Trie()
    for word in words:
        trie.add(word)

    trie.dfs(trie.head, 0, 0)
    
    return trie.cnt