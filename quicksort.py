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


"""
This code below implements the Quicksort algorithm in Python, including a randomized version. 
The randomized version improves the average performance by reducing the chance of encountering 
the worst-case scenario, which occurs when the pivot selection is poor. 
Quicksort has an average time complexity of O(n log n) and a worst-case time complexity of O(n^2).
This implementation is optimized to have better average performance in practice.
"""

import random  # Import random module for random pivot selection

def randomized_quicksort(arr):
    # If the array is empty or has one element, it is already sorted
    if len(arr) <= 1:
        return arr  # Return the array as it is (base case)

    # Select the pivot element randomly
    pivot = random.choice(arr)  # Choose a random element from the array as the pivot

    # Partition the array into three parts:
    # - Elements less than the pivot
    # - Elements equal to the pivot
    # - Elements greater than the pivot
    less_than_pivot = [x for x in arr if x < pivot]  # Elements less than pivot
    equal_to_pivot = [x for x in arr if x == pivot]  # Elements equal to pivot
    greater_than_pivot = [x for x in arr if x > pivot]  # Elements greater than pivot

    # Recursively apply quicksort to the 'less than pivot' and 'greater than pivot' subarrays
    # Combine the sorted subarrays and the pivot to form the final sorted array
    return randomized_quicksort(less_than_pivot) + equal_to_pivot + randomized_quicksort(greater_than_pivot)

# Example usage:
# Define an unsorted array
unsorted_array = [3, 6, 8, 10, 1, 2, 1]

# Sort the array using the randomized version of quicksort
sorted_array = randomized_quicksort(unsorted_array)

# Print the sorted array
print("---------------------------------------------------------")
print("Given unsorted array:", unsorted_array)
print("Sorted array (randomized quicksort):", sorted_array)


"""
This code below implements and empirically compares the deterministic and randomized versions 
of the Quicksort algorithm. It measures the execution time of both versions on arrays of 
different sizes and distributions (random, sorted, reverse-sorted). It also generates a graph 
to visualize the performance differences and saves this graph as an image file.
"""

print("---------------------------------------------------------")
print("Comparison and visulization of data")

import random  # Import random module for generating test cases
import time  # Import time module for measuring execution time
import matplotlib.pyplot as plt  # Import matplotlib for plotting

def deterministic_quicksort(arr):
    # If the array is empty or has one element, it is already sorted
    if len(arr) <= 1:
        return arr  # Return the array as it is (base case)

    # Select the pivot element (middle element)
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
    return deterministic_quicksort(less_than_pivot) + equal_to_pivot + deterministic_quicksort(greater_than_pivot)

def randomized_quicksort(arr):
    # If the array is empty or has one element, it is already sorted
    if len(arr) <= 1:
        return arr  # Return the array as it is (base case)

    # Select the pivot element randomly
    pivot = random.choice(arr)  # Choose a random element from the array as the pivot

    # Partition the array into three parts:
    # - Elements less than the pivot
    # - Elements equal to the pivot
    # - Elements greater than the pivot
    less_than_pivot = [x for x in arr if x < pivot]  # Elements less than pivot
    equal_to_pivot = [x for x in arr if x == pivot]  # Elements equal to pivot
    greater_than_pivot = [x for x in arr if x > pivot]  # Elements greater than pivot

    # Recursively apply quicksort to the 'less than pivot' and 'greater than pivot' subarrays
    # Combine the sorted subarrays and the pivot to form the final sorted array
    return randomized_quicksort(less_than_pivot) + equal_to_pivot + randomized_quicksort(greater_than_pivot)


def test_quicksort_versions():
    # Define different input sizes to test the sorting algorithms
    input_sizes = [100, 1000, 5000, 10000]
    
    # Define different input distributions to see how the algorithms perform on various data types
    distributions = {
        'random': lambda size: [random.randint(0, size) for _ in range(size)],  # Random array
        'sorted': lambda size: list(range(size)),  # Sorted array
        'reverse_sorted': lambda size: list(range(size, 0, -1)),  # Reverse-sorted array
    }

    # Store results for plotting later
    results = {
        'Deterministic': {dist_name: [] for dist_name in distributions.keys()},  # To store results for deterministic Quicksort
        'Randomized': {dist_name: [] for dist_name in distributions.keys()}  # To store results for randomized Quicksort
    }

    # Run tests for each input size and distribution
    for size in input_sizes:
        print(f"Input size: {size}")  # Print the current input size
        for dist_name, dist_func in distributions.items():
            # Generate the test array based on the current distribution
            test_array = dist_func(size)
            
            # Measure the execution time for the deterministic version
            start_time = time.time()  # Record start time
            deterministic_quicksort(test_array.copy())  # Sort using the deterministic version
            deterministic_duration = time.time() - start_time  # Calculate duration
            results['Deterministic'][dist_name].append(deterministic_duration)  # Store the duration for later plotting

            # Measure the execution time for the randomized version
            start_time = time.time()  # Record start time
            randomized_quicksort(test_array.copy())  # Sort using the randomized version
            randomized_duration = time.time() - start_time  # Calculate duration
            results['Randomized'][dist_name].append(randomized_duration)  # Store the duration for later plotting

            # Print the results for the current input size and distribution
            print(f"  {dist_name.capitalize()} array - Deterministic: {deterministic_duration:.6f}s, Randomized: {randomized_duration:.6f}s")
        print()  # Print a newline for better readability

    # Plot the results to visualize the performance differences
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))  # Create subplots for each distribution
    for i, (dist_name, ax) in enumerate(zip(distributions.keys(), axes)):
        # Plot the execution times for the deterministic version
        ax.plot(input_sizes, results['Deterministic'][dist_name], label='Deterministic Quicksort', marker='o')
        # Plot the execution times for the randomized version
        ax.plot(input_sizes, results['Randomized'][dist_name], label='Randomized Quicksort', marker='x')
        ax.set_title(f'Performance on {dist_name.capitalize()} Array')  # Set the title of the subplot
        ax.set_xlabel('Input Size')  # Set the x-axis label
        ax.set_ylabel('Time (seconds)')  # Set the y-axis label
        ax.legend()  # Show the legend
        ax.grid(True)  # Show the grid for easier interpretation of the graph

    # Save the plot as an image file in the current working directory
    image_path = 'quicksort_performance_comparison.png'
    plt.savefig(image_path)  # Save the figure to the specified path
    plt.close()  # Close the plot to free up memory

    print(f"Graph has been saved as {image_path}")  # Print the path where the graph was saved

# Run the empirical tests and visualization
test_quicksort_versions()


