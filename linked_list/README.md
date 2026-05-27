# Singly Linked List

A from-scratch implementation of a singly linked list in Python,
built without using any built-in list or collection types.

## What is a Linked List?
A linked list is a linear data structure where each element (called 
a node) stores a value and a pointer to the next node in the sequence. 
Unlike arrays, linked lists don't store elements in contiguous memory —
each node can live anywhere and simply points to the next one.

## Methods

| Method | Description | Time Complexity |
|---|---|---|
| `insert_at_beginning(value)` | Adds a node to the front of the list | O(1) |
| `insert_at_end(value)` | Adds a node to the back of the list | O(n) |
| `delete(value)` | Removes the first node matching the value | O(n) |
| `search(value)` | Returns True if value exists, False if not | O(n) |
| `traverse()` | Prints each value from head to tail | O(n) |
| `length()` | Returns the number of nodes in the list | O(n) |

## How to Run
```bash
python3 linked_list.py
```

## What I Learned
Building a linked list from scratch helped me understand how pointers 
work at a fundamental level. Tracking both the current and previous node 
during deletion was the trickiest part — it made me think carefully about 
how nodes reference each other in memory rather than relying on indexes 
like a regular list.