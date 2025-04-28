class Tree:
  def __init__(self, data):
      self.value = data
      self.left = None
      self.right = None

  def in_order_traversal_iterative(root):
      result = []
      stack = []
      current = root
      
      while current or stack:
          # Reach the leftmost node of the current subtree
          while current:
              stack.append(current)
              current = current.left
              
          # Current is now None, pop from stack and visit
          current = stack.pop()
          result.append(current.value)
          
          # Now visit right subtree
          current = current.right
          
      return result
    
# Creating a tree at the root
root = Tree(88)

# Populate the left subtree
root.left = Tree(60)
root.left.left = Tree(43)
root.left.right = Tree(67)
root.left.left.left = Tree(10)
root.left.left.left.right = Tree(22) 

# Populate the right subtree
root.right = Tree(93)
root.right.left = Tree(91)
root.right.right = Tree(99)
root.right.right.right = Tree(101)

# Perform in-order traversal
result = Tree.in_order_traversal_iterative(root)
print("In-order Traversal:", result)