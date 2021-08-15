from Graphs import Graph
from Graphs import Vertex


# from binHeap import BinHeap


def testGraph():
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    g.vertList
    g.addEdge(5, 1, 8)
    g.addEdge(1, 2, 19)
    g.addEdge(5, 0, 10)
    g.addEdge(4, 6, 11)
    g.addEdge(6, 10, 23)
    g.addEdge(10, 9, 33)
    g.addEdge(9, 8, 7)
    g.addEdge(6, 7, 6)
    g.addEdge(8, 7, 1)
    g.addEdge(9, 6, 9)
    g.addEdge(7, 10, 14)
    g.addEdge(0, 4, 15)
    g.addEdge(0, 3, 16)
    g.addEdge(0, 2, 5)
    g.addEdge(0, 1, 2)
    g.addEdge(2, 3, 4)
    g.addEdge(3, 4, 30)
    g.addEdge(4, 5, 18)
    g.addEdge(5, 2, 22)
    g.addEdge(3, 1, 17)

    for v in g:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))
    print("Adjacent matrix:")
    AdjMat = list()
    AdjMat = g.createAdjMatrix()
    for i in range(g.numVertices):
        for j in range(g.numVertices):
            print(AdjMat[i][j], end=" ")
        print()

    start = g.getVertex(3)

    print("Depth first Traversal")
    g.dfs(start)
    g.printdfs()
    print("Breadth first Traversal")
    g.bfs(start)
    # g.mstKruskal()


def main():
    testGraph()


if __name__ == "__main__":
    main()
