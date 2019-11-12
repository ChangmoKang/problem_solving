import sys
sys.stdin = open('input/17143.txt')


dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]
other_way = {0: 1, 1:0, 2:3, 3:2}
R, C, M = map(int, input().split())

# 결과
result = 0

# 초기 상어 입력과 상어 인덱스
sharks = []
for _ in range(M):
    r, c, s, d, size = map(int, input().split())
    sharks.append([r - 1, c - 1, s, d - 1, size])
sharks_index = list(range(M))

# 낚시꾼의 C 위치(초기 -1)
fisher_C = -1

# 시작
while True:
    # 초기 상어의 위치 입력 및 이후 상어가 이동한 후 잡아 먹히는 부분
    dic = {}
    trash = set()
    for index in sharks_index:
        r, c, s, d, size = sharks[index]
        if (r, c) not in dic:
            dic[r, c] = index
        else:
            other_index = dic[r, c]
            other_size = sharks[other_index][-1]
            if other_size > size:
                trash.add(index)
            else:
                trash.add(other_index)
                dic[r, c] = index

    if trash:
        sharks_index = list(set(sharks_index) - trash)

    # 낚시꾼 이동
    fisher_C += 1

    # 낚시 하는 부분
    for r in range(R):
        if (r, fisher_C) in dic:
            index = dic[r, fisher_C]
            result += sharks[index][-1]
            sharks_index.remove(index)
            break

    # 끝에 왔으면 종료
    if fisher_C == C - 1:
        break

    # 상어가 이동하는 부분
    for index in sharks_index:
        r, c, s, d, size = sharks[index]
        rr, cc, ss = r, c, s
        if d == 0:
            if rr != 0:
                if 0 <= ss < rr:
                    rr -= ss
                elif ss >= rr:
                    ss -= rr
                    rr = 0
                    d = other_way[d]
                    # % 연산 시작
                    ss = ss % (2 * (R - 1))
                    if 0 <= ss < (R - 1):
                        rr = ss
                    else:
                        rr = (R - 1) - (ss - (R - 1))
                        d = other_way[d]
            else:
                d = other_way[d]
                # % 연산 시작
                ss = ss % (2 * (R - 1))
                if 0 <= ss < (R - 1):
                    rr = ss
                else:
                    rr = (R - 1) - (ss - (R - 1))
                    d = other_way[d]  

        elif d == 1:
            if rr != 0:
                if 0 <= ss < (R - 1) - rr:
                    rr += ss
                elif (R - 1) - rr <= ss < (R - 1) - rr + (R - 1):
                    rr = (R - 1) - (ss - ((R - 1) - rr))
                    d = other_way[d]
                elif ss >= (R - 1) - rr + (R - 1):
                    ss -= (R - 1) - rr + (R - 1)
                    rr = 0
                    # % 연산 시작
                    ss = ss % (2 * (R - 1))
                    if 0 <= ss < (R - 1):
                        rr = ss
                    else:
                        rr = (R - 1) - (ss - (R - 1))
                        d = other_way[d]
            else:
                # % 연산 시작
                ss = ss % (2 * (R - 1))
                if 0 <= ss < (R - 1):
                    rr = ss
                else:
                    rr = (R - 1) - (ss - (R - 1))
                    d = other_way[d]
        elif d == 2:
            if cc != 0:
                if 0 <= ss < (C - 1) - cc:
                    cc += ss
                elif (C - 1) - cc <= ss < (C - 1) - cc + (C - 1):
                    cc = (C - 1) - (ss - ((C - 1) - cc))
                    d = other_way[d]
                elif ss >= (C - 1) - cc + (C - 1):
                    ss -= (C - 1) - cc + (C - 1)
                    cc = 0
                    # % 연산 시작
                    ss = ss % (2 * (C - 1))
                    if 0 <= ss < (C - 1):
                        cc = ss
                    else:
                        cc = (C - 1) - (ss - (C - 1))
                        d = other_way[d]
            else:
                # % 연산 시작
                ss = ss % (2 * (C - 1))
                if 0 <= ss < (C - 1):
                    cc = ss
                else:
                    cc = (C - 1) - (ss - (C - 1))
                    d = other_way[d]

        elif d == 3:
            if cc != 0:
                if 0 <= ss < cc:
                    cc -= ss
                elif ss >= cc:
                    ss -= cc
                    cc = 0
                    d = other_way[d]
                    # % 연산 시작
                    ss = ss % (2 * (C - 1))
                    if 0 <= ss < (C - 1):
                        cc = ss
                    else:
                        cc = (C - 1) - (ss - (C - 1))
                        d = other_way[d]
            else:
                d = other_way[d]
                # % 연산 시작
                ss = ss % (2 * (C - 1))
                if 0 <= ss < (C - 1):
                    cc = ss
                else:
                    cc = (C - 1) - (ss - (C - 1))
                    d = other_way[d]

        sharks[index] = [rr, cc, s, d, size]
print(result)
