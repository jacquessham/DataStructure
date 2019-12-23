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

	def outCost(self, v1:int):
		total_cost = 0
		for i in range(self.vertices):
			if self.edges[i][v1] > 0:
				total_cost += self.edges[i][v1]
		return total_cost
