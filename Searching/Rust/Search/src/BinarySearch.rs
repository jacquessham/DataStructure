pub fn BinarySearch(arr: &[i128], target: i128) -> i128{
	let mut num_min: usize = 0;
	let mut num_max: usize = arr.len() as usize;

	let mut ans: i128 = -1;

	while num_min <= num_max{
		let num_mid: usize = (num_min + num_max)/2;
		if arr[num_mid] == target{
			let ans = arr[num_mid];
			break;
		}
		if target > arr[num_mid]{
			num_min = num_mid + 1;
		} else {
			num_max = num_mid - 1;
		}
	}
	ans
}