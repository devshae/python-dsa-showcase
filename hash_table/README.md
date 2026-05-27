# Hash Table

A from-scratch implementation of a Hash Table in Python, including 
a custom hash function and collision handling via chaining.

## What is a Hash Table?
A hash table stores data as key-value pairs — similar to a dictionary 
in Python. It uses a hash function to convert a key into an index, 
then stores the value at that index in an array. This makes insertions, 
lookups, and deletions extremely fast on average.

Think of it like a library filing system — instead of searching every 
shelf one by one, the filing system tells you exactly which shelf to 
go to instantly.

## How it Works
key: "name"
↓
hash("name") % 10 = 3
↓
table[3] → [["name", "Devon"]]

## Collision Handling — Chaining
Sometimes two different keys hash to the same index. This is called 
a **collision**. This implementation handles collisions using **chaining** 
— each index holds a list of key-value pairs so multiple items can 
share the same index without overwriting each other.

table[3] → [["name", "Devon"], ["city", "Ridgecrest"]]

## Methods

| Method | Description | Avg Time Complexity | Worst Case |
|---|---|---|---|
| `_hash(key)` | Converts a key to a table index | O(1) | O(1) |
| `insert(key, value)` | Inserts or updates a key-value pair | O(1) | O(n) |
| `search(key)` | Returns the value for a key, or None | O(1) | O(n) |
| `delete(key)` | Removes a key-value pair, returns True/False | O(1) | O(n) |

## A Note on Worst Case
The worst case O(n) occurs when many keys collide at the same index, 
forcing a linear search through all pairs at that index. A good hash 
function minimizes collisions and keeps average performance at O(1).
This is why choosing a strong hash function matters in production 
hash table implementations.

## How to Run
```bash
python3 hash_table.py
```

## What I Learned
Building a hash table from scratch made it clear why Python dictionaries 
are so fast — the hash function does the heavy lifting by mapping keys 
directly to indexes instead of searching through everything. Implementing 
collision handling with chaining was the most interesting part — it showed 
that even a simple list of lists can solve a complex problem elegantly. 
Understanding the difference between average case O(1) and worst case O(n) 
also deepened my understanding of why Big O notation describes a range of 
possible performance rather than a single fixed value.