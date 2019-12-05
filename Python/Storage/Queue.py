class ArrayQueue:
	def __init__(self):
		self.arr = []
		self.head = 0
		self.tail = 0

	def enqueue(self, new_elem):
		self.arr.append(new_elem)
		self.tail += 1

	def dequeue(self):
		# Edge case: When arr has nothing
		if len(self.arr) == 0:
			return None
		item = self.arr[self.head]
		self.head += 1
		return item

	def empty(self):
		if (self.head==self.tail):
			return True
		return False
