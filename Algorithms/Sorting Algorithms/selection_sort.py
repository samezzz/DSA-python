'''
Selection sort is a simple sorting algorithm that works by dividing the input array into two parts: the sorted part and the unsorted part. The algorithm repeatedly selects the minimum element from the unsorted part and appends it to the sorted part until the entire array is sorted.

The algorithm starts by assuming that the first element in the array is the minimum, and then compares this element to the rest of the elements in the unsorted part of the array. If a smaller element is found, the minimum is updated to the index of the smaller element. Once the minimum element has been found, it is swapped with the first element in the unsorted part. The algorithm then moves the boundary between the sorted and unsorted parts one step to the right, and repeats the process until the entire array is sorted.

The time complexity of selection sort is O(n^2), where n is the number of elements in the array. This means that the running time of the algorithm increases quadratically as the size of the input array increases, making it less efficient for large data sets compared to other sorting algorithms such as quicksort or merge sort. However, selection sort is still a useful algorithm to learn and understand, especially for beginners who are just starting to learn about sorting algorithms.
'''

def selection_sort(array):
    # Get the length of the array
    n = len(array)

    # Repeat the sorting process n-1 times
    for i in range(n-1):
        # Find the index of the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j

        # Swap the minimum element with the first element in the unsorted part of the array
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]

    # Return the sorted array
    return array


'''
Selection sort is a simple and intuitive sorting algorithm that is well suited for small data sets or for educational purposes. Here are a few reasons why you might use selection sort:

When you want a simple and straightforward sorting algorithm that is easy to understand and implement.
When you have a small amount of data to sort, and the time complexity of O(n^2) is not a concern.
When you want to sort an array in-place, i.e., without using any additional memory.
When you need to sort a list of items in ascending or descending order.
When you want to learn about the basic principles of sorting algorithms, as selection sort is a good starting point for beginners.
It's important to note that, while selection sort is simple and easy to understand, it is not an efficient sorting algorithm for large data sets. For larger data sets, you might want to consider using a different sorting algorithm, such as quicksort or merge sort, which have better time complexity and are more efficient for larger data sets.
'''