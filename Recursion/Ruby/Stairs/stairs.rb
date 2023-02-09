def stairs(n)
	if n==1
		return [[1]]
	end # end if
	if n==2
		return [[1,1],[2]]
	end # end if

	one_step = stairs(n-1)
	one_step.each{|elem| elem << 1}

	two_step = stairs(n-2)
	two_step.each{|elem| elem << 2}
	
	return one_step + two_step
end #end func

def stairs_poss(n)
	poss = stairs(n)
	return poss.length()
end # end if
