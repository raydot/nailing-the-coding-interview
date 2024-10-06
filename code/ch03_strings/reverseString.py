# BAD WAY, forloop

def reverseString(myString):
  reversed = ""
  for i in range(len(myString)- 1, -1, -1):
    reversed += myString[i]
  return reversed

test_var = "Hello, world!"
print(reverseString(test_var)) # olleh