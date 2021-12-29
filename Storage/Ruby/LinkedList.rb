require_relative 'Link'


class LinkedList
	def initialize(elem=nil)
		@top = Link.new(elem)
		@size = 1
	end

	def add_Elem(elem)
		temp = @top
		# Loop until the last node
		while !temp.next_Link.nil? do
			temp = temp.next_Link
		end # end while
		temp.next_Link = Link.new(elem)
		@size += 1
	end # end func

	def add_Elem_pos(pos, elem)
		# Stop if pos is greater than the linkedlist size
		if pos > @size then return end
		new_node = Link.new(elem)
		# If Add node at top
		if pos == 0
			then new_node.next_Link = @top
			@top = new_node
			return
		end # end if
		temp = @top
		it = 0
		# Loop until the previous node of pos
		while !temp.next_Link.nil? && it < pos do
			# If the next node is pos
			if it+1 == pos
				last_node = temp
				next_node = temp.next_Link
				new_node.next_Link = next_node
				last_node.next_Link = new_node
				@size += 1
				return
			end # end if
			temp = temp.next_Link
			it += 1
		end # end while
		# Add node at tail
		if it+1 == pos then
			temp.next_Link = new_node
			@size += 1
		end # end if
	end #end func

	def remove(pos)
		# Stop if pos is greater than the linkedlist size
		if pos > @size then return end
		# If removing the top
		if pos == 0
			unless @top.next_link.nil?
				@top.next_Link = nil
			else
				@top = @top.next_Link
			end # end unless
			@size -= 1
			return # return once it is done
		end # end if
		temp = @top
		it = 0
		# Loop until the previous node of pos
		while !temp.next_Link.nil? do
			if it+1 == pos
				then
					# If this is tail
					if temp.next_Link.nil? then temp.next_Link = nil 
					else
						# if this is not tail; if the next node is node is fine
						temp.next_Link = temp.next_Link.next_Link
					end # end if
					@size -= 1
					return
			end # end if
			temp = temp.next_Link
			it += 1
		end # end while
	end # end func

	def get(pos)
		# If linkedlist is empty
		if @size == 0 then return nil end
		# If pos is greater than size
		if pos > @size then return nil end
		temp = @top
		it = 0
		while !temp.next_Link.nil? and it < pos do
			temp = temp.next_Link
			it += 1
		end # end while
		return temp.elem
	end # end func

	def getSize
		return @size
	end # end func

	def printList
		# Helper function to print the whole linkedlist
		temp = @top
		if temp.nil? 
			then puts"This is Empty" 
				return 
		end # end if

		puts temp.elem
		while !temp.next_Link.nil? do
			temp = temp.next_Link
			puts temp.elem
		end # end while
	end # end func
end # end class