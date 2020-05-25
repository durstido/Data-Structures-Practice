from collections import defaultdict
from Queue import Queue

class Graph:

	def __init__(self):
		self.graph = defaultdict(list)
		self.queue = Queue()
		self.visited={}

	def addEdge(self, u, v): #u is current node, v are all nodes can get from here
		self.graph[u].append(v)

	def BFS(self, s): #s is current node 
		visited = {}

		visited[s] = True
		self.queue.write(s)

		print("BFS:")
		while self.queue.queue:
			s = self.queue.read()
			print(s)

			for node in self.graph[s]:
				if not (visited.get(node, False)):
					visited[node] = True
					self.queue.write(node)


graph = Graph()
graph.addEdge(2,1)
graph.addEdge(2,3)
graph.addEdge(1,3)
graph.addEdge(3,5)
graph.BFS(2)
