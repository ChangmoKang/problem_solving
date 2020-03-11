from collections import defaultdict

def solution(clothes):
    clothes_sort_by_kind = defaultdict(int)
    
    for _, kind in clothes:
        clothes_sort_by_kind[kind] += 1
    
    pieces = [count + 1 for count in clothes_sort_by_kind.values()]
    return eval("*".join(str(piece) for piece in pieces)) - 1


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