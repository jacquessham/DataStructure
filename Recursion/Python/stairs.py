def stairs(n):
	# Ensure n to be a non-negative number
	if n < 0: return None
	# The calculation starts here
	if n==1: return [[1]]
	if n==2: return [[1,1],[2]]

	# If taking one step
	one_step = stairs(n-1)
	for elem in one_step:
		elem.append(1)
	# If taking two steps
	two_step = stairs(n-2)
	for elem in two_step:
		elem.append(2)
	return one_step + two_step

def stairs_poss(n):
	# Ensure n to be a non-negative number
	if n < 0: return None
	# The calculation starts here
	poss = stairs(n)
	return len(poss)
