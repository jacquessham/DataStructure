def swap(arr: list, i: int, j: int) -> list:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

def quickSort(arr:list) -> list:
    return qsort(arr, 0, len(arr)-1)

def qsort(arr:list, low:int, high:int) -> list:
    if low < high:
        pivot = partition(arr, low, high)
        qsort(arr, low, pivot-1)
        qsort(arr, pivot+1, high)
    return arr

def partition(arr, low, high) -> int:
    i = (low -1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr = swap(arr, i, j)
    arr = swap(arr, i+1, high)
    return (i+1)
