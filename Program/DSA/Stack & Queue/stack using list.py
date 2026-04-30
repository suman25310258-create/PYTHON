#WAP TO DEMONSTRATE STACK DATA-STRUCTURE USING ARRAY
#---------------------------------------------------#

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
          return "Stack is empty"
                   #(OR)
          #raise IndexError("Stack is empty")  
        else:
          return self.stack.pop()

    def peek(self):
        if self.isEmpty():
          return "Stack is empty"
        else:
          return self.stack[-1]

    def isEmpty(self):        
          return len(self.stack) == 0

    def size(self):
          return len(self.stack)


# Create Stack class object 'myStack'
myStack = Stack()

myStack.push('A')
myStack.push('B')
myStack.push('C')
myStack.push('D')

print("Stack:", myStack.stack)
print("Pop:", myStack.pop())
print("Stack after Pop:", myStack.stack)
print("Peek:", myStack.peek())
print()

print("Pop:", myStack.pop())
print("Stack after Pop:", myStack.stack)
print("Peek:", myStack.peek())
print()

print("Pop:", myStack.pop())
print("Stack after Pop:", myStack.stack)
print("Peek:", myStack.peek())
print()

print("Pop:", myStack.pop())
print("Stack after Pop:", myStack.stack)
print("Peek:", myStack.peek())
print()

print("Stack is Empty:", myStack.isEmpty())
print("Stack Size:", myStack.size())
