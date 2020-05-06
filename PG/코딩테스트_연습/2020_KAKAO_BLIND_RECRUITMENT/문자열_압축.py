def solution(s):

    def concat():
        nonlocal sub_answer

        sub_answer += f'{target}' if repeat == 1 else f'{repeat}{target}'

        
    N = len(s)
    
    answer = N
    for interval in range(1, N//2 + 1):
        sub_answer = ''
        target = s[:interval]
        repeat = 1
        
        for idx in range(interval, N, interval):
            if s[idx:idx + interval] == target:
                repeat += 1
            else:
                concat()

                target = s[idx:idx + interval]
                repeat = 1
                
        concat()
        
        sub_answer += s[idx + interval:]
        
        if answer > len(sub_answer):
            answer = len(sub_answer)
            
    return answer
