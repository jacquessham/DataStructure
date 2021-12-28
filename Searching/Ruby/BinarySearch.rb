def BinarySearch(arr, target) 
	# Halt if arr is not array
	return -1 unless arr.is_a? Array
	num_min = 0
	num_max = arr.length
	while num_min <= num_max do
		mid = ((num_min+num_max)/2).to_i
		if arr[mid] == target then return arr[mid] end
		if target > arr[mid] 
			then num_min = mid
		else
			num_max = mid
		end # end if
	end # end while
	return -1
end