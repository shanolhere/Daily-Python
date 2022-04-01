#Calculate Median
'''
Median is the middle value among all the values in sorted order.

- when the total number of values is even: Median  = [(n/2)th term + {(n/2)+1}th]/2

- when the total number of values is odd: Median = {(n+1)/2}thterm

'''

list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
list1.sort()

if len(list1)%2==0:
    median = (list1[len(list1)//2] + list1[len(list1)//2 - 1])/2
else:
    median = list1[len(list1)//2]
print(median)