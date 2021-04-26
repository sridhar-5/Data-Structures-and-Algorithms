import math


class percentile:
    class Node:
        def __init__(self, data):
            self.data = data
            self.leftchild = None
            self.rightchild = None

    def __init__(self):
        self.root = None
        self.size = 0

    def InsertNode(self, key):
        new_node = self.Node(key)

        iterate = self.root

        if iterate is None:
            self.root = new_node
        else:
            iterate_2 = None
            while iterate is not None:
                iterate_2 = iterate

                if key >= iterate.data:
                    iterate = iterate.rightchild
                elif key < iterate.data:
                    iterate = iterate.leftchild

            if key > iterate_2.data:
                iterate_2.rightchild = new_node
            else:
                iterate_2.leftchild = new_node

        self.size += 1

    def preOrderTraversal(self, iterate):
        if iterate is not None:
            print(iterate.data, end=" ")
            self.preOrderTraversal(iterate.leftchild)
            self.preOrderTraversal(iterate.rightchild)



    def getPercentile(self, val):
        current = self.root
        count = 0
        stack = []
        stack2 = []
        while True:
            if current is not None:
                stack.append(current)
                current = current.leftchild

            elif stack:
                current = stack.pop()
                stack2.append(current.data)
                if current.data <= val:
                    count = count + 1
                current = current.rightchild
            else:
                break
        if val not in stack2:
            return        
        fraction = count/self.size
        percent = fraction * 100
        print(round(percent))
    """
        def percGreater(self, val):
            self.return_greater_lesser(val)
            print(self.g_t)
    """

    def percGreater(self, val):
        index  = int((val*self.size)/100)
        return self.size - index    

    def getHundred(self):
        k = self.root

        while k.rightchild is not None:
            k = k.rightchild
        return k.data    


def main():
    object = percentile()
    testcases = int(input())

    for i in range(testcases):
        express = input()
        operation = express.split()
        if operation[0] == "I":
            object.InsertNode(int(operation[1]))
            object.preOrderTraversal(object.root)
            print()
        elif operation[0] == "P":
            object.getPercentile(int(operation[1]))

        elif operation[0] == "G":
            k = object.percGreater(int(operation[1]))
            print(k)
        elif operation[0] == "H":
            k = object.getHundred()
            print(k)    

if __name__ == "__main__":
    main()
