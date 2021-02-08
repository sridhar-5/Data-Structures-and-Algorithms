class DLList:
    class node:
        def __init__(self, data):
            self.element = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = self.node(None)
        self.tail = self.head
        self.sz = 0

    def getHead(self):
        # @start-editable@

        return self.head

        # @end-editable@

    def getLastNode(self):
        # @start-editable@

        return self.tail

        # @end-editable@

    def insertLast(self, u):
        # @start-editable@

        new_node = self.node(u)

        if self.size() == 0:
            self.head = new_node
            self.tail = new_node
            self.sz += 1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.sz += 1

            # @end-editable@

    def insertFirst(self, u):
        # @start-editable@

        new_node = self.node(u)
        if self.size() == 0:
            self.head = new_node
            self.tail = new_node
            self.sz += 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.sz += 1

            # @end-editable@

    # insert a node with value u after the node containing value v
    # error message: Node to insert after not found
    def insertAfter(self, u, v):
        # @start-editable@

        node_insert = self.node(u)
        node_2 = self.findNode(v)

        if node_2 == self.tail:
            self.insertLast(u)
            
        elif node_2 is not None:
            if node_2.next is not None:
                node_insert.next = node_2.next
                node_2.next.prev = node_insert
            node_insert.prev = node_2
            node_2.next = node_insert
            self.sz += 1
        else:
            print("Node to insert after not found")

            # @end-editable@

    # insert a node with value u before the node containing value v
    # error message: Node to insert before not found
    def insertBefore(self, u, v):
        # @start-editable@

        new_node = self.node(u)
        node_2 = self.findNode(v)

        if node_2 == self.head:
            self.insertFirst(u)
        elif node_2 is not None:
            new_node.next = node_2
            new_node.prev = node_2.prev
            node_2.prev.next = new_node
            node_2.prev = new_node
            self.sz += 1
        else:
            print("Node to insert before not found")

            # @end-editable@

    def deleteFirst(self):
        # @start-editable@

        if self.size() == 0:
            print("List Empty")
        elif self.sz == 1:
            self.head = self.tail = None
            self.sz = 0
        else:
            delete_node = self.head
            self.head = self.head.next
            self.head.prev = None
            delete_node.next = None
            self.sz -= 1

            # @end-editable@

    def deleteLast(self):
        # @start-editable@

        if self.size() == 0:
            print("List Empty")
        elif self.sz == 1:
            self.head = self.tail = None
            self.sz = 0
        else:
            delete_node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            delete_node.prev = None
            self.sz -= 1

            # @end-editable@

    # delete the node after the node containting value u
    # error message: Node to delete after not found
    def deleteAfter(self, u):
        # @start-editable@

        node_find = self.findNode(u)

        if node_find is None:
            print("Node to delete after not found")
        elif node_find.next is self.tail:
            self.deleteLast()
        elif node_find is self.tail:
            return
        elif node_find.next is not None and node_find is not None and node_find.next is not None:
            node_find.next = node_find.next.next
            if node_find.next is not None:
                node_find.next.prev = node_find
            self.sz -= 1

            # @end-editable@

    # delete the node before the node containting value u
    # error message: Node to delete before not found
    def deleteBefore(self, u):
        # @start-editable@

        node_find = self.findNode(u)

        if node_find is None:
            print("Node to delete before not found")
        elif node_find.prev is self.head:
            self.deleteFirst()
        elif node_find is self.head:
            return
        elif node_find is not None and node_find is not None and node_find.prev is not None:
            node_find.prev = node_find.prev.prev
            if node_find.prev is not None:
                node_find.prev.next = node_find
            self.sz -= 1

            # @end-editable@

    def findNode(self, val):
        # @start-editable@

        if self.size() == 0:
            return None

        iterate = self.head
        while iterate is not None:
            if iterate.element == val:
                return iterate
            iterate = iterate.next
        return None

        # @end-editable@

    # swap the nodes containing u and v
    def swap(self, u, v):
        # @start-editable@

        iterate_1 = self.head
        while iterate_1 is not None:
            if iterate_1.element == u:
                break
            iterate_1 = iterate_1.next
        iterate_2 = self.head
        while iterate_2 is not None:
            if iterate_2.element == v:
                break
            iterate_2 = iterate_2.next

        temp = iterate_1.element
        iterate_1.element = iterate_2.element
        iterate_2.element = temp

        # @end-editable@

    def isEmpty(self):
        # @start-editable@

        # @end-editable@
        return (self.sz == 0)

    def size(self):
        # @start-editable@

        # @end-editable@
        return self.sz

    def printList(self):
        if (self.isEmpty()):
            print("Linked List Empty Exception")
        else:
            tnode = self.head
            while tnode != None:
                print(tnode.element, end="->")
                tnode = tnode.next
            print(" ")
            tnode = self.tail
            while tnode != None:
                print(tnode.element, end="->")
                tnode = tnode.prev
            print(" ")
        return


def testDLL():
    dll = DLList()
    inputs = int(input())
    while inputs > 0:
        command = input()
        operation = command.split()
        if (operation[0] == "S"):
            print(dll.size())
        elif (operation[0] == "I"):
            print(dll.isEmpty())
        elif (operation[0] == "IF"):
            dll.insertFirst(int(operation[1]))
            dll.printList()
        elif (operation[0] == "IL"):
            dll.insertLast(int(operation[1]))
            dll.printList()
        elif (operation[0] == "DF"):
            dll.deleteFirst()
            dll.printList()
        elif (operation[0] == "DL"):
            dll.deleteLast()
            dll.printList()
        elif (operation[0] == "IA"):
            dll.insertAfter(int(operation[1]), int(operation[2]))
            dll.printList()
        elif (operation[0] == "IB"):
            dll.insertBefore(int(operation[1]), int(operation[2]))
            dll.printList()
        elif (operation[0] == "DA"):
            dll.deleteAfter(int(operation[1]))
            dll.printList()
        elif (operation[0] == "DB"):
            dll.deleteBefore(int(operation[1]))
            dll.printList()
        elif (operation[0] == "F"):
            print(dll.getHead().element)
        elif (operation[0] == 'L'):
            print(dll.getLastNode().element)
        elif (operation[0] == 'FIND'):
            temp = dll.findNode(int(operation[1]))
            if (temp != None):
                print(temp.element)
            else:
                print("NULL")
        elif (operation[0] == 'SW'):
            dll.swap(int(operation[1]), int(operation[2]))
            dll.printList()
        inputs -= 1


def main():
    testDLL()


if __name__ == '__main__':
    main()