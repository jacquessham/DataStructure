def LinearSearch(arr, target)
	# Halt if arr is not array
	return -1 unless arr.is_a? Array
	for i in arr do
		if i == target then return i end # end if
	end # end for
	return -1
end