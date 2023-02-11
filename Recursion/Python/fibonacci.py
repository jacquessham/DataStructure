def fibonacci(n):
	# Ensure n to be a non-negative number
	if n < 0: return None
	# The calculation starts here
	if n == 0 or n==1: return n
	return fibonacci(n-2) + fibonacci(n-1)
