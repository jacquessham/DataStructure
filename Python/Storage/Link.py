class Link:
	def __init__(self, elem, next_Link=None):
		self.elem = elem
		self.next_Link = next_Link

	def getElem(self):
		return self.elem

	def getNext(self):
		return self.next_Link

	def setElement(self, new_elem):
		self.elem = new_elem

	def setNext(self, next_Link):
		self.next_Link = next_Link