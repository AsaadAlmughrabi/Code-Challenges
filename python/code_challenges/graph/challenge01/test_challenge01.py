# Write your test here
import pytest
from collections import deque

# Assuming the Node, Edge, and Graph classes are defined in a file named graph.py
from challenge01 import Node, Edge, Graph

def test_bfs_traversal():
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

    # Perform BFS starting from node 'A'
    start_value = "A"
    expected_output = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K"]
    assert graph.bfs_traversal(start_value) == expected_output

    # Test BFS starting from node 'C'
    start_value = "C"
    expected_output = ["C", "A", "E", "F", "B", "G", "H", "D", "I", "K"]
    assert graph.bfs_traversal(start_value) == expected_output

    # Test BFS with a non-existent start node
    start_value = "Z"
    assert graph.bfs_traversal(start_value) == "Start node not found in the graph"

def test_add_node():
    graph = Graph()
    nodeA = graph.add_node("A")
    assert nodeA.value == "A"
    assert nodeA in graph.adj_list

def test_add_edge():
    graph = Graph()
    nodeA = graph.add_node("A")
    nodeB = graph.add_node("B")
    graph.add_edge(nodeA, nodeB)
    assert len(graph.adj_list[nodeA]) == 1
    assert len(graph.adj_list[nodeB]) == 1

    # Test adding edge with non-existent nodes
    nodeC = Node("C")
    assert graph.add_edge(nodeA, nodeC) == "A node does not exist"

if __name__ == "__main__":
    pytest.main()
