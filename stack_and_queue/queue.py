from linked_list import LinkedList

# TODO: Implement a Queue class using a LinkedList
    # Create a Queue class that uses a LinkedList internally
    # Add an enqueue(value) method — adds an item to the back of the line
    # Add a dequeue() method — removes and returns the item from the front
    # Add a peek() method — returns the front item without removing it
    # Add an is_empty() method — returns True if the queue is empty
    # Add a quick test block at the bottom to verify it works

class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, value):
        self.queue.insert_at_end(value)

    def dequeue(self):
        if self.queue.head is None:
            raise Exception('Queue is empty.')
        value = self.queue.head.value
        self.queue.head = self.queue.head.next
        return value

    def peek(self):
        if self.queue.head is None:
            raise Exception('Queue is empty.')
        return self.queue.head.value
    
    def is_empty(self):
        if self.queue.head is None:
            return True
        return False
    
    def show(self):
        self.queue.traverse()
    
# Test Code
# Create a queue and perform some operations
queue = Queue()


# Enqueue some values onto the queue
queue.enqueue(10)
queue.enqueue(20)

# Peek at the front value
queue.peek()

# Print the queue
queue.show()

# Dequeue values from the queue
queue.dequeue()  # Should return 10
queue.dequeue()  # Should return 20

# Check if the queue is empty
queue.is_empty()  # Should return True

# Dequeue from an empty queue (should raise an exception)
queue.dequeue()