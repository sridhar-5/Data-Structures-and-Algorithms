class MyQueue():
    def __init__(self):
        self.first=self.node(None)
        self.rear=None
        self.sz=0
        
    class node():
        def __init__(self,value): 
            self.element = value 
            self.next = None
        

    def enqueue(self, value):
        nnode=self.node(value)
        if(self.sz==0):
            self.rear=nnode
            self.first=self.rear
            nnode.next=None
            self.sz+=1
        
        else:
            self.rear.next=nnode
            nnode.next=None
            self.sz+=1
            self.rear=nnode
        return
    
        

    def dequeue(self):
        if self.sz==0:
            print("Queue Empty Exception")
            return 
        elif self.sz == 1:
            a=self.first.element
            self.first = None
            self.rear = self.first
            self.sz -= 1
            return a
        else:
            temp=self.first
            a=temp.element
            self.first=self.first.next
            temp.next=None
            self.sz-=1
            return a
        
    def front(self):
        
        if(self.sz==0):
            print("Queue Empty Exception")
            return
        else:
            return self.first.element

    # returns True if stack is empty   
    def isEmpty(self):
        return self.sz==0

    # returns the number of elements currently in stack 
    def size(self):
        return self.sz




    def printQueue(self):
        if (self.isEmpty()):
            print("Queue Empty")
        else:
            cur=self.first
            while(cur!=None):
                print(cur.element,end=" ")
                cur=cur.next
            print()
        return

# Driver code.---------------------------------------------

def testqueue():
    q1 = MyQueue()
    inputs=int(input())
    while inputs>0:
        command=input()
        operation=command.split()
        if(operation[0]=="S"):
            print(q1.size())
        elif(operation[0]=="I"):
            print(q1.isEmpty())
        elif(operation[0]=="E"):
            q1.enqueue(int(operation[1]))
            q1.printQueue()
        elif(operation[0]=="D"):
            print(q1.dequeue())
            q1.printQueue()
        elif(operation[0]=="F"):
            print(q1.front())
        elif(operation[0]=="DK"):
            q1.delK(int(operation[1]))
            q1.printQueue()
        inputs-=1

def main():
    testqueue()

if __name__ == '__main__':
    main()






 