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
  
  def print(self):
    node = self.root
    queue = [ node ]
    print(node.value, '\n')
    while(len(queue) > 0):
      node = queue.pop(0)
      if(node):
        if(node.left):
          queue.append(node.left)
        if(node.right):
          queue.append(node.right)
        if(node.left and node.right):
          print(node.left.value, node.right.value, '\n')


binaryTree = BinaryTree(20)
binaryTree.insert(10)
binaryTree.insert(30)
binaryTree.insert(7)
binaryTree.insert(13)
binaryTree.insert(27)
binaryTree.insert(33)

binaryTree.print()

