use std::time::SystemTime;
use rand::Rng;
mod BinarySearch;
mod LinearSearch;


fn main(){
	// let arr: [i128; 100000] = rand::random();
	let arr = [(); 10000].map(|_| rand::thread_rng().gen_range(0..=100000));
	let arr_last_index = arr.len()-1;
	let target:i128 = rand::thread_rng().gen_range(0..=arr_last_index) as i128;
	println!("Now we are searching {target} between 0 and {arr_last_index}");

	// Linear Search
	let ls_start = SystemTime::now();
	LinearSearch::LinearSearch(&arr, target);
	let ls_end = SystemTime::now();
	let ls_diff = ls_end.duration_since(ls_start);
	println!("LinearSearch() took {ls_diff:?} ms");


	// Binary Searchlet 
	// let bs_start = SystemTime::now();
	// BinarySearch::BinarySearch(&arr, target);
	// let bs_end = SystemTime::now();
	// let bs_diff= bs_end.duration_since(bs_start);
	// println!("BinarySearch() took {bs_diff:?} ms");


}