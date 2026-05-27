# Create a merge sort algorithm in Python
# Write a merge_sort(arr) function that takes a list
# If the list has one or zero elements, it's already sorted
# Otherwise, split the list into two halves, sort each half recursively, and then merge the sorted halves together
# Add a test block at the bottom to demonstrate the function

def merge(left, right):
    result = []
    i = j = 0

    # Compare elements from both lists and add the smaller one to the result
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # If there are remaining elements in left or right, add them to the result
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

# Test block
if __name__ == "__main__":
    test_array = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", test_array)
    sorted_array = merge_sort(test_array)
    print("Sorted array:", sorted_array)

