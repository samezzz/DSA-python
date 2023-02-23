arr = [46, 12, 26, 74, -4, 5, -24, 57]

def bubble_sort(array):
  n = len(array)
  for i in range(n):
    swap = False
    for j in range(n - i - 1):
      if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j + 1], array[j]
        swap = True
    if not swap:
      break
  return print(array, swap)
  
bubble_sort(arr)