import sys
sys.stdin = open('input/18312.txt')

    
N, K = input().split()
N = int(N)
H, M, S = 0, 0, 0
result = 0

while True:
    if H == N + 1:
        break
    
    if 0 <= H < 10 or 0 <= M < 10 or 0 <= S < 10:
        a = '0' + str(H) + str(M) + str(S)
    else:
        a = str(H) + str(M) + str(S)

    if K in a:
        result += 1

    s_flag = 0
    if S == 59:
        s_flag = 1
        S = 0
    else:
        S += 1

    if s_flag:
        m_flag = 0
        if M == 59:
            m_flag = 1
            M = 0
        else:
            M += 1

        if m_flag:
            H += 1

print(result)
