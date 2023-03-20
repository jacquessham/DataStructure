import java.util.Stack;

public class GraphAdjMatrix implements Graph {
	private int [][] edges;
	private int size;
	// Row: From/Source
	// Column: To/Target
	
	public GraphAdjMatrix(int size){
		this.size = size;
		edges = new int[size][size];
		for (int i=0; i<size; i++)
			for (int j=0; j<size; j++)
				if (i==j)
					edges[i][j] = 0;
				else
					edges[i][j] = -1;
	} 
	// Negative number means the path is not accessible
	// Zero is itself
	// Positive number means the cost to go from v1 to v2
	
	
	public void addEdge(int v1, int v2){
		edges[v1][v2]=1;
	}
	public void topologicalSort(){
		int [] indegree = new int[size];
		
		for (int i = 0; i<size; i++)
			indegree[i] = inDegree(i);
		
		
		Stack stack = new Stack();
		for (int i=size; i>=0; i--){
			for (int j=0; j<size; j++)
				if (indegree[j]==i)
					stack.push(j);
		}
		while (!stack.empty()){
			System.out.print(stack.pop()+" ");
		}
		System.out.println();
	}
	public int[] neighbors(int vertex){
		if (size <= 0)
			return null;
		// Validate edges is not empty
		int[] temp = new int[size-1];
		int temp_counter=0;
		for (int i=0; i<size; i++){
			if(!findZero(vertex,i)){
				temp[temp_counter]=i;
				temp_counter++;
			}
		}
		return temp;
	}
		private boolean findZero(int v1, int v2){
			if (edges[v1][v2]==0)
				return true;
			return false;
		}
	
	private int inDegree(int v){
		int degree = 0;
		for (int i=0; i<size; i++){
			if (edges[i][v]!=0)
				degree++;
		}
		return degree;
	}
	
	public void printEdges(){
		for (int i=0; i<size; i++){
			for (int j=0;j<size; j++){
				System.out.print(edges[i][j]+" ");
			}
			System.out.println();
		}
	}
	
	
	public void addEdge(int v1, int v2, int weight){
		if (weight >= 0){
			edges[v1][v2]=weight;
			edges[v2][v1]=weight;
		}
	}
	public int getEdge(int v1, int v2){
		return edges[v1][v2];
	}
	
	private int findShortestDistance(int v1, boolean[] notVisited){
		int min = 0;	
		
		if (inDegree(v1) == 0)
			return -1;
		for (int i=0; i<size; i++){
			if (edges[v1][i] !=0 && edges[v1][i] != -1){
				min = edges[v1][i];
				continue;
			}
		}
		for (int i=0; i<size; i++){
			if (edges[v1][i] < min && notVisited[i] && edges[v1][i] != 0 && edges [v1][i] != -1)
				min = edges[v1][i];
		}
		return min;
	}
	
	public int createSpanningTree(){
		boolean [] notVisited = new boolean [size];
		int[] distance = new int[size];
		int cost = 0;
		
		for (int i=0; i<size; i++){
			distance[i] = findShortestDistance(i,notVisited);
			notVisited[i] = true;
		}
		
		for (int i=1; i<size; i++){
			if (distance[i] != -1)
				cost += distance[i];
		}
		
		return cost;
	}
	
	
}
