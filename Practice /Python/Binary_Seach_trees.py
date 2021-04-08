import math
from collections import deque


class BinarySearchTree:
    """
        This defines the node class. The children can be individually declared or stored
        in a list. We are adding a pos value to help with visualization
    """

    class node:
        def __init__(self):
            self.element = 0
            self.leftchild = None
            self.rightchild = None
            self.pos = -1
            self.parent = None

    """
        This initializes the binary search tree. ht is the height of the tree, sz is the
        number of nodes. You may define this appropriately.
    """

    def __init__(self):
        self.sz = 0
        self.root = None
        self.ht = 0

    """
        This method implements the functionality of finding an element in the tree. The function
        findElement(e) finds the node in the current tree, whose element is e. Depending on the
        value of e and in relation to the current element visited, the algorithm visits the left
        or the right child till the element is found, or an external node is visited. Your
        algorithm can be iterative or recursive

        Output: True if tree contains e or False if e not present in T
    """

    def findElement(self, e, curnode):
        if curnode is None:
            return curnode
        if curnode.element == e:
            return True

        if e > curnode.element:
            return self.findElement(e, curnode.rightchild)
        if e < curnode.element:
            return self.findElement(e, curnode.leftchild)

    """
        This method implements insertion of an element into the binary search tree. Using the
        findElement(e) method find the position to insert, and insert a node with element e,
        as left or right child accordingly

    """

    def insertElement(self, e):
        # creating a node here
        new_node = self.node()
        new_node.element = e

        iterate = self.root

        if iterate is None:
            self.root = new_node
        else:
            iterate_2 = None
            while iterate != None:
                iterate_2 = iterate

                if e > iterate.element:
                    iterate = iterate.rightchild
                else:
                    iterate = iterate.leftchild

            if e > iterate_2.element:
                iterate_2.rightchild = new_node
            else:
                iterate_2.leftchild = new_node

    """
        This method inorderTraverse(self,v) performs an inorder traversal of the BST, starting
        from node v which is initially the root and prints the elements of the nodes as they
        are visited. Remember the inorder traversal first visits the left child, followed by
        the parent, followed by the right child. This could be used to print the tree.
    """

    def inorderTraverse(self, v):
        curnode = v
        if (curnode.leftchild != None):
            self.inorderTraverse(curnode.leftchild)
        print(curnode.element, end=",")
        if (curnode.rightchild != None):
            self.inorderTraverse(curnode.rightchild)

    """
        Given a node v this will return the next element that should be visited after v in the
        inorder traversal.
    """

    fqueue = deque()
    pos = 0
    i = 0

    def inorderwithqueue(self):
        curnode = self.root
        if (curnode.returnNextInorder != None):
            self.returnNextInorder(curnode.leftchild)

        if (curnode.element == self.v):
            self.pos = self.i + 1

        self.fqueue.append(self.v)
        self.i += 1

        if (curnode.rightchild != None):
            self.returnNextInorder(curnode.rightchild)

    def returnNextInorder(self, v):
        i = 0
        self.inorderwithqueue()
        while (i < self.pos):
            self.fqueue.popleft()

        print(self.fqueue.popleft())

    """
        This method deleteElement(self, e), removes the node with element e from the tree T.
        There are three cases:
            1. Deleting a leaf or external node:Just remove the node
            2. Deleting a node with one child: Remove the node and replace it with its child
            3. Deleting a node with two children: Instead of deleting the node replace with
                a) its inorder successor node or b)Inorder predecessor node
    """

    def deleteElement(self,e):

        pointer_1 = None
        pointer_2 = self.root

        while pointer_2 is not None and pointer_2.element != e:
            pointer_1 = pointer_2

            if e < pointer_2.element:
                pointer_2 = pointer_2.leftchild
            else:
                pointer_2 = pointer_2.rightchild

        if pointer_2 is None:
            print("Error ! Element not found")
            return

        #leaf node
        if pointer_2.leftchild is None and pointer_2.rightchild is None:
            if pointer_2 == self.root:
                self.root = None
            else:
                if pointer_1.leftchild is pointer_2:
                    pointer_1.leftchild = None
                else:
                    pointer_1.rightchild = None

        #only one child node exists
        elif pointer_2.leftchild is None or pointer_2.rightchild is None:

            if pointer_2.leftchild is not None:
                pointer_2.element = pointer_2.leftchild.element
                pointer_2.leftchild = None
            else:
                pointer_2.element = pointer_2.rightchild.element
                pointer_2.rightchild = None






    def createTree(self, items):
        self.sz = len(items)
        mid = int(math.floor(len(items) / 2))
        self.insertElement(items[mid])
        del items[mid]
        if (len(items) > 1):
            self.createTree(items[0:mid])
            self.createTree(items[mid:len(items) + 1])
        else:
            if (len(items) == 1):
                self.insertElement(items[0])
            return

    """
        There are other support methods which maybe useful for implementing your functionalities.
        These include
            1. isExternal(self,v): which returns true if the node v is external
            2. printTree(self): to visualize the tree for your debugging purposes. You may print it
            using text formatting or use a turtle library given along with the file.
    """

    def isExternal(self, curnode):
        if (curnode.leftchild == None and curnode.rightchild == None):
            return True
        else:
            return False

    def getChildren(self, curnode):
        children = []
        # if curnode.leftchild!= None:
        children.append(curnode.leftchild)
        # if curnode.rightchild!= None:
        children.append(curnode.rightchild)
        return children

    def isExternal(self, curnode):
        if (curnode.leftchild == None and curnode.rightchild == None):
            return True
        else:
            return False

    def preorderTraverse(self, v):
        curnode = v
        print(curnode.element, end=",")
        if (curnode.leftchild != None):
            self.preorderTraverse(curnode.leftchild)
        if (curnode.rightchild != None):
            self.preorderTraverse(curnode.rightchild)
        return

    def postorderTraverse(self, v):
        curnode = v
        if (curnode.leftchild != None):
            self.postorderTraverse(curnode.leftchild)
        if (curnode.rightchild != None):
            self.postorderTraverse(curnode.rightchild)
        print(curnode.element)
        return

    def findDepthIter(self, v):
        if v == self.root:
            return 0
        else:
            return 1 + self.findDepthIter(v.parent)

    def findDepth(self, v):
        return self.findDepthIter(self.findElement(v.element, self.root))

    def findHeightIter(self, v):
        if self.isExternal(v):
            return 0
        else:
            h = 0
            if (v.leftchild != None):
                h = max(h, self.findHeightIter(v.leftchild))
            if (v.rightchild != None):
                h = max(h, self.findHeightIter(v.rightchild))
            return 1 + h

    def findHeight(self, v):
        return self.findHeightIter(self.findElement(v.element, self.root))

    def finRange(self, r, low, high):
        v = self.root
        bqueue = deque()
        list = []
        bqueue.append(v)
        while len(bqueue) > 0:
            pointer = bqueue.popleft()
            if pointer.element >= low and pointer.element <= high:
                list.append(pointer.element)
            if pointer.leftchild is not None:
                bqueue.append(pointer.leftchild)
            if pointer.rightchild is not None:
                bqueue.append(pointer.rightchild)  
        list.sort()
        return list


    def findMedian(self):
        return

def testbst():
    # initialize Data structure here
    ds = BinarySearchTree()
    arr = list(map(int, input().split()))
    ds.createTree(arr)
    ds.preorderTraverse(ds.root)
    print()
    inputs = int(input())
    while inputs > 0:
        command = input()
        operation = command.split()
        if (operation[0] == "M"):
            ds.preorderTraverse(ds.root)
            print()
            print(ds.findMedian())
        elif (operation[0] == "R"):
            print(ds.findrange(int(operation[1]), int(operation[2])))
        elif (operation[0] == "I"):
            ds.insertElement(int(operation[1]))
            ds.preorderTraverse(ds.root)
            print()
        elif (operation[0] == "Pre"):
            ds.preorderTraverse(ds.root)
            print()
        elif (operation[0] == "In"):
            ds.inorderTraverse(ds.root)
            print()
        elif (operation[0] == "F"):
            temp = ds.findElement(int(operation[1]))
            if (temp == None):
                print(False)
            else:
                print(True)
        elif (operation[0] == "D"):
            ds.deleteElement(int(operation[1]))
            ds.preorderTraverse(ds.root)
            print()
        inputs -= 1


def main():
    testbst()


if __name__ == '__main__':
    main()