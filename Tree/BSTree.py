from BSTNode import BSTNode

class BSTree:
	def __init__(self, root=None):
		self.root = root

	def setRoot(self, root:BSTNode):
		self.root = root

	def insert_node(self, node, elem):
		if node is None:
			return BSTNode(elem=elem)
		if elem < node.getElem():
			node.setLeft(self.insert_node(node.getLeft(), elem))
			return node
		else:
			node.setRight(self.insert_node(node.getRight(), elem))
			return node

	def insert(self, elem):
		if self.root is None:
			self.root = BSTNode(elem=elem)
			return
		if elem < self.root.getElem():
			self.root.setLeft(self.insert_node(self.root.getLeft(), elem))
		else:
			self.root.setRight(self.insert_node(self.root.getRight(), elem))

	def find_min_node(self, node):
		curr_node = node
		# Loop until the leftmost leaf
		while curr_node.getLeft() is not None:
			curr_node = curr_node.getLeft()
		return curr_node

	def deleteNode(self, node, val):
		if node is None: return None
		if node.getElem() == val:
			# When node has one or no child
			if node.getLeft() is None:
				return node.getRight()
			elif node.getRight() is None:
				return node.getLeft()
			# When node has two children
			temp = self.find_min_node(node.getRight())
			node.setElem(temp.getElem())
			node.setRight(self.deleteNode(node.getRight(), temp.getElem()))
			return node
		if val < node.getElem():
			node.setLeft(self.deleteNode(node.getLeft(), val))
		else:
			node.setRight(self.deleteNode(node.getRight(), val))
		return node

	def delete(self, val):
		if self.root is None: return None
		if self.root.getElem() == val:
			if self.root.getLeft() is None:
				self.root = self.root.getRight()
				return
			elif self.root.getRight() is None:
				self.root = self.root.getLeft()
				return
			else:
				temp = self.find_min_node(self.root.getRight())
				self.root.setElem(temp.getElem())
				self.root.setRight(self.deleteNode(self.root.getRight(), temp.getElem()))
				return
		if val < self.root.getElem():
			self.root.setLeft(self.deleteNode(self.root.getLeft(), val))
		else:
			self.root.setRight(self.deleteNode(self.root.getRight(), val))

	def findNode(self, node, val):
		if node is None:
			return False
		# If Node is null, code will crash
		if node.getElem() == val: 
			return True
		elif val < node.getElem():
			return self.findNode(node.getLeft(), val)
		elif val > node.getElem():
			return self.findNode(node.getRight(), val)

	def find(self, val):
		return self.findNode(self.root, val)

	def printElem_inorder(self, node):
		if node is None: return
		self.printElem_inorder(node.getLeft())
		print(node.getElem())
		self.printElem_inorder(node.getRight())

	def printElem_preorder(self, node):
		if node is None: return
		print(node.getElem())
		self.printElem_inorder(node.getLeft())
		self.printElem_inorder(node.getRight())

	def printElem_postorder(self, node):
		if node is None: return
		self.printElem_inorder(node.getLeft())
		self.printElem_inorder(node.getRight())
		print(node.getElem())

	def printElem(self, order='in'):
		if order == 'in':
			self.printElem_inorder(self.root)
		elif order == 'pre':
			self.printElem_preorder(self.root)
		elif order == 'post':
			self.printElem_postorder(self.root)
