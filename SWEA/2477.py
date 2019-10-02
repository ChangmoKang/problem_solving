import sys
sys.stdin = open('input/2477.txt')


def receipt_and_repair():
    for i in range(N):
        if receipt_status[i] > 0:
            receipt_status[i] -= 1
            if receipt_status[i] == 0:
                repair_wait.append(receipt_visit[i][-1])
    
    for j in range(M):
        if repair_status[j] > 0:
            repair_status[j] -= 1



for tc in range(1, int(input()) + 1):
    N, M, K, A, B = map(int, input().split())
    A -= 1
    B -= 1
    receipt_time = list(map(int, input().split()))
    repair_time = list(map(int, input().split()))
    customer_arrival = list(enumerate(list(map(int, input().split())), start=1))
    
    receipt_visit = [[] for _ in range(N)]
    receipt_status = [0] * N

    repair_wait = []
    repair_visit = [[] for _ in range(M)]
    repair_status = [0] * M

    t = customer_arrival[0][1]

    while True:
        for i in range(N):
            if customer_arrival:
                if receipt_status[i] == 0 and customer_arrival[0][1] <= t:
                    customer = customer_arrival.pop(0)
                    receipt_status[i] = receipt_time[i]
                    receipt_visit[i].append(customer[0])
            else:
                break
        

        for i in range(M):
            if repair_wait:
                if repair_status[i] == 0:
                    customer = repair_wait.pop(0)
                    repair_status[i] = repair_time[i]
                    repair_visit[i].append(customer)
            else:
                break
        
        receipt_and_repair()
        
        t += 1
        
        if not customer_arrival and not sum(receipt_status) and not repair_wait and not sum(repair_status):
            break

    result = sum(set(receipt_visit[A]) & set(repair_visit[B]))

    print(f"#{tc} {result}") if result else print(f"#{tc} -1")
