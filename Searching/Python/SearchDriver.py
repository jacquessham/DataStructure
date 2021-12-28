import LinearSearch as ls
import BinarySearch as bs

arr = range(5)
target = 2

for i in range(5):
	target = i
	print(ls.LinearSearch(arr,target))
	print(bs.BinarySearch(arr,target))