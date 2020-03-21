ENTRANCE, EXIT = 0, 1
def solution(routes):
    routes.sort()
        
    answer = 1
    camera = routes[0][EXIT]
    for route in routes[1:]:
        if route[ENTRANCE] > camera:
            answer += 1
            camera = route[EXIT]
        elif route[EXIT] < camera:
            camera = route[EXIT]

    return answer
