public class FibonacciIterative implements Fibonacci {
	public int fibonacci(int n){
		int [] f = new int[n+1]; // Declare array to store every Fibonacci value from 0 to n
		f[0] = 0; // Declare n=0
		f[1] = 1; // Declare n=1
		for (int i=2;i<=n;i++) // Loop from n+2 until n to get value
			f[i] = f[i-1] + f[i-2];
		return f[n]; // Return the last Fibonacci value in the array
	}
}
