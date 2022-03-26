#Given a decimal number convert it to a binary number.

# platform from where I have referred is https://www.educative.io/collection/page/6151088528949248/4547996664463360/5697630963236864
def dectoBin(n):
    if n<=1:
        return str(n)
    else:
        return dectoBin(n//2) + dectoBin(n%2)

n = int(input())
print(dectoBin(n))