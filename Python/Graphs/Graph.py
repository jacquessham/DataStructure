from collections import deque
from sys import maxsize


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
				visited, stack = self.topSortUtil(i, visited, stack)
		# Reversing the list is same as popping all elems to a list
		return list(stack)[::-1]

	# Source: https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
	def minDistance(self, dist, sptSet):
		minDist = maxsize

		for v in range(self.vertices):
			# Find the vertex if they are not in min distance vertex
			if dist[v] < minDist and sptSet[v] is False:
				minDist = dist[v]
				min_index = v

		return min_index

	def dijkstra(self, origin):
		print('We called the function')
		# Put every vertice distance be inf
		dist = [maxsize for i in range(self.vertices)]
		# Origin to origin is 0 in distance
		dist[origin] = 0
		# Declase a list of visited to keep track
		sptSet = [False for i in range(self.vertices)]

		for _ in range(self.vertices):
			# Find the closest vertex
			u = self.minDistance(dist, sptSet)
			# Keep track of the min distance vertex has found
			sptSet[u] = True
			print(sptSet)
			print('Now is', _)
			print('u is', u)

			# Update distance of adjacent vertices of picked vertex
			# if the current distance is greater than new distance
			for v in range(self.vertices):
				print(dist[u],'+',self.edges[u][v],'=',dist[u] + self.edges[u][v])
				if self.edges[u][v] > 0 and sptSet[v] is False and \
				dist[v] > dist[u] + self.edges[u][v]:
					dist[v] = dist[u] + self.edges[u][v]
			print(dist)

		print("Vertex \tDistance from Source")
		for node in range(self.vertices): 
			print(node, "\t", dist[node])
