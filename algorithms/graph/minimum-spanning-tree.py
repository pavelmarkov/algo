# python3 ./algorithms/graph/minimum-spanning-tree.py

from graph import Graph

class Kruskal(Graph):

  def spanningTree(self):
    group2node = {}
    node2group = {}
    result = []

    for i, node in enumerate(self.nodes):
      group2node[i] = {node}
      node2group[node] = i

    sortedEdges = sorted(self.edges, key=lambda e: e.weight)
    for edge in sortedEdges:
      [node1, node2] = [edge.src, edge.dist]
      [n1group, n2group] = [node2group[node1], node2group[node2]]
      [group1, group2] = [group2node[n1group], group2node[n2group]]
      [group1Len, group2Len] = [len(group1), len(group2)]

      # print('node1: ', node1, n1group, group1Len, '; node2: ', node2,n2group, group2Len)

      if(n1group == n2group): # cycle: don't include this edge
        continue

      if(group1Len > group2Len): # determine the largest group before group merge
        node2group[node2] = n1group
        group2node[n1group].update(group2)
        del group2node[n2group]
      else:        
        node2group[node1] = n2group
        group2node[n2group].update(group1)
        del group2node[n1group]

      result.append(edge)
    
    print(len(result), sum([edge.weight for edge in result]))
    return result

# test cases: https://workat.tech/problem-solving/practice/minimum-spanning-tree-using-kruskals-algorithm

spanTree = Kruskal(directed=True)
spanTree.addEdge('0', '1', 2)
spanTree.addEdge('0', '3', 3)
spanTree.addEdge('0', '6', 4)
spanTree.addEdge('1', '2', 3)
spanTree.addEdge('1', '4', 2)
spanTree.addEdge('3', '4', 5)
spanTree.addEdge('4', '5', 7)
spanTree.addEdge('4', '6', 6)
spanTree.spanningTree()

spanTree = Kruskal(directed=True)
spanTree.addEdge('0', '1', 2)
spanTree.addEdge('1', '2', 3)
spanTree.addEdge('0', '2', 4)
spanTree.spanningTree()

spanTree = Kruskal(directed=True)
spanTree.addEdge('0', '1', 2)
spanTree.addEdge('1', '2', 3)
spanTree.spanningTree()

spanTree = Kruskal(directed=True)
spanTree.addEdge('0', '0', 2)
spanTree.spanningTree()
