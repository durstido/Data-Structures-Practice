
class DFS:

	def __init__(self):
		self.graph = {}
		self.visited = {}


	def addEdge(self,u,v):
		if u in self.graph:
			tmp = self.graph[u]
			tmp.append(v)
			self.graph[u] = tmp
		else:
			self.graph[u] = [v]

	def DFS(self, s): #s is starting vertex

		self.visited[s] = 1
		print(s)

		if s in self.graph:
			for neighbor in self.graph[s]:
				if (neighbor not in self.visited):
					self.DFS(neighbor)



graph = DFS()
graph.addEdge(1,0)
graph.addEdge(1,2)
graph.addEdge(0,4)
graph.addEdge(0,3)
graph.addEdge(2,3)
graph.addEdge(2,5)
print(graph.graph)

graph.DFS(1)
