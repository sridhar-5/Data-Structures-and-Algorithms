import math
from collections import deque


class BinaryTree:
    class node:
        def __init__(self):
            self.element = 0
            self.parent = None
            self.leftchild = None
            self.rightchild = None

    def __init__(self):
        self.sz = 0
        self.root = self.node()
        self.ht = 0

    def getChildren(self, curnode):
        children = []
        if curnode.leftchild != None:
            children.append(curnode.leftchild)
        if curnode.rightchild != None:
            children.append(curnode.rightchild)
        return children

    def isExternal(self, curnode):
        if (curnode.leftchild == None and curnode.rightchild == None):
            return True
        else:
            return False

    def isRoot(self, curnode):
        if (curnode.parent == None):
            return True
        else:
            return False

    def inorderTraverse(self, v):
        curnode = v
        if (curnode.leftchild != None):
            self.inorderTraverse(curnode.leftchild)
        print(curnode.element, end=",")
        if (curnode.rightchild != None):
            self.inorderTraverse(curnode.rightchild)

    def preorderTraverse(self, v):
        curnode = v
        print(curnode.element, end=",")
        if (curnode.leftchild != None):
            self.preorderTraverse(curnode.leftchild)
        if (curnode.rightchild != None):
            self.preorderTraverse(curnode.rightchild)

    def postorderTraverse(self, v):
        curnode = v
        if (curnode.leftchild != None):
            self.postorderTraverse(curnode.leftchild)
        if (curnode.rightchild != None):
            self.postorderTraverse(curnode.rightchild)
        print(curnode.element, end=",")

    def levelorderTraverse(self, v):
        q1 = deque()
        q1.append(v)
        while (len(q1) > 0):
            temp = q1.popleft()
            print(temp.element, end=",")
            if temp.leftchild != None:
                q1.append(temp.leftchild)
            if temp.rightchild != None:
                q1.append(temp.rightchild)
        return

    def buildTree(self, expr):
        # @start-editable@
        expr = expr.replace(" ", "")
        nodelist = []

        for x in expr:
            if(x is "("):


        # @end-editable@
        return nodelist

    # write a function to visualize the tree

    def equivalent(self, treevec1, root1, treevec2, root2):

    # @start-editable@

    # @end-editable@

    def printTree(self, nlist):
        for i in range(len(nlist)):
            print(nlist[i].element, end=" ")

    def isEmpty(self):
        return (self.sz == 0)

    def size(self):
        return self.sz


def main():
    tree1 = BinaryTree()
    tree2 = BinaryTree()
    inputs = int(input())
    while (inputs > 0):
        exp1 = input()
        exptree1 = tree1.buildTree(exp1)
        tree1.printTree(exptree1)
        exp2 = input()
        exptree2 = tree2.buildTree(exp2)
        tree2.printTree(exptree2)
        print(tree1.equivalent(exptree1, tree1.root, exptree2, tree2.root))
        inputs -= 1


if __name__ == '__main__':
    main()

    #[1, 2, 2, 3, -1, 3, 3]
