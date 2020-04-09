from collections import defaultdict

METHOD, ID, NAME, IDX = 0, 1, 2, 2
def solution(record):
    idx = 0
    name_dic, log_dic = {}, defaultdict(list)

    for log in record:
        log = log.split()
        if log[METHOD] == 'Enter' or log[METHOD] == 'Leave':
            if log[METHOD] == 'Enter':
                name_dic[log[ID]] = log[NAME]
            log_dic[log[ID]].append((log[METHOD], log[ID], idx))
            idx += 1
        elif log[METHOD] == 'Change':
            name_dic[log[ID]] = log[NAME]
            
    result = []
    for value in log_dic.values():
        result.extend(value)
    result.sort(key=lambda x: x[IDX])
    
    answer = []
    for log in result:
        if log[METHOD] == 'Enter':
            answer.append(f"{name_dic[log[ID]]}님이 들어왔습니다.")
        else:
            answer.append(f"{name_dic[log[ID]]}님이 나갔습니다.")

    return answer
