
public class BSTree {
	protected class BSTNode{
		private Comparable data;
		private BSTNode left;
		private BSTNode right;
		
		public BSTNode(Comparable data){
			this.data = data;
		}
		
		public String toString(){
			return (String) data;
		}
	}
	
	private BSTNode root;
	
	public boolean find(Comparable value){
		return find(value,root);
	}
	
	public boolean find(Comparable value,BSTNode node){
		if (node == null)
			return false;
		if (node.data.compareTo(value)==0)
			return true;
		else if (node.data.compareTo(value)<0)
			return find(value,node.left);
		else 
			return find(value,node.right); 
	}
	
	public BSTNode insert(Comparable value){
		if (root == null){
			root = insert(value,root);
			return root;
		}
		return insert(value,root);
	}
	
	public BSTNode insert(Comparable value, BSTNode node){
		if (node == null)
			return new BSTNode(value);
		if(node.data.compareTo(value)<0){
			node.left = insert(value, node.left);
			return node;
		}
		else{
			node.right = insert(value, node.right);
			return node;
		}	
	}
	
	public BSTNode delete(Comparable value){
		root = delete(value,root);
		return root;
	}
	
	public BSTNode delete(Comparable value,BSTNode node){
		if (node == null)
			return null;
		if (node.data.compareTo(value)==0){
			if (node.left == null)
				return node.right;
			else if (node.right == null)
				return node.left;
			else{
				if(node.right.left == null){
					node.data = node.right.data;
					node.right = node.right.right;
					return node;
				}
				else{
					node.data = removeSmallest(node.right);
					return node;
				}
			}// End outer-else
		} // End outer-if
		else if (value.compareTo(node.data)<0){
			node.left = delete(value, node.left);
			return node;
		}
		else{
			node.right = delete(value, node.right);
			return node;
		}
	}// End func
	
	private Comparable removeSmallest(BSTNode node){
		if (node.left.left == null){
			Comparable smallest = node.left.data;
			node.left = node.left.right;
			return smallest;
		}
		else
			return removeSmallest(node.left);
			
	}
	
	
	private String print(BSTNode node){
		if (node == null)
			return "";
		String str = "";
		str += print(node.right);
		str += node.data+",";
		str += print(node.left);
		return str;
	}
	
	public String toStringInOrder(){
		String str = print(root);
		String[] elem = str.split(",");
		str = "";
		for(int i=0;i<elem.length;i++){
			str += elem[i];
			if(i != elem.length-1)
				str += " ";
		}
		return str;
	}
	
	public String printPreOrder(BSTNode node) {
		if (node == null)
			return "";
		String str = "";
		str += node.data +",";
		str += print(node.left);
		str += print(node.right);
		return str;
	}
	public String toStringPreOrder(){
		String str = printPreOrder(root);
		String[] elem = str.split(",");
		str = "";
		for(int i=0;i<elem.length;i++){
			str += elem[i];
			if(i != elem.length-1)
				str += " ";
		}
		return str;
	}
	
}
