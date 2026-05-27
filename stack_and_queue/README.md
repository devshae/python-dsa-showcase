# Stack & Queue

From-scratch implementations of a Stack and a Queue in Python,
both built on top of a custom LinkedList as the underlying structure.

## What is a Stack?
A stack is a last in, first out (LIFO) data structure — like a stack 
of plates. The last item you put on is the first one you take off.
Think: undo history, browser back button, call stacks in code.

## What is a Queue?
A queue is a first in, first out (FIFO) data structure — like a line 
at a coffee shop. The first person in line is the first one served.
Think: print queues, task scheduling, message processing.

## Stack Methods

| Method | Description | Time Complexity |
|---|---|---|
| `push(value)` | Adds an item to the top of the stack | O(1) |
| `pop()` | Removes and returns the top item | O(1) |
| `peek()` | Returns the top item without removing it | O(1) |
| `is_empty()` | Returns True if the stack is empty | O(1) |

## Queue Methods

| Method | Description | Time Complexity |
|---|---|---|
| `enqueue(value)` | Adds an item to the back of the queue | O(n) |
| `dequeue()` | Removes and returns the front item | O(1) |
| `peek()` | Returns the front item without removing it | O(1) |
| `is_empty()` | Returns True if the queue is empty | O(1) |

## Note on enqueue Time Complexity
`enqueue` is O(n) because it uses `insert_at_end` from the LinkedList,
which has to traverse the entire list to find the last node. This is a 
known tradeoff of using a singly linked list as the underlying structure.
A doubly linked list with a tail pointer would bring this down to O(1).

## How to Run
```bash
python3 stack.py
python3 queue.py
```

## What I Learned
Building both structures on top of my linked list made the relationship 
between data structures really click — a stack and a queue aren't entirely 
new things, they're just a linked list with rules about where you can 
add and remove items. The enqueue O(n) tradeoff was also a good lesson 
in how implementation choices affect performance.