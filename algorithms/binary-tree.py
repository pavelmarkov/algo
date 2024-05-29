# python3 ./algorithms/binary-tree.py

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
      
  def findMinNodeInSubtree(self, node):
    minNode = node
    parentNode = node
    while(minNode.left):
      parentNode = minNode
      minNode = minNode.left
    return minNode, parentNode
  

  
  def print(self, startingNodes = None):
    print('tree: ')
    numLevels = self.printPiramid(startingNodes)
    print('-=-' * (numLevels - 2))
    print('\n')

  def countChildren(self, node):
    count = 0
    if(node.left):
      count += 1
    if(node.right):
      count += 1
    return count

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
  
  def printPiramid(self, nodes = None, level = 0):
    if(not nodes):
      maxElements = self.printPiramid([ self.root ], 0)
      print(' ' * (maxElements - 1) + str(self.root.value))
      return maxElements
    nodeExist = False
    for node in nodes:
      if(node):
        nodeExist = True
        break
    numOfNodesOnThisLevel = pow(2, level)
    if(not nodeExist):
      return numOfNodesOnThisLevel
    thisLevelNodes = []
    for node in nodes:
      if(not node):
        thisLevelNodes.append(None)
        thisLevelNodes.append(None)
        continue
      thisLevelNodes.append(node.left)
      thisLevelNodes.append(node.right)
    maxNum = self.printPiramid(thisLevelNodes, level+1)
    treeRow = [((node and str(node.value)) or ' ') for node in thisLevelNodes]
    padding = ' ' * (maxNum // len(treeRow))
    print(padding + padding.join(treeRow) + padding)
    return maxNum
  
  def dfs(self, node):
    if(not node):
       return []
    leftSubtree = self.dfs(node.left)
    rightSubtree = self.dfs(node.right)
    return  leftSubtree + [node.value] + rightSubtree
  
  def bfs(self, node):
    visited = {}
    queue = [ node ]
    result = []
    while(len(queue)):
      node = queue.pop(0)
      result.append(node.value)
      if(node.left): queue.append(node.left)
      if(node.right): queue.append(node.right)
    return result



binaryTree = BinaryTree(20)
binaryTree.insert(10)
binaryTree.insert(30)
binaryTree.insert(7)
binaryTree.insert(13)
binaryTree.insert(27)
binaryTree.insert(33)


print('printPiramid(): ', '\n')
binaryTree.print()

findNode = binaryTree.findNodeByValue(30)
print('findNodeByValue(30): ', findNode.left.value, '\n')

minNode, minNodeParent = binaryTree.findMinNodeInSubtree(findNode)
print('binaryTree.findMinNodeInSubtree(findNode): ', minNode.value, '\n')

binaryTree.delete(10)
print('delete(10): ', '\n')
binaryTree.print()

binaryTree.insert(40)
binaryTree.insert(15)
binaryTree.insert(2)
binaryTree.insert(25)
binaryTree.insert(29)
binaryTree.insert(32)
binaryTree.print()
binaryTree.print([binaryTree.root.right])

dfsOrder = binaryTree.dfs(binaryTree.root)
print('dfs result: ', dfsOrder)

bfsOrder = binaryTree.bfs(binaryTree.root)
print('bfs result: ', bfsOrder)