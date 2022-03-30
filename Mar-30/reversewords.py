
# We are given a string and we need to reverse words of a given string?
string = input()
words = string.split(" ")
reverseSentence = " ".join(reversed(words))
print(reverseSentence)