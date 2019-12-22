import sys
sys.stdin = open('input/1966.txt')


for _ in range(int(input())):
    N, target_index = map(int, input().split())
    q = list(enumerate(list(map(int, input().split()))))
    
    prior_list = [0] * 10
    for index, prior in q:
        prior_list[prior] += 1

    order = 1
    while True:
        if N == 1:
            break

        check = q.pop(0)

        flag = 0
        for i in range(check[1] + 1, 10):
            if prior_list[i]:
                flag = 1
                break

        if flag:
            q.append(check)
        else:
            if check[0] == target_index:
                break
            order += 1
            prior_list[check[1]] -= 1

    print(order)
