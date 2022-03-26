#March 24 - 7:30PM
#Reverse an array

T = int(input())  #NO. of testcases
for i in range(1, T+1):
    N = int(input()) #NO. of elements
    l = list(map(int, input().rstrip().split())) #Taking list elements in one line
l = l[::-1]
print(*l) 