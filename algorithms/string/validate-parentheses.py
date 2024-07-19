# python3 ./algorithms/string/validate-parentheses.py

class StringExpression:
  def __init__(self, expression = '', openSymbol = '(', closeSymbol = ')'):
    self.expression = expression
    self.openSymbol = openSymbol
    self.closeSymbol = closeSymbol

  def print(self):
    print(self.expression)
  
  def isValid(self):
    counter = 0
    for char in self.expression:
      if(char == self.openSymbol): counter += 1
      if(char == self.closeSymbol): counter -= 1
      if(counter < 0):
        return False
    if(counter == 0):
      return True
    return False

expression1 = StringExpression('((()))')
print(expression1.isValid())

expression2 = StringExpression('((())))')
print(expression2.isValid())