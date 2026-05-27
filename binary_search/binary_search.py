# Write an iterative_binary_search(arr, target) function using a loop
# Write a recursive_binary_search(arr, target, low, high) function using recursion
# Add a test block at the bottom testing both versions

def iterative_binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check if the target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half, and target is in right half
        elif arr[mid] < target:
            low = mid +1
        # If target is smaller, ignore right half, and target is in left half
        else:
            high = mid - 1
    # Target was not found in the array
    return -1

def recursive_binary_search(arr, target, low, high):
    if low > high:
        return -1 # Target was not found in the array
    
    mid = (low + high) // 2

    # Check if the target is present at mid
    if arr[mid] == target:
        return mid
    # If target is greater, ignore left half, and target is in right half
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, high)
    # If target is smaller, ignore right half, and target is in left half
    else:
        return recursive_binary_search(arr, target, low, mid - 1)
    
# Test block
if __name__ == "__main__":
    test_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 5

    print("Testing iterative binary search:")
    result_iterative = iterative_binary_search(test_array, target)
    if result_iterative != -1:
        print(f"Element {target} found at index: {result_iterative}")
    else:
        print(f"Element {target} not found in the array.")

    print("\nTesting recursive binary search:")
    result_recursive = recursive_binary_search(test_array, target, 0, len(test_array) - 1)
    if result_recursive != -1:
        print(f"Element {target} found at index: {result_recursive}")
    else:
        print(f"Element {target} not found in the array.")