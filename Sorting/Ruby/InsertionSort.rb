def insertionSort(arr)
	for i in (1..arr.length-1) do
		temp = arr[i]
		j = i-1
		while (arr[j]> temp and j >= 0) do
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = temp
		end # end while
	end # end for
	return arr
end # end func