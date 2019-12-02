def solution(participant, completion):
    dic = {}
    for p in participant:
        if p not in dic:
            dic[p] = 1
        else:
            dic[p] += 1
    
    for c in completion:
        if c not in dic:
            return c
        else:
            dic[c] -= 1
            
    for key in dic:
        if dic[key]:
            return key


if __name__ == "__main__":
    INPUT1 = [
        ["leo", "kiki", "eden"],
        ["marina", "josipa", "nikola", "vinko", "filipa"],
        ["mislav", "stanko", "mislav", "ana"]
    ]

    INPUT2 = [
        ["eden", "kiki"],
        ["josipa", "filipa", "marina", "nikola"],
        ["stanko", "ana", "mislav"]
    ]
    ANSWER = [
        "leo",
        "vinko",
        "mislav"
    ]

    for index in range(2):
        print(True) if ANSWER[index] == solution(INPUT1[index], INPUT2[index]) else print(False)