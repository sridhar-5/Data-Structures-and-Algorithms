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
        #@start-editable@

        return self.head.element
  
	    #@end-editable@
        
    
    def getLastNode(self):
        #@start-editable@

        return self.tail.element
			
	    #@end-editable@
        
     
    def insertLast(self,u):
        #@start-editable@


        new_node = self.node(u)

        if self.size() == 0:
            self.head = self.tail
            self.head.element = u
            self.sz += 1
        else:
            temp = self.tail
            self.tail.next = new_node
            self.tail = new_node
            new_node.prev = temp
            new_node.next = None
            self.sz += 1
            
        return    
    
			
	    #@end-editable@
        

    def insertFirst(self,u):
        #@start-editable@


        new_node = self.node(u)
        if self.size() == 0:
            self.head = self.tail
            self.head.element = u
            self.sz += 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None
            self.sz += 1
            
        return	
  	
			
	    #@end-editable@
        
        
         
    #insert a node with value u after the node containing value v
    # error message: Node to insert after not found
    def insertAfter(self,u,v):
        #@start-editable@


        newnode = self.node(u)

        iterate = self.head
        while iterate.next is not None:
            if iterate.element == v:
                break
            iterate = iterate.next
        if iterate.next is None:
            print("Node to insert after not found")
        elif iterate.next is None:
            newnode.next = None
            newnode.prev = iterate
            self.tail = newnode
            self.sz += 1
        else:
            newnode.next = iterate.next
            iterate.next.prev = newnode
            newnode.prev = iterate
            iterate.next = newnode
            self.sz += 1
			
	    #@end-editable@
        return


    #insert a node with value u before the node containing value v
    # error message: Node to insert before not found
    def insertBefore(self,u,v):
        #@start-editable@

        new_node = self.node(u)
        iterate = self.head

        while iterate.next is not None:
            if iterate.element == v:
                break
            iterate = iterate.next

        if iterate.next is None:
            print("Node to insert before not found")
        elif iterate.prev is self.head:
            new_node.prev = None
            new_node.next = iterate
            self.head = new_node
            self.sz += 1
        else:
            iterate = iterate.prev
            new_node.next = iterate.next
            iterate.next.prev = new_node
            new_node.prev = iterate
            iterate.next = new_node
            self.sz += 1
        return
			
	    #@end-editable@
        

    def deleteFirst(self):
        #@start-editable@


        if self.size() == 0:
            return
        else:
            delete_this = self.head
            temp = self.head.next
            temp.prev = None
            self.head = self.head.next
            self.head.prev = None
            del delete_this
            self.sz -= 1
            
        return    

	    #@end-editable@
        

    def deleteLast(self):
        #@start-editable@

        if self.size() == 0:
            return
        else:
            delete_this = self.tail
            temp = self.tail.prev
            temp.next = None
            self.tail = self.tail.prev
            self.tail.next = None
            delete_this.prev = None
            del delete_this
            self.sz -= 1
        return	
			
	    #@end-editable@
          

    #delete the node after the node containting value u
    # error message: Node to delete after not found
    def deleteAfter(self,u):
        #@start-editable@


        iterate = self.head

        while iterate.next is not None:
            if iterate.element == u:
                break
            iterate = iterate.next

        if iterate.next is None:
            print("Node to delete after not found")
        else:
            del_node = iterate.next
            iterate.next.next.prev = iterate
            iterate.next = iterate.next.next
            del del_node
        return    
   
			
	    #@end-editable@
        

    #delete the node before the node containting value u
    # error message: Node to delete before not found
    def deleteBefore(self,u):
        #@start-editable@


        iterate = self.head

        while iterate is not None:
            if iterate.element == u:
                break
            iterate = iterate.next

        if iterate is None:
            print("Node to delete before not found")
        elif iterate.prev is self.head:
            temp = iterate.prev
            iterate.prev = None
            self.head = iterate
            del temp
        else:
            temp = iterate.prev.prev
            del_node = iterate.prev
            iterate.prev = iterate.prev.prev
            temp.next = iterate
            del del_node
        return    
	
	    #@end-editable@
        

    def findNode(self, val):
        #@start-editable@


        iterate = self.head

        while iterate.next is not None:
            if iterate.element == val:
                return val
            iterate = iterate.next
        return    
	
	    #@end-editable@
        

    #swap the nodes containing u and v
    def swap(self,u,v):
        #@start-editable@

		#swapping the nodes element just to test
        iterate_1 = self.head
        while iterate_1.next is not None:
            if iterate_1.element == u:
                break
            iterate_1 = iterate_1.next
        iterate_2 = self.head
        while iterate_2.next is not None:
            if iterate_2.element == v:
                break
            iterate_2 = iterate_2.next

        temp = iterate_1.element
        iterate_1.element = iterate_2.element
        iterate_2.element = temp

        return

			
	    #@end-editable@
        
 
    def isEmpty(self):
        #@start-editable@

			
			
	    #@end-editable@
        return (self.sz==0)

    def size(self):
        #@start-editable@

			
			
	    #@end-editable@
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
            dll.insertBefore(int(operation[1]),int(operation[2]))
            dll.printList()
        elif(operation[0]=="DA"):
            dll.deleteAfter(int(operation[1]))
            dll.printList()
        elif(operation[0]=="DB"):
            dll.deleteBefore(int(operation[1]))
            dll.printList()   
        elif(operation[0]=="F"):
            print(dll.getHead().element)
        elif(operation[0]=='L'):
            print(dll.getLastNode().element)
        elif(operation[0]=='FIND'):
            temp = dll.findNode(int(operation[1]))
            if (temp!=None):
                print(temp.element)
            else:
                print("NULL")
        elif(operation[0]=='SW'):
            dll.swap(int(operation[1]),int(operation[2]))
            dll.printList()
        inputs-=1


def main():
    testDLL()

if __name__ == '__main__':
    main()