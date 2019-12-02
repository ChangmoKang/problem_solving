"""
def solution(heights):
    def check():
        f = heights.pop()
        for i in range(len(heights) - 1, -1, -1):
            t = heights[i]
            if t > f:
                return i + 1
        return 0
                
    result = []
    while heights:
        result.append(check())
    return result[::-1]
"""

def solution(heights):
    answer = [0] * len(heights)
    for f in range(len(heights) - 1, -1, -1):
        for t in range(f - 1, -1, -1):
            if heights[t] > heights[f]:
                answer[f] = t + 1
                break
    return answer


if __name__ == "__main__":
    INPUT = [
        [6,9,5,7,4],
        [3,9,9,3,5,7,2],
        [1,5,3,6,7,6,5]
    ]
    ANSWER = [
        [0,0,2,2,4],
        [0,0,0,3,3,3,6],
        [0,0,2,0,0,5,6]
    ]

    for index in range(3):
        print(True) if ANSWER[index] == solution(INPUT[index]) else print(False)
        