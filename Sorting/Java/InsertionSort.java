
public class InsertionSort implements SortingAlgorithm {
	public void sort(int[]a){
		int temp; // Declare temp variable for swapping
		for (int i =1;i<a.length;i++){ // First pointer from the beginning
			for(int j=i; j>0;j--){ // Second pointer to scan from the end to i
				if (a[j]<a[j-1]){
					temp = a[j];
					a[j]=a[j-1];
					a[j-1] = temp;
				}
					
			}
		}
	
	}
	
} // End class
