# python-dsa-showcase
Project: Python Data Structures &amp; Algorithms Showcase

Collection of data structures & algorithms to showcase conceptual understanding of python data structures.

Data Structures Included:
1. Linked List — implement a singly linked list with insert, delete, search, and traversal methods
2. Stack & Queue — build both using your linked list as the underlying structure
3. Binary Search Tree — insert, search, and in-order traversal
4. Bubble Sort & Merge Sort — implement both, then write a short comparison of their time complexity
5. Binary Search — implement on a sorted list, include both iterative and recursive versions
6. Hash Table — basic implementation with a hash function and collision handling

# Python Data Structures & Algorithms Showcase

A from-scratch implementation of core data structures and algorithms 
in Python, built as a portfolio project to demonstrate computer science 
fundamentals and software engineering skills.

Each implementation is written without relying on Python's built-in 
data structure shortcuts — the goal is to show understanding of how 
these structures work under the hood, not just how to use them.

---

## Why I Built This
As a software engineering graduate student (M.S., DevOps) with a 
background in web development and design, I built this project to 
strengthen and showcase my CS fundamentals. Every structure is 
documented with time complexity analysis, inline comments explaining 
my reasoning, and a README breaking down what I learned.

---

## What's Inside

### 🔗 Linked List
A singly linked list with insert, delete, search, traverse, and length 
methods. The foundation for the Stack and Queue implementations.
→ [View Linked List](./linked_list/)

### 📚 Stack & Queue
A Stack (LIFO) and Queue (FIFO) built on top of the custom LinkedList 
as the underlying structure.
→ [View Stack & Queue](./stack_and_queue/)

### 🌳 Binary Search Tree
A BST with insertion, search, and in-order traversal. Includes a 
discussion of balanced vs unbalanced trees and worst case performance.
→ [View Binary Search Tree](./binary_search_tree/)

### 🔃 Sorting Algorithms
Implementations of Bubble Sort and Merge Sort with a side-by-side 
performance comparison and discussion of when to use each.
→ [View Sorting Algorithms](./sorting/)

### 🔍 Binary Search
Both iterative and recursive implementations of binary search, with 
a comparison of their space complexity tradeoffs.
→ [View Binary Search](./binary_search/)

### #️⃣ Hash Table
A hash table with a custom hash function and collision handling via 
chaining. Includes insert, search, and delete methods.
→ [View Hash Table](./hash_table/)

---

## Time Complexity Overview

| Structure | Operation | Average Case | Worst Case |
|---|---|---|---|
| Linked List | Insert at beginning | O(1) | O(1) |
| Linked List | Insert at end | O(n) | O(n) |
| Linked List | Search / Delete | O(n) | O(n) |
| Stack | Push / Pop / Peek | O(1) | O(1) |
| Queue | Enqueue | O(n) | O(n) |
| Queue | Dequeue / Peek | O(1) | O(1) |
| BST | Insert / Search | O(log n) | O(n) |
| Bubble Sort | Sort | O(n²) | O(n²) |
| Merge Sort | Sort | O(n log n) | O(n log n) |
| Binary Search | Search | O(log n) | O(log n) |
| Hash Table | Insert / Search / Delete | O(1) | O(n) |

---

## How to Run Any File

Clone the repo:
```bash
git clone https://github.com/[your-username]/python-dsa-showcase.git
cd python-dsa-showcase
```

Run any file directly:
```bash
python3 linked_list/linked_list.py
python3 stack_and_queue/stack.py
python3 stack_and_queue/queue.py
python3 binary_search_tree/binary_search_tree.py
python3 sorting/bubble_sort.py
python3 sorting/merge_sort.py
python3 binary_search/binary_search.py
python3 hash_table/hash_table.py
```

---

## Tech Stack
- Language: Python 3
- No external libraries — all implementations are built from scratch

---

## Author
**Devon Schiavone**
