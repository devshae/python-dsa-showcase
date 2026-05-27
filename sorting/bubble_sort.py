# Bubble Sort (bubble_sort.py)
# Write a bubble_sort(arr) function that takes a list
# Repeatedly compare adjacent elements and swap them if they're in the wrong order
# Keep doing this until no swaps are needed
# Add a test block at the bottom

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already in place, no need to check thems
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Test block
if __name__ == "__main__":
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_array)
    sorted_array = bubble_sort(test_array)
    print("Sorted array:", sorted_array)