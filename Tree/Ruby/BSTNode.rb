class BSTNode
	def initialize(elem=nil, left=nil, right=nil)
		@elem = elem
		@left = left
		@right = right
	end # end constructor

	attr_accessor :elem
	attr_accessor :left
	attr_accessor :right
end # end class