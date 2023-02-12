def mergeSort(arr)
	if arr.length > 1 then
		mid = (arr.length/2).to_i
		l = arr[0..mid-1]
		r = arr[mid..-1]

		l = mergeSort(l)
		r = mergeSort(r)

		i = 0
		j = 0
		k = 0

		while (i < l.length-1 and j < r.length-1) do
			if l[i] < r[j] then
				arr[k] = l[i]
				i += 1
			else
				arr[k] = r[j]
				j += 1
			end # end if
			k += 1
		end # end while

		while i < l.length-1 do
			arr[k] = l[i]
			i += 1
			k += 1
		end # end while

		while j < r.length-1 do
			arr[k] = r[j]
			j += 1
			k += 1
		end # end while
	
	end # end if
	return arr
end # end func