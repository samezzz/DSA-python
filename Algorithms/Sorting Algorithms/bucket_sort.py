'''
Bucket sort is a sorting algorithm that is used to sort a list of elements into a linear order. The idea behind bucket sort is to divide the elements into several "buckets", each of which represents a range of values. The elements are then sorted within each bucket, and the resulting sorted buckets are concatenated to form the final sorted list.

Bucket sort works by first dividing the elements into n uniformly spaced buckets, where n is the number of elements in the list. The element values are then assigned to the appropriate bucket based on the value of the element. Once all of the elements have been assigned to a bucket, the elements within each bucket are sorted using another sorting algorithm, such as insertion sort or quicksort. The sorted buckets are then concatenated to form the final sorted list.

Bucket sort has a time complexity of O(n), where n is the number of elements in the list. This makes it an efficient sorting algorithm for small datasets, or for datasets where the elements are distributed uniformly across the range of values. However, if the elements are not distributed uniformly, then bucket sort can be much less efficient, as some buckets may be much larger than others.

Bucket sort is often used as a pre-processing step in other algorithms, such as radix sort, which sorts elements based on their digits. By using bucket sort to sort the elements into ranges, radix sort can then be used to sort the elements within each range more efficiently.
'''

def bucket_sort(arr):
    max_val = max(arr)  # Find the maximum value in the array
    size = max_val/len(arr)  # Divide the maximum value by the number of elements to get the size of each bucket
    buckets = [[] for _ in range(len(arr))]  # Initialize an empty list of buckets
    for i in range(len(arr)):
        j = int(arr[i]/size)  # Determine which bucket the current element belongs in
        if j != len(arr):
            buckets[j].append(arr[i])  # Append the element to the appropriate bucket
    for i in range(len(arr)):
        buckets[i] = sorted(buckets[i])  # Sort the elements within each bucket
    result = []  # Initialize an empty list to store the sorted elements
    for i in range(len(arr)):
        result = result + buckets[i]  # Concatenate the sorted buckets to form the final sorted list
    return result


'''
Bucket sort is a distribution sort algorithm that is often used when the input data has a well-defined distribution, such as when the data is uniformly distributed or when the data can be easily partitioned into a fixed number of buckets.

For example, if you had a list of exam scores that ranged from 0 to 100 and you wanted to sort the scores, bucket sort would be a good choice because you can easily divide the possible scores into 100 buckets (one for each possible score value).

Bucket sort has a best-case time complexity of O(n) when the input data is uniformly distributed, making it much faster than other sorting algorithms such as quicksort, merge sort, and heapsort. However, the time complexity of bucket sort can become O(n^2) if the input data is not well-distributed, so it's important to choose an appropriate sorting algorithm based on the properties of the input data.

In conclusion, bucket sort is a useful sorting algorithm when the input data has a well-defined distribution, but it may not be the best choice for more general sorting tasks.
'''