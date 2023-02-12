def swap(arr, i, j)
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr
end # end func

def quickSort(arr)
    return qsort(arr,0,arr.length-1)
end # end func

def qsort(arr, low, high)
    if low < high then
        pivot = partition(arr, low, high)
        qsort(arr, low, pivot-1)
        qsort(arr, pivot+1, high)
    end # end if
    return arr
end # end func

def partition(arr, low, high)
    i = (low -1)
    pivot = arr[high]
    for j in (low..high-1) do
        if arr[j] <= pivot then
            i += 1
            arr = swap(arr, i, j)
        end # end if
    end # end for
    arr = swap(arr, i+1, high)
    return (i+1)
end # end func
