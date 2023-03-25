pub fn LinearSearch(arr: &[i128], target:i128) -> i128{
	let mut ans: i128 = -1;
	for num in arr{
		if (*num as i128) == target{
			let ans = num;
			break;
		}
	}
	ans
}