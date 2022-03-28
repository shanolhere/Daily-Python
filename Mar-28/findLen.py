#Given a string find its length using recursion.

def recursiveLength(testVariable) : 
	if (testVariable == "") : 
		return 0
    
	else : 
		return 1 + recursiveLength(testVariable[1:]) 
n = input()
print(recursiveLength(n))