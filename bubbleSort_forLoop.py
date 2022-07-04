array = [5,6,8,3,2,9,7,4,1,12,10,13,11,15,16,19,18,17,14]

def bubbleSort(array):
  num_items = len(array)
  temp = 0

  for item in array:
    for i in range(num_items - 1):
      if (array[i] > array[i+1]):
        temp = array[i]
        array[i] = array[i+1]
        array[i+1] = temp
        print(array)

print(bubbleSort(array))