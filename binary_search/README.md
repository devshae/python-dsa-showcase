# Binary Search

From-scratch implementations of Binary Search in Python — both an 
iterative and a recursive version.

## What is Binary Search?
Binary search is a fast search algorithm that works on sorted lists. 
Instead of checking every element one by one, it repeatedly cuts the 
search space in half by comparing the target to the middle element.

Think of it like a guessing game — if you're guessing a number between 
1 and 100 and I tell you "too high" or "too low" after each guess, 
you'd naturally start in the middle and work your way in. That's 
exactly how binary search works.

**Important:** Binary search only works on a sorted list.

## Visual Example

Searching for 11 in `[1, 3, 5, 7, 9, 11, 13, 15]`:

Step 1: low=0, high=7, mid=3 → arr[3]=7  → too low, go right
Step 2: low=4, high=7, mid=5 → arr[5]=11 → Found at index 5! ✅

Two steps to find the target in a list of 8 elements. A linear search 
could have taken up to 8 steps.

## Implementations

### Iterative
Uses a `while` loop with `low` and `high` pointers that move closer 
together with each step until the target is found or the search space 
is exhausted.

### Recursive
Uses the same logic but calls itself with an updated `low` or `high` 
on each step instead of looping. The base case returns `-1` when 
`low` exceeds `high`.

Both versions return the **index** of the target if found, or `-1` 
if not found.

## Performance

| Version | Best Case | Average Case | Worst Case | Space |
|---|---|---|---|---|
| Iterative | O(1) | O(log n) | O(log n) | O(1) |
| Recursive | O(1) | O(log n) | O(log n) | O(log n) |

**Note on space complexity:** The iterative version uses O(1) space 
because it just moves pointers. The recursive version uses O(log n) 
space because each recursive call adds a frame to the call stack.

## How to Run
```bash
python3 binary_search.py
```

## What I Learned
Implementing binary search in both styles made the difference between 
iterative and recursive thinking really clear. The logic is identical 
but the recursive version expresses it more elegantly by breaking the 
problem into smaller versions of itself. The space complexity difference 
between the two was also an interesting tradeoff I hadn't considered 
before — the iterative version is actually more memory efficient because 
it doesn't build up a call stack.