'''
Quick sort is a popular sorting algorithm that sorts an array or list by dividing the list into smaller sub-lists and sorting each sub-list. Here's how it works:

Choose a pivot element from the array. This element will be used to divide the list into smaller sub-lists.

Divide the list into two sub-lists: elements less than the pivot and elements greater than the pivot.

Recursively sort the two sub-lists using the quick sort algorithm.

Join the two sub-lists and the pivot element to form the final sorted list.
'''

def quick_sort(array):
  # Base case: if the length of the array is 1 or less, return the array as is
  if len(array) <= 1:
    return array

  # Choose the first element as the pivot
  pivot = array[0]

  # Create two lists: less and greater
  # less contains all elements less than or equal to the pivot
  # greater contains all elements greater than the pivot
  less = [x for x in array[1:] if x <= pivot]
  greater = [x for x in array[1:] if x > pivot]

  # Recursively sort the less and greater lists using the quick_sort function
  # Then concatenate the sorted less list, pivot element, and sorted greater list
  return quick_sort(less) + [pivot] + quick_sort(greater)

my_list = [-1, 3, 5, 7, 12, -24, 45, -43, 32]

print(quick_sort(my_list))

'''
Quick sort is often used when:

Sorting large data sets: Quick sort has an average time complexity of O(n log n), which makes it an efficient sorting algorithm for large data sets.

Sorting data that is randomly distributed: Quick sort performs well when the data being sorted is randomly distributed. This is because the pivot element used in the algorithm divides the data into roughly equal parts, which helps ensure good performance.

Sorting data that is already partially sorted: Quick sort can also perform well when sorting data that is already partially sorted. This is because the pivot element is chosen from the data, so it can help ensure that the sub-lists are divided into roughly equal parts.

When memory usage is a concern: Quick sort is a "in-place" sorting algorithm, which means that it only requires a constant amount of memory to sort the data, regardless of the size of the data.

That being said, quick sort is not always the best choice for sorting data. Other sorting algorithms, such as merge sort and heap sort, may perform better in certain cases. It's important to understand the trade-offs of each sorting algorithm and choose the best one for the specific use case.
'''
