#WAP TO IMPLEMENT STACK USING LINK-LIST
#-------------------------------------#

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None  # Stack is empty
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top  # link to old top
        self.top = new_node       # move top
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.top.data

    def isEmpty(self):
        return self.size == 0

    def stackSize(self):
        return self.size

    def display(self):
        if self.isEmpty():
            print("Stack is empty")
            return

        temp = self.top
        print("Stack (Top → Bottom):")
        while temp:
          print(temp.data)
          temp = temp.next
            
s = Stack()
s.push(10)
s.push(20)
s.push(30)

s.display()
print("Peek:", s.peek())
print("Pop:", s.pop())
print("Is Empty:", s.isEmpty())
print("Size:", s.stackSize())

print()
s.display()
print("Peek:", s.peek())
print("Pop:", s.pop())
print("Is Empty:", s.isEmpty())
print("Size:", s.stackSize())

print()
s.display()
print("Peek:", s.peek())
print("Pop:", s.pop())
print("Is Empty:", s.isEmpty())
print("Size:", s.stackSize())