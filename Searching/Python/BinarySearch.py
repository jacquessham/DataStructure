def BinarySearch(arr: list, target):
    num_min = 0
    num_max = len(arr)-1
    while (num_min <= num_max):
        mid = (num_min + num_max)//2
        if arr[mid] == target: return arr[mid]
        if target > arr[mid]: num_min = mid + 1
        else: num_max = mid -1
    return -1