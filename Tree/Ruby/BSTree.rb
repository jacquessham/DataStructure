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
			node.left = BSTNode.new(elem=elem)
		else
			node.right = BSTNode.new(elem=elem)
		end # end if
	end # end func

	def insert(elem)
		if @root.nil? then 
			@root = BSTNode.new(elem=elem) 
		end # end if

		if elem < @root.elem then
			@root.left = BSTNode.new(elem=elem)
		else
			@root.right = BSTNode.new(elem=elem)
		end # end if
	end # end func

	def find_min_node(node)
		curr_node = node
		# Loop until the leftmost leaf
		while !curr_node.left.nil?
			curr_node = curr_node.left
		end # end while
	end # end func

end # end class