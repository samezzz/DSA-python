'''
Insertion sort is a simple sorting algorithm that builds a sorted array one item at a time. It is an in-place sorting algorithm, meaning it doesn't require any additional memory to sort an array, and it is also an efficient algorithm for small arrays.

Here's how insertion sort works:

The algorithm starts with an unsorted array and considers the first element of the array to be a sorted subarray of length 1.

The next element from the unsorted part of the array is then selected and compared to each element in the sorted subarray.

If the selected element is smaller than the first element in the sorted subarray, it is inserted in front of the first element. If it is larger than the first element but smaller than the second element, it is inserted in between the first and second elements. This process continues until the selected element is larger than or equal to the last element in the sorted subarray.

The process of selecting an element from the unsorted part of the array and inserting it into the correct position in the sorted subarray is repeated until there are no more elements in the unsorted part of the array.
'''

def insertion_sort(array):
    # loop over the elements in the array starting from the second one
    for i in range(1, len(array)):
        # select the current element
        current = array[i]
        # initialize the position of the previous element
        j = i - 1
        # loop over the elements to the left of the current element
        while j >= 0 and array[j] > current:
            # if the previous element is larger than the current element,
            # move the previous element one position to the right
            array[j + 1] = array[j]
            # decrement the position of the previous element
            j = j - 1
        # insert the current element into the correct position
        array[j + 1] = current
    # return the sorted array
    return array

my_list = [12, 3, 7, 22, -12, 100, 1]

print(insertion_sort(my_list))

'''
Insertion sort is often used when:

Sorting small data sets: Insertion sort has a simple and straightforward implementation, making it a good choice for sorting small data sets. Its time complexity is O(n^2), which makes it less efficient than other sorting algorithms for large data sets, but still acceptable for small data sets.

Sorting partially sorted data: Insertion sort is particularly efficient when sorting data that is already partially sorted. In this case, the number of comparisons and swaps required to sort the data is significantly reduced.

Sorting data with limited memory: Insertion sort is an "in-place" sorting algorithm, which means that it requires only a constant amount of memory to sort the data, regardless of the size of the data. This makes it a good choice for sorting data with limited memory.

Stable sorting: Insertion sort is a stable sorting algorithm, which means that it maintains the relative order of equal elements in the sorted data.

Online sorting: Insertion sort can be used to sort data as it is being received. This is because it only requires a constant amount of memory to sort the data, and it can sort the data in place as it is being received, without having to wait for all the data to be received before sorting it.

That being said, insertion sort is not always the best choice for sorting data. Other sorting algorithms, such as quick sort and merge sort, may perform better in certain cases. It's important to understand the trade-offs of each sorting algorithm and choose the best one for the specific use case.
'''