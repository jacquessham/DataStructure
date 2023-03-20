public class BinaryRecursiveSearch implements Search {
	public String searchName(){
		return "Binary Recursive Search";
	}
	
	public int search(int [] arr, int target, int min, int max) { // Declare function to pass min and max
		int mid = (min+max)/2; // Declare mid point first
		if (min>max)
			return -1; // Base case: If target not found, return -1
		if (arr[mid] == target)
			return mid; // If target is found, return target
		if (arr[mid]>target)
			return search(arr, target, min, mid-1); // If not found, search the first half
		else
			return search(arr,target, mid+1, max); // Else, search the second half
		
	}
	public int search(int [] arr, int target){
		return search(arr, target, 0, arr.length-1);

	}
}
