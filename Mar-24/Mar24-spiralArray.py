#March 24 - 7:30PM
#spiral Matrix (imp ;-;)

def spiralMatrix(m, n, a):
    k = 0 #starting row Index
    l = 0 #starting column Index 
    while(k<m and l<n):
        for i in range(l,n):
            print(a[k][i], end=" ")
        k+=1 
        
        for i in range(k,m):
            print(a[i][n-1], end=" ")
        n-=1 
        
        if(k<m):
            for j in range(n-1, l-1, -1):
                print(a[n-1][j], end=" ")
            m-=1 
        
        if(l<n):
            for j in range(m-1, k-1,-1):
                print(a[j][l], end=" ")
            l+=1
            
m = 3
n = 4
A = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
spiralMatrix(m, n, A)
'''1  2  3  4
   5  6  7  8
   9  10 11 12 '''