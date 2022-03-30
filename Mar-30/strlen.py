#Find length of a string in python (4 ways)
''' 
len(string); using count++; 
'''

string = input()
count=0
for i in string.split(" "): #for i in string:
    count+=1
print(count)