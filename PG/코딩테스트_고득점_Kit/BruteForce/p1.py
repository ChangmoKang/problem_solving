def solution(answers):
    ways = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    correct = [0] * len(ways)
    
    for number, answer in enumerate(answers):
        for way_index in range(len(ways)):
            way = ways[way_index]
            if answer == way[(number % len(way))]:
                correct[way_index] += 1
                
    return [i + 1 for i in range(len(correct)) if correct[i] == max(correct)]


if __name__ == "__main__":
    INPUT1 = [
        [1,2,3,4,5],
        [1,3,2,4,2]
    ]
    ANSWER = [
        [1],
        [1,2,3]
    ]

    for index in range(2):
        print(True) if ANSWER[index] == solution(INPUT1[index]) else print(False)