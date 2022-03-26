#find the sum of numbers from 1 to n using recursion
def sumOfNumbers(N):
    if N==1:
        return 1 
    else:
        return N + sumOfNumbers(N-1)
print(sumOfNumbers(10))