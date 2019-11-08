import sys
sys.stdin = open('input/2020_kakao_1.txt')

for tc in range(1, int(input()) + 1):
    s = input()
    answer = len(s)

    for x in range(1, int(len(s)/2) + 1):
        data = [s[0:x]]
        num = [1]
        idx = 1
        while True:
            front = x * idx
            end = x * (idx + 1)

            if end > len(s):
                break
            
            if s[front:end] == data[-1]:
                num[-1] += 1
            else:
                data.append(s[front:end])
                num.append(1)

            idx += 1
        
        sub_answer = len(data) * x + len(s[front:])
        for i in range(len(num)):
            if num[i] != 1:
                sub_answer += len(str(num[i]))

        if answer > sub_answer:
            answer = sub_answer

    print(answer)
