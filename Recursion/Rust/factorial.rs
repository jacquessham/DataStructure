pub fn factorial(n: i128) -> i128{
	// No need to check n < 0 since i32 restricted it already
	let ans = if n == 0 {1} else {n*factorial(n-1)};
	ans
}
