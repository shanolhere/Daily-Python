#learn how to replace all negative numbers with 0 in an array recursively.
def replace(array, currentIndex) :
  if currentIndex < len(array) :
    if array[currentIndex] < 0 :
      array[currentIndex] = 0

    return replace(array, currentIndex + 1)

# Driver Code
array = [2, -3, 4, -1, -7, 8]
print("Original Array --> " + str(array))
replace(array, 0)
print("Modified Array --> " + str(array))