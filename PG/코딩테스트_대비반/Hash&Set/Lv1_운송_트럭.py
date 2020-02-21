def solution(max_weight, specs, names):
    answer = 0
    specs = {name: int(weight) for name, weight in specs}
    
    curr_weight = 0
    for name in names:
        product_weight = specs[name]
        if curr_weight + product_weight <= max_weight:
            curr_weight = curr_weight + product_weight
        else:
            answer += 1
            curr_weight = product_weight
    
    return answer + 1  # 마지막 남은 물건(들)을 보내야 하기 때문에 +1
