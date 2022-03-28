#merge 2 sorted strings lexicographically
def mergeStrings(string1, string2):
    if string1 == "":
        if string2=="":
            return ""
        return string2
    elif string2=="":
        return string1
    elif string1[0] > string2[0]:
        return string2[0] + mergeStrings(string1, string2[1:])
    else:
        return string1[0] + mergeStrings(string1[1:], string2)
    
string1 = input()
string2 = input()
print(mergeStrings(string1, string2))