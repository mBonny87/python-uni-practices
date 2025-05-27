# Write a Python program that takes as input a positive integer N 
# and prints the integers between 1 and N (inclusive) with one integer on line 1, 2 integers on line 2 and so on. 

def half_pyramid(n):
  row_len = 1
  prev_row_last_value = 0
  
  for i in range(1, n+1):
    print(i, end=" ")
    if((i - prev_row_last_value) == row_len):
      row_len += 1
      prev_row_last_value = i
      print("\n")

half_pyramid(28)