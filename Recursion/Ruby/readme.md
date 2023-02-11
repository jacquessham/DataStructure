# Recursion (Ruby)
Recursion is able to solve for problems where it depends on smaller instance of the same problem, such as Factorial or Fibonacci series.

## Classic Examples
### Factorial
The formula of factorial is <i>n! = n\*(n-1)\*(n-2)...2\*1</i> where <i>n > 0</i>. You may use recursion to calculate it. You may utilize <i>factorial.rb</i> to make the calculation. The script will ensure the input is a non-negative number, and return <i>nil</i> if the input is a negative number.

### Fibonacci Series
The formula of Fibonacci Series is <i>F<sub>n</sub> = F<sub>n-1</sub> + F<sub>n-2</sub></i>. You may use recursion to calculate the previous and the second previous integer. You may utilize <i>fibonacci.rb</i> to make the calculation. The script will ensure the input is a non-negative number, and return <i>nil</i> if the input is a negative number.

## Other Examples
### Stairs
One person is climbing up n stairs. This person can only climb up 1 stair, or 2 stairs at each step. Define a function to show how many different ways this person can choose to climb up to the top. This is an example of an application using Fibonacci Series. You may utilize <i>stairs.rb</i> to find the solution. There are 2 functions in this file that you may either find the solution of combinations of steps and the number of combinations. The script will ensure the input is a non-negative number, and return <i>nil</i> if the input is a negative number.
<br><br>
Note: If you choose to call the function to find the combinations of steps and would like to print the array. Please sure to convert the array to string, ie:

```
stairs(4).to_s
```