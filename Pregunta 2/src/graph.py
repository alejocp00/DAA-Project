class Graph:

    def __init__(self, n, edges):
        self._vertices = [[] for _ in range(n)]
        self._edges = edges
        for u, v, w in edges:
            self._vertices[u].append((v, w))
            self._vertices[v].append((u, w))
        self._verticesCount = n
        self._edgesCount = len(edges)
        
    @property
    def VerticesCount(self):
        return self._verticesCount

    @property
    def EdgesCount(self):
        return self._edgesCount

    @property
    def Vertices(self):
        return self._vertices
    
    @property
    def Edges(self):
        return self._edges