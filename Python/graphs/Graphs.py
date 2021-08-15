"""The code is borrowed from the book "Problem Solving with Algorithms and Data Structures"
   http://interactivepython.org/courselib/static/pythonds/Graphs/graphintro.html
   
"""


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + " connectedTo: " + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

        self.front = []
        self.back = []
        self.depfs = []

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):  # f is from node, t is to node
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def printdfs(self):
        print("Front edges:", self.front)
        print("Back edges:", self.back)
        print("dfs:")
        for i in range(len(self.depfs)):
            print(self.depfs[i].getId(), end=" ")
        print()

    def __iter__(self):
        return iter(self.vertList.values())

    """
    Write a method to generate an adjacency matrix representation of the graph
    """

    def createAdjMatrix(self):
        rows, cols = (self.numVertices, self.numVertices)
        adjacent_matrix = [[0 for i in range(cols)] for j in range(rows)]
        for i in range(cols):
            for j in range(rows):
                adjacent_matrix[i][j] = 0

        for i in self.getVertices():
            l = self.getVertex(i)
            for w in l.getConnections():
                k = w.getId()
                adjacent_matrix[l.getId()][k] = 1
        return adjacent_matrix

        return

    """
    Write a method to traverse the graph using dfs from start node. 
    The function must print the nodes and edges in the order in which 
    they are visited, and mention if it is a forward or backward edge.
    """

    def dfs(self, stnode):
        self.depfs.append(stnode)
        for vertex in stnode.getConnections():
            if vertex not in self.depfs:
                self.front.append(stnode.getWeight(vertex))
                self.dfs(vertex)
            else:
                self.back.append(stnode.getWeight(vertex))
        return

    """
    Write a method to traverse the graph using bfs from start node.  The function must print the nodes and edges in the order in which 
    they are visited, and mention if it is a forward or cross edge.
    """

    def bfs(self, stnode):
        front = []
        back = []
        brefs = []

        brefs.append(stnode)
        for vertex in brefs:
            for neighbour in vertex.getConnections():
                if neighbour not in brefs:
                    brefs.append(neighbour)
                    front.append(vertex.getWeight(neighbour))
                else:
                    back.append(vertex.getWeight(neighbour))

        print("front edges: ", front)
        print("back edges: ", back)
        print("Bfs : ")
        for i in range(len(brefs)):
            print(brefs[i].getId(), end=" ")

    """
    Write a method to generate the minimum spanning tree of the graph using Kruskal algorithm
    """

    def mstKruskal(self):
        return
