'''
Counting sort is a non-comparison based sorting algorithm. It is used to sort a set of elements that have a non-negative integer key value. The algorithm works by creating an auxiliary array to store the count of each key value and then using this information to determine the position of each element in the sorted output.

Here's how the algorithm works in detail:

Determine the range of the key values: In order to sort the elements, we first need to determine the range of the key values. This is used to determine the size of the auxiliary array that will be used to store the count of each key value.

Count the occurrences of each key value: Next, we use a loop to count the number of times each key value appears in the input array. We store this count in the auxiliary array at the index corresponding to the key value.

Calculate cumulative count: Next, we calculate the cumulative count of the key values by adding the count of the current key value to the count of the previous key value. This is used to determine the final position of each element in the sorted output.

Sort the input array: Finally, we use another loop to sort the input array based on the cumulative count information stored in the auxiliary array. We create an auxiliary output array to store the sorted elements.

In the code below, we first determine the range of the key values by finding the minimum and maximum values in the input array. We then create an auxiliary array count of size k to store the count of each key value. We use two loops to count the occurrences of each key value and calculate the cumulative count, and a final loop to sort the input array based on this information. The sorted elements are stored in the output array.
'''

def counting_sort(arr):
    # Determine the range of the key values
    max_value = max(arr)
    min_value = min(arr)
    k = max_value - min_value + 1

    # Create the auxiliary array for counting
    count = [0] * k

    # Count the occurrences of each key value
    for i in arr:
        count[i - min_value] += 1

    # Calculate the cumulative count
    for i in range(1, k):
        count[i] += count[i - 1]

    # Sort the input array
    output = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_value] - 1] = arr[i]
        count[arr[i] - min_value] -= 1

    return output


'''
Counting sort is an efficient and linear sorting algorithm that can be used when the elements being sorted are small integers. The algorithm operates by creating an auxiliary array (count array) of size equal to the range of the input elements, counting the frequency of each element, and then using the frequency information to place each element in its final sorted position. The algorithm has a linear time complexity of O(n) and is most useful in situations where the input elements are integers and the range is small relative to the number of elements. Some of the scenarios where counting sort can be used include:

Sorting items by their count, frequency or popularity, such as in a histogram.

Sorting elements with a limited range of values, such as ages or scores.

Sorting items in an array of integers where the range is small compared to the number of elements, such as sorting grades in a class of 30 students where grades are between 0 and 100.

When stability is required. Counting sort is a stable sorting algorithm, meaning that it preserves the relative order of equal elements.

Sorting data in linear time, which can be useful when sorting large datasets.
'''