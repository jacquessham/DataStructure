public class FibonacciRecursive implements Fibonacci {
	public int fibonacci(int n){
		if (n==0||n==1) // Base case at n=0 or n=1
			return n;
		return fibonacci(n-1) + fibonacci(n-2); // Add every Fibonacci value until base case
	}

}
