def stairs(n):
	if n==1: return [[1]]
	if n==2: return [[1,1],[2]]

	one_step = stairs(n-1)
	for elem in one_step:
		elem.append(1)
	two_step = stairs(n-2)
	for elem in two_step:
		elem.append(2)
	return one_step + two_step

def stairs_poss(n):
	poss = stairs(n)
	return len(poss)
