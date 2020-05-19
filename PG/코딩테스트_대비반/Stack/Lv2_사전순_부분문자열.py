def solution(s):
    stack = []
    
    for elem in s:           
        while stack:
            if elem > stack[-1]:
                stack.pop()
            else:
                break
        
        stack.append(elem)
    
    return "".join(stack)
