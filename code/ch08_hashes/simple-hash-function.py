def simple_hash(key, table_size):
    """
    A simple hash function that:
    1. Converts each character to its ASCII value
    2. Multiplies by position
    3. Sums all values
    4. Uses modulo to fit within table size
    """
    hash_value = 0
    for pos, char in enumerate(str(key)):
        hash_value += (ord(char) * (pos + 1))
    return hash_value % table_size

class SimpleHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # Using chaining for collision resolution
    
    def insert(self, key, value):
        index = simple_hash(key, self.size)
        # Handle collisions with chaining
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value  # Update existing key
                return
        self.table[index].append([key, value])
    
    def get(self, key):
        index = simple_hash(key, self.size)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None

# Example usage
hash_table = SimpleHashTable()

# Insert some key-value pairs
hash_table.insert("name", "John")
hash_table.insert("age", 30)
hash_table.insert("city", "Boston")
hash_table.insert("name", "Popeye the Sailor")
hash_table.insert("name", "Olive Oyl")
hash_table.insert("name", "Bluto")
hash_table.insert("name", "Wimpy")

print(hash_table.get("name")) # "Popeye the Sailor"

# Demonstrate usage
print(f"Hash of 'name': {simple_hash('name', 10)}")
print(f"Value for 'name': {hash_table.get('name')}")
print(f"Value for 'age': {hash_table.get('age')}")
print(f"Value for 'city': {hash_table.get('city')}")
print(f"Value for 'country': {hash_table.get('country')}")  # Non-existent key

print(simple_hash("name", 10))  # Single digit between 0-9
print(simple_hash("mane", 10))
print(simple_hash("age", 10))   # Single digit between 0-9
print(simple_hash("city", 10)) 

# Add this to your file to see collisions in action
print("\nDemonstrating Collisions:")
# Let's say these hash to the same value
key1 = "name"
key2 = "name"
print(f"Hash of '{key1}': {simple_hash(key1, 10)}")
print(f"Hash of '{key2}': {simple_hash(key2, 10)}")

# Add debugging prints
hash_table = SimpleHashTable()
index1 = simple_hash(key1, 10)
index2 = simple_hash(key2, 10)
print(f"\nIndices: key1='{key1}' hashes to {index1}, key2='{key2}' hashes to {index2}")

hash_table.insert(key1, "Popeye the Sailor")
print(f"After inserting {key1}: {hash_table.table[index1]}")
hash_table.insert(key2, "Jane")
print(f"After inserting {key2}: {hash_table.table[index2]}")

# Show all non-empty buckets
print("\nAll non-empty buckets:")
for i, bucket in enumerate(hash_table.table):
    if bucket:
        print(f"Bucket {i}: {bucket}")