# python3 ./algorithms/linear/stack.py
from linkedlist import LinkedList

class Stack:
  def __init__(self):
    self.linkedList = LinkedList()

  def push(self, element):
    self.linkedList.addFirst(element)
  
  def pop(self):
    return self.linkedList.deleteFirst()

  def print(self):
    self.linkedList.print()

print('--- stack ---')
stack = Stack()

for i in [ 15, 10, 6, 11, 17, 7, 42, 
           3, 7, 1, 2, 5, 6, 4 ]:
  stack.push(i)

stack.print()

for _ in range(0, len(stack.linkedList.toArray())):
  stack.pop()
  stack.print()

