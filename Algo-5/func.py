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
    
    def _search(self,data):
        if data == self.value:
            return True
        elif self.value > data: 
            if self.left: 
                return self.left._search(data)
            else: 
                return False
        else: 
            if self.right: 
                return self.right._search(data)
            else: 
                return False

    def _delete(self,data):
        if self == None:
            return self
        if self.value > data:
            self.left = self.left._delete(data)
        elif self.value < data:
            self.right = self.right._delete(data)
        else:
            if self.left == None and self.right == None:
                self = None
            elif self.left == None:
                temp = self.right
                self = None
                return temp
            elif self.right == None:
                temp =  self.left
                self = None
                return temp
            else:
                temp = self.right
                while temp.left:
                    temp = temp.left
                self.value = temp.value
                self.right = self.right._delete(temp.value)
        return self


    
    def _getmax(self):
        if self.right:
            return self.right._getmax()
        else:
            return self.value

    def _getmin(self):
        if self.left:
            return self.left._getmin()
        else:
            return self.value
    
    def _inorder(self):
        if self.left:
            self.left._inorder()
        print(self.value)
        if self.right:
            self.right._inorder()
        return

    def _preorder(self):
        print(self.value)
        if self.left:
            self.left._preorder()
        if self.right:
            self.right._preorder()
        return
    
    def _postorder(self):
        if self.left:
            self.left._postorder()
        if self.right:
            self.right._postorder()
        print(self.value)
        return

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
        if self.root:
            return self.root._search(data)
        else:
            return False
    
    def delete(self,data):
        if self.root:
            return self.root._delete(data)
        else:
            return False
    
    def getMax(self):
        if self.root:
            return self.root._getmax()
        else:
            return False

    def getMin(self):
        if self.root:
            return self.root._getmin()
        else:
            return False
    
    def inOrder(self):
        if self.root:
            return self.root._inorder()
        else:
            return False
    
    def preOrder(self):
        if self.root:
            return self.root._preorder()
        else:
            return False
    
    def postOrder(self):
        if self.root:
            return self.root._postorder()
        else:
            return False

def searchTree(tree, data):
    if tree.search(data):
        print(data,"found")
    else:
        print(data,"not found")
