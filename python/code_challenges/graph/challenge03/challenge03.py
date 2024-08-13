# Write here the code challenge solution
from collections import defaultdict

class Graph:
    def __init__(self, edges):
        """
        Initializes a new instance of the Graph class.

      
        """
        self.graph = defaultdict(list)
        self.vertices = set()
        self._create_graph(edges)

    def _create_graph(self, edges):
        """
        Creates an adjacency list representation of a graph from a list of edges.

       
        """
        for u, v in edges:
            self.graph[u].append(v)
            self.vertices.add(u)
            self.vertices.add(v)

    def _dfs(self, v, visited):
        """
        Performs a Depth-First Search (DFS) traversal of the graph starting from the given vertex.
        
      
        """
        visited.add(v)
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self._dfs(neighbor, visited)

    def _get_transpose(self):
        """
        Returns the transpose of the current graph.
        
        The transpose of a graph is another graph where the direction of all edges is reversed.
        
        """
        transpose_graph = Graph([])
        for v in self.graph:
            for neighbor in self.graph[v]:
                transpose_graph.graph[neighbor].append(v)
        return transpose_graph

    def is_strongly_connected(self):
        """
        Checks if the graph is strongly connected.

        A graph is strongly connected if there is a path from every vertex to every other vertex.
        This function performs a Depth-First Search (DFS) traversal of the graph starting from an arbitrary vertex.
        If all vertices are visited, it reverses the graph and performs another DFS traversal.
        If all vertices are visited again, the graph is strongly connected.

       .
        """
       
        start_vertex = next(iter(self.vertices))
        visited = set()
        self._dfs(start_vertex, visited)
        
        
        if len(visited) != len(self.vertices):
            return "Not strongly connected"

        transpose_graph = self._get_transpose()
        visited = set()
        transpose_graph._dfs(start_vertex, visited)

        if len(visited) != len(self.vertices):
            return "Not strongly connected"

        return "Strongly connected"

# Example 1
numbers1 = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,4],[1,7],[7,3]]
graph1 = Graph(numbers1)
print(graph1.is_strongly_connected())  # Output: Not strongly connected

# Example 2
numbers2 = [[1,2],[1,0],[0,4],[4,3],[3,2],[3,1],[2,1],[2,4]]
graph2 = Graph(numbers2)
print(graph2.is_strongly_connected())  # Output: Strongly connected
