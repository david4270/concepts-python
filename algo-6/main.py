#red-black tree
import func

def main():
    tr = func.Tree()
    tr.insert(3)
    tr.insert(5)
    tr.insert(2)
    tr.insert(4)
    tr.insert(7)
    tr.insert(6)
    tr.insert(1)
    
    print("In-order traversal:")
    tr.inOrder()
    print("Pre-order traversal:")
    tr.preOrder()
    print("Post-order traversal:")
    tr.postOrder()    

    print("Maximum is:",tr.getMax())
    print("Minimum is:",tr.getMin())

    func.searchTree(tr,4)
    func.searchTree(tr,7)
    func.searchTree(tr,1)
    func.searchTree(tr,8)

    tr.delete(3)
    tr.delete(5)

    print("In-order traversal:")
    tr.inOrder()

    tr.insert(3)
    tr.insert(5)

    print("In-order traversal:")
    tr.inOrder()

if __name__ == "__main__":
    main()