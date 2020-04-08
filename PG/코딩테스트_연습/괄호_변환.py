def check(brackets):
    stack = 0
    for bracket in brackets:
        if bracket == "(":
            stack += 1
        else:
            if stack:
                stack -= 1
            else:
                return False

    return True


def solution(p):
    if p == '':
        return ''

    u, v = '', ''
    for i in range(2, len(p) + 1, 2):
        u_target = p[:i]
        if u_target.count('(') == i // 2:
            v_target = p[i:]
            if v_target.count('(') == (len(p) - i) // 2:
                u = u_target
                v = v_target
                break

    if check(u):
        v = solution(v)
        return u + v
    else:
        answer = '(' + solution(v) + ')'

        for bracket in u[1:-1]:
            if bracket == "(":
                answer +=  ")"
            else:
                answer += "("

        return answer