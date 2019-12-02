def solution(bridge_length, weight, truck_weights):
    answer = 0
    current_weight = []
    current_distance = []
    while True:
        answer += 1
        if current_distance:
            for i in range(len(current_distance)):
                current_distance[i] += 1
        
        if current_distance and current_distance[0] == bridge_length:
            current_weight.pop(0)
            current_distance.pop(0)
            
        if sum(current_distance) == 0 and truck_weights == []:
            break
        
        if truck_weights and sum(current_weight) + truck_weights[0] <= weight:
            current_weight.append(truck_weights.pop(0))
            current_distance.append(0)
        
    return answer


if __name__ == "__main__":
    INPUT1 = [
        2,
        100,
        100
    ]

    INPUT2 = [
        10,
        100,
        100
    ]

    INPUT3 = [
        [7,4,5,6],
        [10],
        [10,10,10,10,10,10,10,10,10,10]
    ]

    ANSWER = [
        8,
        101,
        110
    ]

    for index in range(2):
        print(True) if ANSWER[index] == solution(INPUT1[index], INPUT2[index], INPUT3[index]) else print(False)