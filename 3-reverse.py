# Write a Python program to reverse a string given as input.

def reverse(s):
  # for i in range(len(s)-1, -1, -1):
  #   print(s[i], end="")
  print(s[::-1])


reverse("Anna")