def BinarySearch(arr: list, target):
    num_min = 0
    num_max = len(arr)
    while (num_min <= num_max):
        mid = int((num_min + num_max)/2)
        if arr[mid] == target: return arr[mid]
        if target > arr[mid]: num_min = mid
        else: num_max = mid
    return -1