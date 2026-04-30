#WAP TO DEMONSTRATE SIMPLE STACK OPERATION (WITHOUT OOP)
#------------------------------------------------------#

stack = []

# Push
stack.append('A')
stack.append('B')
stack.append('C')
stack.append('D')
print("Stack: ", stack)

# Peek
topElement = stack[-1]
print("Peek: ", topElement)

# Pop
poppedElement = stack.pop()
print("Pop: ", poppedElement)

# Stack after Pop
print("Stack after Pop: ", stack)

# isEmpty
isEmpty = not bool(stack)     # bool(stack)->True → if stack has at least one elements.
print("isEmpty: ", isEmpty)   # bool(stack) -> False → if the list is empty []
                              # not bool(stack) → reverses the result
                           
# Size
print("Size: ",len(stack))