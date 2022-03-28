#Given an array of numbers, compute the average of all the numbers recursively. 
def average(testVariable, currentIndex = 0) : 
	if currentIndex == len(testVariable) - 1 : 
		return testVariable[currentIndex] 
	
	if currentIndex == 0 : 
		return ((testVariable[currentIndex] + average(testVariable, currentIndex + 1)) / len(testVariable)) 
	
	return (testVariable[currentIndex] + average(testVariable, currentIndex + 1)) 
testVariable = [10, 2, 3, 4, 8, 0] 
currentIndex = 0
print(average(testVariable, currentIndex))