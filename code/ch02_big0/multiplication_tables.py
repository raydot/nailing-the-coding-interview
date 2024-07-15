
def multiply(limit):
  for i in range(1, limit + 1):
    for j in range(1, limit + 1):
      print(f"{i * j}", end=" ")
    print("\n")
  
multiply(10)