#palindrome or symmetrical 
def isPalindrome(s):
    return s==s[::-1]
s = input()
print(isPalindrome(s))


'''
run loop from 0 to len/2
for i in range(i, int(len(s)/2)):
    if str[i]!= str[len(s)-i-1]:
       return False
return True
'''