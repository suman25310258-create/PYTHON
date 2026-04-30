# WAP TO DEMONSTRATE QUEUE USING OOPS
#-----------------------------------#

class Queue:
  def __init__(self):
    self.queue = []
    
  def enqueue(self, element):
    self.queue.append(element)

  def dequeue(self):
    if self.isEmpty() == True:
      return "Queue is empty"
    return self.queue.pop(0)

  def peek(self):
    if self.isEmpty() == True:
      return "Queue is empty"
    return self.queue[0]

  def isEmpty(self):
    return len(self.queue) == 0   # Return 'True' if empty, else Return 'False'

  def size(self):
    return len(self.queue)

# Create a 'myQueue' object of the class 'Queue'
myQueue = Queue()

#Pushing items in the Queue (enqueue)
myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

print("Queue: ", myQueue.queue)
print("Peek: ", myQueue.peek())

#Popping items from the Queue (dequeue)
print("Dequeue: ", myQueue.dequeue())
print("Dequeue: ", myQueue.dequeue())

print("Queue after Dequeue: ", myQueue.queue)
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())