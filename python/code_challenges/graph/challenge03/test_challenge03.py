# Write your test here
import pytest
from challenge03 import Graph

def test_strongly_connected_graph():
    edges = [[1,2],[1,0],[0,4],[4,3],[3,2],[3,1],[2,1],[2,4]]
    graph = Graph(edges)
    assert graph.is_strongly_connected() == "Strongly connected"

def test_not_strongly_connected_graph():
    edges = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,4],[1,7],[7,3]]
    graph = Graph(edges)
    assert graph.is_strongly_connected() == "Not strongly connected"

def test_single_node_graph():
    edges = [[1, 1]]
    graph = Graph(edges)
    assert graph.is_strongly_connected() == "Strongly connected"

def test_disconnected_graph():
    edges = [[1, 2], [3, 4]]
    graph = Graph(edges)
    assert graph.is_strongly_connected() == "Not strongly connected"

def test_cycle_graph():
    edges = [[1,2],[2,3],[3,1]]
    graph = Graph(edges)
    assert graph.is_strongly_connected() == "Strongly connected"
