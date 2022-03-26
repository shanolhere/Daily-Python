# Python Program to find Perfect Number using For loop

N = int(input())
sum = 0
for i in range(1,N):
    if N%i==0:
        sum= sum+i
if sum==N:
    print("Perfect Number")
else:
    print("Not a perfect number")