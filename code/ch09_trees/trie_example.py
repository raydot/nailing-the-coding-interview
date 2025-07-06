class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes (key = character, value = TrieNode)
        self.children = {}
        # Flag to mark the end of a word
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        """Initialize an empty Trie with a root node"""
        self.root = TrieNode()
    
    def insert(self, word):
        """Insert a word into the trie"""
        current = self.root
        
        # Traverse the trie character by character
        for char in word:
            # If character doesn't exist, add a new node
            if char not in current.children:
                current.children[char] = TrieNode()
            # Move to the next node
            current = current.children[char]
        
        # Mark the end of the word
        current.is_end_of_word = True
    
    def search(self, word):
        """Search for an exact word in the trie"""
        current = self.root
        
        # Traverse the trie character by character
        for char in word:
            # If character doesn't exist, word is not in trie
            if char not in current.children:
                return False
            current = current.children[char]
        
        # Return True if we've reached the end of a word
        return current.is_end_of_word
    
    def starts_with(self, prefix):
        """Check if any word in the trie starts with the given prefix"""
        current = self.root
        
        # Traverse the trie character by character
        for char in prefix:
            # If character doesn't exist, prefix is not in trie
            if char not in current.children:
                return False
            current = current.children[char]
        
        # If we reach here, the prefix exists in the trie
        return True
    
    def get_suggestions(self, prefix):
        """Return all words that start with the given prefix"""
        suggestions = []
        current = self.root
        
        # First, navigate to the node corresponding to the prefix
        for char in prefix:
            if char not in current.children:
                return suggestions  # No suggestions if prefix doesn't exist
            current = current.children[char]
        
        # Now collect all words starting from this node
        self._collect_words(current, prefix, suggestions)
        return suggestions
    
    def _collect_words(self, node, prefix, suggestions):
        """Helper method to recursively collect words from a given node"""
        # If we're at the end of a word, add it to suggestions
        if node.is_end_of_word:
            suggestions.append(prefix)
        
        # Recursively explore all children
        for char, child_node in node.children.items():
            self._collect_words(child_node, prefix + char, suggestions)
            
    def visualize_trie(self, node=None, prefix="", level=0):
      """
      Prints a visual representation of the trie structure.
      Shows character-by-character organization and prefix sharing.
      """
      if node is None:
          node = self.root
          print("Trie Visualization:")
          print("└── ROOT")
      
      # Sort children for consistent visualization
      sorted_children = sorted(node.children.items())
      
      # Process each child
      for i, (char, child_node) in enumerate(sorted_children):
          # Determine if this is the last child at this level
          is_last = i == len(sorted_children) - 1
          
          # Create the branch symbol
          branch = "└── " if is_last else "├── "
          
          # Create indentation based on level
          indent = "    " if level == 0 else "│   " * (level - 1) + ("    " if is_last else "│   ")
          
          # Print the node with its character
          end_marker = "*" if child_node.is_end_of_word else ""
          print(f"{indent}{branch}{char} {end_marker}")
          
          # Recursively visualize child nodes
          self.visualize_trie(child_node, prefix + char, level + 1)


# Example usage
def demonstrate_trie():
    # Create a trie
    trie = Trie()
    
    # Insert some words
    words = ["apple", "application", "apply", "banana", "band", "bat"]
    for word in words:
        trie.insert(word)
        
    print("Words inserted into the trie:")
    print(words)
    
    # Search for words
    print(f"Is 'apple' in trie? {trie.search('apple')}")       # True
    print(f"Is 'app' in trie? {trie.search('app')}")           # False
    print(f"Is 'banana' in trie? {trie.search('banana')}")     # True
    print(f"Is 'ball' in trie? {trie.search('ball')}")         # False
    
    # Check prefixes
    print(f"Does any word start with 'app'? {trie.starts_with('app')}")  # True
    print(f"Does any word start with 'ban'? {trie.starts_with('ban')}")  # True
    print(f"Does any word start with 'cat'? {trie.starts_with('cat')}")  # False
    
    # Get autocomplete suggestions
    print(f"Suggestions for 'app': {trie.get_suggestions('app')}")  # ['apple', 'application', 'apply']
    print(f"Suggestions for 'ba': {trie.get_suggestions('ba')}")    # ['banana', 'band', 'bat'] 
    
    # Visualize the trie structure
    print("\nTrie Structure:")
    trie.visualize_trie()

if __name__ == "__main__":
    demonstrate_trie()