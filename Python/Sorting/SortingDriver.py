from random import randint
from time import time
from sys import setrecursionlimit
from SelectionSort import selectionSort
from BubbleSort import bubbleSort
from InsertionSort import insertionSort
from MergeSort import mergeSort
from QuickSort import quickSort


# Set the size of array
arr_len = 10000

# Increase Python recursion limit
if arr_len > 1000:
    setrecursionlimit(arr_len*2)

# Build an array with numbers randomly assigned
min_num = 0
max_num = 50000
arr = []
for i in range(arr_len):
    arr.append(randint(min_num,max_num))

# Time for selection sort
start = time()
arr_selectSorted = selectionSort(arr)
end = time()
time_diff = end - start
print('It took', round(time_diff, 4), 'seconds to sort with Selection Sort')

# Time for Bubble Sort
start = time()
arr_bubbleSorted = bubbleSort(arr)
end = time()
time_diff = end - start
print('It took', round(time_diff, 4), 'seconds to sort with Bubble Sort')

# Time for Insertion Sort
start = time()
arr_insertionSorted = insertionSort(arr)
end = time()
time_diff = end - start
print('It took', round(time_diff, 4), 'seconds to sort with Insertion Sort')

# Time for Merge Sort
start = time()
arr_mergeSorted = mergeSort(arr)
end = time()
time_diff = end - start
print('It took', round(time_diff, 4), 'seconds to sort with Merge Sort')

# Time for Quick Sort
start = time()
arr_quickSorted = quickSort(arr)
end = time()
time_diff = end - start
print('It took', round(time_diff, 4), 'seconds to sort with Quick Sort')