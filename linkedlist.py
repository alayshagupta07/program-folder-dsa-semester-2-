# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # 1️⃣ Insert at Beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 2️⃣ Insert at End
    def insert_end(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node

    # 3️⃣ Delete a Node by Value
    def delete(self, key):
        temp = self.head

        # If head itself is to be deleted
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        prev.next = temp.next
        temp = None

    # 4️⃣ Traverse (Print List)
    def traverse(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Create object
ll = LinkedList()

# Insert elements
ll.insert_beginning(10)
ll.insert_beginning(5)
ll.insert_end(20)
ll.insert_end(30)

# Traverse
print("Linked List:")
ll.traverse()

# Delete element
ll.delete(20)

print("After Deletion:")
ll.traverse()