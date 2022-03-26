#Challenge 1: Compute Square of a Number using recursion

def findSquare(n):
    if n==0:
        return 0 
    else:
        return findSquare(n-1) + 2*n -1
        
    
    
n = int(input())
print(findSquare(n))