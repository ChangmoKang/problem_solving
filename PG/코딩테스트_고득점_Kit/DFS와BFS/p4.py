def solution(tickets):

    def dfs(count, List):
        if not result:
            if count == len(tickets):
               result.append(List)
            else:
                if List[-1] in dic:
                    for t_i in range(len(dic[List[-1]])):
                        t = dic[List[-1]][t_i]
                        if not visited[List[-1]][t_i]:
                            visited[List[-1]][t_i] = 1
                            dfs(count + 1, List + [t])
                            visited[List[-1]][t_i] = 0


    dic = {}
    for f, t in tickets:
        if f not in dic:
            dic[f] = [t]
        else:
            dic[f].append(t)

    for key in dic:
        dic[key].sort()

    result = []
    visited = {key: [0]*len(value) for key, value in dic.items()}
    dfs(0, ['ICN'])

    return result[0]


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
        