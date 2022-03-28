#how to inverse an array recursively.
def reverse(array):
    if len(array)==[]:
        return 0
    if len(array)==1:
        return array
    else:
        length = len(array)
        return [array[length-1]] + reverse(array[:length-1])

array = [1,2,3,5,6]
print(reverse(array))