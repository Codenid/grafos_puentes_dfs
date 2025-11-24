from typing import List
from graph import Graph

class BridgeFinder:
    """Implementa DFS para identificar puentes en un grafo."""

    def __init__(self, graph: Graph):
        self.g = graph
        self.n = graph.n
        self.time = 0
        self.disc = [-1] * self.n
        self.low = [-1] * self.n
        self.bridges: List[List[int]] = []

    def dfs(self, u: int, parent: int):
        self.disc[u] = self.low[u] = self.time
        self.time += 1

        for v in self.g.adj[u]:
            if self.disc[v] == -1:  # arista de árbol
                self.dfs(v, u)
                self.low[u] = min(self.low[u], self.low[v])

                # Condición de puente
                if self.low[v] > self.disc[u]:
                    self.bridges.append([u, v])

            elif v != parent:       # arista de retroceso
                self.low[u] = min(self.low[u], self.disc[v])

    def get_bridges(self) -> List[List[int]]:
        """Retorna todas las aristas que son puentes."""
        for i in range(self.n):
            if self.disc[i] == -1:
                self.dfs(i, -1)
        return self.bridges
