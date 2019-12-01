from random import randint
from SelectionSort import selectionSort
from BubbleSort import bubbleSort
from InsertionSort import insertionSort

arr = []
for i in range(5):
    arr.append(randint(0,100))
print(arr)

"""
arr_selectSorted = selectionSort(arr)
print(arr_selectSorted)
"""
"""
arr_bubbleSorted = bubbleSort(arr)
print(arr_bubbleSorted)
"""
arr_insertionSorted = insertionSort(arr)
print(arr_insertionSorted)