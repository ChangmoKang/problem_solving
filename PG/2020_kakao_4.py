# 효율성 테스트 2번 통과 못함
import sys
sys.stdin = open('input/2020_kakao_4.txt')

words = list(input().split())
queries = list(input().split())

dic = {}
answer = [-1]*len(queries)

for query_idx in range(len(queries)):
    query = queries[query_idx]

    if query not in dic:
        N = len(query)
        check = [i for i in range(N) if query[i] != "?"]
        correct_cnt = 0
        for word in words:
            if len(word) == N:
                flag = 1
                for check_idx in check:
                    if query[check_idx] != word[check_idx]:
                        flag = 0
                        break

                if flag:
                    correct_cnt += 1

        dic[query] = correct_cnt
        answer[query_idx] = correct_cnt
    else:
        answer[query_idx] = dic[query]

print(answer)
