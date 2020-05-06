BRACKET = {'(': ')', ')': '('}


def solution(p):
    
    def check(target, method='b'):
        s = 0
        
        for ch in target:
            if ch == '(':
                s += 1
            else:
                if method == 'c' and s == 0:
                    return False
                s -= 1
        
        return True if s == 0 else False


    if p == '':
        return ''
    
    for i in range(2, len(p) + 1, 2):
        if check(p[:i]):
            break
            
    u = p[:i]
    v = p[i:]
    
    if check(u, 'c'):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + "".join(map(lambda x: BRACKET[x], u[1:-1]))
    