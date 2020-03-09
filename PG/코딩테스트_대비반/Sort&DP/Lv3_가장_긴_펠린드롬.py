def solution(s):
    answer = [0]*2  # 홀수, 짝수 최대 펠린드롬 길이 저장

    for i in range(len(s)):
        width = answer[0] + 1
        while True:
            if i - width >= 0 and i + width + 1 <= len(s):
                if s[i - width:i] == s[i + 1: i + width + 1][::-1]:
                    if width > answer[0]:
                        answer[0] = width
                width += 1
            else:
                break

        width = answer[1]
        while True:
            if i - width >= 0 and i + width + 2 <= len(s):
                if s[i - width:i + 1] == s[i + 1: i + width + 2][::-1]:
                    if width + 1 > answer[1]:
                        answer[1] = width + 1
                width += 1
            else:
                break
        
        if answer[0] > answer[1]:
            answer[1] = answer[0]

    return max(2*answer[0] + 1, 2 * answer[1])
