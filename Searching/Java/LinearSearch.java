public class LinearSearch implements Search {
	public String searchName(){
		return "Linear Search";
	}
	
	public int search(int [] arr, int target){
		for (int i=0; i<arr.length; i++) // Linear Search
			if (arr[i]==target)
				return i;// Return i if found
		return -1;
	}
}
