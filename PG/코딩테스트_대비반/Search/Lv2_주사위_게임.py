from functools import reduce

def solution(monster, *dices):
    def check(count, loc):
        nonlocal empty_loc_cases
        if count == 3:
            if loc in monster_loc:
                empty_loc_cases -= 1
        else:
            for i in range(dices[count]):
                check(count + 1, loc + (i + 1))  # 주사위가 1부터 시작하므로 1을 더해줌


    monster_loc = set(monster)
    
    # all_cases = eval("*".join(map(str, dices)))
    all_cases = reduce(lambda a, b: a*b, dices)
    empty_loc_cases = all_cases
    
    check(0, 1)
    
    return int(empty_loc_cases/all_cases*1000)
