#Given a string containing numbers, calculate the sum of those numbers.

def sumDigits(testVariable):
  # Write your code here
  if testVariable == "":
    return 0
  else:
    return int(testVariable[0]) + sumDigits(testVariable[1:])
    
n = input()
print(sumDigits(n))