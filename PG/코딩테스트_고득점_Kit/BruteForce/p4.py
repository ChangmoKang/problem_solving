def solution(brown, red):
    total = brown + red
    height = 2
    while True:
        if total % height == 0:
            width = int(total / height)
            if (width - 2) * (height - 2) == red:
                break
        height += 1
    return [width, height]


if __name__ == "__main__":
    INPUT1 = [
        10,
        8,
        24
    ]
    INPUT2 = [
        2,
        1,
        24
    ]
    ANSWER = [
        [4, 3],
        [3, 3],
        [8, 6]
    ]

    for index in range(3):
        print(True) if ANSWER[index] == solution(INPUT1[index], INPUT2[index]) else print(False)