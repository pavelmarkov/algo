# python3 ./algorithms/linear/priority-queue.py
from maxheap import MaxHeap

class PriorityQueue:
  def __init__(self):
    self.queue = MaxHeap()

  def size(self):
    return len(self.queue.heap)

  def enqueue(self, element):
    self.queue.add(element)
  
  def dequeue(self):
    element = self.queue.removeMax()
    return element

  def print(self):
    print(self.queue.heap)

priorityQueue = PriorityQueue()

for i in [ 15, 10, 6, 11, 17, 7, 42, 
           3, 7, 1, 2, 5, 6, 4 ]:
  priorityQueue.enqueue(i)

priorityQueue.print()

for _ in range(0, priorityQueue.size()):
  priorityQueue.dequeue()
  priorityQueue.print()

