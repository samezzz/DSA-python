'''
Bubble sort is a simple sorting algorithm that works by repeatedly swapping adjacent elements in an array until the array is sorted.

Here's how the algorithm works in detail:

Start at the beginning of the array: The algorithm starts at the first element in the array and compares it to the next element.

Swap elements if necessary: If the first element is greater than the second element, the two elements are swapped. This process continues for each subsequent pair of elements in the array.

Move to the next element: After each pass through the array, the algorithm moves to the next element and repeats the process of comparing and swapping elements.

Repeat until the array is sorted: The algorithm repeats this process of comparing and swapping elements until the array is sorted. This is determined when no more swaps are made on a pass through the array.

Return the sorted array: The final sorted array is returned as the result of the bubble sort algorithm.

The time complexity of bubble sort is O(n^2), which makes it less efficient than other sorting algorithms such as quicksort or merge sort. However, bubble sort is easy to understand and implement, making it a good choice for small data sets or educational purposes.

In this implementation, the bubble_sort function takes an array as input and returns the sorted array. The function first gets the length of the array, n, and then repeatedly passes through the array, swapping elements if they are out of order. The sorting process continues until no more swaps are made, at which point the array is considered to be sorted.
'''

def bubble_sort(array):
    # Get the length of the array
    n = len(array)

    # Repeat the sorting process until the array is sorted
    for i in range(n):
        # Check if any swaps were made in this pass through the array
        swap = False
        for j in range(n - i - 1):
            # Compare the current element with the next element
            if array[j] > array[j + 1]:
                # Swap the elements if the current element is greater
                array[j], array[j + 1] = array[j + 1], array[j]
                # Set the swap flag to True
                swap = True

        # If no swaps were made, the array is already sorted
        if not swap:
            break

    # Return the sorted array
    return array

'''
Bubble sort is not the most efficient sorting algorithm and is generally not used in real-world applications. However, it is often used as a teaching tool or for small data sets because it is relatively simple to understand and implement.

Bubble sort is not recommended for large data sets or for use in performance-critical applications because of its poor time complexity of O(n^2). This means that the time it takes to sort the data increases quickly as the size of the data set increases.

In general, other sorting algorithms such as quicksort, merge sort, or even insertion sort are better choices for sorting larger data sets, due to their more efficient time complexities. However, bubble sort can still be a useful learning tool for those just starting to learn about sorting algorithms.
'''