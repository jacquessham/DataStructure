
public class MergeSort implements SortingAlgorithm {
	protected void merge_divide(int[] a){
		int size = a.length;
		int mid = a.length/2;
		if (size<2)
			return;
		int [] top = new int [mid]; // top array
		int [] bot = new int [size-mid]; // bottom array
		for (int i = 0; i<mid; i++){
			top[i]= a[i];
		} // Create top array
		for (int j = mid; j<size; j++){
			bot[j-mid] = a[j];
		} // Create bottom array
		merge_divide(top);
		merge_divide(bot);
		merge(a,top,bot);
	}
	
	protected void merge(int[] a, int[] top, int[] bot){
		int top_size = top.length;
		int bot_size = bot.length;
		int i=0, j=0, k=0; // i for top, j for bot, k for a
		while (i<top_size && j<bot_size){
			if (top[i] <= bot[j]){
				a[k] = top[i];
				i++;
				k++;
			} // End if
			else{
				a[k] = bot[j];
				j++;
				k++;
			} // End else
		} // End while
		
		while (i<top_size){
			a[k] = top[i];
			i++;
			k++;
		}
		while (j<bot_size){
			a[k] = bot[j];
			j++;
			k++;
		}
	}
	
	public void sort(int [] a){
		merge_divide(a);
	}
}
