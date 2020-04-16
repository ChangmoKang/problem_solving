import sys
sys.setrecursionlimit(1_000_000)


X_VALUE, Y_VALUE = 0, 1

class Tree:
    def __init__(self, data_info):
        self.root = max(data_info, key=lambda info: info[Y_VALUE])
        left_info = [info for info in data_info if info[X_VALUE] < self.root[X_VALUE]]
        right_info = [info for info in data_info if info[X_VALUE] > self.root[X_VALUE]]
        
        if left_info:
            self.left = Tree(left_info)
        else:
            self.left = None
            
        if right_info:
            self.right = Tree(right_info)
        else:
            self.right = None

            
def solution(nodeinfo):
    def traverse(node):
        pre.append(node.root)
        
        if node.left is not None:
            traverse(node.left)
        
        if node.right is not None:
            traverse(node.right)
            
        post.append(node.root)


    tree = Tree(nodeinfo)
    pre = []
    post = []
    traverse(tree)
    
    answer = []
    answer.append(list(map(lambda x: nodeinfo.index(x) + 1, pre)))
    answer.append(list(map(lambda x: nodeinfo.index(x) + 1, post)))

    return answer
