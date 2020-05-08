FORWARD, BACKWARD = 0, 1
def solution(words, queries):
    trie = {}

    for word in words:
        length = len(word)

        trie.setdefault(length, ({}, {}))

        target = trie[length][FORWARD]
        for ch in word:
            target['count'] = target.get('count', 0) + 1
            target = target.setdefault(ch, {})

        target = trie[length][BACKWARD]
        for ch in word[::-1]:
            target['count'] = target.get('count', 0) + 1
            target = target.setdefault(ch, {})
    
    answer = []
    for query in queries:
        length = len(query)

        if length not in trie:
            answer.append(0)
            continue

        if query[0] == '?':
            query = query[::-1]
            target = trie[length][BACKWARD]
        else:
            target = trie[length][FORWARD]

        for ch in query:
            if ch == '?':
                answer.append(target.get('count', 0))
                break
            if ch not in target:
                answer.append(0)
                break
            target = target[ch]

    return answer