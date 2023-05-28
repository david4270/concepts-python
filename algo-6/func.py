class Node:
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None
        self.colour = False

class Tree:
    def __init__(self, root = None):
        self.root = root
    
    def insert(self,data):
        if self.root:
            return self.root._insert(data)
        else:
            self.root = Node(data)
            return True

def searchTree(tree,data):
    if tree.search(data):
        print(data,"found")
    else:
        print(data,"not found")