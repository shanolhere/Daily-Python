#Given an index, find the corresponding Fibonacci number.

def fibonacci(N):
    if N<=1:
        return N 
    else:
        return fibonacci(N-1) + fibonacci(N-2)
N = int(input())
print(fibonacci(N))