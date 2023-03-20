public class FactorialRecursive implements Factorial {
	public int factorial(int n){
		if (n==1)
			return 1; // Base case at 1
		return n*factorial(n-1); // Multiply n-1 until base case
	}
}
