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
        if (self.size() >= self.max_stack_size):
            print("StackFullException")
            return
      
        else:
            self.t+=1;
            self.stack[self.t] = value;
      	
        return
        

    # returns top element of stack if not empty, else throws stack empty exception
    def pop(self):
        if (self.isEmpty()):
            print("StackEmptyException")
            return 
      
        else:
            x = self.stack[self.t]
            self.stack[self.t] = "None"
            self.t = self.t-1
            return x

        
    # returns top element without removing it if the stack is not empty, else throws exception   
    def top(self):
        if self.isEmpty():
          print("StackEmptyException")
          return -1
        else:
          return self.stack[self.t]  

    # returns True if stack is empty   
    def isEmpty(self):
        if (self.t == -1):
            return True
        else:
            return False

    # returns the number of elements currently in stack 
    def size(self):
        return self.t+1




    def printStack(self):
        if (self.isEmpty()):
            print("Empty")
        else:
            for i in range(self.max_stack_size):
                if self.stack[i]!=None:
                    print(self.stack[i],end=" ")
            print()
        return

# Driver code.---------------------------------------------

def teststack():
    stacksize=int(input())
    st1 = MyStack(stacksize)
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
            print(st1.top())
            st1.printStack()
        inputs-=1

def main():
    teststack()

if __name__ == '__main__':
    main()


