def LinearSearch(arr: list, target):
	for i in arr:
		if i == target:
			return i
	return -1