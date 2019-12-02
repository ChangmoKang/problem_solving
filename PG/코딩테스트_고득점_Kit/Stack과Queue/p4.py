from math import ceil

def solution(progresses, speeds):
    answer = []
    while progresses:
        required_day = ceil((100 - progresses[0]) / speeds[0])
        for i in range(len(progresses)):
            progresses[i] += required_day * speeds[i]
        
        flag = 0
        for i in range(len(progresses)):
            if progresses[i] < 100:
                flag = 1
                break

        if flag:
            answer.append(i)
            progresses = progresses[i:]
            speeds = speeds[i:]
        else:
            answer.append(len(progresses))
            progresses = []
    return answer


if __name__ == "__main__":
    INPUT1 = [
        [93, 30, 55]
    ]

    INPUT2 = [
        [1, 30, 5]
    ]

    ANSWER = [
        [2, 1]
    ]

    for index in range(1):
        print(True) if ANSWER[index] == solution(INPUT1[index], INPUT2[index]) else print(False)