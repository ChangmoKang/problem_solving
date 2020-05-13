DIGIT = '0123456789ABCDEF'

def solution(n, t, m, p):
    
    def convert(num, base):
        q, r = divmod(num, base)
        digit = DIGIT[r]
        return convert(q, base) + digit if q else digit
    
    result = ''
    
    target = 0
    while len(result) < m * t:
        result += convert(target, n)
        target += 1
    
    return "".join([r for i, r in enumerate(result) if i % m == p - 1][:t])
