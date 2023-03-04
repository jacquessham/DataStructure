require_relative "BSTNode"


class BSTree
	def initialize(root=nil)
		@root = root
	end # end constructor

	attr_writer :root

	def insert_node(node, elem)
		if node.nil? then 
			return BSTNode.new(elem=elem) 
		end # end if

		if elem < node.elem then
			node.left = self.insert_node(node.left, elem)
		else
			node.right = self.insert_node(node.right, elem)
		end # end if
		return node
	end # end func

	def insert(elem)
		if @root.nil? then 
			@root = BSTNode.new(elem=elem) 
		end # end if

		if elem < @root.elem then
			@root.left = self.insert_node(@root.left, elem)
		else
			@root.right = self.insert_node(@root.right, elem)
		end # end if
	end # end func

	def find_min_node(node)
		curr_node = node
		# Loop until the leftmost leaf
		while !curr_node.left.nil?
			curr_node = curr_node.left
		end # end while
		return curr_node
	end # end func

	def deleteNode(node, val)
		if node.nil? then return nil end # end if

		if node.elem == val
			then
				# When node has one or no child
				if node.left.nil?
					then return node.right
				elsif node.left.nil?
					then return node.left
				end # end inner if

				temp = self.find_min_node(node.right)
				node.elem = temp.elem
				node.right = self.deleteNode(node.right, temp.elem)
				return node
		end # end outer if

		if val < node.elem
			then node.left = self.deleteNode(node.left, val)
		else
			node.right = self.deleteNode(node.right, val)
		end # end if
		return node
	end # end func

	def delete(val)
		if @root.nil? then return nil end # end if

		if @root.elem == val
			then 
				if @root.left.nil?
					then @root = @root.right
					return
				elsif @root.right.nil?
					then @root = @root.left
					return
				else
					temp = self.find_min_node(@root.right)
					@root.elem = temp.elem
					@root.right = self.deleteNode(@root.right, temp.elem)
					return
				end # end inner if
		end # end outer if

		if val < @root.elem
			then @root.left = self.deleteNode(@root.left, val)
		else
			@root.right = self.deleteNode(@root.right, val)
		end # end if
	end # end func

	def findNode(node, val)
		if node.nil? then return false end # end if

		# If Node is null, code will crush
		if node.elem == val then return true
		elsif val < node.elem
			then return self.findNode(node.left, val)
		elsif val > node.elem
			then return self.findNode(node.right, val)
		end # end if
	end # end func

	def find(val)
		return self.findNone(@root, val)
	end # end func

	def printElem_inorder(node)
		if node.nil? then return end # end if
		self.printElem_inorder(node.left)
		print "#{node.elem} "
		self.printElem_inorder(node.right)
	end # end func

	def printElem_preorder(node)
		if node.nil? then return end # end if
		print "#{node.elem} "
		self.printElem_preorder(node.left)
		self.printElem_preorder(node.right)
	end # end func

	def printElem_postorder(node)
		if node.nil? then return end # end if
		self.printElem_postorder(node.left)
		self.printElem_postorder(node.right)
		print "#{node.elem} "
	end # end func

	def printElem(order='in')
		if order == 'in'
			then self.printElem_inorder(@root)
		elsif order == 'pre'
			then self.printElem_preorder(@root)
		elsif order == 'post'
			then self.printElem_postorder(@root)
		end # end if
		puts
	end # end func

end # end class
