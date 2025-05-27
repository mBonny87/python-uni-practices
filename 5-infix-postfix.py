# Write a program in Python that takes a mathematical expression given as a string in infix format and outputs the expression in postfix format.
# Example: 
# infix => 3 + 4 * 2 / ( 1 - 5 )
# postfix => 3 4 2 * 1 5 - / +

# todo

operators = {
  "*": 2,
  "/": 2,
  "+": 1,
  "-": 1,
}

def infix_to_postfix(s):
  output = []
  stack = []
  for c in s[::1]:


# infix_to_postfix("3+4*2/(1-5)")