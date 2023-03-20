public class BinaryIterativeSearch implements Search {
	public String searchName(){
		return "Binary Iterative Search";
	}
	public int search(int [] arr, int target){
		int min = 0;
		int max = arr.length-1;
		int mid; // Declare min, max, and mid point
		
		while (min<=max){ // While loop until not found
			mid = (min+max)/2;
			if (arr[mid]==target)
				return mid; // Return target
			if (arr[mid]>target)
				max = mid-1; // If not found, find the first half
			else
				min = mid+1; // Else, find the second half
		}
		
		return -1;
	}
}
