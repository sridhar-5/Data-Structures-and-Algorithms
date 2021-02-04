class DLList:
    class node:
        def __init__(self,data):
           self.element = data
           self.next = None
           self.prev = None
           
          
    def __init__(self):
        self.head = self.node(None)
        self.tail = self.head
        self.sz = 0
      
    def returnLast(self):
        return self.head
     
    def insertLast(self,u):
        return      

    def insertFirst(self,u):
        return
         
    #insert a node with value u after the node containing value v
    def insertAfter(self,u,v):
        return

    #insert a node with value u before the node containing value v

    def insertBefore(self,u,v):
        return

    def deleteFirst(self):
        return

    def deleteLast(self):
        return

    #delete the node after the node containting value u
    def deleteAfter(self,u):
        return

    #delete the node before the node containting value u
    def deleteBefore(self,u):
        return

    def findNode(self, val):
        return

    #swap the nodes containing u and v
    def swap(self,u,v):
        return
 
    def isEmpty(self):
        return 

    def size(self):
        return self.sz

    def printList(self):
        if (self.isEmpty()):
            print ("Linked List Empty Exception")
        else:
            tnode = self.head
            while tnode!= None:
                print(tnode.element,end="->")
                tnode = tnode.next
            print(" ")
            tnode = self.tail
            while tnode!= None:
                print(tnode.element,end="->")
                tnode = tnode.prev
            print(" ")
        return
    
def testDLL():
    dll = DLList()
    inputs=int(input())
    while inputs>0:
        command=input()
        operation=command.split()
        if(operation[0]=="S"):
            print(dll.size())
        elif(operation[0]=="I"):
            print(dll.isEmpty())
        elif(operation[0]=="IF"):
            dll.insertFirst(int(operation[1]))
            dll.printList()
        elif(operation[0]=="IL"):
            dll.insertLast(int(operation[1]))
            dll.printList()
        elif(operation[0]=="DF"):
            dll.deleteFirst()
            dll.printList()
        elif(operation[0]=="DL"):
            dll.deleteLast()
            dll.printList()
        elif(operation[0]=="IA"):
            dll.insertAfter(int(operation[1]),int(operation[2]))
            dll.printList()
        elif(operation[0]=="IB"):
            dll.insertBefore(int(operation[1],int(operation[2])))
            dll.printList()
        elif(operation[0]=="DA"):
            dll.deleteFirst()
            dll.printList()
        elif(operation[0]=="DB"):
            dll.deleteLast()
            dll.printList()   
        elif(operation[0]=="F"):
            print(dll.getHead())
        elif(operation[0]=='L'):
            print(dll.getLastNode())
        elif(operation[0]=='FIND'):
            print(dll.findNode(int(operation[1])))
        elif(operation[0]=='SW'):
            dll.swap(int(operation[1],int(operation[2])))
            dll.printList()
        inputs-=1


def main():
    testDLL()

if __name__ == '__main__':
    main()

