from collections import deque

class Node:
    def __init__(self, value=None):
        """Initialize a node with an optional value."""
        self.value = value

    def __str__(self):
        """Return the string representation of the node's value."""
        return self.value

class Edge:
    def __init__(self, vertex, weight=0):
        """Initialize an edge with a destination vertex and optional weight."""
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        """Initialize an empty adjacency list for the graph."""
        self.adj_list = {}

    def add_node(self, value):
        """Add a node with the given value to the graph."""
        new_vertex = Node(value)
        self.adj_list[new_vertex] = []
        return new_vertex
    
    def add_edge(self, node1, node2, weight=0):
        """Add an edge between two nodes with an optional weight."""
        if node1 not in self.adj_list:
            return "A node does not exist"
        
        if node2 not in self.adj_list:
            return "A node does not exist"
        
        edge1 = Edge(node2, weight)
        self.adj_list[node1].append(edge1)

        edge2 = Edge(node1, weight)
        self.adj_list[node2].append(edge2)
    
    def bfs_traversal(self, start_value):
        """Perform BFS traversal starting from the given node value."""
        start_node = None
        for node in self.adj_list.keys():
            if node.value == start_value:
                start_node = node
                break
        
        if start_node is None:
            return "Start node not found in the graph"
        
        visited = set()
        queue = deque([start_node])
        traversal_order = []

        while queue:
            current_node = queue.popleft()
            if current_node not in visited:
                traversal_order.append(current_node.value)
                visited.add(current_node)
                for edge in self.adj_list[current_node]:
                    if edge.vertex not in visited:
                        queue.append(edge.vertex)
        
        return traversal_order

    def __str__(self):
        """Return a string representation of the graph."""
        output = ''
        for vertex in self.adj_list.keys():
            output += f'{vertex} -> '
            for edge in self.adj_list[vertex]:
                output += f'{edge.vertex} ({edge.weight}) ------> ' 
            output += '\n'
        return output

# Example Usage
graph = Graph()

nodeA = graph.add_node("A")
nodeB = graph.add_node("B")
nodeC = graph.add_node("C")
nodeD = graph.add_node("D")
nodeE = graph.add_node("E")
nodeF = graph.add_node("F")
nodeG = graph.add_node("G")
nodeH = graph.add_node("H")
nodeI = graph.add_node("I")
nodeK = graph.add_node("K")

graph.add_edge(nodeA, nodeB)
graph.add_edge(nodeA, nodeC)
graph.add_edge(nodeB, nodeD)
graph.add_edge(nodeC, nodeE)
graph.add_edge(nodeC, nodeF)
graph.add_edge(nodeE, nodeG)
graph.add_edge(nodeF, nodeH)
graph.add_edge(nodeG, nodeI)
graph.add_edge(nodeI, nodeK)

start_value = "A"
print(graph.bfs_traversal(start_value))  # Output: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K']
