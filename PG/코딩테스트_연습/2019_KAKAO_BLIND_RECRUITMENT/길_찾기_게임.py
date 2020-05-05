import sys
sys.setrecursionlimit(1_000_000)


X, Y = 0, 1
IDX, NODE = 0, 1


class Tree(object):
    pre = []
    post = []

    def __init__(self, data):
        self.root = max(data, key=lambda x: x[NODE][Y])
        self.left = self.sub_tree([elem for elem in data if elem[NODE][X] < self.root[NODE][X]])
        self.right = self.sub_tree([elem for elem in data if elem[NODE][X] > self.root[NODE][X]])
        
    def sub_tree(self, data):
        return Tree(data) if data else None
    
    def traverse(self):
        Tree.pre.append(self.root[IDX])
        
        if self.left is not None:
            self.left.traverse()
            
        if self.right is not None:
            self.right.traverse()
            
        Tree.post.append(self.root[IDX])
    
    
def solution(nodeinfo):
    nodeinfo = [(i, node) for i, node in enumerate(nodeinfo, start=1)]
    
    tree = Tree(nodeinfo)
    tree.traverse()
    
    return [tree.pre, tree.post]
