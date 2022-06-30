array = []

for i in range(0,100):
  array.append(i)

def linearSearch(array, searchedItem):
  for i in array:
    if array[i] == searchedItem:
      return ("Item " + str(searchedItem) + " is at position " + str(i))
  return ("Item " + str(searchedItem) + " not found")

print(linearSearch(array, 6))
      