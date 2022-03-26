#Given an array find the first occurrence of the target number.
def firstIndex(arr, targetNumber, currentIndex):
    if len(arr) == currentIndex:
        return None 
    if arr[currentIndex] == targetNumber:
        return currentIndex
    else:
        return firstIndex(arr, targetNumber, currentIndex+1)
    
    
arr = [9, 8, 1, 8, 1, 7]
targetNumber = 1
currentIndex = 0
print(firstIndex(arr, targetNumber, currentIndex))