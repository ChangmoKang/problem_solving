def solution(tickets):
    def bfs():
        VISITED = {key: [0]*len(value) for key, value in dic.items()}
        q = [['ICN', ['ICN'], VISITED]]
        while q:
            f, sub_result, visited = q.pop(0)
            if f in dic:
                for index in range(len(dic[f])):
                    # value를 shallow copy해주어야 한다.
                    copied_visited = {key: value[:] for key, value in visited.items()}
                    copied_sub_result = sub_result[:]
                    if not copied_visited[f][index]:
                        copied_visited[f][index] = 1
                        copied_sub_result.append(dic[f][index])
                        if len(copied_sub_result) == len(tickets) + 1:
                            return copied_sub_result
                        q.append([dic[f][index], copied_sub_result, copied_visited])


    dic = {}
    for f, t in tickets:
        if f not in dic:
            dic[f] = [t]
        else:
            dic[f].append(t)
    
    for key in dic:
        dic[key].sort()

    result = bfs()
    return result


if __name__ == "__main__":
    INPUT = [
        [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]],
        [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]],
        [["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]
    ]
    ANSWER = [
        ["ICN", "JFK", "HND", "IAD"],
        ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"],
        ["ICN", "COO", "ICN", "BOO", "DOO"]
    ]
    
    for index in range(3):
        if ANSWER[index] == solution(INPUT[index]):
            print(True)
        else:
            print(False)
        