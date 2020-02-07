def solution(skill, skill_trees):
    answer = 0
    word_to_idx = {word: idx for idx, word in enumerate(skill)}
    A = set(skill)
    for skill_tree in skill_trees:
        skill_tree = list(skill_tree)
        B = set(skill_tree)
        for el in B - A:
            skill_tree.remove(el)
        
        flag = 0
        for idx in range(len(skill_tree)):
            skill_tree[idx] = word_to_idx[skill_tree[idx]]
            if idx != skill_tree[idx]:
                flag = 1
                break
        
        if not flag:
            answer += 1

    return answer


if __name__ == "__main__":
    INPUT1 = [
        "CBD"
    ]
    INPUT2 = [
        ["BACDE", "CBADF", "AECB", "BDA"]
    ]
    ANSWER = [
        2
    ]
    
    for index in range(len(ANSWER)):
        print(True) if ANSWER[index] == solution(INPUT1[index], INPUT2[index]) else print(False)
