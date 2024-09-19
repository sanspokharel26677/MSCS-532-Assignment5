"""
This program implements the Quicksort algorithm in Python. 
Quicksort is a divide-and-conquer sorting algorithm that works as follows:
1. Select a pivot element from the array.
2. Partition the array into two subarrays:
   - Elements less than or equal to the pivot
   - Elements greater than the pivot
3. Recursively apply the same logic to the subarrays.
4. Combine the sorted subarrays to produce the final sorted array.
Quicksort has an average time complexity of O(n log n) and is widely used due to its efficiency in practice.
"""

def quicksort(arr):
    # If the array is empty or has one element, it is already sorted
    if len(arr) <= 1:
        return arr  # Return the array as it is (base case)

    # Select the pivot element
    pivot = arr[len(arr) // 2]  # Select the middle element as the pivot

    # Partition the array into three parts:
    # - Elements less than the pivot
    # - Elements equal to the pivot
    # - Elements greater than the pivot
    less_than_pivot = [x for x in arr if x < pivot]  # Elements less than pivot
    equal_to_pivot = [x for x in arr if x == pivot]  # Elements equal to pivot
    greater_than_pivot = [x for x in arr if x > pivot]  # Elements greater than pivot

    # Recursively apply quicksort to the 'less than pivot' and 'greater than pivot' subarrays
    # Combine the sorted subarrays and the pivot to form the final sorted array
    return quicksort(less_than_pivot) + equal_to_pivot + quicksort(greater_than_pivot)

# Example usage:
# Define an unsorted array
unsorted_array = [3, 6, 8, 10, 1, 2, 1]

# Sort the array using quicksort
sorted_array = quicksort(unsorted_array)

# Print the sorted array
print("Given unsorted array:", unsorted_array)
print("Sorted array using quick sort:", sorted_array)

