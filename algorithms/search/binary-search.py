# python3 ./algorithms/search/binary-search.py

def binarySearch(values, searchValue):
  start = 0
  end = len(values) - 1
  middle = end // 2
  
  while(start <= end):
    if(searchValue == values[middle]):
      return middle
    if (searchValue > values[middle]): 
      start = middle + 1
    else: 
      end = middle - 1
    middle = (end + start) // 2
  
  return None

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(binarySearch(array, -1))
print(binarySearch(array, 0))
print(binarySearch(array, 1))
print(binarySearch(array, 2))
print(binarySearch(array, 3))
print(binarySearch(array, 4))
print(binarySearch(array, 5))
print(binarySearch(array, 6))
print(binarySearch(array, 7))
print(binarySearch(array, 8))
print(binarySearch(array, 9))
print(binarySearch(array, 10))
print(binarySearch(array, 11))
print(binarySearch(array, 12))
print(binarySearch(array, 29))
print(binarySearch(array, 31))

# array with 1 element
array2 = [1]
print(binarySearch(array2, 1))

# empty array
array3 = []
print(binarySearch(array3, 1))
