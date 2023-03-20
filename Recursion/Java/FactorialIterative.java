public class FactorialIterative implements Factorial {
	public int factorial(int n){
		int answer = 1; // Declare answer to 1 to multiply
		while (n>0){
			answer = answer*n;
			n--;
		} // Multiply the answer by (n-1) until 1
		return answer; // Return answer
	}
}
