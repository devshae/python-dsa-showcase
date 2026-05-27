# Binary Search Tree

A from-scratch implementation of a Binary Search Tree (BST) in Python,
including insertion, search, and in-order traversal.

## What is a Binary Search Tree?
A BST is a tree data structure where each node has at most two children —
a left and a right. The rule is simple: values smaller than a node go to 
the left, values larger go to the right. This structure makes searching 
extremely efficient because you can eliminate half the remaining nodes 
at every step.

## Visual Example
    10
   /  \
  5    15
 / \   / \
3   7 12  20

In order traversal of this tree returns: [3, 5, 7, 10, 12, 15, 20]

## Methods

| Method | Description | Time Complexity |
|---|---|---|
| `insert(value)` | Inserts a value in the correct position | O(log n) avg, O(n) worst |
| `search(value)` | Returns True if value exists, False if not | O(log n) avg, O(n) worst |
| `in_order_traversal()` | Returns all values in ascending order | O(n) |

## A Note on Worst Case
The worst case O(n) happens when the tree becomes unbalanced — for example 
if you insert values in order (1, 2, 3, 4, 5...) every node ends up on 
the right side and the tree essentially becomes a linked list. Balanced 
BST variants like AVL trees and Red-Black trees solve this problem 
automatically.

## How to Run
```bash
python3 binary_search_tree.py
```

## What I Learned
Writing recursive methods for the first time was a big moment in this 
project. The insert and search methods both call themselves with a smaller 
version of the problem until they hit a base case — once that clicked, 
recursion went from confusing to elegant. The in-order traversal returning 
values in sorted order was also a satisfying result that made the BST's 
structure feel really intuitive.