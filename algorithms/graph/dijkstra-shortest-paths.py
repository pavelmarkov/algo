# python3 ./algorithms/graph/dijkstra-shortest-paths.py

from graph import Graph

class Dijkstra(Graph):

  def dijkstraShortestPaths(self, start = 'A'):
    distance = {}
    queue = [ start ]
    visited = []

    for n in self.nodes:
      distance[n] = float('inf')
    distance[start] = 0

    while len(queue) > 0:
      node = queue.pop(0)
      visited.append(node)
      for edge in self.adjacencyList[node]:
        connectedNode = edge.dist
        if connectedNode not in visited:
          queue.append(connectedNode)
          newDist = distance[node] + edge.weight
          if(distance[connectedNode] > newDist):
            distance[connectedNode] = newDist
    print(f'Distances from {start}: ', distance)

dijkstraGraph = Dijkstra()

dijkstraGraph.addEdge('A', 'B', 1)
dijkstraGraph.addEdge('B', 'C', 2)
dijkstraGraph.addEdge('B', 'D', 3)

dijkstraGraph.dijkstraShortestPaths('A')