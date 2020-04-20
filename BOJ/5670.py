import sys
sys.stdin = open('input/5670.txt')
input = sys.stdin.readline


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

    
    def search(self, word):
        curr = self.head

        for ch in word:
            if ch not in curr:
                return False
            curr = curr[ch]
        
        if END in curr:
            return True
        else:
            return False


    def dfs(self, curr, depth):
        nexts = list(curr.keys())

        if len(nexts) == 1:
            # 맨 처음은 하나라도 입력해야 하기 때문에
            if depth == 0:
                depth = 1

            next = nexts[0]

            if next == END:
                self.cnt += depth
                return

            self.dfs(curr[next], depth)
        else:
            for next in nexts:
                if next == END:
                    self.cnt += depth
                    continue

                self.dfs(curr[next], depth + 1)


    @property
    def result(self):
        r = str(round(self.cnt/N, 2))
        if len(r) != 4:
            r += '0'*(4 - len(r))
        return r


while True:
    N = input()

    if N == '':
        break
    else:
        N = int(N)

    trie = Trie()

    for _ in range(N):
        trie.add(input().strip())

    trie.dfs(trie.head, 0)
    print(trie.result)
