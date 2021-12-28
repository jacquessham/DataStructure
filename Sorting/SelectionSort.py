def swap(arr: list, i: int, j: int) -> list:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

def findSmallest(arr: list , start_pt: int) -> int:
    smallest = start_pt
    for i in range(start_pt + 1, len(arr)):
        if arr[i]< arr[smallest]:
            smallest = i
    return smallest

def selectionSort(arr: list) -> list:
    for i in range(len(arr)):
        smallest = findSmallest(arr, i)
        arr = swap(arr, smallest, i)
    return arr
