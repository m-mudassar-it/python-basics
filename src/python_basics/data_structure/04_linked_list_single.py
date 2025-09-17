# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Reference to next node

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:  # If list is empty
            self.head = new_node
        else:
            current = self.head
            while current.next:   # Traverse till end
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    def display_reverse(self, node):
        if node:
            self.display_reverse(node.next)
            print(node.data, end=" -> ")

# Usage
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)

ll.display()  # Output: 10 -> 20 -> 30 -> None
print("Reverse:")
ll.display_reverse(ll.head)
print("None")
