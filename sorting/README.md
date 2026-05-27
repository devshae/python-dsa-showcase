# Sorting Algorithms

From-scratch implementations of two classic sorting algorithms in Python —
Bubble Sort and Merge Sort — including a comparison of their performance
and tradeoffs.

## Algorithms Implemented

### Bubble Sort
Bubble sort works by repeatedly comparing adjacent elements and swapping 
them if they are in the wrong order. The largest values "bubble up" to 
the end of the list one at a time with each pass. Simple to understand 
but gets slow quickly on large lists.

### Merge Sort
Merge sort uses a divide and conquer approach — it recursively splits 
the list in half until each piece has one element, then merges the pieces 
back together in sorted order. More complex than bubble sort but 
significantly faster on large datasets.

## Visual Example

**Bubble Sort** — one pass through `[5, 3, 8, 1]`:

[5, 3, 8, 1]  →  compare 5 and 3, swap
[3, 5, 8, 1]  →  compare 5 and 8, no swap
[3, 5, 8, 1]  →  compare 8 and 1, swap
[3, 5, 1, 8]  ✅ 8 has bubbled to the end

**Merge Sort** — splitting and merging `[38, 27, 43, 3]`:

[38, 27, 43, 3]
[38, 27]          [43, 3]
[38]  [27]        [43]  [3]
[27, 38]          [3, 43]
[3, 27, 38, 43] ✅

## Performance Comparison

| Algorithm | Best Case | Average Case | Worst Case | Space |
|---|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |

## When to Use Which

**Bubble Sort** is rarely used in production because of its O(n²) average 
and worst case performance. It's useful for educational purposes and works 
fine on very small or nearly sorted lists.

**Merge Sort** is preferred for larger datasets because it guarantees 
O(n log n) performance regardless of the input. The tradeoff is that it 
requires O(n) extra space to store the split halves during merging.

## How to Run
```bash
python3 bubble_sort.py
python3 merge_sort.py
```

## What I Learned
Implementing both algorithms back to back made their differences really 
concrete. Bubble sort was intuitive to write but seeing how quickly O(n²) 
grows compared to O(n log n) on paper made it clear why merge sort is 
preferred in the real world. Writing merge sort also reinforced recursion 
— breaking a problem into smaller versions of itself until you hit a base 
case is a pattern that keeps showing up across data structures.