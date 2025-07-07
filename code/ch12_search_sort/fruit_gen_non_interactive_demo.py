class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        
class FruitTrie:
    def __init__(self):
        self.root = TrieNode()
        self.fruit_suggestions = {}  # Maps complete words to fruit objects
    
    def insert_fruit(self, fruit):
        """Insert a fruit into the trie for autocomplete"""
        name = fruit['name'].lower()
        self.fruit_suggestions[name] = fruit
        
        # Insert into trie
        current = self.root
        for char in name:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True
    
    def get_autocomplete_suggestions(self, prefix):
        """Get fruit suggestions for autocomplete"""
        prefix_lower = prefix.lower()
        
        # Navigate to prefix node
        current = self.root
        for char in prefix_lower:
            if char not in current.children:
                return []
            current = current.children[char]
        
        # Collect all complete words from this prefix
        suggestions = []
        self._collect_suggestions(current, prefix_lower, suggestions)
        
        # Return corresponding fruit objects
        return [self.fruit_suggestions[word] for word in suggestions if word in self.fruit_suggestions]
    
    def _collect_suggestions(self, node, prefix, suggestions):
        if node.is_end_of_word:
            suggestions.append(prefix)
        
        for char, child_node in node.children.items():
            self._collect_suggestions(child_node, prefix + char, suggestions)

def step_by_step_autocomplete_demo():
    """Show exactly how the trie builds suggestions step by step"""
    
    # Create a small, controlled dataset for clear demonstration
    sample_fruits = [
        {"name": "Apple", "color": "Red", "region": "North America"},
        {"name": "Apricot", "color": "Orange", "region": "Europe"},
        {"name": "Banana", "color": "Yellow", "region": "South America"},
        {"name": "Cherry", "color": "Red", "region": "Europe"},
        {"name": "Coconut", "color": "Brown", "region": "Pacific Islands"}
    ]
    
    fruit_trie = FruitTrie()
    
    print("Building Trie with Sample Fruits:")
    print("=" * 40)
    
    for fruit in sample_fruits:
        fruit_trie.insert_fruit(fruit)
        print(f"Added: {fruit['name']}")
    
    print("\nTesting Autocomplete:")
    print("=" * 40)
    
    # Test various prefixes
    test_cases = [
        ("a", "Should find Apple and Apricot"),
        ("ap", "Should find Apple and Apricot"),
        ("app", "Should find only Apple"),
        ("c", "Should find Cherry and Coconut"),
        ("co", "Should find only Coconut"),
        ("z", "Should find nothing")
    ]
    
    for prefix, explanation in test_cases:
        suggestions = fruit_trie.get_autocomplete_suggestions(prefix)
        names = [fruit['name'] for fruit in suggestions]
        print(f"'{prefix}' → {names} ({explanation})")

if __name__ == "__main__":
    step_by_step_autocomplete_demo()