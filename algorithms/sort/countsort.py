
# python3 ./algorithms/sort/countsort.py

def countsort(values):
  countDict = {}
  maxValue = -1
  sortedArray = []

  for v in values:
    if(v > maxValue):
      maxValue = v
    if(v in countDict):
      countDict[v] += 1
    else:
      countDict[v] = 1

  for value in range(0, maxValue + 1):
    if(value in countDict):
      for j in range(0, countDict[value]):
        sortedArray.append(value)

  return sortedArray
  

array = [44, 9, 16, 23, 3, 44, 3, 16, 9, 10, 3, 9, 44, 16]
print(countsort(array))