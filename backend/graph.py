class Graph:
    """Grafo no dirigido usando lista de adyacencia.
    Nodos desde 0 hasta n-1.
    """

    def __init__(self, n: int):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u: int, v: int):
        """Agrega una arista no dirigida (u -- v)."""
        self.adj[u].append(v)
        self.adj[v].append(u)
