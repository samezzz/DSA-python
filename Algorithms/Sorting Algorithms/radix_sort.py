'''
Radix sort is an integer sorting algorithm that sorts a collection of integers based on the digits of each integer. It is an efficient algorithm for sorting large collections of integers that have a fixed number of digits.

Radix sort works by repeatedly sorting the integers based on one digit at a time, starting from the least significant digit and working towards the most significant digit. At each step, the integers are grouped into buckets based on the current digit, and then reassembled back into the original list in order. This process is repeated for each digit until all digits have been considered and the list is fully sorted.

One key advantage of radix sort is its time complexity, which is O(d(n+b)), where d is the number of digits in the integers being sorted, n is the number of integers, and b is the number of buckets used. This time complexity is linear in the number of digits, making it very efficient for large collections of integers.

Additionally, radix sort is a non-comparative sorting algorithm, meaning that it does not compare the values of the integers being sorted. Instead, it relies on the positional values of the digits to determine their order. This makes it much faster than other sorting algorithms like bubble sort and selection sort, which require a lot of comparisons.

Overall, radix sort is a useful algorithm for sorting large collections of integers, especially when the integers have a fixed number of digits. However, it is not suitable for sorting floating-point numbers or other data types that do not have a fixed number of digits.
'''
def radix_sort(arr):
    # Get the maximum number of digits in the array
    max_digits = max(len(str(x)) for x in arr)
  
    # Repeat the sorting process for each digit
    for i in range(max_digits):
        # Create a list of empty buckets for each digit (0-9)
        buckets = [[] for _ in range(10)]
    
        # Sort the elements into the appropriate bucket based on the current digit
        for x in arr:
            digit = (x // 10**i) % 10
            buckets[digit].append(x)
    
        # Reassemble the elements back into the original list
        arr = []
        for bucket in buckets:
            arr.extend(bucket)
    
    # Return the sorted list
    return arr
