class ArrayQueue
	def initialize
		@arr = []
		@head = 0
		@tail = 0
	end

	def enqueue(new_elem)
		@arr << new_elem
		@tail += 1
	end

	def dequeue
		# Edge case: When arr has nothing
		if @arr.length == 0 then return nil end
		item = @arr[@head]
		@head += 1
		return item
	end

	def empty
		if @head == @tail then return true end
		return false
	end
end # end class