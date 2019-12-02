def solution(clothes):

    def mul(List):
        tmp = 1
        for el in List:
            tmp *= el
        return tmp


    # kind별로 name을 정리함
    dic = {}
    for name, kind in clothes:
        if kind not in dic:
            dic[kind] = [name]
        else:
            dic[kind].append(name)
    
    # 각각의 kind의 name의 갯수
    names_each_kind = [len(value) + 1 for value in dic.values()]

    # 경우의 수 계산
    answer = mul(names_each_kind) - 1
    return answer

if __name__ == "__main__":
    INPUT1 = [
        [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]],
        [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
    ]
    ANSWER = [
        5,
        3
    ]

    for index in range(2):
        print(True) if ANSWER[index] == solution(INPUT1[index]) else print(False)