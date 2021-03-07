
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
        if (curnode.leftchild==None and curnode.rightchild==None):
        	return (True)
        else:
        	return (False)

    def isRoot(self,curnode):
        if (curnode.parent==None):
            return True
        else:
            return False   	

    def inorderTraverse(self, v):
        if v != None:
            self.inorderTraverse(v.leftchild)
            print(v.element, end=" ")
            self.inorderTraverse(v.rightchild)


    def preorderTraverse(self, v):
        if v != None: 
            print(v.element,end=" ")
            self.preorderTraverse(v.leftchild)
            self.preorderTraverse(v.rightchild)

    def postorderTraverse(self, v):
        if v != None:
            self.postorderTraverse(v.leftchild)
            self.postorderTraverse(v.rightchild)
            print(v.element,end=" ")


    def levelorderTraverse(self, v):
        #we solve or code the level order traversal using a deque 
        queue = deque()
        queue.append(v)
        while len(queue) > 0:
            pointer = queue.popleft()
            print(pointer.element," ")
            if pointer.leftchild is not None:
                queue.append(pointer.leftchild)
            if pointer.rightchild is not None:
                queue.append(pointer.rightchild)

    #using parents node
    def findDepth(self, v):
        depth = 0
        while v.parent is not None:
            parent = parent.parent
            depth += 1
        return depth    
    
    def findHeight(self, v):
    	if v is None:
            return -1
        return max(self.findDepth(v.leftchild)+1,self.findDepth(v.rightchild)+1)

    # delete leaves in the tree
    def delLeaves(self, v):
        return
    # returns true if tree is proper
    def isProper(self, v):
        if v == None:
            return True
        if v.leftchild == None and v.rightchild == None:
            return True
        if v.leftchild != None and v.rightchild != None:
            return self.isProper(v.leftchild) and self.isProper(v.rightchild)      
        return False    


    # create a tree that is a mirror image of the original tree and print its levelorder
    def mirror(self, v):
        if v is None:
            return
        self.mirror(v.leftchild)
        self.mirror(v.rightchild)

        temp = v.leftchild
        v.leftchild = v.rightchild
        v.rightchild = temp

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
        self.sz=len(nodelist)
        #print("final nodelist", len(nodelist))
        return nodelist

    # write a function to visualize the tree

    def printTree(self, nlist):
        for i in range(len(nlist)):
            if (nlist[i] != None):
                print(nlist[i].element,end=" ");
            else:
                print(None)


    def isEmpty(self):
        return (self.sz == 0)

    def size(self):
        return self.sz


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
         inputs -= 1

if __name__ == '__main__':
    main()



#hai da
