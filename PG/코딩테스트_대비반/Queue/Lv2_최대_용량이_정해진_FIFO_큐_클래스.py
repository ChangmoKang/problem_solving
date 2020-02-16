class EmptyException(Exception): ...

class MyStack(object):
    def __init__(self):
        self.lst = list()

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        return self.lst.pop()

    def size(self):
        return len(self.lst)

class MyQueue(object):
    def __init__(self, max_size):
        self.stack1 = MyStack()
        self.stack2 = MyStack()
        self.max_size = max_size

    def qsize(self):
        return self.stack1.size() + self.stack2.size()

    def push(self, item):
        if self.qsize() == self.max_size:
            return False
        
        self.stack1.push(item)
        return True

    def pop(self):
        if self.qsize() == 0:
            raise EmptyException
        
        if self.stack2.size() == 0:
            while self.stack1.size() > 0:
                self.stack2.push(self.stack1.pop())

        return self.stack2.pop()
            
    
N, max_size = map(int, input().strip().split(' '))
q = MyQueue(max_size)
for _ in range(N):
    try:
        method = input().strip().split()
        if method[0] == 'PUSH':
            result = q.push(method[1])
        elif method[0] == 'POP':
            result = q.pop()
        elif method[0] == 'SIZE':
            result = q.qsize()
        print(result)

    except EmptyException:
        print(False)
