FROM, TO = 0, 1
def solution(tickets):

    def dfs(start, count, route):
        nonlocal answer

        if answer:
            return

        if count == N:
            answer = route[:]
            return
        else:
            for i, ticket in enumerate(tickets):
                if not visited[i] and ticket[FROM] == start:
                    visited[i] = True
                    route.append(ticket[TO])
                    dfs(ticket[TO], count + 1, route)
                    route.pop()
                    visited[i] = False
                    

    tickets.sort(key=lambda x: x[1])

    N = len(tickets)
    visited = [False]*N

    answer = []
    dfs('ICN', 0, ['ICN'])
    return answer
