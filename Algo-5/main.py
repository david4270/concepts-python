#BST

class Node:
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None
    def _insert(self,data):
        if data == self.value: #if key = self.value, failed to insert
            return False
        elif self.value > data: #if self.value is larger than data, go left to insert
            if self.left: #if self.left exists, recursively call _insert for self.left
                return self.left._insert(data)
            else: #if self.left doesn't exist, add node at self.left and return True
                self.left = Node(data)
                return True
        else: #if self.value is smaller than data, go right to insert
            if self.right: #if self.right exists, recursively call _insert for self.right
                return self.right._insert(data)
            else: #if self.right doesn't exist, add node at self.right and return True
                self.right = Node(data)
                return True

class Tree:
    def __init__(self, root = None):
        self.root = root
    
    def insert(self,data):
        if self.root: #if root != None
            return self.root._insert(data)
        else: #if root == None
            self.root = Node(data)
            return True
    
    def search(self,data):
        ()
    
    def delete(self,data):
        ()
    
    def getMax(self):
        ()

    def getMin(self):
        ()
    
    def inOrder(self):
        ()
    
    def preOrder(self):
        ()
    
    def postOrder(self):
        ()

def main():
    tr = Tree()
    tr.insert(3)
    tr.insert(5)
    tr.insert(2)

if __name__ == "__main__":
    main()