"""
def solution(k, room_number):
    
    def find_other_room(target_room):
        return assigned_room[target_room]

    
    assigned_room = {}
    
    result = []
    for p_num in room_number:
        if p_num not in assigned_room:
            result.append(p_num)
            assigned_room[p_num] = p_num + 1
            continue

        s_num = assigned_room[p_num]
        if s_num not in assigned_room:
            result.append(s_num)
            assigned_room[s_num] = s_num + 1
            continue

        update_nums = [s_num]

        while True:
            s_num = find_other_room(s_num)
            update_nums.append(s_num)
            if s_num not in assigned_room:
                result.append(s_num)
                assigned_room[s_num] = s_num + 1
                break

        for update_num in update_nums:
            assigned_room[update_num] = s_num + 1

    return result
"""


def solution(k, room_number):    
    result = []
    assigned = {}
    
    for room in room_number:
        visited = [room]
        
        while room in assigned:
            room = assigned[room]
            visited.append(room)
        
        result.append(room)
        
        for visit in visited:
            assigned[visit] = room + 1
        
    return result
