from collections import deque


class Graph:
	def __init__(self, vertices:int):
		self.edges = []
		self.vertices = vertices

		for i in range(vertices):
			sub_edges = []
			for j in range(vertices):
				sub_edges.append(0)
			self.edges.append(sub_edges)

	def addEdge(self, v1:int, v2:int, weight=1, isBothway=True):
		self.edges[v1][v2] = weight
		if isBothway:
			self.edges[v2][v1] = weight

	def outDegree(self, v1:int):
		degree = 0
		for i in range(self.vertices):
			if self.edges[v1][i] > 0:
				degree += 1
		return degree

	def inDegree(self, v1:int):
		degree = 0
		for i in range(self.vertices):
			if self.edges[i][v1] > 0:
				degree += 1
		return degree

	def inCost(self, v1:int):
		total_cost = 0
		for i in range(self.vertices):
			if self.edges[v1][i] > 0:
				total_cost += self.edges[v1][i]
		return total_cost

	def outCost(self, v1:int):
		total_cost = 0
		for i in range(self.vertices):
			if self.edges[i][v1] > 0:
				total_cost += self.edges[i][v1]
		return total_cost

	def topSortUtil(self, v:int, visited:list, stack:deque):
		visited[v] = True

		for i in range(len(self.edges[v])):
			# To get the edge has never visited and vertice exists
			if visited[i] is False and self.edges[v][i] > 0:
				visited, stack = self.topSortUtil(i, visited, stack)

		# If there is no next vertice exist, push this node to stack
		stack.append(v)
		return visited, stack


	def topologicalSort(self):
		indegree = []
		# To add the indegree for every edge
		for i in range(self.vertices):
			indegree.append(self.inDegree(i))

		# Declare stack for ordering and a list of visited to keep track
		stack = deque()
		visited = []
		for i in range(self.vertices):
			visited.append(False)

		for i in range(self.vertices):
			if visited[i] is False:
				print(i)
				visited, stack = self.topSortUtil(i, visited, stack)
		print(stack)
		# Reversing the list is same as popping all elems to a list
		return list(stack)[::-1]
