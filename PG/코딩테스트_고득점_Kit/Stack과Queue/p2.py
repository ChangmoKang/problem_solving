def solution(priorities, location):
    answer = 0
    priorities = list(enumerate(priorities))
    while priorities:
        front = priorities.pop(0)

        flag = 1
        for i in range(len(priorities)):
            if front[1] <priorities[i][1]:
                flag = 0
                break

        if flag:
            answer += 1
            if front[0] == location:
                break
        else:
            priorities.append(front)
    return answer


if __name__ == "__main__":
    INPUT1 = [
        [2, 1, 3, 2],
        [1, 1, 9, 1, 1, 1]
    ]

    INPUT2 = [
        2,
        0
    ]

    ANSWER = [
        1,
        5
    ]

    for index in range(2):
        print(True) if ANSWER[index] == solution(INPUT1[index], INPUT2[index]) else print(False)