# @start-editable@

from collections import deque


# @end-editable@

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
            return (True)
        else:
            return (False)

    def isRoot(self, curnode):
        if (curnode.parent == None):
            return True
        else:
            return False

    def inorderTraverse(self, v):
        # @start-editable@

        if v != None:
            self.inorderTraverse(v.leftchild)
            print(v.element, end=",")
            self.inorderTraverse(v.rightchild)

            # @end-editable@

    def preorderTraverse(self, v):
        # @start-editable@

        if v != None:
            print(v.element, end=",")
            self.preorderTraverse(v.leftchild)
            self.preorderTraverse(v.rightchild)

            # @end-editable@
    def preorder_iterative(selfself,root):
        if root is None:
            return
        else:
            traversal_order = []
            to_2 = []
            traversal_order.append(root)
            while len(traversal_order) > 0:
                pointer = traversal_order.pop()
                to_2.append(pointer.data)
                if pointer.right is not None:
                    traversal_order.append(pointer.right)
                if pointer.left is not None:
                    traversal_order.append(pointer.left)
            return to_2

    def postorderTraverse(self, v):
        # @start-editable@

        if v != None:
            self.postorderTraverse(v.leftchild)
            self.postorderTraverse(v.rightchild)
            print(v.element, end=",")

            # @end-editable@

    def levelorderTraverse(self, v):
        # @start-editable@

        bqueue = deque()
        bqueue.append(v)
        while len(bqueue) > 0:
            pointer = bqueue.popleft()
            print(pointer.element, end=",")
            if pointer.leftchild != None:
                bqueue.append(pointer.leftchild)
            if pointer.rightchild != None:
                bqueue.append(pointer.rightchild)

            # @end-editable@

    def findDepth(self, v):
        # @start-editable@

        depth = 0
        while v.parent is not None:
            v = v.parent
            depth += 1
        return depth

        # @end-editable@

    def findHeight(self, v):
        # @start-editable@

        if v is None:
            return -1
        return max(self.findHeight(v.leftchild) + 1, self.findHeight(v.rightchild) + 1)

        # @end-editable@

    # delete leaves in the tree
    def delLeaves(self, v):
        # @start-editable@

        if v is None:
            return None
        if v.leftchild is None and v.rightchild is None:
            return None

        v.leftchild = self.delLeaves(v.leftchild)
        v.rightchild = self.delLeaves(v.rightchild)

        return v

        # @end-editable@

    # returns true if tree is proper
    def isProper(self, v):
        # @start-editable@

        if v is None:
            return True
        if v.leftchild == None and v.rightchild == None:
            return True

        if v.leftchild != None and v.rightchild != None:
            return self.isProper(v.rightchild) and self.isProper(v.leftchild)

        return False

        # @end-editable@

    # create a tree that is a mirror image of the original tree and print its levelorder
    def mirror(self, v):
        # @start-editable@

        if v is None:
            return

        self.mirror(v.leftchild)
        self.mirror(v.rightchild)

        temp = v.leftchild
        v.leftchild = v.rightchild
        v.rightchild = temp

        # @end-editable@

    def buildTree(self, eltlist):
        nodelist = []
        nodelist.append(None)
        for i in range(len(eltlist)):
            if (i != 0):
                if (eltlist[i] != -1):
                    tempnode = self.node()
                    tempnode.element = eltlist[i]
                    if i != 1:
                        tempnode.parent = nodelist[i // 2]
                        if (i % 2 == 0):
                            nodelist[i // 2].leftchild = tempnode
                        else:
                            nodelist[i // 2].rightchild = tempnode
                    nodelist.append(tempnode)
                else:
                    nodelist.append(None)

        self.root = nodelist[1]
        self.sz = len(nodelist)
        return nodelist

    # write a function to visualize the tree

    def printTree(self, nlist):
        for i in range(len(nlist)):
            if (nlist[i] != None):
                print(nlist[i].element, end=" ");
            else:
                print(None)

    def isEmpty(self):
        return (self.sz == 0)

    def size(self):
        return self.sz

    # determine whether there exists a root-to-leaf path whose nodes sum is equal to a specified integer
    def root2leafsum(self, k):
        # @start-editable@

        print(self.baby_prog(self.root, k))

    def baby_prog(self, node, sum):
        if node is None:
            return False

        if node.element == sum and node.leftchild is None and node.rightchild is None:
            return True

        return self.baby_prog(node.leftchild, sum - node.element) or self.baby_prog(node.rightchild, sum - node.element)

        # @end-editable@

    # determine the value of the leaf node in a given binary tree that is the terminal node of a path of least value from the root of the binary tree to any leaf. The value of a path is the sum of values of nodes along that path.
    def leastleaf(self):
        bqueue = deque()
        queue = deque()
        bqueue.append(self.root)

        while len(bqueue) > 0:
            pointer = bqueue.popleft()
            if pointer.leftchild is None and pointer.rightchild is None:
                queue.append(pointer.element)
            if pointer.leftchild is not None:
                bqueue.append(pointer.leftchild)
            if pointer.rightchild is not None:
                bqueue.append(pointer.rightchild)

        print(min(queue))
# editable

# @end-editable@


def main():
    tree = BinaryTree()
    arraySize = int(input())
    arr = list(map(int, input().split()))
    nlist = tree.buildTree(arr)
    inputs = int(input())
    while inputs > 0:
        command = input()
        operation = command.split()
        if (operation[0] == "I"):
            tree.inorderTraverse(tree.root)
            print()
        elif (operation[0] == "P"):
            tree.preorderTraverse(tree.root)
            print()
        elif (operation[0] == "Post"):
            tree.postorderTraverse(tree.root)
            print()
        elif (operation[0] == "L"):
            tree.levelorderTraverse(tree.root)
            print()
        elif (operation[0] == "D"):
            pos = int(operation[1])
            print(tree.findDepth(nlist[pos]))
        elif (operation[0] == "H"):
            pos = int(operation[1])
            print(tree.findHeight(nlist[pos]))
        elif (operation[0] == "IP"):
            print(tree.isProper(tree.root))
        elif (operation[0] == 'M'):
            tree.mirror(tree.root)
            tree.levelorderTraverse(tree.root)
            print()
        elif (operation[0] == 'DL'):
            tree.delLeaves(tree.root)
            tree.levelorderTraverse(tree.root)
            print()
        elif (operation[0] == 'RL'):
            tree.root2leafsum(int(operation[1]))
            print()
        elif (operation[0] == 'ML'):
            tree.leastleaf()
            print()
        elif (operation[0] == 'PREI'):
            tree.preorder_iterative(tree.root)
        inputs -= 1


if __name__ == '__main__':
    main()
