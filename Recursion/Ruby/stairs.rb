def stairs(n)
	# Ensure n to be a non-negative number
	if n < 0
		return nil
	end
	# Calculation starts here
	if n==1
		return [[1]]
	end # end if
	if n==2
		return [[1,1],[2]]
	end # end if

	# If taking one step
	one_step = stairs(n-1)
	one_step.each{|elem| elem << 1}
	# If taking two steps
	two_step = stairs(n-2)
	two_step.each{|elem| elem << 2}
	
	return one_step + two_step
end #end func

def stairs_poss(n)
	# Ensure n to be a non-negative number
	if n < 0
		return nil
	end
	# Calculation starts here
	poss = stairs(n)
	return poss.length()
end # end if
