
public class QuickSort implements SortingAlgorithm {
	protected void swap(int[] a, int i, int j){
		int temp = a[i];
		a[i] = a[j];
		a[j] = temp;
	}
	
	protected void qsort(int[] a, int top, int bot){
		int pivot = patition(a, top, bot);
		if (top<pivot-1)
			qsort(a,top,pivot-1); // Base case
		if (bot>pivot)
			qsort(a,pivot,bot); // Base case
	}
	
	protected int patition(int[] a, int top, int bot){
		int i = top;
		int j = bot;
		int pivot = (top+bot)/2;
		
		while (i<=j){
			while (a[i]<a[pivot])
				i++;
			while (a[j]>a[pivot])
				j--;
			if (i<= j){
				if (i == pivot)
					pivot = j;
				else if (j == pivot)
					pivot = i;
				swap(a,i++,j--);
			}
		}
		
		return i;
	}
	
	
	public void sort(int [] a){
		qsort(a,0,a.length-1);
	}
}
