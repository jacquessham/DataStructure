class Link
	def initialize(elem, next_Link=nil)
		@elem = elem
		@next_Link = next_Link
	end # end def

	attr_accessor :elem
	attr_accessor :next_Link

end # end class