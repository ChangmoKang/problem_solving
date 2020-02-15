# 스킬트리
def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        tree = ''
        for s in skill_tree:
            if s in skill:
                tree += s
        
        if skill.startswith(tree):
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
