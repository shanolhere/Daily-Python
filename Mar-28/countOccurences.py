#count all occurrences of a key in a given array.
def count(array, key):
    if array==[]:
        return 0
    if array[0]==key:
        return 1+ count(array[1:], key)
    else:
        return 0 + count(array[1:], key)
array= [1,2,2,3,4,5,5]
key = int(input())
print(count(array, key))