class BSTNode:
	def __init__(self, elem=None, left=None, right=None):
		self.elem = elem
		self.left = left
		self.right = right

	def setElem(self, elem):
		self.elem = elem

	def setLeft(self, left):
		self.left = left

	def setRight(self, right):
		self.right = right

	def getElem(self):
		return self.elem

	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right
