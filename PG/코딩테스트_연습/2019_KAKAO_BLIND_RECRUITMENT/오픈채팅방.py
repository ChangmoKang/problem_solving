KIND, ID, NICK = 0, 1, 2
DO = {'Enter': '들어왔습니다.', 'Leave': '나갔습니다.'}

    
def solution(record):

    def id_to_nick(target):
        kind, id = target
        return f"{user[id]}님이 {DO[kind]}"
    

    user = {}
    answer = []
    for info in record:
        info = info.split()
        
        if info[KIND] != 'Change':
            answer.append((info[KIND],info[ID]))
            
        if info[KIND] != 'Leave':
            user[info[ID]] = info[NICK]
    
    answer = list(map(id_to_nick,answer))
    
    return answer
