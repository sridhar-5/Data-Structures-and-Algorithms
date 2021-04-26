class MyStack():
    def __init__(self,size):
        self.stack = []
        # this is the stack container called 'stack'
        self.max_stack_size = size
        for i in range(self.max_stack_size):
            self.stack.append(None)
        # define the stack size 'max_stack_size' and initialize it
        self.t = -1
        #print(self.stack)

    # define the push operation which  pushes the value into the stack, must throw a stack full exception
    def push(self, value):
        if (self.size() == self.max_stack_size):
            print("StackFullException")
        else:
            self.t= self.t+1
            self.stack[self.t] = value
        return


    # returns top element of stack if not empty, else throws stack empty exception
    def pop(self):
        if (self.size() == 0):
            print("StackEmptyException")
            return
        else:
            toret = self.stack[self.t]
            self.stack[self.t] = None
            self.t = self.t-1
            return toret


    # returns top element without removing it if the stack is not empty, else throws exception   
    def top(self):
        if (self.size() == 0):
            #print ("StackEmptyException")
            return
        else:
            return self.stack[self.t]


    # returns True if stack is empty   
    def isEmpty(self):
        return (self.t<0)

    # returns the number of elements currently in stack 
    def size(self):
        return (self.t+1)


    def printStack(self):
        if (self.isEmpty()):
            print("Empty")
        else:
            for i in range(self.max_stack_size):
                if self.stack[i]!=None:
                    print(self.stack[i],end=" ")
                    print(self.stack)
        return
    
class MyQueue():
    
    def __init__(self,size):
        # this is the queue container called 'queue'
        self.queue = []
        # front and back indexes
        self.f = 0
        self.r = -1
        # define the queue size 'max_queue_size' and initialize it
        self.max_queue_size = size
        for i in range(0,self.max_queue_size):
            self.queue.append(None)
        self.sz=0

    # define the enqueue operation which inserts the value into the queue, must throw a queue full exception
    # call print queue after enqueue (not when there is an exception)
    def enqueue(self, value):
        if self.size() == self.max_queue_size:
            print("Queue Full Exception")
            return
        else:
            self.r = (self.r+1)%self.max_queue_size
            self.queue[self.r] = value
            self.sz+=1
            self.printQueue()
            
                
    # returns first elt of the queue if not empty, else throws queue empty
    # exception
    
    def dequeue(self):
        if self.size()==0:
            print("Queue Empty Exception")
        else:
            obj = self.queue[self.f]
            self.queue[self.f] = None                
            self.f = (self.f+1)%self.max_queue_size            
            self.sz = self.sz-1
            return obj
       
    
    # returns front element without removing it if the queue is not empty, else throws exception   
    def front(self):
        if (self.size()!=0):
            return self.queue[self.f]
        else:
            print("Queue Empty Exception")
     
    # returns True if queue is empty
    def isEmpty(self):
        return (self.sz==0)

    # returns the number of elements currently in queue
        
    def size(self):
        return (self.sz)


    
    def printQueue(self):
        if (self.isEmpty()):
            print ("Queue Empty")
        else:
            for i in range(self.max_queue_size):
                #if self.queue[i]!=None:
                print(self.queue[i],end=" ")
            print(" ")


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

    def getHead(self):
        return self.head
    
    def getLastNode(self):
        return self.tail
     
    def insertLast(self,u):
        nnode=self.node(u)
        if (self.head.element == None):
            self.head.element = nnode.element
            self.sz+=1
        else:
            self.tail.next=nnode
            nnode.prev=self.tail
            self.tail = nnode
            self.sz+=1
        return

    def insertFirst(self,u):
        nnode=self.node(u)
        if (self.head.element == None):
            self.head.element = nnode.element
            self.sz+=1
        else:
            nnode.next = self.head
            self.head.prev=nnode
            self.head = nnode
            self.sz+=1
        return
        


    def deleteFirst(self):
        if self.size()!=0:
            if self.head.next == None:
                tempval = self.head.element
                self.head.element = None
                #self.sz= self.sz-1
            else:
                temp = self.head
                tempval = temp.element
                self.head = self.head.next
                self.head.prev = None
                del temp
            self.sz = self.sz-1
        else:
            print ("List Empty")
        return tempval

    def deleteLast(self):
        if self.size()!=0:
            if self.head.next == None:
                tempval = self.head.element
                self.head.element = None
                #self.sz= self.sz-1
            else:
                temp = self.tail
                tempval = temp.element
                self.tail=self.tail.prev
                self.tail.next=None
                del temp
            self.sz = self.sz-1
            if self.sz==1:
                self.tail=self.head
        else:
            print ("List Empty")
        return tempval

    def findNode(self, val):
        curnode = self.head
        if (self.size()>0):
            while (curnode.next!=None):
                if (curnode.element == val):
                    #print(curnode)
                    return curnode
                else:
                    curnode = curnode.next
            if (curnode.element == val):
                    #print(curnode)
                    return curnode
        return None

    
 
    def isEmpty(self):
        return (self.sz==0)

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

class SLList:

     class node:
          def __init__(self):
               self.element = None
               self.next = None
               
          
     def __init__(self):
          self.head = self.node()
          self.sz = 0

     def insertFirst(self,u):
          if (self.size()==0):
               self.head.element = u.element
               self.sz+=1
          else:
               u.next = self.head
               self.head=u
               self.sz+=1
          return

     def insertLast(self,u):
          if (self.size()==0):
               self.head.element = u.element
               self.sz+=1
          else:
               curnode = self.head
               while (curnode.next!=None):
                    curnode = curnode.next
               curnode.next=u
               self.sz+=1
          return


     def deleteFirst(self):
          if (self.size()==0):
               return("List Empty")
          elif (self.size()==1):
               self.head.element=None
               self.sz-=1
          else:
               temp = self.node()
               temp = self.head
               self.head = self.head.next
               temp.next = None
               self.sz-=1
          return

     def deleteLast(self):
          if (self.size()==0):
               return("List Empty")
          elif (self.size()==1):
               self.head.element=None
               self.sz-=1
          else:
               curnode = self.head
               while (curnode.next.next!=None):
                    curnode = curnode.next
               curnode.next=None
               self.sz-=1
          return


     def printList(self):
          tnode = self.head
          if (self.size==0):
               return("List Empty")
          while tnode!= None:
               print(tnode.element,end="->")
               tnode = tnode.next
          print()
          return
     
     
     def isEmpty(self):
          return (self.sz==0)

     def size(self):
          return (self.sz)

class DeckRemove:
    #@start-editable@

    def __init__(self):
        self.deck = DLList()

    def logic(self,input_sz,deck1):
        
        sum = 0
        size = input_sz
        works = 0
        w_final = -1
        #print(size)

        while(size>3 and works>-1):
            works = -1
            sum1 = 0
            sum2 = 0
            sum3 = 0

            for i in range(1,size+1):
                #print("in >3 loop",size,pos)
                self.temp = self.deck.head
                    
                sum1 = self.deck.head.element + self.deck.head.next.element + self.deck.tail.element  


                #print(sum1)
                    
                sum2 = self.deck.head.element + self.deck.tail.element + self.deck.tail.prev.element

                #print(sum2)
                sum3 = self.deck.tail.element + self.deck.tail.prev.element + self.deck.tail.prev.prev.element

                #print(sum3)

            if(sum1==10 or sum1==20 or sum1==30):
                sum+=sum1
                size -= 3
                works = 0
                self.deck.deleteFirst()
                self.deck.deleteFirst()
                self.deck.deleteLast()
                
            
            elif sum2 == 10 or sum2 == 20 or sum2 == 30:
                sum += sum2
                #print("sum2")
                size-=3
                works = 0
                self.deck.deleteFirst()
                self.deck.deleteLast()
                self.deck.deleteLast()
                
                
            elif sum3 == 10 or sum3 == 20 or sum3 == 30:
                sum += sum3
                #print("sum3",sum3)
                size-=3
                works = 0
                self.deck.deleteLast()
                self.deck.deleteLast()
                self.deck.deleteLast()

            w_final = works
            self.add_three(deck1)
        
        sum4 = 0
        while not self.deck.isEmpty():
            sum4+=self.deck.deleteFirst()

        sum+=sum4

        if w_final==0 and sum%10==0:    
        #if(sum%10==0 and ):
            print("True " + str(sum))

        else:
            print("False "+ str(sum-sum4))
            
        return
    
    
	#@end-editable@

    def checkDeck(self, deck1):
    
    #@start-editable@

        for i in range(7):
            if deck1[i] == 'K' or deck1[i] == 'Q' or deck1[i] == 'J':
                self.deck.insertLast(10)
                deck1[i] = None


            elif deck1[i] == 'A':
                self.deck.insertLast(1)
                deck1[i] = None


            else:
                self.deck.insertLast(int(deck1[i]))
                deck1[i] = None

            


        self.logic(len(deck1),deck1)        

        return
        

    def add_three(self,deck1):
        for i in range(1,len(deck1)):
            if deck1[i]!=None:
                if deck1[i] == 'K' or deck1[i] == 'Q' or deck1[i] == 'J':
                    self.deck.insertLast(10)
                    deck1[i] = None


                elif deck1[i] == 'A':
                    self.deck.insertLast(1)
                    deck1[i] = None


                else:
                    self.deck.insertLast(int(deck1[i]))
                    deck1[i] = None

			
	#@end-editable@   
        
    
def test():
    d1 = DeckRemove()
    inputs=int(input())
    while inputs>0:
        arraySize = int(input())
        arr = list((input().split()))
        d1.checkDeck(arr)
        inputs-=1


def main():
    test()

if __name__ == '__main__':
    main()