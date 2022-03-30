#Python | Check if a Substring is Present in a Given String

#Method-1: Using user-defined function str.find(sub_str)
string1 = "geeks for geeks"
string2 = "geeks"

'''print(string1.find(string2))find() function returns -1 if it is not found, 
else it returns the first occurrence, so using this function this problem can be solved.'''

if (string1.find(string2)==-1):
    print("NO")
else:
    print("YES")
    
'''
Method 2: Using “count()” method:-
if(string1.count(string2)>0):
   print("YES")
else:
   print("NO")


Method 3: Using regular expressions
if(re.search(string1, string2)):
  print("YES")
else:
  print("NO")




'''