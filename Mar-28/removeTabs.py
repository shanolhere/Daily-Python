
# remove tabs in string using recursion
def removeTabs(string):
    if not string:
        return ""
    if string[0]=="\t" or string[0]==" ":
        return removeTabs(string[1:])
    else:
        return string[0]+removeTabs(string[1:])
string = input()
print(removeTabs(string))