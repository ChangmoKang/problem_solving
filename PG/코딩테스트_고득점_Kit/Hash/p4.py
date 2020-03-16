from collections import defaultdict

GENRE, PLAY = 0, 1
INDEX = 0
RECORD = 2
def solution(genres, plays):
    music_dic = defaultdict(list)
    count_dic = defaultdict(int)
    
    for index, music in enumerate(zip(genres, plays)):
        music_dic[music[GENRE]].append([index, music[PLAY]])
        count_dic[music[GENRE]] += music[PLAY]
    
    for genre in music_dic:
        music_dic[genre].sort(reverse=True, key=lambda x:x[PLAY])
        music_dic[genre] = [music[INDEX] for music in music_dic[genre]]
        
    result = []
    for music in sorted(count_dic.items(), key=lambda x: -x[PLAY]):
        result += music_dic[music[GENRE]][:RECORD]
    
    return result


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