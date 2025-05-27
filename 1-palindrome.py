# Write a Python program to check if a given positive integer is a palindrome or not. 
# For example, 13531, 5555, 2442, 7290927 are palindromes, while 12531, 1234, 94783 are non-palindromes.  You are only allowed to use math operations without converting the integer into a string.

def palindrome(n):
  list = []
  temp = n
  m = 0

  while temp / 10 > 0:
    remainder = temp % 10
    list.append(remainder)
    temp = (int)(temp / 10)

  dec = 1

  for i in range(len(list) - 1, -1, -1):
    print(i)
    m += (list[i] * dec)
    dec *= 10

  return n == m

print(palindrome(13531))