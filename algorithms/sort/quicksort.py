
# python3 ./algorithms/sort/quicksort.py

def quicksort(values):
  arrayLength = len(values)
  if(arrayLength == 0):
    return []
  if(arrayLength == 1):
    return values
  middleValue = values[arrayLength // 2]
  leftPart = [v for v in values if v < middleValue]
  rightPart = [v for v in values if v > middleValue]
  return quicksort(leftPart) \
          + [middleValue] \
        + quicksort(rightPart)

array = [4, 1, 53, 23, 3, 45, 3, 6, 9, 10, 15, 2, 44, 16]

print(quicksort(array))

  