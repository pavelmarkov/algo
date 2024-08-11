# python3 ./algorithms/linear/maxheap.py

class MaxHeap:
  def __init__(self):
    self.heap = []

  def swapByIndex(self, index1, index2):
    temp = self.heap[index1]
    self.heap[index1] = self.heap[index2]
    self.heap[index2] = temp

  def getParentIndex(self, index):
    if(index < 1):
      return None
    return (index - 1) // 2


  def getElementByIndex(self, index):
    if(index is None or 
       index < 0 or 
       index >= len(self.heap)):
      return None
    return self.heap[index]
  
  def getChildren(self, index):
    indexes = [index * 2 + 1, index * 2 + 2]
    elements = [self.getElementByIndex(indexes[0]),
                self.getElementByIndex(indexes[1])]
    return indexes, elements
  
  def up(self, index):

    while(True):
      element = self.getElementByIndex(index)
      parentIndex = self.getParentIndex(index)
      parentElement = self.getElementByIndex(parentIndex)

      if(parentIndex is None or 
         element <= parentElement):
        break

      self.swapByIndex(index, parentIndex)
      index = parentIndex

  def down(self, index):

    element = self.heap[index]

    while(index * 2 + 1 < len(self.heap)):
      childIdxes, childElements = self.getChildren(index)

      if(childElements[1] is None):
        if(element < childElements[0]):
          self.swapByIndex(index, childIdxes[0])
        break

      if(childElements[0] > childElements[1]):
        if(element < childElements[0]):
          self.swapByIndex(index, childIdxes[0])
          index = childIdxes[0]
      elif(element < childElements[1]):
          self.swapByIndex(index, childIdxes[1])
          index = childIdxes[1]
      else: break

  def removeMax(self):
    maxValue = self.heap[0]
    self.heap[0] = self.heap[-1]
    del self.heap[-1]
    if(len(self.heap) > 0):
      self.down(0)
    return maxValue

  def add(self, element):
    self.heap.append(element)
    self.up(len(self.heap) - 1)

  def print(self):
    i = 0
    level = 2**i
    currentIndex = 0
    padding = len(self.heap) // 3
    while(currentIndex < len(self.heap)):
      levelElements = []
      for j in range(0, level):
        index = currentIndex + j
        if(index > len(self.heap)-1):
          break
        levelElements.append(self.heap[index])
      print(padding * ' ', ' '.join([str(_) for _ in levelElements]))
      i += 1
      currentIndex += level
      level = 2**i
      padding //= 2
    print('\n')

heap = MaxHeap()

for i in [ 15, 10, 6, 11, 17, 7, 42, 
           3, 7, 1, 2, 5, 6, 4 ]:
  heap.add(i)

heap.print()

#     42
#   15 17
#  10 11 6 7
# 3 7 1 2 5 6 4

for _ in range(0, len(heap.heap)):
  heap.removeMax()
  heap.print()

