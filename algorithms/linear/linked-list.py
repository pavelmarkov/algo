# python3 ./algorithms/linear/linked-list.py

class Node:
  def __init__(self, data = None, connected = []):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def findLast(self):
    if(self.head == None):
      return None
    node = self.head
    while(node.next):
      node = node.next
    return node
  
  def addFirst(self, data):
    newNode = Node(data)
    if(self.head == None):
      self.head = newNode
    else:
      newNode.next = self.head
      self.head = newNode
    return newNode
  
  def addLast(self, data):
    newNode = Node(data)
    if(self.head == None):
      self.head = newNode
    else:
      currentLast = self.findLast()
      currentLast.next = newNode
    return newNode
  
  def deleteNodeAtIndex(self, index):
    if(self.head == None):
      return None
    if(index == 0):
      deletedNode = self.head
      self.head = None
      return deletedNode
    currentIndex = 0
    prevNode = None
    node = self.head
    while(node.next and currentIndex <= index):
      currentIndex += 1
      prevNode = node
      node = node.next
      if(currentIndex == index):
        prevNode.next = node.next
        return node

    return None
  
  def toArray(self):
    result = []
    node = self.head
    while(node):
      result.append(node.data)
      node = node.next
    return result

  def print(self):
    array = map(str, self.toArray())
    print(' -> '.join(array))


linkedList = LinkedList()
linkedList.addFirst(1)
linkedList.addLast(2)
linkedList.addFirst(3)
linkedList.addLast(4)
linkedList.addFirst(5)
linkedList.addLast(6)
linkedList.addFirst(7)
linkedList.addLast(8)

linkedList.print()

deletedNode = linkedList.deleteNodeAtIndex(3)
print(deletedNode.data)

linkedList.print()