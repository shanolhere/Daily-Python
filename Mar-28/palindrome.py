#Given a string, check whether it is a palindrome or not.
def isPalindrome(testVariable) :
  # Write your code here
  if len(testVariable) <= 1 :
      return True

  length = len(testVariable)
  if testVariable[0] == testVariable[length -1]:
      return isPalindrome(testVariable[1:length-1])
  return False
  
n = input()
print(isPalindrome(n))