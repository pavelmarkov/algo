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
  

  
  def print(self):
    print('=========')
    node = self.root
    queue = [ node ]
    print(node.value, '\n')
    while(len(queue) > 0):
      node = queue.pop(0)
      if(node):
        trio = []
        trio.append(node.value)
        if(node.left):
          queue.append(node.left)
          trio.append(node.left.value)
        else:
          trio.append(None)
        if(node.right):
          queue.append(node.right)
          trio.append(node.right.value)
        else:
          trio.append(None)
        print(trio)
    print('=========')

  def countChildren(self, node):
    count = 0
    if(node.left):
      count += 1
    if(node.right):
      count += 1
    return count

  def delete(self, value):
    print(f'deleting node with value {value}')
    deleteNode = self.findNodeByValue(value)
    print(deleteNode.value)
    childNum = self.countChildren(deleteNode)
    print(childNum)
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
        print(deleteNode.value, deleteNode.left.value, deleteNode.right )


binaryTree = BinaryTree(20)
binaryTree.insert(10)
binaryTree.insert(30)
binaryTree.insert(7)
binaryTree.insert(13)
binaryTree.insert(27)
binaryTree.insert(33)

binaryTree.print()

findNode = binaryTree.findNodeByValue(30);
print(findNode.left.value)

minNode, minNodeParent = binaryTree.findMinNodeInSubtree(findNode)
print(minNode.value)

binaryTree.delete(10)
binaryTree.print()



# binaryTree.insert(15)
# binaryTree.print()
