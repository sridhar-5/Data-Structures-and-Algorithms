class MyStack():

    class linked_list():

        class node:
            def __init__(self,data):
                self.element = data
                self.next = None

        def __init__(self):
            self.head = self.node(None)
            self.sz = 0   

        def size(self):
            return self.sz 

        def insertFirst(self,data):
            
            #@start-editable@

            nnode = self.node(data)
        
            if self.size() == 0:
                self.head = nnode
                self.sz+=1
        
            else:
                nnode.next = self.head
                self.head = nnode
                self.sz+=1
        
            #@end-editable@
            return

        
        def deleteFirst(self):

        # @start-editable@

            if self.size() == 0:
                return "ListEmptyException"
            
            elif self.size() == 1:
                self.head.element = None
                self.sz -= 1
            
            else:
                temp = self.head
                self.head = self.head.next
                self.sz -= 1
                x = temp.element
                del temp    
        # @end-editable@
            return x   
        
        
        def getHead(self):
            return self.head.element
        
     
        def isEmpty(self):
            return(self.sz==0)


        def printList(self):
            if (self.isEmpty()):
                print ("List Empty")
            else:
                tnode = self.head
                while tnode!= None:
                    print(tnode.element,end=" ")
                    tnode = tnode.next
            return
    
    def __init__(self):
        self.top=-1
        self.stack = self.linked_list()        

    # define the push operation which  pushes the value into the stack, must throw a stack full exception
    def push(self, value):
        self.stack.insertFirst(value);
        self.top+=1 
        return
        

    # returns top element of stack if not empty, else throws stack empty exception
    def pop(self):
        x = self.stack.deleteFirst()
        self.top-=1
        return x
        
    # returns top element without removing it if the stack is not empty, else throws exception   
    def Top(self):
        x = self.stack.getHead()
        return x

    # returns True if stack is empty   
    def isEmpty(self):
        self.stack.isEmpty

    # returns the number of elements currently in stack 
    def size(self):
        return self.sz

    def printStack(self):
        self.stack.printList()
        print()
        return

    
# Driver code.---------------------------------------------

def teststack():

    st1 = MyStack()
    inputs=int(input())
    while inputs>0:
        command=input()
        operation=command.split()
        if(operation[0]=="S"):
            print(st1.size())
        elif(operation[0]=="I"):
            print(st1.isEmpty())
        elif(operation[0]=="P"):
            st1.push(int(operation[1]))
            st1.printStack()
        elif(operation[0]=="O"):
            print(st1.pop())
            st1.printStack()
        elif(operation[0]=="T"):
            print(st1.Top())
            st1.printStack()
        inputs-=1

def main():
    teststack()

if __name__ == '__main__':
    main()


