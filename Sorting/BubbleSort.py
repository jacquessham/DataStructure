def swap(arr: list, i: int, j: int) -> list:
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp
	return arr

def bubbleSort(arr: list) -> list:
	for i in range(len(arr)):
		for j in range(len(arr)-i-1):
			if arr[j] > arr[j+1]:
				swap(arr, j, j+1)
			print(arr)
	return arr