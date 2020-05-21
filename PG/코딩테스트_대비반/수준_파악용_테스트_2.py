# 스킬트리
def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        cleaned = "".join([elem for elem in skill_tree if elem in skill])
        
        if skill.startswith(cleaned):
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
