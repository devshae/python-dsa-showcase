import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

# TODO: Implement Stack using LinkedList
    # Create a Stack class that uses a LinkedList internally
    # Add a push(value) method — adds an item to the top
    # Add a pop() method — removes and returns the item from the top
    # Add a peek() method — returns the top item without removing it
    # Add an is_empty() method — returns True if the stack is empty
    # Add a quick test block at the bottom to verify it works

class Stack:
    def __init__(sefl):
        self.stack = LinkedList()

    def push(self, value):
        self.stack.insert(value)

    def pop(self):
        if self.stack.head is None:
            raise Exception('Stack is empty.')
        value = self.stack.head.value
        self.stack.head = self.stack.head.next
        return value

    def peek(self):
        if self.stack.head is None:
            raise Exception('Stack is empty.')
        return self.stack.head.value

    def is_empty(self):
        if self.stack.head is None:
            return True
        return False
    
# Test Code

# Create a stack and perform some operations
stack = Stack()

# Push some values onto the stack
stack.push(10)
stack.push(20)
stack.push(30)

# Peek at the top value
print("Top value (peek):", stack.peek())  # Should print 30

# Pop values from the stack
print("Popped value:", stack.pop())  # Should print 30
print("Top value after pop (peek):", stack.peek())  # Should print 20

# Check if the stack is empty
print("Is stack empty?", stack.is_empty())  # Should print False

# Pop remaining values
print("Popped value:", stack.pop())  # Should print 20
print("Popped value:", stack.pop())  # Should print 10

# Check if the stack is empty
print("Is stack empty?", stack.is_empty())  # Should print True
