#find their greatest common divisor using recursion
def gcd(a, b):
    if a==b:
        return a 
    if a>b:
        return gcd(a-b, b)
    else:
        return gcd(a, b-a)
a = 24
b = 42
print(gcd(a,b))