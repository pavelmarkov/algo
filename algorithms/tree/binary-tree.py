# python3 ./algorithms/tree/binary-tree.py

class Node:
  def __init__(self, value = None):
    self.value = value
    self.left = None
    self.right = None

class BinaryTree:
  def __init__(self, rootValue):
    self.root = Node(rootValue)
  
  def insert(self, value):
    node = self.root
    while(node):
      if(value > node.value):
        if(not node.right):
          node.right = Node(value)
          break
        node = node.right
      elif(value < node.value):
        if(not node.left):
          node.left = Node(value)
          break
        node = node.left
      else:
        raise Exception('Duplicate value: ', value)

  def findNodeByValue(self, value):
    node = self.root
    while(True):
      if(not node):
        return None
      
      if(value > node.value):
        node = node.right
      elif(value < node.value):
        node = node.left
      else:
        return node

  def countChildren(self, node):
    count = 0
    if(node.left):
      count += 1
    if(node.right):
      count += 1
    return count

  def findMinNodeInSubtree(self, node):
    minNode = node
    parentNode = node
    while(minNode.left):
      parentNode = minNode
      minNode = minNode.left
    return minNode, parentNode

  def delete(self, value):
    deleteNode = self.findNodeByValue(value)
    childNum = self.countChildren(deleteNode)
    if(childNum == 0):
      deleteNode = None
    elif(childNum == 1):
      if(deleteNode.right):
        deleteNode = deleteNode.right
      if(deleteNode.left):
        deleteNode = deleteNode.left
    else:
      if(deleteNode.right.left):
        minNodeInSubtree, minNodeParent = self.findMinNodeInSubtree(deleteNode.right)
        deleteNode.value = minNodeInSubtree.value
        minNodeParent.left = None
      else:
        deleteNode.value = deleteNode.right.value
        deleteNode.right = deleteNode.right.right

  def dfs(self, node):
    if(not node):
       return []
    leftSubtree = self.dfs(node.left)
    rightSubtree = self.dfs(node.right)
    return  leftSubtree + [node.value] + rightSubtree
  
  def bfs(self, node):
    queue = [ node ]
    result = []
    while(len(queue)):
      node = queue.pop(0)
      result.append(node.value)
      if(node.left): queue.append(node.left)
      if(node.right): queue.append(node.right)
    return result
  
  def treeToArrayBfs(self):
    if(not self.root):
      return []
    
    result = [ self.root ] # tree values in bfs order
    cursor = 0 # current node index
    level = 0 # current level

    expectedNumOfNodesOnLevel = pow(2, level) # expected number of nodes on this level
    nodeExists = True # if any node exists on this level

    while(True):
      nodeExists = False

      for _ in range(0, expectedNumOfNodesOnLevel):
        node = result[cursor]
        cursor += 1
        if(not node):
          result.extend([None, None])
          continue
        for childNode in [node.left, node.right]:
          if(childNode): 
            result.append(childNode) 
            nodeExists = True
          else: result.append(None)
      
      if(not nodeExists):
        return result[0:cursor]
      
      level += 1
      expectedNumOfNodesOnLevel = pow(2, level)

  def print(self):
    print('\n')
    nodesInBfsOrder = self.treeToArrayBfs()
    numOfNodes = len(nodesInBfsOrder)
    level = 0
    cursor = 0
    expectedNumOfNodesOnLevel = pow(2, level)
    while(cursor < numOfNodes):
      row = [
        ((node and str(f'{node.value:02}')) or ' ') 
        for node in nodesInBfsOrder[
          cursor:cursor+expectedNumOfNodesOnLevel
        ]
      ]
      shift = ' ' * ((numOfNodes + 1) // (expectedNumOfNodesOnLevel * 2))
      print(shift + shift.join(row) + shift)
      
      level += 1
      cursor += expectedNumOfNodesOnLevel
      expectedNumOfNodesOnLevel = pow(2, level)
    print('\n')
    


binaryTree = BinaryTree(20)
[binaryTree.insert(value) for value in [10, 30, 7, 13, 27, 33]]

binaryTree.print()

findNode = binaryTree.findNodeByValue(30)
print('findNodeByValue(30): ', findNode.left.value, '\n')

minNode, minNodeParent = binaryTree.findMinNodeInSubtree(findNode)
print('binaryTree.findMinNodeInSubtree(findNode): ', minNode.value, '\n')

binaryTree.delete(10)
print('delete(10): ', '\n')
binaryTree.print()

[binaryTree.insert(value) for value in [40, 15, 2, 25, 29, 32, 45]]

binaryTree.print()

dfsOrder = binaryTree.dfs(binaryTree.root)
print('dfs result: ', dfsOrder, '\n')

bfsOrder = binaryTree.bfs(binaryTree.root)
print('bfs result: ', bfsOrder, '\n')