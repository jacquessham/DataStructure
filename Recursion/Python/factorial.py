def factorial(n):
	# Ensure n to be a non-negative number
	if n < 0: return None
	# The calculation starts here
	if n == 0: return 1
	return n*factorial(n-1)
