def solution(genres, plays):
    answer = []
    # 고유 번호를 재생 횟수에 입력
    plays = list(enumerate(plays))

    # 장르별로 분류하는 작업
    dic = {}
    for i in range(len(genres)):
        genre = genres[i]
        if genre not in dic:
            dic[genre] = [plays[i]]
        else:
            dic[genre].append(plays[i])
    
    # 각 장르별 내림차순 정렬
    for key in dic:
        dic[key].sort(key=lambda x: x[1], reverse=True)
    

    # 각각의 장르에 총 재생 횟수와 재생 횟수를 기준으로 내림차순 정렬
    each_genre_sum = []
    for key, value in dic.items():
        each_genre_sum.append([key, sum([value[w][1] for w in range(len(value))])])
    each_genre_sum.sort(key=lambda x: x[1], reverse=True)
    
    # 재생 횟수가 가장 큰 장르부터 두개씩 고유번호 추출
    for i in range(len(dic)):
        answer.extend(dic[each_genre_sum[i][0]][:2])

    # 다듬기
    answer = [answer[i][0] for i in range(len(answer))]
    return answer


if __name__ == "__main__":
    INPUT1 = [
        ["classic", "pop", "classic", "classic", "pop"]
    ]
    INPUT2 = [
        [500, 600, 150, 800, 2500]
    ]
    ANSWER = [
        [4, 1, 3, 0]
    ]

    for index in range(1):
        print(True) if ANSWER[index] == solution(INPUT1[index], INPUT2[index]) else print(False)