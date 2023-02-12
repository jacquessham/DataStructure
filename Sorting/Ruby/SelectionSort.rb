def swap(arr,i,j)
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp
	return arr
end # end func

def findSmallest(arr,start_pt)
    smallest = start_pt
    for i in (start_pt + 1)..arr.length-1 do
        if arr[i]< arr[smallest]
            then smallest = i
        end # end if
    end # end for
    return smallest
end # end func

def selectionSort(arr)
    for i in 0..arr.length-1 do
        smallest = findSmallest(arr, i)
        arr = swap(arr, smallest, i)
    end # end for
    return arr
end # end func