#replaces all occurrences of substring b with substring a in string using recursion
def replace(string, a, b) :
  # Base case
  if not string:
    return ""
  
  # Recursive case
  elif string[:len(b)] == b :
    return a + replace(string[len(b):], a, b)
    
  else :
    return string[0] + replace(string[1:], a, b)