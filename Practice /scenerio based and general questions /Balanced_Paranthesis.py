class MyStack():
    def __init__(self, size):
        self.stack = []
        # this is the stack container called 'stack'
        self.max_stack_size = size
        for i in range(self.max_stack_size):
            self.stack.append(None)
        # define the stack size 'max_stack_size' and initialize it
        self.t = -1
        # print(self.stack)

    # define the push operation which  pushes the value into the stack, must throw a stack full exception
    def push(self, value):
        if (self.size() == self.max_stack_size):
            # print("StackFullException")
            return
        else:
            self.t = self.t + 1
            self.stack[self.t] = value
            return

    # returns top element of stack if not empty, else throws stack empty exception
    def pop(self):
        if (self.size() == 0):
            # print("StackEmptyException")
            return
        else:
            toret = self.stack[self.t]
            self.stack[self.t] = None
            self.t = self.t - 1
            return toret

    # returns top element without removing it if the stack is not empty, else throws exception
    def top(self):
        if (self.size() == 0):
            # print ("StackEmptyException")
            return
        else:
            return self.stack[self.t]

    # returns True if stack is empty
    def isEmpty(self):
        return (self.t < 0)

    # returns the number of elements currently in stack
    def size(self):
        return (self.t + 1)

    def printStack(self):
        if (self.isEmpty()):
            print("Empty")
        else:
            for i in range(self.max_stack_size):
                if self.stack[i] != None:
                    print(self.stack[i], end=" ")
                    print(self.stack)
        return


class Parentheses():
    def __init__(self, stacksize):
        self.S = MyStack(stacksize)

    # @start-editable@

    def balance_paranthesis(self, input_str):
        list_man = []
        string = ""
        for i in range(len(input_str)):
            for j in range(0, i + 1):
                string = input_str[j:i + 1]
                left_paranthesis = 0
                right_paranthesis = 0

                for k in range(len(string)):
                    if string[k] == "(":
                        left_paranthesis += 1
                        self.S.push(string[k])
                    if string[k] == ")":
                        right_paranthesis += 1
                        self.S.pop()

                if self.S.isEmpty() == True and left_paranthesis == right_paranthesis and len(string) % 2 == 0:
                    list_man.append(string)
                else:
                    while not self.S.isEmpty():
                        self.S.pop()
        length = 0
        if len(list_man) == 0:
            print(length, "")
        else:
            maxi = max(list_man, key=len)
            print(len(maxi), maxi)

            # @end-editable@


def teststack():
    testcases = int(input())
    while testcases > 0:
        pattern = input()
        # Must use the stack ADT
        # @start-editable@

        object_bal = Parentheses(len(pattern))
        object_bal.balance_paranthesis(pattern)
        testcases -= 1

        # @end-editable@


def main():
    teststack()


if __name__ == '__main__':
    main()