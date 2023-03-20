
public class ArrayQueue implements Queue {
	private Object[] arr;
	private int head, tail;
	
	public ArrayQueue(){
		arr = new Object[600];
		head = 0;
		tail = 0;
	}
	
	public Object dequeue(){
		if (empty())
			return null;
		Object item = arr[head];
		head++;
		if(head==arr.length)
			head=0;
		return item;
	}
	public void enqueue(Object item){
		if(full())
			grow_queue();
		arr[tail++]= item;
		if(tail==arr.length)
			tail=0;
	}
	public boolean empty(){
		if(head == tail)
			return true;
		return false;
	}
	
	private boolean full(){ // Helping function to check if array has empty slot
		if((tail+1)%arr.length==head)
			return true;
		return false;
	}
	
	private void grow_queue(){ // Must be wrong here
		Object[] new_arr = new Object[arr.length*2];
		if(tail<head){
			System.arraycopy(arr, head, new_arr, 0, arr.length-head);
		}
		System.arraycopy(arr, tail, new_arr, 0, arr.length-head-tail); //Not right
		arr = new_arr;
	}
	
}
