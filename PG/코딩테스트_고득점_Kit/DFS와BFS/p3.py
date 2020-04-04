def solution(begin, target, words):
    def check(word_a, word_b):
        cnt = 0
        for a, b in zip(word_a, word_b):
            if a != b:
                cnt += 1

        if cnt == 1:
            return True
        return False


    q = [begin]
    visited = set([begin])

    step = 0
    while q:
        qs, q = q, []
        for search_target in qs:
            for word in words:
                if word not in visited and check(search_target, word):
                    if word == target:
                        return step + 1
                    
                    visited.add(word)
                    q.append(word)
        step += 1
    
    return 0
