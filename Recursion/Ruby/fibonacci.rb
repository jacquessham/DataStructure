def fibonacci(n)
	if n==0 || n==1
		return n
	end # end if
	return fibonacci(n-2)+fibonacci(n-1)
end # end func
