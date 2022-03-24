#March 24 - 7:30PM
#Rotate an array by d times

def rotateArray(arr, d):
    #store d elements in temp Array
    #shift rest of the array 
    #store back the d elements
    temp = []
    for i in range(0,d):
        temp.append(arr[i])
    j = 0
    while(d < len(arr)):
        arr[j] = arr[d] 
        j = j+1 
        d = d+1 
    arr[:] = arr[:j] + temp
    print(arr)
   
arr = [1, 2, 3, 4, 5, 6, 7]
d = int(input())
rotateArray(arr,d)