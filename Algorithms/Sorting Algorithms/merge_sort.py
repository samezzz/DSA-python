'''
The merge sort algorithm is a divide-and-conquer sorting algorithm that works by dividing the array into two equal parts, sorting each part recursively, and then merging the sorted parts back together to form a single sorted array.

Here's how the algorithm works in detail:

Divide the array: The array is divided into two equal parts, with one part stored in a left array and the other part stored in a right array.

Recursively sort the arrays: The left and right arrays are each sorted recursively using the merge sort function.

Merge the sorted arrays: The sorted left and right arrays are merged back together to form a single sorted array. This is done by initializing two pointers, i and j, to keep track of the current position in the left and right arrays, respectively. The algorithm then compares the elements at the current positions in the left and right arrays, and adds the smaller one to a new result array. This process continues until all elements from both left and right arrays have been added to the result array.

Return the result array: The final result array is returned as the sorted array.

The merge sort algorithm has a time complexity of O(n log n), making it an efficient sorting algorithm for large data sets. It is also a stable sorting algorithm, which means that it maintains the relative order of equal elements in the sorted data.

I hope this explanation provides a more in-depth understanding of the merge sort algorithm!
'''

def merge_sort(array):
  # Base case: if the length of the array is 1 or less, return the array as is
  if len(array) <= 1:
    return array

  # Divide the array into two equal parts
  mid = len(array) // 2
  left = array[:mid]
  right = array[mid:]

  # Recursively sort the left and right arrays using the merge_sort function
  left = merge_sort(left)
  right = merge_sort(right)

  # Initialize two pointers, i and j, to keep track of the current position in the left and right arrays, respectively
  i = j = 0

  # Create a new list, result, to store the sorted elements
  result = []

  # Compare the elements at the current positions in the left and right arrays, and add the smaller one to the result list
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  # Add any remaining elements from the left or right arrays to the result list
  result.extend(left[i:])
  result.extend(right[j:])

  # Return the result list
  return result

my_list = [12, 3, 7, 22, -12, 100, 1]

print(merge_sort(my_list))

'''
Merge sort is often used in cases where it is necessary to sort large data sets efficiently. Its time complexity of O(n log n) makes it well-suited for sorting large amounts of data.

Another advantage of merge sort is that it is a stable sorting algorithm, meaning that it maintains the relative order of equal elements in the sorted data. This property makes it useful in cases where the order of equal elements is important, such as in certain databases or other applications where data integrity is critical.

Additionally, merge sort is a versatile sorting algorithm that can be used for arrays of any data type, including numerical arrays, arrays of strings, and arrays of objects.

In summary, merge sort is often used for large data sets, where stability and versatility are important factors in choosing a sorting algorithm.
'''