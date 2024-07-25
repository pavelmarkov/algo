# python3 ./algorithms/graph/graph.py

from collections import defaultdict

class Node:
  def __init__(self, value = None, connected = []):
    self.value = value
    self.connected = connected

class Edge:
  def __init__(self, src, dist, weight = None):
    self.weight = weight
    self.src = src
    self.dist = dist
  
  def get(self):
    return (self.src, self.dist)

class Graph():
  def __init__(self, directed = False):
    self.nodes = set()
    self.edges = []
    self.adjacencyList = defaultdict(list)
    self.adjacencyMatrix = []
    self.directed = directed
  
  def addNode(self, node):
    self.nodes.add(node)
  
  def addEdge(self, src, dist, weight = None, stop = False):
    
    if(not stop):
      for node in [src, dist]:
        if(node not in self.nodes): self.addNode(node)

    edge = Edge(src, dist, weight)
    self.edges.append(edge)
    self.adjacencyList[src].append(edge)

    if(not self.directed):
      if(stop): return
      else: self.addEdge(dist, src, weight, True)

  def print(self):
    for node in self.adjacencyList.keys():
      row = node + ': {'
      row += ', '.join(
        [ edge.dist for edge in self.adjacencyList[node] ]
      )
      row += '}'
      print(row)



graph = Graph()

graph.addEdge('A', 'B', 1)
graph.addEdge('B', 'C', 2)
graph.addEdge('B', 'D', 3)

print(graph.nodes)
graph.print()
