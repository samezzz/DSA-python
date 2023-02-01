'''
Heap sort is a comparison-based sorting algorithm that uses a data structure called a binary heap to sort elements in an array. A binary heap is a complete binary tree, which has the property that the value of a parent node is always greater than or equal to its children (for a max-heap) or less than or equal to its children (for a min-heap). The elements in a binary heap are stored in an array, so that it is possible to sort the elements by transforming the binary heap into a sorted array.

Here is the step-by-step process of how heap sort works:

Build a binary heap: The first step is to build a binary heap from the elements in the array. A binary heap can be constructed in O(n) time by starting with an empty binary heap and repeatedly inserting elements one by one.

Extract the maximum (or minimum) element: Once the binary heap has been constructed, the maximum (or minimum) element can be extracted and placed at the end of the sorted array. This operation takes O(log n) time, as it involves swapping the root of the binary heap with the last element in the heap, then fixing the binary heap property by swapping elements until the binary heap property is restored.

Repeat step 2: The process of extracting the maximum (or minimum) element and placing it at the end of the sorted array is repeated until the binary heap is empty. This results in the elements being sorted in ascending (or descending) order.

In the code below, the heapify function is a helper function that takes an array, the number of elements in the array, and an index i and restores the binary heap property for the sub-tree rooted at index i. The heapSort function builds the binary heap and then repeatedly extracts the maximum (or minimum) element and places it at the end of the sorted array. The time complexity of heap sort is O(n log n
'''

def heapify(arr, n, i):
    """Helper function to maintain the binary heap property"""
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)

    return arr


'''
Heap sort is used when you want to sort an array or list of items in ascending or descending order. The heap sort algorithm takes advantage of the property of a complete binary tree called a heap to sort the elements in O(nlogn) time complexity. This is faster than some other sorting algorithms like bubble sort and selection sort, which have a time complexity of O(n^2).

Heap sort is useful when you need to sort large datasets efficiently, as it performs well with large amounts of data. It is also an in-place sorting algorithm, meaning it sorts the elements in place and does not require any extra memory to store the sorted elements. This makes it a good choice when you have limited memory available.

Additionally, heap sort is not a stable sorting algorithm, which means that if two elements have the same value, their order may change after sorting. This is not a problem for most use cases, but it's important to keep in mind if you need to preserve the order of equal elements in your data.
'''