#Email Slicer - AmanKharwal's 
#we need to divide the email into two strings using ‘@’ as the separator.
#Let’s see how to separate the email and domain name with Python:

email = input("Enter ur email pls: ")
username = email[:email.index("@")]
domainName = email[email.index("@")+1:]
print("Your username is "+username +" and domain Name is "+domainName +" ")