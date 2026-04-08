# A simple implementation of a singly linked list in Python

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete(self, value):
        current_node = self.head
        previous_node = None
        while current_node:
            if current_node.value == value:
                if previous_node:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                return
            previous_node = current_node
            current_node = current_node.next

    def search(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False    
        
    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    def length(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

# Quick test

ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
print("Linked List after inserting 1, 2, 3 at the end:")
ll.traverse()
ll.insert_at_beginning(0)
print("Linked List after inserting 0 at the beginning:")
ll.traverse()
print("Length of the linked list:", ll.length())
print("Searching for 2 in the linked list:", ll.search(2))
ll.delete(2)
print("Linked List after deleting 2:")
ll.traverse()
print("Searching for 2 in the linked list after deletion:", ll.search(2))
