from itertools import product


def solution(monster, *dices):
    monster = set(monster)
    
    case = eval("*".join(map(str, dices)))
    
    dices = [range(1, dice + 1) for dice in dices]
    
    answer = 0
    for order in product(*dices):
        if sum(order) + 1 not in monster:
            answer += 1

    return int(answer/case*1000)
