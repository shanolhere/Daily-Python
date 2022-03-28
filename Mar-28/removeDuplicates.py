# remove all adjacent duplicates from a string using recursion.
def removeDuplicates(string):
    if not string:
        return ""
    elif len(string)==1:
        return string 
    elif string[0]==string[1]:
        return removeDuplicates(string[1:])
    else:
        return string[0] + removeDuplicates(string[1:])
string = input()
print(removeDuplicates(string))