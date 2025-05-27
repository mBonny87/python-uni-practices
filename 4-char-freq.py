# Write a Python program that counts the frequencies of different characters in a string given as input and prints the character(s) with the minimum frequency. 
# One of the ways to solve this is to use a dictionary.

def char_freq(s):
  dictionary = {}
  for c in s[::1]:
    if(c != " "):
      dictionary[c] = dictionary.get(c, 0) + 1
  
  min_value = min(dictionary.values())

  for c in dictionary:
    if(dictionary[c] == min_value):
      print("char: %s with value: %i",c,min_value)


char_freq("aabbccc")