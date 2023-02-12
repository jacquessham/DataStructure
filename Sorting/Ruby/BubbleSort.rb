def swap(arr,i,j)
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp
	return arr
end # end func

def bubbleSort(arr)
	for i in (0...arr.length) do
		for j in (0...(arr.length-i-1)) do
			if arr[j] > arr[j+1]
				then swap(arr, j, j+1)
			end # end if
		end # end inner for
	end # end outer for
	return arr
end # end func