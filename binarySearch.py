array = []

for i in range(0,100):
  array.append(i)

def binarySearch(array, searchedItem):
  index = -1
  found = False
  first = 0
  last = len(array) - 1

  while first <= last and found == False:
    midpoint = (first + last) // 2
    if array[midpoint] == searchedItem:
      index = midpoint
      found = True
    elif array[midpoint] < searchedItem:
      first = midpoint + 1
      if len(array[first:last]) == 0:
        return "item not found"
      print(array[first:last])
    else:
      last = midpoint - 1
      if len(array[first:last]) == None:
        return "item not found"
      print(array[first:last])
  return index

  
print(binarySearch(array, 100))