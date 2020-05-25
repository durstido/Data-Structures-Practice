from collections import defaultdict

class Graph:

	def __init__(self,vertices):
		self.graph = defaultdict(list)
		self.V = vertices #number of vertices

	def addEdge(self,u,v): #edge from vertex u to vertx v
		if u not in self.graph:
			self.graph[u] = [v]
		elif u in self.graph:	
			self.graph[u].append(v)

	def topologicalSort(self): #edge list: [ [0,1], [0,6] ] edge between 0->1, 0->6

		visited = [False]*self.V
		stack = []

		for vertex in self.graph:
			if visited[vertex] == False:
				self.topologicalSortUtil(vertex, visited, stack)

		print(stack)

	def topologicalSortUtil(self, vertex, visited, stack):

		visited[vertex] = True

		if vertex in self.graph: 
			for v in self.graph[vertex]: #for all adjecent vertices
				if visited[v] == False:
					self.topologicalSortUtil(v, visited, stack)

		stack.insert(0,vertex)

g= Graph(6) 
g.addEdge(5, 2); 
g.addEdge(5, 0); 
g.addEdge(4, 0); 
g.addEdge(4, 1); 
g.addEdge(2, 3); 
g.addEdge(3, 1); 
print(g.topologicalSort())