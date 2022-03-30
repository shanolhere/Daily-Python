#Ways to remove i’th character from string in Python
string = input()
pos = int(input())
for i in range(0, len(string)):
    if i==pos:
        continue
    print(string[i], end="")
    
'''
This one is a naive approach
other ways are: str.replace
                Using slice + concatenation
                using str.join() and list comprehension
                
# Removing 1st occurrence of s, i.e 5th pos.
# if we wish to remove it.
new_str = test_str.replace('s', '', 1)

'''