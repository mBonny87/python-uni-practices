# Write a Python program to split a string based on a special character, like a comma, into substrings. 
# Each substring is stored as elements in a list. The program outputs the list. 

def split_string(s):
  list = []
  for word in str(s).split(','):
    list.append(word.strip())
  print(list)

  

split_string("This, is, a, random string")
