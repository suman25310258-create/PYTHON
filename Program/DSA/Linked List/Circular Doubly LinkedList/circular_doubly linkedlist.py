#WAP TO DEMONSTRATE CIRCULAR-DOUBLY LINKED-LIST (INSERT/DELETE/DISPLAY/SEARCH)
#----------------------------------------------------------------------------#
# A Circular Doubly Linked List has:
  # next pointer → to next node
  # prev pointer → to previous node
  # Last node’s next → points to head
  # Head’s prev → points to last node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

#===================== Insert at Beginning ============================
        
    def insert_begin(self, data):
        new_node = Node(data)

        if self.head is None:
            new_node.next = new_node.prev = new_node
            self.head = new_node
            return

        tail = self.head.prev
        new_node.next = self.head
        new_node.prev = tail
        tail.next = self.head.prev = new_node
        self.head = new_node

#============================== Insert at End =========================
        
    def insert_end(self, data):
        if self.head is None:
            self.insert_begin(data)
            return

        new_node = Node(data)
        tail = self.head.prev

        tail.next = new_node
        new_node.prev = tail
        new_node.next = self.head
        self.head.prev = new_node

#=========================== Insert at Position ======================
        
    def insert_pos(self, data, pos):
        if pos == 1:
            self.insert_begin(data)
            return

        new_node = Node(data)
        temp = self.head

        for _ in range(pos - 2):
            temp = temp.next
            if temp == self.head:
                print("Position out of range")
                return

        new_node.next = temp.next
        new_node.prev = temp
        temp.next.prev = new_node
        temp.next = new_node

#==================== Delete from Beginning =========================
        
    def delete_begin(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        tail = self.head.prev
        self.head = self.head.next
        self.head.prev = tail
        tail.next = self.head

#====================== Delete from End ============================
        
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        tail = self.head.prev
        new_tail = tail.prev
        new_tail.next = self.head
        self.head.prev = new_tail

#============== Delete from Position ==============================
        
    def delete_pos(self, pos):
        if self.head is None:
            print("List is empty")
            return

        if pos == 1:
            self.delete_begin()
            return

        temp = self.head

        for _ in range(pos - 1):
            temp = temp.next
            if temp == self.head:
                print("Position out of range")
                return

        temp.prev.next = temp.next
        temp.next.prev = temp.prev

#================ Search a particular value ========================
        
    def search(self, key):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        pos = 1

        while True:
            if temp.data == key:
                print(f"Element found at position {pos}")
                return
            temp = temp.next
            pos += 1

            if temp == self.head:
                break

        print("Element not found")

#============== Display in both Direction ===================
        
    def display_both(self):
      if self.head is None:
        print("List is empty")
        return

      print("(tail)", end=" <-> ")


      temp = self.head
      while True:
         print(temp.data, end=" <-> ")
         temp = temp.next
         if temp == self.head:
          break
      print("(head)")

   
#================== Menu Driven Program ======================
      
cdll = CircularDoublyLinkedList()

while True:
    print("\n--- Circular Doubly Linked List ---")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Delete from Beginning")
    print("5. Delete from End")
    print("6. Delete from Position")
    print("7. Display (Both Direction Style)")
    print("8. Search")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter value: "))
        cdll.insert_begin(data)

    elif choice == 2:
        data = int(input("Enter value: "))
        cdll.insert_end(data)

    elif choice == 3:
        data = int(input("Enter value: "))
        pos = int(input("Enter position: "))
        cdll.insert_pos(data, pos)

    elif choice == 4:
        cdll.delete_begin()

    elif choice == 5:
        cdll.delete_end()

    elif choice == 6:
        pos = int(input("Enter position: "))
        cdll.delete_pos(pos)

    elif choice == 7:
        cdll.display_both()

    elif choice == 8:
        key = int(input("Enter element to search: "))
        cdll.search(key)

    elif choice == 9:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")