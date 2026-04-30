# WAP TO DEMONSTRATE VARIOUS QUEUE OPERATIONS
#-------------------------------------------#

queue = []

# Enter Element In Queue(Enqueue)
#-------------------------------#
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue: ", queue)

# 1st Element of the Queue (Peek)
#-------------------------------#
frontElement = queue[0]
print("Peek: ", frontElement)

# Delete Element from the Queue (Dequeue)
#---------------------------------------#
poppedElement = queue.pop(0)
print("Dequeue: ", poppedElement)
print("Queue after Dequeue: ", queue)

# Test Queue is Empty or not (isEmpty)
#------------------------------------#
if len(queue) == 0:
  print("isEmpty: True")
else:
  print("isEmpty: False")   

# Number of Elements in Queue (Size)
#----------------------------------#
print("Size: ", len(queue))
