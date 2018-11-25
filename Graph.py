class Vertex:
	def __init__(self,id):
		self.id =id
		self.edges={}
	def addEdge(self,vertex2,weight=0):
		self.edges[vertex2] = weight
	def getEdges(self):
		return self.edges.keys()
	def __str__(self):
		return " node "+ str(self.id) + " is connected to : " + str([neighbor.id for neighbor in self.edges])
		
class Graph:
	def __init__(self):
		self.vertices = {}
		self.numVertices = 0
	def addVertex(self,key):
		if key in self.vertices:
			print("The vertex is already in the graph")
			return
		else:
			self.numVertices += 1
			newVertex = Vertex(key)
			self.vertices[key] = newVertex
			return newVertex
		
	def getVertex(self, key):
		if key in self.vertices:
			return vert.vertices[key]
		else:
			return False
	def getVertices(self):
		return self.vertices.keys()
	def addEdge(self, fromnode, tonode, weight=0):
		if fromnode not in self.vertices:
			self.addVertex(fromnode)
		if tonode not in self.vertices:
			self.addVertex(tonode)
		self.vertices[fromnode].addEdge(self.vertices[tonode], weight)
		
	def __iter__(self):
		return iter(self.vertices.values())
		

g1 = Graph()
for i in range(6):
	g1.addVertex(i)

print(g1.getVertices())
g1.addEdge(0,1,2)
g1.addEdge(0,4,5)
g1.addEdge(1,2,7)
g1.addEdge(2,3,6)
g1.addEdge(3,4,8)
g1.addEdge(4,5,2)
for node in g1:
	print(node)

