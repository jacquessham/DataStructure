class ArrayStack
	def initialize
		@arr = []
	end 

	def push(new_elem)
		@arr << new_elem
	end

	def pop
		if @arr.length == 0 then return nil end
		return @arr.pop()
	end

	def peak
		if @arr.length == 0 then return nil end
		return @arr[@arr.length-1]
	end

	def empty
		if @arr.length == 0 then return true end
		return false
	end

	def size
		return @arr.length
	end

end # end class