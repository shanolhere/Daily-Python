#Generate password using python
import random
length = int(input("Enter length of the password:"))
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?"
password = "".join(random.sample(letters,length))
print(password)